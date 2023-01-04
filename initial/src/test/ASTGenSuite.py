import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    num = 300
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}
        """
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect, self.num))
        self.num += 1

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class Shape {
            int a;
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[
            AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))]
        )]))
        self.assertTrue(TestAST.test(input,expect, self.num))
        self.num += 1

    # def test_class_with_two_decl_program(self):
    #     """More complex program"""
    #     input = """class Shape {
    #         int a,b,c,d;        
    #     }"""
    #     expect = str(Program([ClassDecl(Id("Shape"),[
    #         AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
    #         AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),
    #         AttributeDecl(Instance(),VarDecl(Id("c"),IntType())),
    #         AttributeDecl(Instance(),VarDecl(Id("d"),IntType())),
    #         ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_decl_init(self):
    #     """More complex program"""
    #     input = """class Shape {
    #         int a = 3;
    #         float b = 3.5;        
    #         boolean c= false;
    #         string d = "hello";
    #     }"""
    #     expect = str(Program([ClassDecl(Id("Shape"),[
    #         AttributeDecl(Instance(),VarDecl(Id("a"),IntType(), IntLiteral(3))),
    #         AttributeDecl(Instance(),VarDecl(Id("b"),FloatType(), FloatLiteral(3.5))),
    #         AttributeDecl(Instance(),VarDecl(Id("c"),BoolType(), BooleanLiteral(False))),
    #         AttributeDecl(Instance(),VarDecl(Id("d"),StringType(), StringLiteral('"hello"')))])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_extend_class(self):
    #     input = """class A extends B {}"""
    #     expect = str(Program([ClassDecl(Id("A"), [], Id("B"))]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_multi_class(self):
    #     input = """class A {}
    #     class B extends A {}"""
    #     expect = str(Program([ClassDecl(Id("A"), []), ClassDecl(Id("B"), [], Id("A"))]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_static_decl(self):
    #     input = """class A {
    #         static int a;
    #         static int a = 3;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Static(), VarDecl(Id("a"), IntType())),
    #         AttributeDecl(Static(), VarDecl(Id("a"), IntType(), IntLiteral(3)))])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_final_decl(self):
    #     input = """class A {
    #         final int b = 4;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), ConstDecl(Id("b"), IntType(), IntLiteral(4)))])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_final_decl(self):
    #     input = """class A {
    #         final int b = 4;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), ConstDecl(Id("b"), IntType(), IntLiteral(4)))])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    
    # def test_final_static_decl(self):
    #     input = """class A {
    #         static final int b = 4;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Static(), ConstDecl(Id("b"), IntType(), IntLiteral(4)))])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1
    
    # def test_decl_array(self):
    #     """Declare array"""
    #     input = """class Shape {
    #         int[2] a;        
    #     }"""
    #     expect = str(Program([ClassDecl(Id("Shape"),[
    #         AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(IntLiteral(2), IntType())))
    #         ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_decl_init_array_1(self):
    #     """init array with zero ele"""
    #     input = """class Shape {
    #         int[1] a = {};        
    #     }"""
    #     expect = str(Program([ClassDecl(Id('Shape'),[
    #         AttributeDecl(Instance(),VarDecl(Id('a'),ArrayType(IntLiteral(1),IntType()),ArrayLiteral([])))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_decl_init_array_2(self):
    #     """init multi element in array"""
    #     input = """class Shape {
    #         int[3] a = {1, 3, 4};        
    #     }"""
    #     expect = str(Program([ClassDecl(Id('Shape'),[
    #         AttributeDecl(Instance(),VarDecl(Id('a'),ArrayType(IntLiteral(3),IntType()),
    #         ArrayLiteral([IntLiteral(1), IntLiteral(3), IntLiteral(4)])))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    
    # def test_method_decl(self):
    #     '''test declare method without params'''
    #     input = """class A {
    #         int a;
    #         int get(){}
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("get"), [], IntType(), Block([], []))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1
    
    # # def test_method_decl_with_param(self):
    # #     '''test declare method with params, body empty'''
    # #     input = """class A {
    # #         int a;
    # #         int get(int c){}
    # #     }"""
    # #     expect = str(Program([ClassDecl(Id("A"), [
    # #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    # #         MethodDecl(Instance(), Id("get"), [VarDecl(Id('c'), IntType())], IntType(), [])
    # #     ])]))
    # #     self.assertTrue(TestAST.test(input,expect, self.num))
    # #     self.num += 1
    
    # # def test_method_decl_multi_param(self):
    # #     '''test declare method multi params, body empty'''
    # #     input = """class A {
    # #         int a;
    # #         int get(int c,d; float b){}
    # #     }"""
    # #     expect = str(Program([ClassDecl(Id("A"), [
    # #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    # #         MethodDecl(Instance(), Id("get"), 
    # #             [VarDecl(Id('c'), IntType()), VarDecl(Id('d'), IntType()), VarDecl(Id('b'), FloatType())], IntType(), []),
    # #     ])]))
    # #     self.assertTrue(TestAST.test(input,expect, self.num))
    # #     self.num += 1

    
    # def test_constructor(self):
    #     '''test declare constructor'''
    #     input = """class Shape {
    #         int a;
    #         Shape(){}
    #     }"""
    #     expect = str(Program([ClassDecl(Id("Shape"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("Shape"), [], None, Block([], []))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1
    
    # def test_void_type(self):
    #     '''test decl method void type'''
    #     input = """class Shape {
    #         int a;
    #         void f(){}
    #     }"""
    #     expect = str(Program([ClassDecl(Id("Shape"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("f"), [], VoidType(), Block([], []))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1
    
    # def test_body_non_empty(self):
    #     '''test declare method with body non empty'''
    #     input = """class A {
    #         int a;
    #         int get(int b){
    #             int c := 2;
    #             #float d := 3.2;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("get"), [VarDecl(Id('b'), IntType())], IntType(), Block([VarDecl(Id('c'), IntType(), IntLiteral(2))], []))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1
    
    # def test_return_stmt(self):
    #     '''test return statment'''
    #     input = """class A {
    #         int a;
    #         int get(int b){
    #             int c := 2;
    #             #float d := 3.2;
    #             return c;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("get"), [VarDecl(Id('b'), IntType())], IntType(), 
    #             Block([VarDecl(Id('c'), IntType(), IntLiteral(2))], [Return(Id('c'))]))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1
        
    # def test_if(self):
    #     '''test if statment'''
    #     input = """class A {
    #         int a;
    #         int get(int n){
    #             if (n == 0) then return 1;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("get"), [VarDecl(Id('n'), IntType())], IntType(), 
    #             Block([], [
    #                 If(BinaryOp('==', Id('n'), IntLiteral(0)), Return(IntLiteral(1)))
    #             ]))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_if_else(self):
    #     '''test if else statment'''
    #     input = """class A {
    #         int a;
    #         int factorial(int n){
    #             if (n == 0) then return 1; else return n * this.factorial(n - 1);
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("factorial"), [VarDecl(Id('n'), IntType())], IntType(), 
    #             Block([], [
    #                 If(BinaryOp('==', Id('n'), IntLiteral(0)), Return(IntLiteral(1)), Return(BinaryOp('*', Id('n'), CallExpr(Id("this"), Id("factorial"), [BinaryOp('-', Id('n'), IntLiteral(1))]))))
    #             ]))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1
    
    # def test_method_invocation(self):
    #     '''test call method statment'''
    #     input = """class A {
    #         int a;
    #         int factorial(int n){
    #             this.factorial(n - 1);
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("factorial"), [VarDecl(Id('n'), IntType())], IntType(), 
    #             Block([], [
    #                 CallStmt(Id("this"), Id('factorial'), [BinaryOp('-', Id('n'), IntLiteral(1))])
    #             ])
    #         )
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_for_stmt(self): 
    #     '''test for statment non {}'''
    #     input = """class A {
    #         int a;
    #         int get(int n){
    #             for x := 5 downto 2 do c := 2;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("get"), [VarDecl(Id('n'), IntType())], IntType(), 
    #             Block([], [
    #                 For(Id('x'), IntLiteral(5), IntLiteral(2), False, Assign(Id('c'), IntLiteral(2)))
    #             ]))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_for_stmt_block(self): 
    #     '''test for statment with block stmt'''
    #     input = """class A {
    #         int a;
    #         int get(int n){
    #             for x := 5 downto 2 do 
    #                 {c := 2; 
    #                 d := 3;}
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("get"), [VarDecl(Id('n'), IntType())], IntType(), 
    #             Block([], [
    #                 For(Id('x'), IntLiteral(5), IntLiteral(2), False, Block([], [Assign(Id('c'), IntLiteral(2)), Assign(Id('d'), IntLiteral(3))]))
    #             ]))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_break(self): 
    #     '''test break statment'''
    #     input = """class A {
    #         int a;
    #         int get(int n){
    #             for x := 5 downto 2 do 
    #                 {if x == 3 then break;}
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("get"), [VarDecl(Id('n'), IntType())], IntType(), 
    #             Block([], [
    #                 For(Id('x'), IntLiteral(5), IntLiteral(2), False, Block([], [If(BinaryOp('==', Id('x'), IntLiteral(3)), Break())]))
    #             ]))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_break(self): 
    #     '''test break statment'''
    #     input = """class A {
    #         int a;
    #         int get(int n){
    #             for x := 5 downto 2 do 
    #                 {if (x == 3) then continue;}
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id("A"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("get"), [VarDecl(Id('n'), IntType())], IntType(), 
    #             Block([], [
    #                 For(Id('x'), IntLiteral(5), IntLiteral(2), False, Block([], [If(BinaryOp('==', Id('x'), IntLiteral(3)), Continue())]))
    #             ]))
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1


    # def test_main(self):
    #     '''test main func'''
    #     input = """
    #     class Example1 {

    #         void main(){
    #             int x;
    #             x := io.readInt();
    #             io.writeIntLn(this.factorial(x));
    #         }
            
    #     }
    #     """
    #     expect = str(Program([ClassDecl(Id("Example1"), [
    #         MethodDecl(Instance(), Id('main'), [], VoidType(), Block(
    #             [VarDecl(Id('x'), IntType())], 
    #             [Assign(Id('x'), CallExpr(Id('io'), Id('readInt'), [])), CallStmt(Id('io'), Id('writeIntLn'), [CallExpr(Id('this'), Id('factorial'), [Id('x')])])]))
            
    #     ])]))
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_field_access(self):
    #     '''test field access statment'''
    #     input = """
    #     class Rectangle extends Shape {
    #         float getArea(){
    #             return this.length * this.width;
    #         }
    #     }
    #     """

    #     expect = str(Program([
    #         ClassDecl(Id('Rectangle'), [
    #             MethodDecl(Instance(), Id('getArea'), [], FloatType(), Block([], [Return(BinaryOp('*', FieldAccess(Id('this'), Id('length')), FieldAccess(Id('this'), Id('width'))))])),
    #         ], Id('Shape')),
    #     ]))
        
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_program_1(self):
    #     '''test return statment'''
    #     input = """
    #     class Example1 {
    #         int a;
    #         int factorial(int n){
    #             if n == 0 then return 1; else return n * this.factorial(n - 1);
    #         }
            
    #         void main(){
    #             int x;
    #             x := io.readInt();
    #             io.writeIntLn(this.factorial(x));
    #         }
            
    #     }
    #     """

    #     expect = str(Program([ClassDecl(Id("Example1"), [
    #         AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
    #         MethodDecl(Instance(), Id("factorial"), [VarDecl(Id('n'), IntType())], IntType(), 
    #             Block([], [
    #                 If(BinaryOp('==', Id('n'), IntLiteral(0)), Return(IntLiteral(1)), Return(BinaryOp('*', Id('n'), CallExpr(Id("this"), Id("factorial"), [BinaryOp('-', Id('n'), IntLiteral(1))]))))
    #             ])), 
    #         MethodDecl(Instance(), Id('main'), [], VoidType(), Block(
    #             [VarDecl(Id('x'), IntType())], 
    #             [Assign(Id('x'), CallExpr(Id('io'), Id('readInt'), [])), CallStmt(Id('io'), Id('writeIntLn'), [CallExpr(Id('this'), Id('factorial'), [Id('x')])])]))
            
    #     ])]))
        
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1

    # def test_program_2(self):
    #     '''test return statment'''
    #     input = """
    #     class Shape {
    #         float length, width;
    #         float getArea() {}
            
    #         Shape(float l, w){
    #             this.length := l;
    #             this.width := w;
    #         }
    #     }
        
    #     class Rectangle extends Shape {
    #         float getArea(){
    #             return this.length * this.width;
    #         }
    #     }

        
    #     class Triangle extends Shape {
    #         float getArea(){
    #             return this.length*this.width / 2;
    #         }
    #     }
    #     class Example2 {
    #         void main(){
    #             Shape s;
    #             s := new Rectangle(3,4);
    #             io.writeFloatLn(s.getArea());
    #             s := new Triangle(3,4);
    #             io.writeFloatLn(s.getArea());
    #             a := b := 3;
    #         }
    #     }
    #     """

    #     expect = str(Program([
    #         ClassDecl(Id('Shape'), [
    #             AttributeDecl(Instance(), VarDecl(Id('length'), FloatType())),
    #             AttributeDecl(Instance(), VarDecl(Id('width'), FloatType())),
    #             MethodDecl(Instance(), Id('getArea'), [], FloatType(), Block([], [])),
    #             MethodDecl(Instance(), Id('Shape'), [VarDecl(Id('l'), FloatType()), VarDecl(Id('w'), FloatType())], None, Block([], [Assign(FieldAccess(Id('this'), Id('length')), Id('l')), Assign(FieldAccess(Id('this'), Id('width')), Id('w'))])),
    #         ]),
    #         ClassDecl(Id('Rectangle'), [
    #             MethodDecl(Instance(), Id('getArea'), [], FloatType(), Block([], [Return(BinaryOp('*', FieldAccess(Id('this'), Id('length')), FieldAccess(Id('this'), Id('width'))))])),
    #         ], Id('Shape')),
    #         ClassDecl(Id('Triangle'), [
    #             MethodDecl(Instance(), Id('getArea'), [], FloatType(), Block([], [Return(BinaryOp('/', BinaryOp('*', FieldAccess(Id('this'), Id('length')), FieldAccess(Id('this'), Id('width'))), IntLiteral(2)))])),
    #         ], Id('Shape')),
    #         ClassDecl(Id('Example2'), [
    #             MethodDecl(Instance(), Id('main'), [], VoidType(), Block(
    #                 [
    #                     VarDecl(Id('s'), ClassType(Id('Shape'))),
    #                 ],
    #                 [
    #                     Assign(Id('s'), NewExpr(Id('Rectangle'), [IntLiteral(3), IntLiteral(4)])),
    #                     CallStmt(Id('io'), Id('writeFloatLn'), [CallExpr(Id('s'), Id("getArea"), [])]),
    #                     Assign(Id('s'), NewExpr(Id('Triangle'), [IntLiteral(3), IntLiteral(4)])),
    #                     CallStmt(Id('io'), Id('writeFloatLn'), [CallExpr(Id('s'), Id("getArea"), [])]),
    #                     Assign(Id('b'), IntLiteral(3)),
    #                     Assign(Id('a'), Id('b')),
    #                 ]
    #             ))
    #         ]),
    #     ]))
        
    #     self.assertTrue(TestAST.test(input,expect, self.num))
    #     self.num += 1