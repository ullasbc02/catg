from basic import Lexer
from parse import Parser

text = input("catg:> ")

tokenizer = Lexer(text)
tokens = tokenizer.tokenize()

print("Tokens:", tokens)

parser = Parser(tokens)
print("Parsed Expression:", parser.parse())
