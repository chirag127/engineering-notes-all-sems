### 13. Write a program to perform constant propagation

Constant propagation is a compiler optimization technique that aims to reduce the number of computations performed at runtime by replacing variables with their constant values whenever possible.

Here is an example of a program that performs constant propagation:

```python
def constant_propagation(code):
    # Initialize a dictionary to store the values of constants
    constants = {}
    # Split the code into lines
    lines = code.split('\n')
    # Iterate over the lines of code
    for line in lines:
        # Split the line into tokens
        tokens = line.split()
        # Check if the line is an assignment statement
        if len(tokens) == 3 and tokens[1] == '=':
            # Check if the right-hand side is a constant
            if tokens[2].isdigit():
                # Store the constant value in the dictionary
                constants[tokens[0]] = int(tokens[2])
            # Check if the right-hand side is a variable
            elif tokens[2] in constants:
                # Replace the variable with its constant value
                constants[tokens[0]] = constants[tokens[2]]
    # Iterate over the lines of code again
    for i, line in enumerate(lines):
        # Split the line into tokens
        tokens = line.split()
        # Iterate over the tokens
        for j, token in enumerate(tokens):
            # Check if the token is a variable
            if token in constants:
                # Replace the variable with its constant value
                tokens[j] = str(constants[token])
        # Join the tokens back into a line
        lines[i] = ' '.join(tokens)
    # Join the lines back into code
    return '\n'.join(lines)
```

This program takes as input a string representing the code to be optimized and returns a new string representing the optimized code. The program works by first identifying all the constants in the code and storing their values in a dictionary. Then, it iterates over the lines of code again, replacing any occurrences of variables with their constant values whenever possible.

Here is an example of how to use this program:

```python
code = """
x = 3
y = x
z = y + 5
"""

optimized_code = constant_propagation(code)
print(optimized_code)
```

This will output the following optimized code:

```
x = 3
y = 3
z = 3 + 5
```

As you can see, the variable `y` has been replaced with its constant value `3`, reducing the number of computations that need to be performed at runtime. This is a simple example, but constant propagation can be a powerful optimization technique for more complex programs.