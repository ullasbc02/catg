from tokens import Integer, Float
class Interpreter:
    def __init__(self, tree, base):
        self.tree = tree
        self.data = base

    def read_INT(self, value):
        return int(value)
    def read_FLT(self, value):
        return float(value)
    
    def read_VAR(self, id):
        # Read variable from data store
        var = self.data.read(id)
        var_type = var.type

        return getattr(self, f"read_{var_type}")(var.value) if var else None
    
    #perform make a = 5
    #perform make b = 4 + 6
    
    def compute_binary_operation(self, left, operator, right):
        left_type = "VAR" if str(left.type).startswith("VAR") else str(left.type)
        right_type = "VAR" if str(right.type).startswith("VAR") else str(right.type)

        # ⚠️ Assignment: evaluate right side before writing
        if operator.value == "=":
            left.type = f"VAR({right_type})"
            self.data.write(left, right)
            return self.data.read_all()

        # Recursively interpret nested expressions
        if isinstance(left, list):
            left = self.interpret(left)
        if isinstance(right, list):
            right = self.interpret(right)

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

        return Integer(output) if (isinstance(output, int)) else Float(output)


    def compute_unary(self, operator, operand):
        operand_type = "VAR" if str(operand.type).startswith("VAR") else str(operand.type)
        operand = getattr(self, f"read_{operand_type}")(operand.value)

        if operator.value == "+":
            return +operand
        elif operator.value == "-":
            return -operand
        
    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree

        if isinstance(tree, list) and len(tree) == 2:
            # If tree is a single element list, interpret it directly
            return self.compute_unary(tree[0], tree[1])
        elif not isinstance(tree, list):
            # If tree is not a list or has less than 3 elements, return it directly
            return tree
        else:

        # Handle binary operations
            left_node = tree[0]
            if isinstance(left_node, list): # Check if left_node is a list
                left_node = self.interpret(left_node)

            right_node = tree[2]
            if isinstance(right_node, list): # Check if right_node is a list
                right_node = self.interpret(right_node)
            operator = tree[1]


            return self.compute_binary_operation(left_node, operator, right_node)

    
