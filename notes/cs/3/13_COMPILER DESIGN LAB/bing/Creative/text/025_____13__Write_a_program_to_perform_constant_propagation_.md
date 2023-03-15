### 13. Write a program to perform constant propagation.

Constant propagation is a compiler optimization technique that replaces the use of constant variables with their values at compile time. This can improve the performance and readability of the code, as well as eliminate unnecessary memory accesses.

A program to perform constant propagation can be written in pseudocode as follows:

```
// Input: a list of statements in the form of (operation, operand1, operand2, result)
// Output: a list of statements with constant propagation applied

// Initialize an empty dictionary to store the values of constant variables
constants = {}

// Loop through each statement in the input list
for each statement in input_list:

  // If the statement is an assignment of a constant value to a variable
  if statement.operation == "=" and is_constant(statement.operand1):

    // Store the variable and its value in the constants dictionary
    constants[statement.result] = statement.operand1

    // Remove the statement from the input list
    input_list.remove(statement)

  // Else, if the statement is an arithmetic operation
  else if statement.operation in ["+", "-", "*", "/"]:

    // If the first operand is a constant variable
    if statement.operand1 in constants:

      // Replace the operand with its value
      statement.operand1 = constants[statement.operand1]

    // If the second operand is a constant variable
    if statement.operand2 in constants:

      // Replace the operand with its value
      statement.operand2 = constants[statement.operand2]

    // If both operands are constant values
    if is_constant(statement.operand1) and is_constant(statement.operand2):

      // Evaluate the operation and store the result in the constants dictionary
      constants[statement.result] = evaluate(statement.operation, statement.operand1, statement.operand2)

      // Remove the statement from the input list
      input_list.remove(statement)

// Return the modified input list as the output
return input_list
```