### Cyclomatic Complexity

- Cyclomatic complexity is a metric that measures the complexity of a program or a module by counting the number of independent paths through the code.
- It was proposed by Thomas J. McCabe in 1976 as a way to quantify the testability and maintainability of software.
- Cyclomatic complexity can be calculated using the following formula:

  - `V(G) = E - N + 2P`

  - Where `V(G)` is the cyclomatic complexity, `E` is the number of edges, `N` is the number of nodes, and `P` is the number of connected components in the control flow graph of the program or module.

- Alternatively, cyclomatic complexity can be calculated using the following formula:

  - `V(G) = R + 1`

  - Where `V(G)` is the cyclomatic complexity and `R` is the number of regions in the control flow graph of the program or module.

- Cyclomatic complexity can also be derived from the source code by counting the number of decision points (such as `if`, `while`, `for`, `case`, etc.) and adding one.

  - `V(G) = D + 1`

  - Where `V(G)` is the cyclomatic complexity and `D` is the number of decision points in the source code of the program or module.

- Cyclomatic complexity can be used to determine the minimum number of test cases required to achieve 100% branch coverage or path coverage of the program or module.
- Cyclomatic complexity can also be used to assess the risk of defects or errors in the program or module. Higher cyclomatic complexity indicates higher risk and lower quality.
- Cyclomatic complexity can be reduced by refactoring the code to eliminate unnecessary branches, loops, or conditions, or by splitting the code into smaller and simpler modules or functions.