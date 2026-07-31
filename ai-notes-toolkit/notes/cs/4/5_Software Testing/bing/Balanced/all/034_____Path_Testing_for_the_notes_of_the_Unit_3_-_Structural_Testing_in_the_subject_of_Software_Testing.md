# Path Testing

Path testing is a white-box testing method that involves using the source code of a program in order to find every possible executable path. It helps to determine all faults lying within a piece of code .

## Path Testing Techniques

- **Control Flow Graph**: The program is converted into a control flow graph by representing the code into nodes and edges. Nodes represent statements or blocks of code, and edges represent the flow of control between them. The control flow graph can be used to identify the different paths that can be executed in the program .
- **Cyclomatic Complexity**: Cyclomatic complexity is a metric that measures the number of linearly independent paths in a program. It can be calculated using the formula: `V(G) = E - N + 2`, where `V(G)` is the cyclomatic complexity, `E` is the number of edges, and `N` is the number of nodes in the control flow graph. Cyclomatic complexity can be used to determine the minimum number of test cases required to cover all the paths in the program .
- **Basis Path Testing**: Basis path testing is a technique that uses the cyclomatic complexity to find a basis set of paths that can cover all the possible paths in the program. A basis set of paths is a set of linearly independent paths that can be combined to form any other path in the program. To find a basis set of paths, the following steps are followed :
  - Draw a control flow graph of the program.
  - Calculate the cyclomatic complexity of the graph.
  - Identify the predicate nodes, which are the nodes that have two or more outgoing edges.
  - For each predicate node, draw a dashed line from the node to its immediate post-dominator, which is the first node that is common to all the paths from the predicate node to the exit node.
  - Number the nodes in the graph in a way that the numbers increase along any path from the entry node to the exit node.
  - Select a path from the entry node to the exit node that does not cross any dashed line. This is the first basis path.
  - For each dashed line, select a path from the entry node to the exit node that crosses the dashed line exactly once. These are the remaining basis paths.
  - Generate test cases to exercise each basis path.