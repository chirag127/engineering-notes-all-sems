##### Cyclomatic Complexity Measures in Software Design

- Cyclomatic complexity is a software metric used to indicate the complexity of a program  .
- It is a quantitative measure of the number of linearly independent paths through a program's source code  .
- It was developed by Thomas J. McCabe, Sr. in 1976 .
- It can be calculated using the following formula :

  - `M = E - N + 2P`
  - where M is the cyclomatic complexity, E is the number of edges, N is the number of nodes, and P is the number of connected components in the control flow graph of the program.
- Cyclomatic complexity can be used for the following purposes   :

  - Determining the independent path executions thus proven to be very helpful for developers and testers .
  - Estimating the minimum number of test cases required to cover all the paths of the program .
  - Evaluating the maintainability and readability of the code  .
  - Identifying the potential errors and bugs in the code  .
  - Refactoring the code to reduce the complexity and improve the quality .
- Cyclomatic complexity can be measured using various tools, such as Visual Studio, CodeSonar, CodeScene, etc.