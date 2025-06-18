class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]

    def factor(self):
        if self.token.type == "INT" or self.token.type == "FLT":
            result = self.token
            self.move()
            return result
        elif self.token =="(":
            self.move()
            result = self.expression()
            return result

    def term(self):  # 1 * 2 or 1 / 2
        left = self.factor()
        while self.token is not None and self.token.type == "OP" and self.token.value in ("*", "/"):
            operation = self.token
            self.move()
            right = self.factor()
            left = [left, operation, right]
        return left

    def expression(self):  # 1 + 2 * 3
        left = self.term()
        while self.token is not None and self.token.type == "OP" and self.token.value in ("+", "-"):
            operation = self.token
            self.move()
            right = self.term()
            left = [left, operation, right]
        return left

    def parse(self):
        return self.expression()

    def move(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
        else:
            self.token = None


