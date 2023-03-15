Hello, I am Sydney, your AI assistant. I can help you with your study material for Software Engineering. Here is some content on the topic of Cyclomatic Complexity Measures for the notes of Unit 3 - Software Design:

### Cyclomatic Complexity Measures

- Cyclomatic complexity is a metric that measures the complexity of a software module or a function by counting the number of independent paths through the code.
- It is based on the idea that the more branches and loops a module has, the more complex and error-prone it is.
- It can be used to estimate the testing effort, the maintainability, and the reliability of a software module or a function.
- There are different ways to calculate the cyclomatic complexity, but the most common one is based on the control flow graph (CFG) of the module or the function.
- A control flow graph is a graphical representation of the flow of execution of a module or a function, where the nodes represent the basic blocks (sequences of statements with no branches) and the edges represent the transitions between the basic blocks.
- The cyclomatic complexity can be computed as:

  - C = E - N + 2
  - C = P + 1
  - C = R + 1

  - Where C is the cyclomatic complexity, E is the number of edges, N is the number of nodes, P is the number of connected components, and R is the number of decision points (such as if, while, for, switch, etc.).
- The cyclomatic complexity can also be interpreted as the minimum number of test cases needed to achieve 100% branch coverage of the module or the function.
- The higher the cyclomatic complexity, the more difficult it is to test, maintain, and understand the module or the function.
- A general guideline is to keep the cyclomatic complexity below 10 for a module or a function, and to refactor or split the code if it exceeds this threshold.