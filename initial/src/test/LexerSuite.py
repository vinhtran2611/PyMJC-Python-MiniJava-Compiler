import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    num = 100
    # def test_lowercase_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.test("aAsVN3", "aAsVN3,<EOF>", 103))

    # def test_mixed_id(self):
    #     self.assertTrue(TestLexer.test("aAsVN3", "aAsVN3,<EOF>", 103))

    # def test_underscore_id(self):
    #     self.assertTrue(TestLexer.test("_abc", "_abc,<EOF>", 103))

    def test_mutable_decl_attr(self):
        self.assertTrue(
            TestLexer.test(
                "class a {     \
                    final int a;            \
                }",
                "class,a,{,final,int,a,;,},<EOF>", LexerSuite.num
            )
        )
        LexerSuite.num += 1

        self.assertTrue(
            TestLexer.test(
                "class a {     \
                    final int a;            \
                    final float b, c;            \
                    final string e;            \
                    final boolean f;            \
                    final int[5] g;            \
                }",
                "class,a,{,final,int,a,;,final,float,b,,,c,;,final,string,e,;,final,boolean,f,;,final,int,[,5,],g,;,},<EOF>", 
                LexerSuite.num
            )
        )
        LexerSuite.num += 1
    
    def test_mutable_decl_method(self):
        self.assertTrue(
            TestLexer.test(
                "class a {              \
                    final int a(int x){};      \
                }",
                "class,a,{,final,int,a,(,int,x,),{,},;,},<EOF>", LexerSuite.num
            )
        )
        LexerSuite.num += 1

    def test_immutable_decl_attr(self):
        self.assertTrue(
            TestLexer.test(
                "class a {     \
                    static int a;            \
                }",
                "class,a,{,static,int,a,;,},<EOF>", LexerSuite.num
            )
        )
        LexerSuite.num += 1
    
    def test_immutable_decl_method(self):
        self.assertTrue(
            TestLexer.test(
                "class a {     \
                    static int a() {};            \
                }",
                "class,a,{,static,int,a,(,),{,},;,},<EOF>", LexerSuite.num
            )
        )
        LexerSuite.num += 1
    
    def test_final_and_static(self):
        self.assertTrue(
            TestLexer.test(
                "class a {     \
                    final static int a;            \
                    static final int c;            \
                }",
                "class,a,{,final,static,int,a,;,static,final,int,c,;,},<EOF>", LexerSuite.num
            )
        )
        LexerSuite.num += 1



    # def test_block_comment(self):
    #     """test block comment"""
    #     self.assertTrue(
    #         TestLexer.test(
    #             "/* This is a block comment so # has no meaning here */", "<EOF>", 105
    #         )
    #     )
    #     self.assertTrue(
    #         TestLexer.test(
    #             "abc def/* This is a block comment so # has no meaning here */",
    #             "abc,def,<EOF>",
    #             106,
    #         )
    #     )
    #     self.assertTrue(
    #         TestLexer.test(
    #             "21abc def/* This is a block comment so # has no meaning here */",
    #             "21,abc,def,<EOF>",
    #             107,
    #         )
    #     )

    # def test_line_comment(self):
    #     """test line comment"""
    #     self.assertTrue(
    #         TestLexer.test(
    #             "#This is a block comment so # has no meaning here */", "<EOF>", 108
    #         )
    #     )
    #     self.assertTrue(
    #         TestLexer.test(
    #             "abc dfg #This is a block comment so # has no meaning here */",
    #             "abc,dfg,<EOF>",
    #             109,
    #         )
    #     )

    # def test_arithmetic_operator(self):
    #     self.assertTrue(TestLexer.test("+-*/", "+,-,*,/,<EOF>", 110))
    #     self.assertTrue(TestLexer.test("a+b-c*d/e", "a,+,b,-,c,*,d,/,e,<EOF>", 111))
    #     self.assertTrue(TestLexer.test("a\\b%C", "a,\,b,%,C,<EOF>", 112))

    # def test_logic_operator(self):
    #     self.assertTrue(
    #         TestLexer.test("a != b == c < d > e", "a,!=,b,==,c,<,d,>,e,<EOF>", 113)
    #     )
    #     self.assertTrue(
    #         TestLexer.test(
    #             "a >= b <= c || d && e ^ f", "a,>=,b,<=,c,||,d,&&,e,^,f,<EOF>", 114
    #         )
    #     )

    # def test_new_operator(self):
    #     self.assertTrue(TestLexer.test("a new b", "a,new,b,<EOF>", 115))

    # def test_separator(self):
    #     self.assertTrue(TestLexer.test("[]{}()", "[,],{,},(,),<EOF>", 116))
    #     self.assertTrue(TestLexer.test("int a,c;", "int,a,,,c,;,<EOF>", 117))

    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 104))
    #     self.assertTrue(TestLexer.test("0 100 255 2500", "0,100,255,2500,<EOF>", 118))

    # def test_float(self):
    #     """test float"""
    #     self.assertTrue(
    #         TestLexer.test(
    #             "9.0 12e8 1. 0.33E-3 128e+42", "9.0,12e8,1.,0.33E-3,128e+42,<EOF>", 119
    #         )
    #     )

    # def test_boolean(self):
    #     """test boolean"""
    #     self.assertTrue(TestLexer.test("int a := true;", "int,a,:=,true,;,<EOF>", 120))

    # def test_string_lit(self):
    #     """test string literal"""
    #     self.assertTrue(TestLexer.test('s := "abc"', 's,:=,"abc",<EOF>', 121))
    #     self.assertTrue(
    #         TestLexer.test(
    #             '"This is a string containing tab \t"',
    #             '"This is a string containing tab \t",<EOF>',
    #             122,
    #         )
    #     )
    #     self.assertTrue(
    #         TestLexer.test(
    #             '"He asked me: "Where is John?""',
    #             '"He asked me: "Where is John?"",<EOF>',
    #             123,
    #         )
    #     )

    # def test_array_same_type(self):
    #     """test array literal same type"""
    #     # self.assertTrue(
    #     #     TestLexer.test("int[] a := {1,2,3};", "int,[,],a,:=,{1,2,3},;,<EOF>", 124)
    #     # )
    #     # self.assertTrue(
    #     #     TestLexer.test(
    #     #         "int[] a := {2.3,4.2,102e3};", "int,[,],a,:=,{2.3,4.2,102e3},;,<EOF>", 125
    #     #     )
    #     # )
    #     self.assertTrue(
    #         TestLexer.test(
    #             "int[] a := {1,        2,                 3};",
    #             "int,[,],a,:=,{,1,,,2,,,3,},;,<EOF>",
    #             126,
    #         )
    #     )

    # def test_array_mix_type(self):
    #     """test array literal mix type"""
    #     self.assertTrue(
    #         TestLexer.test("a := {1,        2.0}", "a,:=,{,1,,,2.0,},<EOF>", 127)
    #     )

    # def test_neg_number(self):
    #     """test negative number"""
    #     self.assertTrue(
    #         TestLexer.test("a", "a,<EOF>", 128)
    #     )

    # def test_assign(self):
    #     """test negative number"""
    #     self.assertTrue(
    #         TestLexer.test("a := b + 4", "a,:=,b,+,4,<EOF>", 130)
    #     )

    # def test_invalid_char(self):
    #     """test invalid char"""
    #     self.assertTrue(
    #         TestLexer.test("abc?bcd", "abc,Error Token ?", 130)
    #     )

    # def test_error_extends(self):
    #     """test invalid extends"""
    #     self.assertTrue(
    #         TestLexer.test("class ABC extends { }", "class,ABC,extends,{,},<EOF>", 131)
    #     )
