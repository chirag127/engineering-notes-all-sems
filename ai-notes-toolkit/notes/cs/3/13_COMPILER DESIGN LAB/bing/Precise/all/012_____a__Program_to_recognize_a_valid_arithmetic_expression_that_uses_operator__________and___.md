### a) Program to recognize a valid arithmetic expression that uses operator +, – , * and /.

A valid arithmetic expression is a string of characters that represents a mathematical calculation. It can contain numbers, operators, and parentheses. To recognize a valid arithmetic expression that uses the operators +, -, *, and /, the following rules must be followed:

1. The expression must start and end with a number or a closing parenthesis.
2. The operators +, -, *, and / must be surrounded by numbers or parentheses.
3. Parentheses must be used in pairs, with an opening parenthesis followed by a closing parenthesis.
4. The expression must not contain any other characters except for numbers, operators, and parentheses.

Here is an example of a program in Python that can recognize a valid arithmetic expression using the above rules:

```python
import re

def is_valid_expression(expression):
    # Check if the expression starts and ends with a number or a closing parenthesis
    if not re.match(r'^[\d\)]', expression) or not re.match(r'[\d\)]$', expression):
        return False

    # Check if the operators are surrounded by numbers or parentheses
    if re.search(r'[\+\-\*\/]{2,}', expression) or re.search(r'[\+\-\*\/][^\d\(\)]', expression) or re.search(r'[^\d\(\)][\+\-\*\/]', expression):
        return False

    # Check if the parentheses are used in pairs
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    if stack:
        return False

    # Check if the expression contains any other characters
    if re.search(r'[^\d\+\-\*\/\(\)]', expression):
        return False

    return True
```

This program uses regular expressions to check if the expression follows the rules mentioned above. It returns `True` if the expression is valid and `False` otherwise.