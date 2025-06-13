from basic import Lexer


text = input("catg:> ")
tokenizer = Lexer(text)
tokens = tokenizer.tokenize()
print("Tokens:", tokens)