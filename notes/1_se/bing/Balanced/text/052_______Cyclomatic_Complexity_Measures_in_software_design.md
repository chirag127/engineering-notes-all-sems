##### Cyclomatic Complexity Measures in software design

- Cyclomatic complexity is a metric that measures the complexity of a program or a module by counting the number of independent paths through the code.
- It is based on the idea that the more branches and loops a program has, the more complex and error-prone it is.
- It was proposed by Thomas J. McCabe in 1976 as a way to quantify the maintainability and testability of software.
- The cyclomatic complexity of a program or a module can be calculated by using the following formula:

    - `C = E - N + 2P`
    - Where C is the cyclomatic complexity, E is the number of edges in the control flow graph, N is the number of nodes in the control flow graph, and P is the number of connected components (such as subroutines or functions) in the graph.
- Alternatively, the cyclomatic complexity can be computed by using the following rules:

    - Start with a value of one for the program or module.
    - Add one for each decision point in the code, such as an if statement, a switch statement, a for loop, a while loop, a do-while loop, a break statement, a continue statement, or a goto statement.
    - Add one for each case or default clause in a switch statement.
    - Ignore the complexity of any functions or subroutines that are called from the program or module, unless they are recursive or mutually recursive.
- The cyclomatic complexity can be used to estimate the number of test cases needed to achieve full branch coverage of the code, which is equal to the cyclomatic complexity itself.
- It can also be used to identify the parts of the code that are more likely to contain defects or require more maintenance, which are those with high cyclomatic complexity values.
- A common guideline is to keep the cyclomatic complexity of a program or a module below 10, or at most 15, to ensure good software quality and readability.