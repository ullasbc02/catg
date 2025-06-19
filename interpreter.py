from tokens import Integer, Float
class Interpreter:
    def __init__(self, tree, base):
        self.tree = tree
        self.data = base

    def read_INT(self, value):
        return int(value)
    def read_FLT(self, value):
        return float(value)
    
    #perform make a = 5
    #perform make b = 4 + 6
    
    def compute_binary_operation(self, left, operator, right):
        left_type = str(left.type)
        right_type = str(right.type)

        if operator.value == "=":
            left.type = f"VAR({right_type})"
            self.data.write(left, right)
            return self.data.read_all()

        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self, f"read_{right_type}")(right.value)

        if operator.value == "+":
            output = left + right
        elif operator.value == "-":
            output = left - right
        elif operator.value == "*":
            output = left * right
        elif operator.value == "/":
            output = left / right

        return Integer(output) if (left_type == "INT" and right_type == "INT" and operator.value != "/") else Float(output)

    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree

        left_node = tree[0]
        if isinstance(left_node, list): # Check if left_node is a list
            left_node = self.interpret(left_node)

        right_node = tree[2]
        if isinstance(right_node, list): # Check if right_node is a list
            right_node = self.interpret(right_node)
        operator = tree[1]


        return self.compute_binary_operation(left_node, operator, right_node)

    
