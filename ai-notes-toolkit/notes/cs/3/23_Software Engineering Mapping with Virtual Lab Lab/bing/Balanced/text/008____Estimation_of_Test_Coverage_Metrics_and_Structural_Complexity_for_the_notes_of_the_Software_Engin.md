## Estimation of Test Coverage Metrics and Structural Complexity

- Test coverage metrics are used to measure and monitor the testing activity of a software program. They help to assess the thoroughness, effectiveness and efficiency of testing techniques.
- Structural complexity is a measure of how complex a program is in terms of its control flow and logic. It can be estimated by using control flow graphs (CFGs), which are visual representations of the flow of control within a program .
- A CFG consists of nodes and edges, where nodes represent basic blocks and edges represent transitions between them. A basic block is a sequence of statements that has a single entry point and a single exit point.
- A CFG can help to identify the linearly independent paths in a program, which are paths that traverse at least one edge that is not traversed by any other path. The number of linearly independent paths is also known as the cyclomatic complexity of a program, which is a metric of structural complexity .
- Test coverage metrics can be derived from the CFG and the cyclomatic complexity of a program. Some examples of test coverage metrics are:
  - Statement coverage: the percentage of statements that are executed by the test cases.
  - Branch coverage: the percentage of branches (edges) that are executed by the test cases.
  - Path coverage: the percentage of paths that are executed by the test cases.
  - Condition coverage: the percentage of conditions (boolean expressions) that are evaluated to both true and false by the test cases .
- Test coverage metrics can help to identify the gaps and weaknesses in the testing process, and guide the selection and generation of test cases. They can also help to evaluate the quality and reliability of the software program.