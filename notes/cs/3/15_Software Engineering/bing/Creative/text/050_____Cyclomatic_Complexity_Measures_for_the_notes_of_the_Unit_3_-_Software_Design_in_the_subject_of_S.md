### Cyclomatic Complexity Measures

- Cyclomatic complexity is a software metric used to measure the complexity of a program   .
- It is a quantitative measure of the number of linearly independent paths through a program's source code  .
- It was developed by Thomas J. McCabe, Sr. in 1976 .
- McCabe interprets a computer program as a set of a strongly connected directed graph, where the nodes represent the basic blocks of the program and the edges represent the control flow between them .
- The cyclomatic complexity of a program can be calculated by using the following formula :

  - `V(G) = E - N + 2P`
  - where `V(G)` is the cyclomatic complexity, `E` is the number of edges, `N` is the number of nodes, and `P` is the number of connected components in the graph.

- Alternatively, the cyclomatic complexity can be calculated by using the following formula :

  - `V(G) = R + 1`
  - where `R` is the number of regions in the graph.

- The cyclomatic complexity can also be calculated by counting the number of decision points (such as `if`, `while`, `for`, `case`, etc.) in the program and adding one :

  - `V(G) = D + 1`
  - where `D` is the number of decision points.

- The cyclomatic complexity can be used to estimate the number of test cases required to cover all the possible paths in a program  .
- The cyclomatic complexity can also be used to indicate the maintainability, readability, and testability of a program  .
- The higher the cyclomatic complexity, the more complex the program is, and the more likely it is to contain errors or defects  .
- The lower the cyclomatic complexity, the simpler the program is, and the easier it is to understand, modify, and test  .
- There is no definitive threshold for the acceptable cyclomatic complexity, but some common guidelines are  :

  - A cyclomatic complexity of 1-10 is considered good.
  - A cyclomatic complexity of 11-20 is considered moderate.
  - A cyclomatic complexity of 21-50 is considered high.
  - A cyclomatic complexity of above 50 is considered very high and should be avoided or refactored.

- There are various tools available to measure the cyclomatic complexity of a program, such as Visual Studio, SonarQube, CodeClimate, etc. .