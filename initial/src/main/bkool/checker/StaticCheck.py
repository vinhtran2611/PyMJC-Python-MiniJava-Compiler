from AST import *

# from Visitor import *
# from Utils import Utils
from StaticError import *
from Visitor import BaseVisitor


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None, details=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.details = details
    def __str__(self) -> str:
        return f"Symbol(Name: {self.name}, Type: {self.mtype}, Value: {self.value})"

def intersection(lst1, lst2): 
    for value in lst1:
        if value in lst2:
            return True
    return False

class Env:
    def __init__(self, globalEnv={}, localEnv=None, current_classEnv=None):
        self.o = {}
        self.o["global"] = globalEnv
        self.o["local"] = localEnv
        self.o["current_class"] = current_classEnv

    def openScope(self, o):
        o["local"].append({})

    def closeScope(self, o):
        o["local"].pop()

    def lookUp(self, name):
        if len(self.o["local"]):
            if name in self.o["local"][-1]:
                return True
            return False


class GetEnv(BaseVisitor):
    def visit(self, ast, param):
        return ast.accept(self, param)

    def visitProgram(self, ast, o):
        # decl : List[ClassDecl]
        o = {}
        for class_decl in ast.decl:
            self.visit(class_decl, o)
        return o

    def visitClassDecl(self, ast, o):
        # classname : Id
        # memlist : List[MemDecl]
        # parentname : Id = None # None if there is no parent
        if ast.classname.name in o:
            raise Redeclared(Class(), ast.classname.name)
        o[ast.classname.name] = {
            "parent": ast.parentname.name if ast.parentname else None,
            "members": {},
        }
        for member in ast.memlist:
            self.visit(member, o[ast.classname.name]["members"])

    def visitMethodDecl(self, ast, class_env):
        # kind: SIKind
        # name: Id
        # param: List[VarDecl]
        # returnType: Type  # None for constructor
        # body: Block
        if ast.name.name in class_env:
            raise Redeclared(Method(), ast.name.name)
        class_env[ast.name.name] = (
            ast.kind,
            Symbol(ast.name.name, ast.returnType)
        )

    def visitAttributeDecl(self, ast, class_env):
        # kind: SIKind #Instance or Static
        # decl: StoreDecl # VarDecl for mutable or ConstDecl for immutable
        decl = ast.decl
        value = None
        if isinstance(decl, VarDecl):
            if decl.variable.name in class_env:
                raise Redeclared(Attribute(), (decl.variable.name))
            if isinstance(decl.varType, ClassType):
                value = "objClass"
            class_env[decl.variable.name] = (
                ast.kind,
                Symbol(decl.variable.name, decl.varType, value)
            )
        elif isinstance(decl, ConstDecl):
            if decl.constant.name in class_env:
                raise Redeclared(Attribute(), decl.constant.name)
            value = "constant"
            class_env[decl.constant.name] = (
                ast.kind,
                Symbol(decl.constant.name, decl.constType, value)
            )

