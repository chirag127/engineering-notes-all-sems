Path testing is a white-box testing technique that aims to cover all the possible paths of execution in a program or a module. It uses a control flow graph to represent the code structure and identify the linearly independent paths. A path is a sequence of statements or decisions that start from an entry point and end at an exit point. Path testing helps to detect errors in the logic and flow of the program.

The following diagram illustrates the basic steps of path testing:

```
+-----------------+         +-----------------+         +-----------------+
| Draw a control  |         | Calculate       |         | Find a basis    |
| flow graph      |-------->| cyclomatic      |-------->| set of paths    |
|                 |         | complexity      |         |                 |
+-----------------+         +-----------------+         +-----------------+
                                                                  |
                                                                  |
                                                                  V
                                                         +-----------------+
                                                         | Generate test   |
                                                         | cases for each  |
                                                         | path            |
                                                         +-----------------+
```

The control flow graph is a graphical representation of the program structure, where each node represents a statement or a decision, and each edge represents a possible flow of control. The cyclomatic complexity is a metric that measures the number of linearly independent paths in a graph. It can be calculated using the formula:

```
Cyclomatic complexity = E - N + 2P
```

Where E is the number of edges, N is the number of nodes, and P is the number of connected components in the graph. The basis set of paths is a set of paths that covers all the edges in the graph. It can be derived using the cyclomatic complexity as the size of the set. The test cases are then generated for each path in the basis set, ensuring that each path is executed at least once.