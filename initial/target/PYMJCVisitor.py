# Generated from main/pymjc/parser/PYMJC.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PYMJCParser import PYMJCParser
else:
    from PYMJCParser import PYMJCParser

# This class defines a complete generic visitor for a parse tree produced by PYMJCParser.

class PYMJCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PYMJCParser#program.
    def visitProgram(self, ctx:PYMJCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#class_decl.
    def visitClass_decl(self, ctx:PYMJCParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#member.
    def visitMember(self, ctx:PYMJCParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#attribute_decl.
    def visitAttribute_decl(self, ctx:PYMJCParser.Attribute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#immutable.
    def visitImmutable(self, ctx:PYMJCParser.ImmutableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#mutable.
    def visitMutable(self, ctx:PYMJCParser.MutableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#var_decl_att.
    def visitVar_decl_att(self, ctx:PYMJCParser.Var_decl_attContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#var_decl.
    def visitVar_decl(self, ctx:PYMJCParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#method_decl.
    def visitMethod_decl(self, ctx:PYMJCParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#params.
    def visitParams(self, ctx:PYMJCParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#for_stmt.
    def visitFor_stmt(self, ctx:PYMJCParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#assign_stmt.
    def visitAssign_stmt(self, ctx:PYMJCParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#if_stmt.
    def visitIf_stmt(self, ctx:PYMJCParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#method_invocation.
    def visitMethod_invocation(self, ctx:PYMJCParser.Method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#list_exp.
    def visitList_exp(self, ctx:PYMJCParser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#block_stmt.
    def visitBlock_stmt(self, ctx:PYMJCParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#stmt.
    def visitStmt(self, ctx:PYMJCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#exp.
    def visitExp(self, ctx:PYMJCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#lhs.
    def visitLhs(self, ctx:PYMJCParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#literal.
    def visitLiteral(self, ctx:PYMJCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#bktype.
    def visitBktype(self, ctx:PYMJCParser.BktypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#array_lit.
    def visitArray_lit(self, ctx:PYMJCParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#listID.
    def visitListID(self, ctx:PYMJCParser.ListIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PYMJCParser#ids_att.
    def visitIds_att(self, ctx:PYMJCParser.Ids_attContext):
        return self.visitChildren(ctx)



del PYMJCParser