class StaticChecker(BaseVisitor):
    def visit(self, ast, param):
        return ast.accept(self, param)

    global_envi = [
        Symbol("readInt", MType([], IntType())),
        Symbol("writeInt", MType([IntType()], VoidType())),
        Symbol("writeIntLn", MType([IntType()], VoidType())),
        Symbol("readFloat", MType([FloatType()], FloatType())),
        Symbol("writeFloat", MType([FloatType()], VoidType())),
        Symbol("writeFloatLn", MType([FloatType()], VoidType())),
        Symbol("readBool", MType([BoolType()], BoolType())),
        Symbol("writeBool", MType([BoolType()], VoidType())),
        Symbol("writeBoolLn", MType([BoolType()], VoidType())),
        Symbol("readStr", MType([], StringType())),
        Symbol("writeStr", MType([StringType()], VoidType())),
        Symbol("writeStrLn", MType([StringType()], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, o):
        env = GetEnv().visit(ast, Env())

        for class_decl in ast.decl:
            self.visit(class_decl, env)
        
    def visitClassDecl(self, ast, o):
        # class ClassDecl(Decl):
        # classname : Id
        # memlist : List[MemDecl]
        # parentname : Id = None # None if there is no parent
        if ast.parentname is not None:
            if ast.parentname.name not in o:
                raise Undeclared(Class(), ast.parentname.name)
                
        class_env = {
            'global': o,
            'current_class': ast.classname.name,
        }

        for mem in ast.memlist:
            self.visit(mem, class_env)

    def visitMethodDecl(self, ast, class_env):
        # kind: SIKind
        # name: Id
        # param: List[VarDecl]
        # returnType: Type  # None for constructor
        # body: Block
        method_env = {
            'global': class_env['global'],
            'current_class': class_env['current_class'], #class name
            'name': ast.name.name,
            'local': {},
        }
        for parameter in ast.param:
            self.visit(parameter, method_env)
        self.visit(ast.body, method_env)

    def visitAttributeDecl(self, ast, class_env):
        # kind: SIKind #Instance or Static
        # decl: StoreDecl # VarDecl for mutable or ConstDecl for immutable
        self.visit(ast.decl, class_env)

    def visitConstDecl(self, ast, class_env):
        # constant : Id
        # constType : Type
        # value : Expr
        if isinstance(ast.constType, ClassType):
            if ast.constType.classname.name not in class_env["global"]:
                raise Undeclared(Class(), ast.constType.classname.name)

        if ast.value is None:
            raise TypeMismatchInConstant(ast)
        
        value_typ = self.visit(ast.value, class_env) # return Symbol().mtype
        if type(ast.constType) is FloatType and type(value_typ) not in [FloatType, IntType]:
            raise TypeMismatchInStatement(ast)
        elif type(ast.constType) != value_typ:
            raise TypeMismatchInConstant(ast)
        
    def visitVarDecl(self, ast, env):
        # variable : Id
        # varType : Type
        # varInit : Expr = None # None if there is no initial
        # print(f"Vardecl: {ast}")

        if isinstance(ast.varType, ClassType):
            if ast.varType.classname.name not in env["global"]:
                raise Undeclared(Class(), ast.varType.classname.name)
        
        if ast.varInit:
            value_typ = self.visit(ast.varInit, env) 
            
            if type(ast.varType) is FloatType and value_typ not in [FloatType, IntType]:
                raise TypeMismatchInStatement(ast)
            elif type(ast.varType) != value_typ:
                raise TypeMismatchInStatement(ast)
        if "local" in env:
            if ast.variable.name in env["local"]:
                raise Redeclared(Variable(), ast.variable.name)
            env["local"][ast.variable.name] = Symbol(ast.variable.name, ast.varType)

    def visitBlock(self, ast, method_env):
        # decl:List[StoreDecl]
        # stmt:List[Stmt]
        for decl in ast.decl:
            self.visit(decl, method_env)
            if isinstance(decl, ConstDecl):
                class_name = method_env["current_class"]
                if decl.constant.name in method_env["global"][class_name]["members"]:
                    raise Redeclared(Constant(), decl.constant.name)

                method_env["local"][decl.constant.name] = Symbol(
                    decl.constant.name, decl.constType, "constant"
                )
        for stmt in ast.stmt:
            self.visit(stmt, method_env) 

    def visitIf(self, ast, method_env):
        # class If(Stmt):
        # expr:Expr
        # thenStmt:Stmt
        # elseStmt:Stmt = None # None if there is no else branch
        expr = self.visit(ast.expr, method_env)
        if type(expr) != BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt)
        if ast.elseStmt:
            self.visit(ast.elseStmt)

    def visitBinaryOp(self, ast, method_env):
        # op:str
        # left:Expr
        # right:Expr
        # print(f"visitBinaryOp: {ast}")

        l = self.visit(ast.left, method_env)
        r = self.visit(ast.right, method_env)
        if isinstance(l, Id):
            if l is None:
                raise Undeclared(Identifier(), ast.left.name)
        if isinstance(r, Id):
            if r is None:
                raise Undeclared(Identifier(), ast.right.name)

        if ast.op in ["+", "-", "*", "/", "<", "<=", ">", ">="]:
            if intersection([l, r], [BoolType, StringType]):
                raise TypeMismatchInExpression(ast)
            if ast.op == '/':
                return FloatType
            elif type(l) == IntType and type(r) == IntType:
                return IntType

            return FloatType
        elif ast.op in ["\\", "%"]:
            if intersection([l, r], [FloatType, BoolType, StringType]):
                
                raise TypeMismatchInExpression(ast)
            return IntType
        elif ast.op in ["==", "!="]:
            if intersection([l, r], [FloatType, StringType]):
                raise TypeMismatchInExpression(ast)
            
            if l !=  r:
                raise TypeMismatchInExpression(ast)
            return BoolType
        elif ast.op in ["&&", "||", "!"]:
            if intersection([l, r], [IntType, FloatType, StringType]):
                raise TypeMismatchInExpression(ast)
            return BoolType
        elif ast.op in ["^"]:
            if intersection([l, r], [IntType, FloatType, BoolType]):
                raise TypeMismatchInExpression(ast)
            return StringType

    def visitUnaryOp(self, ast, method_env):
        # op:str
        # body:Expr
        typ = self.visit(ast.body, method_env)

        if ast.op in ["+", "-"]:
            if typ.mtype not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "!":
            if typ != BoolType:
                raise TypeMismatchInExpression(ast)
        return typ

    def visitAssign(self, ast, method_env):
        # lhs:Expr
        # exp:Expr
        # print(f"Assign: {ast}")

        exp = self.visit(ast.exp, method_env)
        lhs = self.visit(ast.lhs, method_env)

        if isinstance(lhs, Id) == False:
            TypeMismatchInStatement(ast)            

        if isinstance(lhs, Symbol):
            if lhs.value == "constant":
                raise CannotAssignToConstant(ast)

            if isinstance(exp, Symbol):
                if type(lhs.mtype) != type(exp.mtype):
                    raise TypeMismatchInStatement(ast)
            elif type(lhs.mtype) != exp:
                raise TypeMismatchInStatement(ast)
            return exp

    def visitFieldAccess(self, ast, o):
        # obj:Expr
        # fieldname:Id
        # print(f"visitFieldAccess: {ast}")

        obj_data = self.visit(ast.obj, o) # Symbol
        
        if type(obj_data.mtype) != ClassType:
            raise TypeMismatchInExpression(ast)

        # typ = "objClass"
        class_name = obj_data.mtype.classname.name
        while True:
            class_store = None
            for cls_decl in o['global']:
                if class_name == cls_decl:
                    class_store = o['global'][cls_decl]
            if class_store is None:
                raise Undeclared(Class(), class_name)
            
            if ast.fieldname.name in class_store['members']:
                return class_store['members'][ast.fieldname.name][1].mtype
            
            if class_store['parent'] is None:
                break
            class_name = class_store['parent']
        raise Undeclared(Attribute(), ast.fieldname.name)  

    def visitId(self, ast, method_env):
        # class Id(LHS):
        # name:str
        # print(f"visitId: {ast}")

        id_name = ast.name
        if id_name in method_env["local"]: #check local
            return Symbol(id_name, method_env["local"][id_name].mtype)

        class_name = method_env["current_class"]
        if id_name in method_env["global"][class_name]["members"]: #check global
            return method_env["global"][class_name]["members"][id_name][1]  # return Symbol

        if id_name in method_env["global"]: # for field asscess
            return Symbol(id_name, ClassType(id_name), "class")

        raise Undeclared(Identifier(), id_name)

    def visitIntLiteral(self, ast, o):
        return IntType

    def visitFloatLiteral(self, ast, o):
        return FloatType

    def visitBooleanLiteral(self, ast, o):
        return BoolType

    def visitStringLiteral(self, ast, o):
        return StringType

    def visitNullLiteral(self, ast, o):
        pass

    def visitSelfLiteral(self, ast, o):
        return Symbol(o["current_class"], ClassType(o["current_class"]), "objClass")
