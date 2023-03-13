### Cyclomatic Complexity for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Cyclomatic complexity is a software metric that measures the number of independent paths in a program's source code .
- It is useful for structured or white box testing, as it can help to evaluate the complexity of a program, the risk associated with it, and the code coverage .
- It can also help to identify the optimal number of test cases needed to cover all the possible paths in a program .
- Cyclomatic complexity can be calculated by using control flow graphs or with respect to the number of decision points in a program  .
- A control flow graph is a graphical representation of the flow of execution of a program, where each node represents a basic block (a sequence of statements with no branches) and each edge represents a possible transition between blocks .
- The cyclomatic complexity of a program can be computed as:

  - `V(G) = E - N + 2`, where `V(G)` is the cyclomatic complexity, `E` is the number of edges, and `N` is the number of nodes in the control flow graph .
  - `V(G) = P + 1`, where `P` is the number of predicate nodes (nodes that contain a condition) in the control flow graph .
  - `V(G) = R`, where `R` is the number of regions in the control flow graph .
  - `V(G) = D + 1`, where `D` is the number of decision points (such as `if`, `while`, `for`, `switch`, etc.) in the program .

- A simple example of calculating cyclomatic complexity using control flow graphs is shown below:

  ```text
  // Program to find the maximum of two numbers
  int max(int a, int b) {
    int result; // 1
    if (a > b) { // 2
      result = a; // 3
    }
    else { // 4
      result = b; // 5
    }
    return result; // 6
  }
  ```

  The control flow graph for this program is:

  ```text
   1
   |
   2
  / \
 3   5
  \ /
   6
  ```

  The cyclomatic complexity can be calculated as:

  - `V(G) = E - N + 2 = 5 - 4 + 2 = 3`
  - `V(G) = P + 1 = 1 + 1 = 2`
  - `V(G) = R = 2`
  - `V(G) = D + 1 = 1 + 1 = 2`

  The optimal number of test cases to cover all the paths is 2, one for each branch of the `if` statement.

- Some advantages of cyclomatic complexity are:

  - It can help to measure the quality of the code by indicating the level of complexity and maintainability .
  - It can help to identify the potential errors and bugs in the code by highlighting the areas that need more testing and debugging .
  - It can help to improve the performance and efficiency of the code by suggesting the possible ways to simplify and refactor the code .

- Some disadvantages of cyclomatic complexity are:

  - It does not consider the data flow or the logical complexity of the code, which may affect the actual complexity and testing effort .
  - It does not account for the different types and levels of decision points, which may have different impacts on the complexity and testing effort .
  - It does not provide a clear and intuitive interpretation of the complexity value, which may vary depending on the context and the application .

- Some mnemonics and learning tricks for cyclomatic complexity are:

  - Cyclomatic complexity is like a cycle of complexity: the more cycles (paths) in the code, the more complex it is.
  - Cyclomatic