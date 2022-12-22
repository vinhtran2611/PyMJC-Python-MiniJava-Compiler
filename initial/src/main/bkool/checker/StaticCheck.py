from AST import *

# from Visitor import *
from Utils import Utils
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
            'current_class': class_env['current_class'],
            'local': {},
        }
        for parameter in ast.param:
            self.visit(parameter, method_env)
        self.visit(ast.body, method_env)

    def visitAttributeDecl(self, ast, class_env):
        # kind: SIKind #Instance or Static
        # decl: StoreDecl # VarDecl for mutable or ConstDecl for immutable
        decl = ast.decl
        self.visit(decl, class_env)
        if isinstance(decl, VarDecl):
            if isinstance(decl.varType, ClassType):
                if decl.varType.classname.name not in class_env["global"]:
                    raise Undeclared(Class(), decl.varType.classname.name)
            
            if decl.varInit:
                value_typ = self.visit(decl.varInit, class_env).mtype # return Symbol().mtype
                print(value_typ)
                if type(decl.varType) is FloatType and type(value_typ) not in [FloatType, IntType]:
                    raise TypeMismatchInConstant(decl)
                elif type(decl.varType) != type(value_typ):
                    raise TypeMismatchInConstant(decl)
        elif isinstance(decl, ConstDecl):
            if isinstance(decl.constType, ClassType):
                if decl.constType.classname.name not in class_env["global"]:
                    raise Undeclared(Class(), decl.constType.classname.name)

            if decl.value is None:
                raise TypeMismatchInConstant(decl)

            value_typ = self.visit(decl.value, class_env).mtype # return Symbol().mtype
            if type(decl.constType) is FloatType and type(value_typ) not in [FloatType, IntType]:
                raise TypeMismatchInConstant(decl)
            elif type(decl.constType) != type(value_typ):
                raise TypeMismatchInConstant(decl)
        # o['global'][o['current_class']]['members'][ast.decl.constant.name] = [ast.kind, Symbol(decl.constant.name, typ, 'constant')]

    def visitConstDecl(self, ast, class_env):
        # constant : Id
        # constType : Type
        # value : Expr
        
        if isinstance(ast.constType, ClassType):
            if ast.constType.classname.name not in class_env["global"]:
                raise Undeclared(Class(), ast.constType.classname.name)

        if ast.value is None:
            raise TypeMismatchInConstant(ast)
        
        value_typ = self.visit(ast.value, class_env).mtype # return Symbol().mtype
        print(value_typ, ast.constType)
        if type(ast.constType) is FloatType and type(value_typ) not in [FloatType, IntType]:
            raise TypeMismatchInConstant(ast)
        elif type(ast.constType) != type(value_typ):
            raise TypeMismatchInConstant(ast)
        
    def visitVarDecl(self, ast, o):
        # variable : Id
        # varType : Type
        # varInit : Expr = None # None if there is no initial
        if ast.variable.name in o["local"]:
            raise Redeclared(Variable(), ast.variable.name)
        if type(ast.varType) is ClassType:
            if not ast.varType.classname.name in o["global"]:
                raise Undeclared(Class(), ast.varType.classname.name)
        o["local"][ast.variable.name] = Symbol(ast.variable.name, ast.varType)

    def visitBlock(self, ast, method_env):
        # decl:List[StoreDecl]
        # stmt:List[Stmt]
        for decl in ast.decl:
            print(type(decl)) 
            self.visit(decl, method_env)
            print(isinstance(decl, ConstDecl))   
            if isinstance(decl, ConstDecl):
                class_name = method_env["current_class"]
                if decl.constant.name in method_env["global"][class_name]["members"]:
                    raise Redeclared(Constant(), decl.constant.name)

                method_env["local"][decl.constant.name] = Symbol(
                    decl.constant.name, decl.constType, "constant"
                )
        for stmt in ast.stmt:
            self.visit(stmt, method_env) 

    def visitBinaryOp(self, ast, o):
        # op:str
        # left:Expr
        # right:Expr
        l = self.visit(ast.left, o)
        r = self.visit(ast.right, o)
        if l is None:
            raise Undeclared(Identifier(), ast.left.name)
        if r is None:
            raise Undeclared(Identifier(), ast.right.name)
        # Arithmetic
        if ast.op in ["+", "-", "*", "/", "\\", "%"]:
            if not l.mtype and r.mtype in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            elif (
                type(l.mtype) != type(r.mtype)
                and l.mtype != IntType
                and (ast.op in ["\\", "%"])
            ):
                raise TypeMismatchInExpression(ast)
            elif ast.op == "/":
                return Symbol("", FloatType)
            elif type(l.mtype) != type(r.mtype):
                return Symbol("", FloatType)
            else:
                return l

        # Boolean
        elif ast.op in ["&&", "||"]:
            if not l.mtype and r.mtype == BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return Symbol("", BoolType)

        # Relational
        elif ast.op in ["==", "!=", ">", "<", ">=", "<="]:
            if ast.op in ["==", "!="]:
                if (not l.mtype and r.mtype in [IntType, BoolType]) or type(
                    l.mtype
                ) != type(r.mtype):
                    raise TypeMismatchInExpression(ast)
            else:
                if not l.mtype and r.mtype in [IntType, FloatType]:
                    raise TypeMismatchInExpression(ast)

            return Symbol("", BoolType)

        # String
        elif ast.op == "^":
            if l.mtype and r.mtype != StringType:
                raise TypeMismatchInExpression(ast)
            return Symbol("", BoolType)

    def visitUnaryOp(self, ast, o):
        # op:str
        # body:Expr
        body = self.visit(ast.body, o)

        if ast.op in ["+", "-"]:
            if not body.mtype in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            else:
                return body.mtype

        elif ast.op == "!":
            if body.mtype != BoolType:
                raise TypeMismatchInExpression(ast)

    def visitAssign(self, ast, o):
        # lhs:Expr
        # exp:Expr
        lhs = self.visit(ast.lhs, o)
        if lhs.value == "constant":
            raise CannotAssignToConstant(ast)

        exp = self.visit(ast.exp, o)
        if type(lhs.mtype) != type(exp.mtype):
            raise TypeMismatchInStatement(ast)

    def visitFieldAccess(self, ast, o):
        # obj:Expr
        # fieldname:Id
        obj = self.visit(ast.obj, o)
        typ = "objClass"
        obj_name = obj.mtype.classname if type(obj.mtype) == ClassType else obj.name
        if type(obj.mtype) != ClassType:
            raise TypeMismatchInExpression(ast)

        if obj.value in ["objClass", "class"]:
            ancestor = obj_name.name if type(obj_name) == Id else obj_name
            while ancestor != None:
                if ast.fieldname.name in o["global"][ancestor]["members"]:
                    if obj.value == "class":
                        if (
                            o["global"][ancestor]["members"][ast.fieldname.name][0]
                            == Instance()
                        ):
                            raise IllegalMemberAccess(ast)
                    elif obj.value == "objClass":
                        if (
                            o["global"][ancestor]["members"][ast.fieldname.name][0]
                            == Static()
                        ):
                            raise IllegalMemberAccess(ast)
                    typ = o["global"][ancestor]["members"][ast.fieldname.name][1]
                    return Symbol("", typ)
                else:
                    ancestor = o["global"][ancestor]["parent"]

            raise Undeclared(Identifier(), ast.fieldname.name)
        else:
            raise Undeclared(Class(), obj.name)

    def visitId(self, ast, o):
        value = None
        name = ast.name
        if ast.name in o["local"]:
            if type(o["local"][ast.name].mtype) == ClassType:
                value = "objClass"
                name = o["local"][ast.name].mtype.classname.name
            if o["local"][ast.name].value == "constant":
                value = "constant"
            return Symbol(name, o["local"][ast.name].mtype, value)

        if ast.name in o["global"][o["current_class"]]["members"]:
            if o["global"][o["current_class"]]["members"][ast.name][1].value == "constant":
                return o["global"][o["current_class"]]["members"][ast.name][1]
            else:
                return Symbol(
                    o["current_class"],
                    o["global"][o["current_class"]]["members"][ast.name][1],
                    "memClass",
                )

        if ast.name in o["global"]:
            return Symbol(ast.name, ClassType(ast.name), "class")

        raise Undeclared(Identifier(), ast.name)

    def visitIntLiteral(self, ast, o):
        return Symbol("", IntType())

    def visitFloatLiteral(self, ast, o):
        return Symbol("", FloatType())

    def visitBooleanLiteral(self, ast, o):
        return Symbol("", BoolType())

    def visitStringLiteral(self, ast, o):
        return Symbol("", StringType())

    def visitNullLiteral(self, ast, o):
        pass

    def visitSelfLiteral(self, ast, o):
        return Symbol(o["current_class"], ClassType(o["current_class"]), "objClass")