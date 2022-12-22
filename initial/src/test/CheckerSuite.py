import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):  
    num = 400
    # def test_redeclare_class(self):
    #     input = """class main {}
    #     class main {}"""
    #     expect = "Redeclared Class: main"
    #     self.assertTrue(TestChecker.test(input, expect, CheckerSuite.num))
    #     CheckerSuite.num += 1

    # def test_redeclare_attr(self):
    #     input = """class main {
    #         int a, a;
    #     }"""
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input, expect, CheckerSuite.num))
    #     CheckerSuite.num += 1

    # def test_redeclare_method(self):
    #     input = """class main {
    #         int a;
    #         int a() {}
    #     }"""
    #     expect = "Redeclared Method: a"
    #     self.assertTrue(TestChecker.test(input,expect,CheckerSuite.num))
    #     CheckerSuite.num += 1

    # def test_constant_decl(self):
    #     input = """class main {
    #         final int a = 12.3;
    #         int foo() {}
    #     }"""
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(12.3))"
    #     self.assertTrue(TestChecker.test(input,expect,CheckerSuite.num))
    #     CheckerSuite.num += 1
    
    # def test_constant_decl_02(self):
    #     input = """class main {
    #         final int a = true;
    #         int foo() {}
    #     }"""
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input,expect,CheckerSuite.num))
    #     CheckerSuite.num += 1

    # def test_constant_decl_non_init(self):
    #     input = """class main {
    #         final int a;
    #         int foo() {}
    #     }"""
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,CheckerSuite.num))
    #     CheckerSuite.num += 1

    # def test_redecl_constant(self):
    #     input = """class main {
    #         final int a, a;
    #         int foo() {}
    #     }"""
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,CheckerSuite.num))
    #     CheckerSuite.num += 1

    # def test_redecl_constant(self):
    #     input = """class main {
    #         final int a;
    #         int foo() {
    #             final int a;
    #         }
    #     }"""
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,CheckerSuite.num))
    #     CheckerSuite.num += 1

    def test_redecl_constant_02(self):
        input = """class main {
            final int a = 3;
            int foo() {
                final int a := 8;
            }
        }"""
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,CheckerSuite.num))
        CheckerSuite.num += 1

    # def test_attr_decl(self):
    #     input = """class main {
    #         int a = 1.2;
    #         int foo() {}
    #     }"""
    #     expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),IntType,FloatLit(1.2))"
    #     self.assertTrue(TestChecker.test(input,expect,CheckerSuite.num))
    #     CheckerSuite.num += 1

    # def test_03(self):
    #     input = """class main {
    #         static int a;
    #         static int a;
    #     }"""
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_04(self):
    #     input = """class main {
    #         void a () {
    #             int a;
    #             int a;
    #         }
    #     }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_05(self):
    #     input = """class main {
    #         static A t;
    #         static void x () {
    #             int a;
    #         }
    #     }
    #     class abc {
    #         abc x;
    #     }
    #     """
    #     expect = "Undeclared Class: A"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_06(self):
    #     input = """class main {
    #         final int a = 1.0 % 2;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(1.0),IntLit(2))"
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test_07(self):
    #     input = """class main {
    #         int a () {
    #             int t;
    #             t := 0.5;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(t),FloatLit(0.5))"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_08(self):
    #     input = """class main {
    #         int t;
    #         int a () {
    #             t := 1.0 + 2;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(t),BinaryOp(+,FloatLit(1.0),IntLit(2)))"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_09(self):
    #     input = """class main {
    #         int t;
    #         int a () {
    #             int tmp;
    #             tmp := abc.def;
    #         }
    #     }
    #     class abc {
    #         int def;
    #     }
    #     """
    #     expect = "Illegal Member Access: FieldAccess(Id(abc),Id(def))"
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # def test_10(self):
    #     input = """class main {
    #         int t;
    #         int a () {
    #             int tmp;
    #             tmp := abc.c;
    #         }
    #     }
    #     class abc {
    #         int def;
    #     }
    #     """
    #     expect = "Undeclared Identifier: c"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_11(self):
    #     input = """class main {
    #         int t;
    #         int a () {
    #             int tmp;
    #             abc x;
    #             tmp := x.def;
    #         }
    #     }
    #     class abc {
    #         static int def;
    #     }
    #     """
    #     expect = "Illegal Member Access: FieldAccess(Id(x),Id(def))"
    #     self.assertTrue(TestChecker.test(input,expect,411))

    # def test_12(self):
    #     input = """class main extends abc {
    #         int t;
    #         int a () {
    #             int tmp;
    #             tmp := this.def;
    #         }
    #     }
    #     class abc {
    #         static int def;
    #     }
    #     """
    #     expect = "Illegal Member Access: FieldAccess(Self(),Id(def))"
    #     self.assertTrue(TestChecker.test(input,expect,412))

    # def test_13(self):
    #     input = """class main extends abc {
    #         int t;
    #         float c;
    #         int a (int tmp) {
    #             int tmp;
    #             tmp := 1 + 2;
    #         }
    #     }
    #     """
    #     expect = "Redeclared Variable: tmp"
    #     self.assertTrue(TestChecker.test(input,expect,413))

    # def test_14(self):
    #     input = """class main extends abc {
    #         final int t = 6;
    #         int a (int tmp) {
    #             t := 5;
    #         }
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(t),IntLit(5))"
    #     self.assertTrue(TestChecker.test(input,expect,414))

    # def test_15(self):
    #     input = """class main extends abc {
    #         int a (int tmp) {
    #             final int t = 6;
    #             t := 5;
    #         }
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(t),IntLit(5))"
    #     self.assertTrue(TestChecker.test(input,expect,415))
