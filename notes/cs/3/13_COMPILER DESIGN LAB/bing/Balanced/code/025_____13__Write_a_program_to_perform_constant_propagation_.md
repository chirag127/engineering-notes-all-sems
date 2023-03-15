### 13. Write a program to perform constant propagation.

Constant propagation is a compiler optimization technique that replaces the use of a variable with its constant value, if the value of the variable is known at compile time.

A program to perform constant propagation can be written in pseudocode as follows:

```
// Input: a control flow graph (CFG) of a program
// Output: an optimized CFG with constant propagation

// Initialize a worklist with all the nodes of the CFG
worklist = CFG.nodes

// Initialize a map to store the constant values of variables
constants = {}

// Repeat until the worklist is empty
while worklist is not empty:

  // Pop a node from the worklist
  node = worklist.pop()

  // For each statement in the node
  for statement in node.statements:

    // If the statement is an assignment of a constant value to a variable
    if statement is of the form x = c, where c is a constant:

      // Update the constant value of the variable in the map
      constants[x] = c

      // For each successor node of the current node
      for successor in node.successors:

        // For each use of the variable in the successor node
        for use in successor.uses(x):

          // Replace the use of the variable with its constant value
          use.replace(x, c)

          // Add the successor node to the worklist if it is not already there
          if successor not in worklist:
            worklist.add(successor)

    // If the statement is an assignment of an expression to a variable
    if statement is of the form x = e, where e is an expression:

      // Evaluate the expression by replacing the variables with their constant values if possible
      e = evaluate(e, constants)

      // If the expression is a constant value
      if e is a constant:

        // Update the constant value of the variable in the map
        constants[x] = e

        // For each successor node of the current node
        for successor in node.successors:

          // For each use of the variable in the successor node
          for use in successor.uses(x):

            // Replace the use of the variable with its constant value
            use.replace(x, e)

            // Add the successor node to the worklist if it is not already there
            if successor not in worklist:
              worklist.add(successor)

// Return the optimized CFG
return CFG
```