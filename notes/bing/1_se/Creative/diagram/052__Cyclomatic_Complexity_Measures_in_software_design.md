Cyclomatic complexity is a software metric that measures the number of independent paths through a program's source code. It is calculated as the number of edges minus the number of nodes plus two in the control flow graph of the program. A control flow graph is a representation of the program's structure, where each node is a basic block of code and each edge is a possible flow of control between the blocks. The cyclomatic complexity can be used to estimate the testing effort and the maintainability of the program.

##### Cyclomatic Complexity Measures in software design

The following diagram illustrates the basic architecture of a control flow graph and how to calculate the cyclomatic complexity using an example program.

```
+----------------+       +----------------+       +----------------+
| Start          |       | if (a > b)     |       | print(a)       |
| a = 10         |       | then           |       |                |
| b = 5          |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                         |    |                     |
       |                         |    |                     |
       |                         |    |                     |
       |                         |    |                     |
       |                         |    |                     |
       |                         |    |                     |
       |                         |    |                     |
       |                         |    |                     |
       |                         |    |                     |
       |                         |    |                     |
       |                         |    +---------------------+
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         +---------------------+
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       +-------------------------------------------+
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
+----------------+       +----------------+       +----------------+
| else           |       | print(b)       |       | End            |
|                |       |                |       |                |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         |                     |
       |                         +---------------------+
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       +-------------------------------------------+
```

In this diagram, there are seven nodes (basic blocks of code) and nine edges (possible flows of control). Therefore, the cyclomatic complexity is 9 - 7 + 2 = 4. This means that there are four independent paths through the program, which can be identified as:

- Start -> if (a > b) -> print(a) -> End
- Start -> if (a > b) -> else -> print(b) -> End
- Start -> if (a > b) -> print(a) -> print(b) -> End
- Start -> if (a > b) -> else -> print(b) -> print(a) -> End

These paths correspond to the different combinations of the condition (a > b) being true or false. To test the program thoroughly, each path should be executed at least once with appropriate input values. The higher the cyclomatic complexity, the more paths there are and the more testing effort is required. The cyclomatic complexity can also indicate the maintainability of the program, as a high complexity may imply a high risk of errors and a low readability. A general guideline is to keep the cyclomatic complexity below 10 for each function or module.