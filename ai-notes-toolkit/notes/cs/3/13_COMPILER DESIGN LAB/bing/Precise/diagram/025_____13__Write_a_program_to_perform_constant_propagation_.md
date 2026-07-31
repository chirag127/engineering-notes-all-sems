### 13. Write a program to perform constant propagation

Constant propagation is a compiler optimization technique that aims to reduce the execution time of a program by replacing the values of variables that are known at compile time with their constant values.

Here are the steps to write a program to perform constant propagation:

1. Identify the variables in the program that have constant values assigned to them.
2. Traverse the program's control flow graph to find the use of these variables.
3. Replace the use of these variables with their constant values.
4. Repeat the process until no more replacements can be made.

Here is an example of a program that performs constant propagation:

```python
def constant_propagation(code):
    # Step 1: Identify the variables with constant values
    constants = {}
    for line in code:
        if '=' in line:
            left, right = line.split('=')
            left = left.strip()
            right = right.strip()
            if right.isdigit():
                constants[left] = right

    # Step 2: Traverse the control flow graph
    new_code = []
    for line in code:
        for var, value in constants.items():
            line = line.replace(var, value)
        new_code.append(line)

    # Step 3: Replace the use of variables with their constant values
    return new_code

# Example
code = [
    'x = 5',
    'y = 3',
    'z = x + y',
    'print(z)'
]

new_code = constant_propagation(code)
for line in new_code:
    print(line)
```

This program takes a list of code lines as input and returns a new list of code lines where the use of variables with constant values has been replaced with their constant values. In the example, the variable `z` is assigned the value of `x + y`, which is `5 + 3`. The program replaces the use of `x` and `y` with their constant values, resulting in the line `z = 5 + 3`. The final output of the program is the new code with the constant propagation optimization applied.