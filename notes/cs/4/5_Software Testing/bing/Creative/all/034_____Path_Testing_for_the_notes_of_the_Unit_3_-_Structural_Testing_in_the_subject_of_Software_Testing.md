# Path Testing

Path testing is a white-box testing method that involves using the source code of a program in order to find every possible executable path. It helps to determine all faults lying within a piece of code .

## Path Testing Techniques

- **Control Flow Graph**: The program is converted into a control flow graph by representing the code into nodes and edges. Nodes represent statements or blocks of code, and edges represent the flow of control between them. The control flow graph can be used to identify the different paths that can be executed in the program .
- **Cyclomatic Complexity**: Cyclomatic complexity is a metric that measures the number of linearly independent paths in a program. It can be calculated using the formula: `V(G) = E - N + 2`, where `E` is the number of edges, `N` is the number of nodes, and `V(G)` is the cyclomatic complexity of the graph `G`. Cyclomatic complexity can be used to determine the minimum number of test cases required to cover all the paths in the program .
- **Basis Path Testing**: Basis path testing is a technique that uses the cyclomatic complexity to find a basis set of paths that can cover all the paths in the program. A basis set is a set of paths that are linearly independent, meaning that no path can be constructed by combining other paths in the set. Basis path testing involves the following steps :
  - Draw a control flow graph of the program.
  - Calculate the cyclomatic complexity of the graph.
  - Find a basis set of paths by using a set of rules, such as:
    - Start from the entry node and follow any edge until reaching the exit node or a node that has already been visited.
    - If a node has already been visited, backtrack to the previous node and follow a different edge.
    - Repeat until all the edges have been traversed at least once.
  - Generate test cases to exercise each path in the basis set.