from PYMJCVisitor import PYMJCVisitor
from PYMJCParser import PYMJCParser
from AST import *

class ASTGeneration(PYMJCVisitor):

    # Visit a parse tree produced by PYMJCParser#program.
    def visitProgram(self, ctx:PYMJCParser.ProgramContext):
        decls = []
        for class_decl in ctx.class_decl():
            decl = self.visit(class_decl)
            decls.append(decl)
        return Program(decls)

    # Visit a parse tree produced by PYMJCParser#class_decl.
    def visitClass_decl(self, ctx:PYMJCParser.Class_declContext):
        if ctx.EXTENDS():
            name = Id(ctx.ID(0).getText())
            parent = Id(ctx.ID(1).getText())
        else:
            name = Id(ctx.ID(0).getText())
            parent = None
        mem_decls = []
        for mem in ctx.member():
            mem_decl = self.visit(mem)
            if isinstance(mem_decl, MethodDecl):
                mem_decls.append(mem_decl)
            else:
                for ele in mem_decl:
                    mem_decls.append(ele)
        return ClassDecl(name, mem_decls, parent)

    # Visit a parse tree produced by PYMJCParser#bktype.
    def visitBktype(self, ctx:PYMJCParser.BktypeContext):
        if ctx.INT():
            type = IntType()
        elif ctx.FLOAT():
            type = FloatType()
        elif ctx.BOOLEAN():
            type = BoolType()
        elif ctx.STRING():
            type = StringType()
        elif ctx.VOID():
            type = VoidType()  
        elif ctx.ID():
            type = ClassType(Id(ctx.ID().getText()))

        if ctx.LQB():
            size = self.visit(ctx.exp())
            return ArrayType(size, type)
        return type
        
    # Visit a parse tree produced by PYMJCParser#member.
    def visitMember(self, ctx:PYMJCParser.MemberContext):
        if ctx.attribute_decl():
            return self.visit(ctx.attribute_decl())
        else:
            return self.visit(ctx.method_decl())


    # Visit a parse tree produced by PYMJCParser#attribute_decl.
    def visitAttribute_decl(self, ctx:PYMJCParser.Attribute_declContext):
        if ctx.mutable():
            return self.visit(ctx.mutable())
        else:
            return self.visit(ctx.immutable())


    # Visit a parse tree produced by PYMJCParser#immutable.
    def visitImmutable(self, ctx:PYMJCParser.ImmutableContext):
        k = Static() if ctx.STATIC() else Instance()
        type, ids = self.visit(ctx.var_decl_att())
        attr = []
        for id, val_init in ids:
            v = ConstDecl(id, type, val_init)
            a = AttributeDecl(k, v)
            attr.append(a)
        return attr
        

    # Visit a parse tree produced by PYMJCParser#mutable.
    def visitMutable(self, ctx:PYMJCParser.MutableContext):
        k = Static() if ctx.STATIC() else Instance()
        type, ids = self.visit(ctx.var_decl_att())
        attr = []
        for id, val_init in ids:
            v = VarDecl(id, type, val_init)
            a = AttributeDecl(k, v)
            attr.append(a)
        return attr


    # Visit a parse tree produced by PYMJCParser#var_decl.
    def visitVar_decl(self, ctx:PYMJCParser.Var_declContext):
        type = self.visit(ctx.bktype())
        ids = self.visit(ctx.listID())
        if ctx.FINAL():
            return type, ids, True
        return type, ids
    
    # Visit a parse tree produced by PYMJCParser#var_decl_att.
    def visitVar_decl_att(self, ctx:PYMJCParser.Var_decl_attContext):
        type = self.visit(ctx.bktype())
        ids = self.visit(ctx.ids_att())
        return type, ids

    # Visit a parse tree produced by PYMJCParser#method_decl.
    def visitMethod_decl(self, ctx:PYMJCParser.Method_declContext):
        if ctx.bktype():
            kind = Instance()
            if ctx.STATIC():
                kind = Static()

            name = Id(ctx.ID().getText())
            ps = self.visit(ctx.params())
            params = []
            for t, lids in ps:
                param = [VarDecl(id, t, val_init) for id, val_init in lids]
                params += param
            rtype = self.visit(ctx.bktype())
            body = self.visit(ctx.block_stmt())

            return MethodDecl(kind, name, params, rtype, body)
        else: 
            # constructor
            kind = Instance()
            name = Id(ctx.ID().getText())
            ps = self.visit(ctx.params())
            params = []
            for t, lids in ps:
                param = [VarDecl(id, t, val_init) for id, val_init in lids]
                params += param
            rtype = None
            body = self.visit(ctx.block_stmt())

            return MethodDecl(kind, name, params, rtype, body)

    # Visit a parse tree produced by PYMJCParser#params.
    def visitParams(self, ctx:PYMJCParser.ParamsContext):
        return [self.visit(v) for v in ctx.var_decl()]

    # Visit a parse tree produced by PYMJCParser#for_stmt.
    def visitFor_stmt(self, ctx:PYMJCParser.For_stmtContext):
        id = Id(ctx.ID().getText())
        exp1 = self.visit(ctx.exp(0))
        exp2 = self.visit(ctx.exp(1))
        up = True if ctx.TO() else False
        loop_stmt = self.visit(ctx.stmt())
        if isinstance(loop_stmt, list):
            return For(id, exp1, exp2, up, loop_stmt[0])
        return For(id, exp1, exp2, up, loop_stmt)

    # Visit a parse tree produced by PYMJCParser#assign_stmt.
    def visitAssign_stmt(self, ctx:PYMJCParser.Assign_stmtContext):
        exp = self.visit(ctx.exp())
        ids = [self.visit(l) for l in ctx.lhs()]
        asl = []
        for i in range(len(ids) - 1):
            asl += [Assign(ids[i], ids[i+1])]
        asl += [Assign(ids[-1], exp)]
        if len(asl) == 1:
            return asl[0]
        return asl[::-1]
    
    # Visit a parse tree produced by PYMJCParser#if_stmt.
    def visitIf_stmt(self, ctx:PYMJCParser.If_stmtContext):
        expr = self.visit(ctx.exp())
        if ctx.ELSE():
            then_stmt = self.visit(ctx.stmt(0))
            else_stmt = self.visit(ctx.stmt(1))
        else:
            then_stmt = self.visit(ctx.stmt(0))
            else_stmt = None
        return If(expr, then_stmt, else_stmt)
    
    # Visit a parse tree produced by PYMJCParser#method_invocation.
    def visitMethod_invocation(self, ctx:PYMJCParser.Method_invocationContext):
        obj = self.visit(ctx.exp())
        method = Id(ctx.ID().getText())
        params = self.visit(ctx.list_exp())
        

        return CallStmt(obj, method, params)

    # Visit a parse tree produced by PYMJCParser#list_exp.
    def visitList_exp(self, ctx:PYMJCParser.List_expContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp())]
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.list_exp())

    # Visit a parse tree produced by PYMJCParser#block_stmt.
    def visitBlock_stmt(self, ctx:PYMJCParser.Block_stmtContext):
        stmts = []
        for s in ctx.stmt():
            stmt = self.visit(s)
            if isinstance(stmt, list):
                stmts += stmt
            else:
                stmts.append(stmt)
                
        vars = []
        for v in ctx.var_decl():
            vardecl = self.visit(v)
            if len(vardecl) == 3:
                type, ids, const  = vardecl
                vars += [ConstDecl(id, type, val_init) for id, val_init in ids]
            else:
                type, ids = vardecl
                vars += [VarDecl(id, type, val_init) for id, val_init in ids]
        return Block(vars, stmts)
 
    # Visit a parse tree produced by PYMJCParser#stmt.
    def visitStmt(self, ctx:PYMJCParser.StmtContext):
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        elif ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.BREAK():
            return Break()
        elif ctx.CONTINUE():
            return Continue()
        elif ctx.RETURN():
            exp = self.visit(ctx.exp())
            return Return(exp)
        elif ctx.method_invocation():
            return self.visit(ctx.method_invocation())

    # Visit a parse tree produced by PYMJCParser#exp.
    def visitExp(self, ctx:PYMJCParser.ExpContext):
        if ctx.getChildCount() == 1 and (ctx.ID() or ctx.THIS()):
            return Id(ctx.getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())
        elif ctx.DOT():
            if ctx.LB():
                obj = self.visit(ctx.exp()[0])
                method = Id(ctx.ID().getText())
                params = []
                if ctx.list_exp():
                    params = self.visit(ctx.list_exp())
                return CallExpr(obj, method, params)
            else:
                obj = self.visit(ctx.exp()[0])
                field_name = Id(ctx.ID().getText())
                return FieldAccess(obj, field_name)
        elif ctx.getChildCount() == 3:
            if ctx.LB():
                return self.visit(ctx.exp()[0])
            else:
                op =  ctx.getChild(1).getText()
                left = self.visit(ctx.getChild(0))
                right = self.visit(ctx.getChild(2))
                return BinaryOp(op, left, right)            
        elif ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.exp())
            return UnaryOp(op, body)
        elif ctx.LQB():
            arr = self.visit(ctx.exp(0))
            idx = self.visit(ctx.exp(1))
            return ArrayCell(arr, idx)
        
        elif ctx.NEW():
            class_name = Id(ctx.ID().getText())
            params = []
            if ctx.list_exp():
                params = self.visit(ctx.list_exp())
            return NewExpr(class_name, params)    
      
    # Visit a parse tree produced by PYMJCParser#lhs.
    def visitLhs(self, ctx:PYMJCParser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.getText())
        elif ctx.LQB():
            arr = ctx.exp(0)
            idx = ctx.exp(1)
            return ArrayCell(arr, idx)
        elif ctx.DOT():
            obj = self.visit(ctx.exp()[0])
            field_name = Id(ctx.ID().getText())
            return FieldAccess(obj, field_name)

    # Visit a parse tree produced by PYMJCParser#literals.
    def visitLiteral(self, ctx:PYMJCParser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.getText()))
        elif ctx.BOOL_LIT():
            return BooleanLiteral(ctx.getText() == 'true')
        elif ctx.STR_LIT():
            return StringLiteral(ctx.getText())
    
    def visitArray_lit(self, ctx:PYMJCParser.Array_litContext):
        lits = []
        for l in ctx.literal():
            lit = self.visit(l)
            lits.append(lit)
        return ArrayLiteral(lits)

    # Visit a parse tree produced by PYMJCParser#listID.
    def visitListID(self, ctx:PYMJCParser.ListIDContext):
        if ctx.CM():
            if ctx.ASSIGN():
                return [(Id(ctx.ID().getText()), self.visit(ctx.exp()))] + self.visit(ctx.listID())
            else:
                return [(Id(ctx.ID().getText()), None)] + self.visit(ctx.listID())
        else:
            if ctx.ASSIGN():
                return [(Id(ctx.ID().getText()), self.visit(ctx.exp()))] 
            else:
                return [(Id(ctx.ID().getText()), None)] 

    # Visit a parse tree produced by PYMJCParser#ids_att.
    def visitIds_att(self, ctx:PYMJCParser.Ids_attContext):
        if ctx.CM():
            if ctx.ASSIGN_ATT():
                return [(Id(ctx.ID().getText()), self.visit(ctx.exp()))] + self.visit(ctx.ids_att())
            else:
                return [(Id(ctx.ID().getText()), None)] + self.visit(ctx.ids_att())
        else:
            if ctx.ASSIGN_ATT():
                return [(Id(ctx.ID().getText()), self.visit(ctx.exp()))] 
            else:
                return [(Id(ctx.ID().getText()), None)] 