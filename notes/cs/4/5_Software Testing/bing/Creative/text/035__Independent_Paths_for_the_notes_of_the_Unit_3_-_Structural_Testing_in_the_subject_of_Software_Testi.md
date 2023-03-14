### Independent Paths

- An independent path is a path through the control flow graph that introduces at least one new edge that is not included in any other independent paths.
- Independent paths are used to measure the cyclomatic complexity of a program, which is a metric of the number of linearly independent paths through a program's source code.
- Independent paths are also used to design test cases that cover all the possible paths of execution in a program, which is known as path testing.
- To find the independent paths of a program, we can use the following steps:
  - Draw the control flow graph of the program, which is a graphical representation of the program's structure, showing the nodes (basic blocks of statements) and the edges (transfers of control) between them.
  - Identify the regions of the graph, which are the areas enclosed by edges. A region can be a node, a loop, or a branch.
  - Calculate the cyclomatic complexity of the graph, which is equal to E - N + 2, where E is the number of edges and N is the number of nodes. Alternatively, it is equal to R + 1, where R is the number of regions.
  - Identify a basis set of independent paths, which is a set of paths that covers all the edges of the graph and has the same size as the cyclomatic complexity. A basis set can be found by starting from a node and tracing a path along the edges until reaching a node that has already been visited, then backtracking to the nearest branching node and taking a different edge, and repeating this process until all the edges are covered.
  - Derive additional independent paths from the basis set by skipping or adding nodes or edges, as long as the resulting path is still a valid path in the graph and introduces a new edge that is not in any other independent paths.