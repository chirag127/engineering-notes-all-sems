### Cyclomatic Complexity

Cyclomatic complexity is a software metric used to indicate the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a program's source code. It was developed by Thomas J. McCabe, Sr. in 1976.

Some of the main points about cyclomatic complexity are:

- It is calculated by developing a control flow graph of the code that measures the number of linearly-independent paths through a program module.
- It is defined as measuring "the amount of decision logic in a source code function". Simply put, the more decisions that have to be made in code, the more complex it is.
- It can be computed using the formula: `Cyclomatic complexity = E – N + 2*P` where, `E` = represents a number of edges in the control flow graph, `N` = represents the number of nodes in the control flow graph, `P` = represents the number of connected components.
- It can also be computed using the formula: `Cyclomatic complexity = Number of decision points + 1` where, decision points are `if`, `while`, `for`, `case`, etc. statements.
- It can be used to measure the quality of the code, as higher cyclomatic complexity implies more testing effort, more maintenance cost, and more potential errors.
- It can be used to set a limit on the maximum allowable complexity for a program module, as a guideline for code refactoring or modularization.
- It can be used to estimate the minimum number of test cases required to achieve 100% branch coverage, as cyclomatic complexity equals the number of independent paths.