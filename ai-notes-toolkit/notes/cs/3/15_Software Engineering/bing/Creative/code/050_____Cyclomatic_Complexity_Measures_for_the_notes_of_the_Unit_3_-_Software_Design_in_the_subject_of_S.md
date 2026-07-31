### Cyclomatic Complexity Measures

Cyclomatic complexity is a software metric used to measure the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a program's source code   . It was developed by Thomas J. McCabe, Sr. in 1976.

Some important points about cyclomatic complexity are:

- It is based on the concept of a control flow graph, which is a graphical representation of the program's structure, showing the nodes (basic blocks) and edges (transfers of control) between them .
- It can be calculated using the formula: `V(G) = E - N + 2`, where `V(G)` is the cyclomatic complexity, `E` is the number of edges, and `N` is the number of nodes in the graph .
- Alternatively, it can be calculated using the formula: `V(G) = P + 1`, where `P` is the number of predicate nodes (nodes that contain a condition) in the graph .
- It can also be calculated using the formula: `V(G) = R + 1`, where `R` is the number of regions (closed areas) in the graph .
- It can be used to estimate the number of test cases required to cover all the possible paths of the program, as well as the difficulty of maintaining and debugging the program  .
- It can be used to set a threshold for the maximum acceptable complexity of a program or a module, and to identify the parts of the code that need refactoring or simplification  .
- It can be measured at different levels of granularity, such as functions, methods, classes, modules, or packages .
- It can be influenced by the programming language, style, and structure of the code, as well as the use of loops, branches, recursion, exceptions, and other control structures  .
- It can be computed using various tools, such as Visual Studio, SonarQube, CodeSonar, NDepend, and others .