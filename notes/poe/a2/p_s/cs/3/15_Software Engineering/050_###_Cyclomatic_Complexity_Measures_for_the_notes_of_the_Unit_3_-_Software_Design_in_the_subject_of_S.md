 Here is the content written in markdown format for the given topic:

### Cyclomatic Complexity Measures

Cyclomatic complexity is a software metric used to indicate the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a program's source code.

- It was developed by Thomas J. McCabe, Sr. in 1976.
- It is calculated as:

Cyclomatic Complexity = E - N + 2

Where E is the number of edges of the graph and N is the number of nodes of the graph.

- A graph is generated from the control flow of the program. Each executable statement is represented as a node and edges between the nodes indicate the flow of control.
- The complexity is minimally 1 (for a sequence of statements with no decisions or loops).
- A higher cyclomatic complexity indicates that the program may be difficult to understand, debug and maintain.
- It can be used to:

- Predict the number of test cases required to achieve a given coverage.
- Identify areas of a program that are more fault-prone.
- Set thresholds for functions/methods to control complexity.

Advantages:

- It is language independent and can be applied to any program.
- It is easy and inexpensive to compute.

Disadvantages:

- It only considers the control flow and ignores data flow, which can also affect complexity.
- The thresholds used are arbitrary and open to interpretation.
- The graph generation can be difficult for complex programs with exceptions and nested control flows.

Examples:

- Sequence: Complexity = 1
- If-then: Complexity = 2
- If-then-else: Complexity = 3
- While loop: Complexity = 2

Applications:

- It is commonly used as a software metric to gain a broad understanding of the complexity of a program.
- It can help in test case generation, fault prediction and code refactoring.
- Many code coverage criteria are based on McCabe's cyclomatic complexity.