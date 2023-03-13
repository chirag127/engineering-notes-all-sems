### Cyclomatic Complexity

- Cyclomatic complexity is a metric that measures the complexity of a program or a module by counting the number of independent paths through the code.
- It was proposed by Thomas J. McCabe in 1976 as a way to assess the quality and maintainability of software.
- Cyclomatic complexity can be calculated using the following formula:

  - `CC = E - N + 2P`

  - Where CC is the cyclomatic complexity, E is the number of edges in the control flow graph, N is the number of nodes in the control flow graph, and P is the number of connected components (usually 1 for a single program).

- Alternatively, cyclomatic complexity can be calculated using the following formula:

  - `CC = D + 1`

  - Where CC is the cyclomatic complexity and D is the number of decision points (such as if, while, for, switch, etc.) in the code.

- Cyclomatic complexity can be used to determine the minimum number of test cases required to achieve 100% branch coverage, which is equal to the cyclomatic complexity value.
- Cyclomatic complexity can also be used to identify the most complex or risky parts of the code that may need more testing, refactoring, or documentation.
- Cyclomatic complexity can be reduced by applying good programming practices, such as modularization, abstraction, simplification, and avoiding nested or redundant conditions.