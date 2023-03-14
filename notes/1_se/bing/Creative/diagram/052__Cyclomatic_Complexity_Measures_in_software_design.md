Cyclomatic complexity is a software metric that measures the number of linearly independent paths in a program. It is computed using the control flow graph of the program, where the nodes represent the smallest group of commands and the edges represent the possible transitions between them. The cyclomatic complexity can be calculated using the formula:

M = E - N + 2P

where M is the cyclomatic complexity, E is the number of edges, N is the number of nodes, and P is the number of connected components in the graph.

The cyclomatic complexity can be used to estimate the difficulty of testing, maintaining, or troubleshooting a program, as well as the risk of errors. Generally, higher values of cyclomatic complexity indicate more complex and less reliable code, while lower values indicate simpler and more reliable code. A common threshold for cyclomatic complexity is 10, although some programs may require higher or lower values depending on the context.

The following diagram illustrates the basic architecture of a control flow graph and how to calculate the cyclomatic complexity using the formula:

```
+-----------------+
| Start of program|
+-----------------+
        |
        v
+-----------------+
|     Node 1      |
+-----------------+
        |
        v
+-----------------+
|     Node 2      |
+-----------------+
        |
        v
+-----------------+
|     Node 3      |
+-----------------+
      /   \
     /     \
    v       v
+-----------------+   +-----------------+
|     Node 4      |   |     Node 5      |
+-----------------+   +-----------------+
    \       /
     \     /
      v   v
+-----------------+
|     Node 6      |
+-----------------+
        |
        v
+-----------------+
| End of program  |
+-----------------+

E = 8 (number of edges)
N = 7 (number of nodes)
P = 1 (number of connected components)

M = E - N + 2P
M = 8 - 7 + 2
M = 3 (cyclomatic complexity)
```