# 13. Write a program to perform constant propagation.

Constant propagation is a compiler optimization technique that replaces the use of constant variables with their values at compile time. This can improve the performance and readability of the code, as well as eliminate unnecessary memory accesses.

A program to perform constant propagation can be written in pseudocode as follows:

```
// Input: a list of statements in the form of (variable, operator, operand1, operand2)
// Output: a list of statements with constant propagation applied

// Initialize an empty dictionary to store the values of constant variables
constants = {}

// Initialize an empty list to store the output statements
output = []

// Loop through each statement in the input list
for each statement in input:

  // Extract the variable, operator, operand1 and operand2 from the statement
  (variable, operator, operand1, operand2) = statement

  // If the operator is "=", then the statement is an assignment
  if operator == "=":

    // If the operand1 is a constant value, then store it in the constants dictionary
    if operand1 is a constant value:
      constants[variable] = operand1

    // Else, if the operand1 is a constant variable, then replace it with its value from the constants dictionary
    else if operand1 is a constant variable:
      operand1 = constants[operand1]

    // Add the statement to the output list
    output.append((variable, operator, operand1, operand2))

  // Else, if the operator is not "=", then the statement is an expression
  else:

    // If the operand1 is a constant value or a constant variable, then replace it with its value from the constants dictionary
    if operand1 is a constant value or a constant variable:
      operand1 = constants[operand1]

    // If the operand2 is a constant value or a constant variable, then replace it with its value from the constants dictionary
    if operand2 is a constant value or a constant variable:
      operand2 = constants[operand2]

    // If both operands are constant values, then evaluate the expression and assign the result to the variable
    if operand1 and operand2 are constant values:
      variable = evaluate(operator, operand1, operand2)

    // Add the statement to the output list
    output.append((variable, operator, operand1, operand2))

// Return the output list
return output
```

For example, given the following input list of statements:

```
a = 10
b = a + 5
c = b * 2
d = c - a
e = d / 5
```

The output list of statements after applying constant propagation would be:

```
a = 10
b = 15
c = 30
d = 20
e = 4
```