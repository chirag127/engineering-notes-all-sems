### 13. Write a program to perform constant propagation.

Constant propagation is a compiler optimization technique that replaces the use of a variable with its constant value, if the value of the variable is known at compile time. This can improve the performance and readability of the code, and also enable further optimizations.

A program to perform constant propagation can be written in the following steps:

- Define a data structure to represent the abstract syntax tree (AST) of the program. The AST should have nodes for variables, constants, operators, assignments, and control flow statements.
- Define a function to traverse the AST in a depth-first order, and maintain a map of variables and their constant values. The map should be updated whenever an assignment of a constant to a variable is encountered, and the map should be copied when entering a new scope.
- Define a function to replace the use of a variable with its constant value, if the variable is in the map. The function should also simplify the expressions involving constants, such as arithmetic operations and comparisons.
- Define a function to print the modified AST in a readable format, or generate the corresponding code.

Here is an example of a program to perform constant propagation in Python:

```python
# Define the AST node class
class Node:
    def __init__(self, type, value=None, children=None):
        self.type = type # the type of the node, such as "var", "const", "add", "assign", etc.
        self.value = value # the value of the node, such as a variable name, a constant value, etc.
        self.children = children # a list of child nodes, if any

# Define a function to traverse the AST and perform constant propagation
def propagate_constants(node, const_map):
    # If the node is a variable, replace it with its constant value if possible
    if node.type == "var":
        if node.value in const_map:
            node.type = "const"
            node.value = const_map[node.value]
    # If the node is an assignment, update the constant map and propagate constants to the right-hand side
    elif node.type == "assign":
        lhs = node.children[0]
        rhs = node.children[1]
        propagate_constants(rhs, const_map)
        # If the right-hand side is a constant, update the constant map with the variable and the value
        if rhs.type == "const":
            const_map[lhs.value] = rhs.value
    # If the node is a control flow statement, copy the constant map and propagate constants to the branches
    elif node.type in ["if", "while"]:
        cond = node.children[0]
        then_branch = node.children[1]
        else_branch = node.children[2] if len(node.children) > 2 else None
        propagate_constants(cond, const_map.copy())
        propagate_constants(then_branch, const_map.copy())
        if else_branch:
            propagate_constants(else_branch, const_map.copy())
    # If the node is an operator, propagate constants to the operands and simplify the expression if possible
    elif node.type in ["add", "sub", "mul", "div", "mod", "eq", "ne", "lt", "gt", "le", "ge", "and", "or", "not"]:
        for child in node.children:
            propagate_constants(child, const_map)
        # If all the operands are constants, evaluate the expression and replace the node with a constant node
        if all(child.type == "const" for child in node.children):
            node.type = "const"
            if node.type == "add":
                node.value = node.children[0].value + node.children[1].value
            elif node.type == "sub":
                node.value = node.children[0].value - node.children[1].value
            elif node.type == "mul":
                node.value = node.children[0].value * node.children[1].value
            elif node.type == "div":
                node.value = node.children[0].value / node.children[1].value
            elif node.type == "mod":
                node.value = node.children[0].value % node.children[1].value
            elif node.type == "eq":
                node.value = node.children[0].value == node.children[1].value
            elif node.type == "ne":
                node.value = node.children[0].value != node.children[1].value
            elif node.type == "lt":
                node.value = node.children[0].value < node.children[1].value
            elif node.type == "gt":
                node.value = node.children[0].value > node.children[1].value
            elif node.type == "le":
                node