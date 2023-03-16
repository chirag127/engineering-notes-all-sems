# Independent Paths

- Independent paths are paths through a program's control flow graph that cannot be reproduced by combining other paths .
- Independent paths are important for path testing, a structural testing method that aims to cover all possible executable paths in a program .
- Path testing can help to find faults in the logic and design of a program, and reduce redundant tests .
- To find the independent paths, we can use the cyclomatic complexity, which is a measure of the number of linearly independent paths in a program .
- Cyclomatic complexity can be calculated by using the formula: V(G) = E - N + 2, where E is the number of edges, N is the number of nodes, and V(G) is the cyclomatic complexity of the graph G .
- Alternatively, we can use the formula: V(G) = P + 1, where P is the number of predicate nodes, which are nodes that contain a condition .
- Once we have the cyclomatic complexity, we can generate test cases for each independent path by using the following steps :
  - Draw the control flow graph of the program.
  - Calculate the cyclomatic complexity of the graph.
  - Identify the basis set of independent paths, which is a set of paths that covers all the edges and nodes of the graph.
  - Derive test cases that can execute each path in the basis set.
  - Run the test cases and check the results.