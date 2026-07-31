# Generation of Graph from Program

- A graph is a mathematical structure that represents the relationships between a set of objects, called nodes or vertices, and a set of pairs of objects, called edges or arcs.
- A graph can be used to model the control flow of a program, which is the sequence of execution of statements and branches based on conditions and loops.
- A control flow graph (CFG) is a type of graph that shows the possible paths of execution of a program, where each node represents a basic block (a sequence of statements that are always executed together) and each edge represents a transfer of control between basic blocks.
- A CFG can be derived from the source code of a program by identifying the entry and exit points, the basic blocks, and the control flow edges between them.
- A CFG can be used for various purposes in software testing, such as measuring the complexity of a program, generating test cases, and evaluating the coverage of test cases.
- One way to measure the complexity of a program is to use the cyclomatic complexity, which is a metric that counts the number of linearly independent paths in a CFG. The cyclomatic complexity can be calculated by using the formula:

  - `V(G) = E - N + 2`, where `V(G)` is the cyclomatic complexity, `E` is the number of edges, and `N` is the number of nodes in the CFG.
  - `V(G) = P + 1`, where `P` is the number of predicate nodes (nodes that have more than one outgoing edge) in the CFG.
- One way to generate test cases for a program is to use the path testing method, which aims to cover all the possible paths of execution in a CFG. The path testing method involves the following steps:

  - Construct the CFG of the program from the source code.
  - Calculate the cyclomatic complexity of the CFG.
  - Identify a set of linearly independent paths in the CFG that covers all the edges. The number of paths should be equal to the cyclomatic complexity.
  - Generate test cases for each path by using techniques such as random testing or symbolic testing.
- One way to evaluate the coverage of test cases for a program is to use the branch coverage criterion, which measures the percentage of edges in the CFG that are executed by the test cases. The branch coverage criterion can be defined as:

  - `BC = (Ee / E) * 100`, where `BC` is the branch coverage, `Ee` is the number of edges executed by the test cases, and `E` is the total number of edges in the CFG.
  - The branch coverage criterion can be improved by using different definitions of branch covering, such as decision coverage, condition coverage, or multiple condition coverage, which consider the outcomes of the predicate nodes in the CFG.
- A decision graph is a type of graph that represents the logical expressions of the predicate nodes in a CFG, where each node represents a condition or a decision, and each edge represents a logical operator or a branch. A decision graph can be used to compare and clarify different definitions of branch covering in software testing.