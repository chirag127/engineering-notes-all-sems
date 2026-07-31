# Identification of Independent Paths for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Path testing is a method of testing the logic of a program by designing test cases that cover all possible paths of execution.
- Independent paths are paths that have at least one edge (or statement) that is not shared by any other path.
- Independent paths are important because they help to ensure that every statement and branch of the program is executed at least once, and that no redundant tests are performed.
- To identify independent paths, the following steps are usually followed:
  - Draw a control flow graph (CFG) of the program, which is a graphical representation of the program's structure, showing the nodes (or blocks) and edges (or transitions) between them.
  - Calculate the cyclomatic complexity (CC) of the CFG, which is a measure of the number of linearly independent paths in the graph. CC can be computed using one of these formulas:
    - CC = E - N + 2, where E is the number of edges and N is the number of nodes in the graph.
    - CC = R + 1, where R is the number of regions (or enclosed areas) in the graph.
    - CC = D + 1, where D is the number of decision points (or nodes with more than one outgoing edge) in the graph.
  - Select a basis set of paths, which is a set of independent paths that covers all the edges in the graph. The number of paths in the basis set should be equal to the CC of the graph. One way to select a basis set is to start from the entry node and follow each possible branch until reaching the exit node, and then repeat the process for each decision point until all the edges are covered.
  - Derive test cases for each path in the basis set, using appropriate input values and expected outputs. The test cases should exercise the logic of the program and reveal any errors or defects in the code.