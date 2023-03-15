# 13. Write a program to perform constant propagation

Constant propagation is a compiler optimization technique that aims to reduce the execution time of a program by replacing the values of variables that are known at compile time with their constant values.

Here is an example of a program that performs constant propagation:

```python
def constant_propagation(code):
    # Initialize a dictionary to store the values of constants
    constants = {}

    # Iterate over each line of code
    for line in code:
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
                line = f"{tokens[0]} = {constants[tokens[2]]}"

        # Print the optimized line of code
        print(line)

# Example usage
code = [
    "x = 5",
    "y = x",
    "z = y + 3"
]
constant_propagation(code)
```

This program takes as input a list of strings representing lines of code. It iterates over each line and checks if it is an assignment statement. If the right-hand side of the assignment is a constant, the program stores its value in a dictionary. If the right-hand side is a variable that has a constant value, the program replaces the variable with its constant value. Finally, the program prints the optimized lines of code.

The output of this program is:

```
x = 5
y = 5
z = y + 3
```

As you can see, the value of `y` has been replaced with its constant value, `5`, resulting in faster execution of the program. This is an example of how constant propagation can be used to optimize a program.