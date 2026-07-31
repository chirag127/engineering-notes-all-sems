### Identification of Independent Paths

- Independent paths are paths through a program or module that execute at least one statement or condition that is not executed by any other path .
- Independent paths are important for path testing, which is a method of testing the logic and control flow of a program or module by covering all possible execution paths  .
- Path testing aims to reduce redundant tests and ensure that every statement and condition is executed at least once .
- To identify independent paths, the following steps are usually followed    :

  1. Draw a control flow graph (CFG) of the program or module, which is a graphical representation of the flow of control among the statements and conditions.
  2. Calculate the cyclomatic complexity (CC) of the CFG, which is a measure of the number of linearly independent paths in the CFG. CC can be computed using any of the following formulas:
    - CC = E - N + 2, where E is the number of edges and N is the number of nodes in the CFG.
    - CC = R + 1, where R is the number of regions in the CFG.
    - CC = D + 1, where D is the number of decision nodes in the CFG.
  3. Identify a basis set of independent paths, which is a set of paths that covers all the edges in the CFG. A basis set can be obtained by starting from the entry node and selecting paths that traverse new edges until the CC is reached.
  4. Derive test cases for each path in the basis set, which are inputs that cause the program or module to execute the corresponding path. Test cases can be designed using various techniques such as boundary value analysis, equivalence partitioning, etc.