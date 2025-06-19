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
            return self.expression()
        elif self.token.type.startswith("VAR"):
            return self.variable()


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

    def variable(self):
        if self.token.type.startswith("VAR"):
            var_node = self.token
            self.move()
            return var_node

    def statement(self):
        if self.token.type == "DECL":
            # Variable assignment
            self.move()
            left_node = self.variable()
            if self.token is not None and self.token.type == "OP" and self.token.value == "=":
                operator = self.token
                self.move()
                right_node = self.expression()
                return [left_node, operator, right_node]
            else:
                return left_node  # Just declaration, no assignment
        elif self.token.type in ("INT", "FLT", "OP"):
            # Arithmetic expression 
            return self.expression()

    def parse(self):
        return self.statement()

    def move(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
        else:
            self.token = None


