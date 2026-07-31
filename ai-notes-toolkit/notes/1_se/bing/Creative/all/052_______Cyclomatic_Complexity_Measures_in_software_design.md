##### Cyclomatic Complexity Measures in Software Design

- Cyclomatic complexity is a software metric used to indicate the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a program's source code  .
- Linearly independent paths are paths that have at least one edge (or statement) that has not been traversed before in any other paths .
- Cyclomatic complexity can be calculated using the following formula :

    `C = E - N + 2P`

    where C is the cyclomatic complexity, E is the number of edges, N is the number of nodes, and P is the number of connected components in the control flow graph of the program.

- Cyclomatic complexity can be used for two purposes:
    - To measure the quality of the code. Higher cyclomatic complexity indicates more decision logic, which may increase the risk of errors, bugs, and maintenance issues. A lower cyclomatic complexity is desirable, as it implies simpler and more readable code.
    - To estimate the testing effort. Higher cyclomatic complexity implies more test cases are needed to achieve full coverage of the code. A lower cyclomatic complexity means fewer test cases are required, which may reduce the testing time and cost.

- Some tools that can be used to measure cyclomatic complexity are :
    - Visual Studio Code Metrics
    - SonarQube
    - Code Climate
    - Lizard
    - PMD

- A possible mnemonic to remember the formula for cyclomatic complexity is:

    `Cyclomatic complexity equals Edges minus Nodes plus two times Parts`

    where Parts refers to the connected components in the graph.