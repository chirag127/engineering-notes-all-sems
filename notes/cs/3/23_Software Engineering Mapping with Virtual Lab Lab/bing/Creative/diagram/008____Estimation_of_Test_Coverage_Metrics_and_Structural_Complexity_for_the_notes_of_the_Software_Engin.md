## Estimation of Test Coverage Metrics and Structural Complexity

- Test coverage metrics are used to measure and monitor the testing activity of a software program. They help to assess the thoroughness, effectiveness and efficiency of testing techniques.
- Structural complexity is a measure of how complex a program is in terms of its control flow and logic. It can be estimated by using a graphical representation of the program called a control flow graph (CFG).
- A CFG shows the basic blocks of a program and the possible paths of execution between them. A basic block is a sequence of statements that has a single entry point and a single exit point.
- A CFG can be used to identify the linearly independent paths in a program, which are the paths that cannot be derived from any combination of other paths. The number of linearly independent paths is also known as the cyclomatic complexity of a program.
- The cyclomatic complexity can be calculated by using the following formula:

  - `V(G) = E - N + 2`, where `V(G)` is the cyclomatic complexity, `E` is the number of edges, and `N` is the number of nodes in the CFG.
  - `V(G) = P + 1`, where `P` is the number of predicate nodes, which are the nodes that have more than one outgoing edge.
  - `V(G) = R`, where `R` is the number of regions in the CFG, which are the areas enclosed by edges.

- The cyclomatic complexity can be used as a test coverage metric, as it indicates the minimum number of test cases required to cover all the possible paths in a program. A higher cyclomatic complexity means a higher testing effort and a higher risk of errors.
- Another test coverage metric is the statement coverage, which measures the percentage of statements that are executed by the test cases. A statement coverage of 100% means that every statement in the program is executed at least once by the test cases.
- A more refined test coverage metric is the branch coverage, which measures the percentage of branches that are executed by the test cases. A branch is a point in the program where the control flow can diverge into two or more paths. A branch coverage of 100% means that every branch in the program is executed at least once by the test cases.
- A further refined test coverage metric is the path coverage, which measures the percentage of paths that are executed by the test cases. A path is a sequence of statements from the entry point to the exit point of the program. A path coverage of 100% means that every path in the program is executed at least once by the test cases.
- The following diagram shows an example of a CFG and the corresponding test coverage metrics:

![CFG and test coverage metrics](https://i.imgur.com/0Yw8wZl.png)

- In this example, the program has 5 nodes, 6 edges, 1 predicate node, and 2 regions. Therefore, the cyclomatic complexity is `V(G) = 6 - 5 + 2 = 3`, or `V(G) = 1 + 1 = 2`, or `V(G) = 2`.
- The program has 3 linearly independent paths: `1-2-5`, `1-3-4-5`, and `1-3-5`. Therefore, the minimum number of test cases required to cover all the paths is 3.
- The program has 5 statements: `a = 0`, `a = a + 1`, `b = 0`, `b = b + 1`, and `print(a, b)`. Therefore, the statement coverage is `5/5 = 100%`.
- The program has 2 branches: `if a < 10` and `else`. Therefore, the branch coverage is `2/2 = 100%`.
- The program has 3 paths: `1-2-5`, `1-3-4-5`, and `1-3-5`. Therefore, the path coverage is `3/3 = 100%`.