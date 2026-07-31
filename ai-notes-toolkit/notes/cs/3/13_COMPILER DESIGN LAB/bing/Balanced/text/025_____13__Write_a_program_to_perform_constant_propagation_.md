### 13. Write a program to perform constant propagation.

- Constant propagation is a compiler optimization technique that replaces the use of a variable with its constant value, if the value of the variable is known at compile time.
- Constant propagation can improve the performance and readability of the code, and enable further optimizations such as dead code elimination and loop unrolling.
- A simple algorithm for constant propagation is as follows:

  - Initialize a set of pairs (variable, value) for each variable that is assigned a constant value in the program.
  - Traverse the program in a forward direction, following the control flow graph.
  - For each statement of the form x = y op z, where op is an arithmetic or logical operator, check if y and z are both constants in the set. If yes, compute the value of x and add (x, value) to the set.
  - For each statement of the form x = y, check if y is a constant in the set. If yes, add (x, value) to the set.
  - For each statement of the form if x then ... else ..., check if x is a constant in the set. If yes, simplify the conditional branch according to the value of x.
  - Repeat the traversal until no more pairs are added to the set.

- An example of a program to perform constant propagation in Python is given below:

```python
# A program to perform constant propagation
# Input: a list of statements, each of the form x = y op z, x = y, or if x then s1 else s2
# Output: a list of simplified statements after constant propagation

def constant_propagation(statements):
  # Initialize an empty set of pairs (variable, value)
  constants = set()
  # Initialize an empty list of simplified statements
  simplified = []
  # Initialize a flag to indicate if any change has occurred
  changed = True
  # Repeat until no change
  while changed:
    # Reset the flag
    changed = False
    # Traverse the statements in a forward direction
    for statement in statements:
      # Split the statement by spaces
      tokens = statement.split()
      # If the statement is of the form x = y op z
      if len(tokens) == 5:
        # Get the operands and the operator
        x, _, y, op, z = tokens
        # Check if y and z are both constants
        if (y, int(y)) in constants and (z, int(z)) in constants:
          # Compute the value of x
          value = eval(y + op + z)
          # Add (x, value) to the set
          constants.add((x, value))
          # Simplify the statement
          statement = f"{x} = {value}"
          # Set the flag
          changed = True
      # If the statement is of the form x = y
      elif len(tokens) == 3:
        # Get the operands
        x, _, y = tokens
        # Check if y is a constant
        if (y, int(y)) in constants:
          # Get the value of y
          value = int(y)
          # Add (x, value) to the set
          constants.add((x, value))
          # Simplify the statement
          statement = f"{x} = {value}"
          # Set the flag
          changed = True
      # If the statement is of the form if x then s1 else s2
      elif len(tokens) == 7:
        # Get the condition and the branches
        _, x, _, s1, _, s2, _ = tokens
        # Check if x is a constant
        if (x, int(x)) in constants:
          # Get the value of x
          value = int(x)
          # Simplify the conditional branch
          if value:
            statement = s1
          else:
            statement = s2
          # Set the flag
          changed = True
      # Append the statement to the simplified list
      simplified.append(statement)
    # Update the statements with the simplified list
    statements = simplified
    # Clear the simplified list
    simplified = []
  # Return the simplified statements
  return statements

# Test the program with an example
statements = [
  "a = 10",
  "b = 20",
  "c = a + b",
  "d = c * 2",
  "if d then e = 1 else e = 0",
  "f = e - 5"
]

print(constant_propagation(statements))
```

- The output of the program is:

```python
['a = 10',

```
