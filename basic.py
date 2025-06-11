class Lexer:
    def __init__(self, text):
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char =self.text[self.idx]
        self.token = None 
        pass

    def tokenize(self):
        while self.idx < len(self.text):
            print(f"Current char: {self.text[self.idx]}")
            self.idx += 1
    

a = Lexer("5 + 3")
a.tokenize()