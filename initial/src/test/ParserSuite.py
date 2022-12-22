import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class Shape {}"""
        input = """class Shape {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_attribute_decl(self):
        input = """class Shape{
            int numOfShape;
            float immuAttribute;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_init_attribute_decl(self):
        input = """class Shape{
            int numOfShape = 10;
            float immuAttribute = 0.20;
            int[2] x = {1, 2};

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    
    def test_static_final(self):
        input = """class Shape{
            static int a = 10;
            final float b = 0.20;
            static final int c = 10;
            final static float d = 0.20;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

        input2 = """class Shape{
            final int a = 1 + 4, b = 2;
            static float c,d = 0.20;
        }"""
        expect2 = "successful"
        self.assertTrue(TestParser.test(input2,expect2,205))

    def test_error_extend(self):
        """Miss ) int main( {}"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,206))
    
    def test_arithmetic_exp(self):
        input = """class Shape{
            final int a = 1 + 4, b = 2;
            static float c,d = 0.20;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_example1(self):
        input = """
        class Example1 {
            int factorial(int n){
                if n == 0 then return 1; else return n * this.factorial(n - 1);
            }
            void main(){
                int x;
                x := io.readInt();
                io.writeIntLn(this.factorial(x));
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_example2(self):
        input = """
        class Shape {
            float length, width;
            float getArea() {}
            Shape(float length, width){
                this.length := length;
                this.width := width;
            }
        }

        class Rectangle extends Shape {
            float getArea(){
                return this.length*this.width;
            }
        }
        class Triangle extends Shape {
            float getArea(){
                return this.length*this.width / 2;
            }
        }

        class Example2 {
            void main(){
                s := Shape;
                s := new Rectangle(3,4);
                io.writeFloatLn(s.getArea());
                s := new Triangle(3,4);
                io.writeFloatLn(s.getArea());
                a :=b := 3;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    
    def test_field_access(self):
        input = """class Shape{
            final int a = 1 + 4, b = 2;
            static float c,d = 0.20;

            void main(){
                x.b[2] := x.m()[3];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))