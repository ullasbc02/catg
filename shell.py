from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data

base = Data()
text = input("catg:> ")

tokenizer = Lexer(text)
tokens = tokenizer.tokenize()
print("Tokens:", tokens)

parser = Parser(tokens)
tree = parser.parse()
print("Parse Tree:", tree)

interpreter = Interpreter(tree, base)
result = interpreter.interpret()
print("Result:", result)
