import unittest
from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data

class TestCatg(unittest.TestCase):
    def setUp(self):
        self.data = Data()

    def run_code(self, code):
        tokenizer = Lexer(code)
        tokens = tokenizer.tokenize()
        parser = Parser(tokens)
        tree = parser.parse()
        interpreter = Interpreter(tree, self.data)
        return interpreter.interpret()

    def read_numeric(self, var_name):
        """Helper: Read variable value and convert to float for comparison."""
        var = self.data.read(var_name)
        if var is None:
            return None
        return float(var.value)

    def test_variable_assignment(self):
        self.run_code("make x = 5")
        self.assertEqual(self.read_numeric("x"), 5.0)

    def test_arithmetic_addition(self):
        self.run_code("make x = 5 + 3")
        self.assertEqual(self.read_numeric("x"), 8.0)

    def test_arithmetic_subtraction(self):
        self.run_code("make x = 10 - 4")
        self.assertEqual(self.read_numeric("x"), 6.0)

    def test_arithmetic_multiplication(self):
        self.run_code("make x = 3 * 2")
        self.assertEqual(self.read_numeric("x"), 6.0)

    def test_arithmetic_division(self):
        self.run_code("make x = 8 / 2")
        self.assertEqual(self.read_numeric("x"), 4.0)

    def test_while_loop(self):
        self.run_code("make x = 3")
        self.run_code("while x > 0 do make x = x - 1")
        self.assertEqual(self.read_numeric("x"), 0.0)

    def test_if_else_true(self):
        self.run_code("make x = 0")
        self.run_code("if 1 ?= 1 do make x = 10 else do make x = 20")
        self.assertEqual(self.read_numeric("x"), 10.0)

    def test_if_else_false(self):
        self.run_code("make x = 0")
        self.run_code("if 1 ?= 0 do make x = 10 else do make x = 20")
        self.assertEqual(self.read_numeric("x"), 20.0)

    def test_comparison_gt(self):
        result = self.run_code("5 > 3")
        self.assertEqual(result.value, 1)

    def test_comparison_eq_false(self):
        result = self.run_code("5 ?= 3")
        self.assertEqual(result.value, 0)

    def test_comparison_eq_true(self):
        result = self.run_code("5 ?= 5")
        self.assertEqual(result.value, 1)

    def test_boolean_and(self):
        result = self.run_code("1 and 0")
        self.assertEqual(result.value, 0)

    def test_boolean_or(self):
        result = self.run_code("1 or 0")
        self.assertEqual(result.value, 1)

    def test_unary_minus(self):
        result = self.run_code("-5")
        self.assertEqual(result.value, -5)

    def test_unary_not(self):
        result = self.run_code("not 1")
        self.assertEqual(result.value, 0)

        result = self.run_code("not 0")
        self.assertEqual(result.value, 1)

if __name__ == "__main__":
    unittest.main()
