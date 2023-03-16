### Independent Paths

- Independent paths are paths through a program's control flow graph that cannot be reproduced by combining other paths .
- Independent paths are useful for path testing, a structural testing method that aims to cover all possible executable paths in a program .
- Path testing can help to find faults in the logic and design of a program, and reduce redundant tests .
- To find the independent paths, the following steps are usually followed  :
  - Draw the control flow graph of the program, which shows the nodes (statements or blocks) and edges (transfers of control) of the program.
  - Calculate the cyclomatic complexity of the graph, which is a measure of the number of linearly independent paths in the graph. There are several ways to calculate the cyclomatic complexity, such as:
    - V(G) = E - N + 2, where E is the number of edges and N is the number of nodes in the graph.
    - V(G) = P + 1, where P is the number of predicate nodes (nodes with two or more outgoing edges) in the graph.
    - V(G) = R, where R is the number of regions in the graph. A region is a maximal area in the graph that has no holes.
  - Identify the basis set of independent paths, which is a set of paths that covers all the edges in the graph. The number of paths in the basis set should be equal to the cyclomatic complexity. There are different ways to identify the basis set, such as:
    - Start from the entry node and follow a path to the exit node, covering as many new edges as possible. Repeat this process until all the edges are covered.
    - Start from the exit node and follow a path to the entry node, covering as many new edges as possible. Repeat this process until all the edges are covered.
    - Start from a predicate node and follow a path to another predicate node, covering as many new edges as possible. Repeat this process until all the edges are covered.
  - Generate test cases for each path in the basis set, using appropriate input values and expected output values. Execute the test cases and check the results.