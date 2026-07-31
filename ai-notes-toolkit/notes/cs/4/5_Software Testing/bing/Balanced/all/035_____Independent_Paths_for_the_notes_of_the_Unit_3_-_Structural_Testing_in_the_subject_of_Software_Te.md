# Independent Paths

- Independent paths are paths through a program's control flow graph that cannot be reproduced by combining other paths .
- Independent paths are important for path testing, a structural testing method that aims to cover all possible executable paths in a program .
- Path testing can help to find faults in the logic and design of a program, and reduce redundant tests .
- To find the independent paths, we can use the cyclomatic complexity, a metric that measures the number of linearly independent paths in a program .
- The cyclomatic complexity can be calculated by using one of the following formulas :
  - V(G) = E - N + 2
  - V(G) = P + 1
  - V(G) = R
  - Where V(G) is the cyclomatic complexity, E is the number of edges, N is the number of nodes, P is the number of predicate nodes, and R is the number of regions in the control flow graph.
- The cyclomatic complexity gives the minimum number of test cases required to cover all the independent paths .
- To generate test cases for each independent path, we can use the following steps :
  - Draw the control flow graph of the program.
  - Calculate the cyclomatic complexity of the graph.
  - Identify the basis set of independent paths.
  - Prepare test cases that will force the execution of each path in the basis set.