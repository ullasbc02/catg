class Lexer:
    digits = "0123456789"
    operators = "+-*/"
    stopwords = " "

    def __init__(self, text):
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char =self.text[self.idx]
        self.token = None 
        pass

    def tokenize(self):
        while self.idx < len(self.text):
            if self.text[self.idx] in Lexer.digits:
                self.token = self.extract_number()
            
            elif self.char in Lexer.operators:
                self.token = Operator(self.char)
                self.move()
            elif self.char in Lexer.stopwords:
                self.move()
                continue
            self.tokens.append(self.token)
        return self.tokens




    def extract_number(self):
        number = ""
        isFloat = False
        while self.idx < len(self.text) and (self.char in Lexer.digits or self.char == '.' ):
            if self.char == '.':
                isFloat = True
            number += self.char
            self.move()
    
        if isFloat:
            return Float(number)    
        return Integer(number)

    def move(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]


# Token classes for different types of tokens
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return str(self.value)

class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)

class Float(Token):
    def __init__(self, value):
        super().__init__("FLT", value)

class Operator(Token):
    def __init__(self, value):
        super().__init__("OP", value)


