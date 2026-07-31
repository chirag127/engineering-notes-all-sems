### Identification of Independent Paths

- Independent paths are paths through a program or module that cannot be reproduced from other paths by other methods.
- Independent paths are important for path testing, which is a method of testing the logic and control flow of a program or module .
- Path testing aims to cover and execute every independent path in a program or module, and to reduce the occurrence of redundant tests.
- To identify independent paths, the following steps are usually followed :
  - Draw a control flow graph of the program or module, which is a graphical representation of the nodes and edges that show the flow of execution.
  - Calculate the cyclomatic complexity of the control flow graph, which is a measure of the number of linearly independent paths in the graph. There are several ways to calculate the cyclomatic complexity, such as :
    - Cyclomatic complexity = Edges - Nodes + 2
    - Cyclomatic complexity = Regions + 1
    - Cyclomatic complexity = Decisions + 1
  - Identify the basis set of independent paths, which is a set of paths that covers all the edges and nodes in the graph. The number of paths in the basis set should be equal to the cyclomatic complexity. One way to identify the basis set is to use the following rules:
    - Start from the entry node and follow a path to the exit node, covering as many new edges and nodes as possible.
    - Repeat the process until all the edges and nodes are covered, and no new paths can be formed by adding new edges or nodes.
    - If there are loops in the graph, make sure to traverse the loop body at least once, and also skip the loop body at least once.
  - Generate test cases for each path in the basis set, using appropriate input values and expected output values.