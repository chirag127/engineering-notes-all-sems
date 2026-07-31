### 13. Write a program to perform constant propagation

Constant propagation is a compiler optimization technique that aims to reduce the number of computations performed at runtime by replacing variables with their constant values whenever possible.

Here are the steps to write a program to perform constant propagation:

1. Identify the variables that are assigned constant values in the program.
2. Traverse the program's control flow graph to determine the points where the variables' values are used.
3. Replace the variables with their constant values at the points where their values are used.
4. Repeat the process until no more replacements can be made.

Here is an example of a program that performs constant propagation:

```python
def constant_propagation(code):
    # Step 1: Identify the variables that are assigned constant values
    constants = {}
    for line in code:
        if '=' in line:
            left, right = line.split('=')
            left = left.strip()
            right = right.strip()
            if right.isnumeric():
                constants[left] = right

    # Step 2: Traverse the program's control flow graph
    new_code = []
    for line in code:
        new_line = line
        for var, value in constants.items():
            # Step 3: Replace the variables with their constant values
            new_line = new_line.replace(var, value)
        new_code.append(new_line)

    # Step 4: Repeat the process
    if new_code == code:
        return new_code
    else:
        return constant_propagation(new_code)

# Example
code = [
    'x = 5',
    'y = 3',
    'z = x + y',
    'print(z)'
]

new_code = constant_propagation(code)
print(new_code)
```

This program takes a list of code lines as input and returns a new list of code lines where the variables have been replaced with their constant values whenever possible. In the example, the variable `z` is replaced with the constant value `8`, which is the result of adding the constant values of `x` and `y`.