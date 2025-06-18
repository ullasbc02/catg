from basic import Lexer
from parse import Parser
from interpreter import Interpreter

text = input("catg:> ")

tokenizer = Lexer(text)
tokens = tokenizer.tokenize()

# print("Tokens:", tokens)

parser = Parser(tokens)
tree = parser.parse()

interpreter = Interpreter(tree)
result = interpreter.interpret()
print("Result:", result)
