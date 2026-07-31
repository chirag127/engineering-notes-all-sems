Cyclomatic complexity is a software metric that measures the number of independent paths through a program's source code. It is calculated as the number of edges minus the number of nodes plus two in the control flow graph of the program. A control flow graph is a graphical representation of the program's structure, where each node is a basic block of code and each edge is a possible flow of control between the blocks. The cyclomatic complexity can be used to estimate the testing effort, the maintainability, and the quality of the program.

Here is an example of a control flow graph and its cyclomatic complexity:

```
    +-----------------+
    | Start/End Block |
    +-----------------+
          |
          v
    +-----------------+
    |     Block 1     |
    +-----------------+
          |
          v
    +-----------------+
    |     Block 2     |
    +-----------------+
         / \
        /   \
       v     v
+-----------------+  +-----------------+
|     Block 3     |  |     Block 4     |
+-----------------+  +-----------------+
       \     /
        \   /
         v v
    +-----------------+
    |     Block 5     |
    +-----------------+
          |
          v
    +-----------------+
    | Start/End Block |
    +-----------------+
```

The cyclomatic complexity of this graph is 6 - 6 + 2 = 2. There are two independent paths: Block 1 -> Block 2 -> Block 3 -> Block 5 and Block 1 -> Block 2 -> Block 4 -> Block 5.