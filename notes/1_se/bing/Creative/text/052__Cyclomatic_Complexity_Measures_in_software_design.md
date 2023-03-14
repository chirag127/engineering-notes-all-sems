##### Cyclomatic Complexity Measures in software design

- Cyclomatic complexity is a software metric used to indicate the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a program's source code.
- It is computed using the control flow graph of the program, where the nodes represent the smallest group of commands and the edges represent the possible transitions between them.
- Mathematically, the cyclomatic complexity M of a structured program is defined as:

  M = E - N + 2P

  where E is the number of edges, N is the number of nodes, and P is the number of connected components in the control flow graph .
- Cyclomatic complexity can be used to determine the independent path executions, which can be helpful for developers and testers to ensure that every path has been tested at least once, to improve code coverage, and to evaluate the risk associated with the program .
- Cyclomatic complexity can also be used as a quality metric, as it gives a relative measure of the complexity of various designs, and can guide the testing process .
- However, cyclomatic complexity has some limitations, such as:
  - It only measures the control complexity and not the data complexity of the program.
  - It may give a misleading figure for simple comparisons and decision structures.
  - It does not account for the nested conditional structures, which are harder to understand than non-nested ones.
- There is no exact limit for cyclomatic complexity that fits all organizations, but a common rule of thumb is to keep it below 10, as suggested by McCabe, the original developer of the metric . Higher values of cyclomatic complexity indicate higher risk, more testing effort, and lower maintainability of the program.