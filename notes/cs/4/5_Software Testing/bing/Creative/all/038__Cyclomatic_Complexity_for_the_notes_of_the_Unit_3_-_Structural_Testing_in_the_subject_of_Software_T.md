### Cyclomatic Complexity for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Cyclomatic complexity is a software metric that measures the number of independent paths in the source code of a program  .
- It is based on a control flow graph, which is a graphical representation of the program, where nodes are processing tasks and edges are control flows between the nodes.
- It can be calculated by using the following formulas :
  - V(G) = E - N + 2, where E is the number of edges, N is the number of nodes, and V(G) is the cyclomatic complexity of the graph G.
  - V(G) = P + 1, where P is the number of predicate nodes (nodes that contain a condition), and V(G) is the cyclomatic complexity of the graph G.
- Cyclomatic complexity can be used to estimate the difficulty of testing, maintaining, or debugging a program  . Higher values of cyclomatic complexity indicate more complex programs that may have more errors and require more test cases to achieve full coverage. Lower values of cyclomatic complexity indicate simpler programs that may have fewer errors and require fewer test cases to achieve full coverage.
- A common guideline is to limit the cyclomatic complexity of a program to 10 or less, as suggested by McCabe, the developer of this metric. However, this limit may vary depending on the context and the nature of the program.
- Cyclomatic complexity can be calculated and visualized by using various tools, such as Visual Studio Code Analysis, CodeSonar, CodeScene, SonarQube, etc .
- Cyclomatic complexity can be used for various purposes, such as:
  - Evaluating the quality and maintainability of a program
  - Identifying the most complex and risky parts of a program
  - Estimating the testing effort and resources required for a program
  - Designing test cases based on the basis path testing technique, which ensures that each independent path in the program is executed at least once
  - Refactoring the code to reduce the complexity and improve the readability and modularity of the program

- Some mnemonics and learning tricks for cyclomatic complexity are:
  - Cyclomatic complexity = Cyclone + Automatic + Complexity. Imagine a cyclone that automatically increases the complexity of a program by adding more paths and conditions.
  - V(G) = E - N + 2. Remember this formula by thinking of V as the vertex of a graph, E as the edge of a graph, N as the node of a graph, and 2 as the two extra paths for the entry and exit of the graph.
  - V(G) = P + 1. Remember this formula by thinking of V as the value of the graph, P as the predicate or condition of the graph, and 1 as the one extra path for the entry or exit of the graph.
  - A simple example of cyclomatic complexity is a program that prints "Hello World". The control flow graph of this program has one node and one edge, so the cyclomatic complexity is V(G) = 1 - 1 + 2 = 2, or V(G) = 0 + 1 = 1. This means that there is only one independent path in the program, and only one test case is needed to cover it.

: https://learn.microsoft.com/en-us/visualstudio/code-quality/code-metrics-cyclomatic-complexity?view=vs-2022
: https://www.guru99.com/cyclomatic-complexity.html
: https://www.educba.com/cyclomatic-complexity/
: https://www.mnemonic-device.com/mathematics/cyclomatic-complexity/