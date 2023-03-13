A control flow graph (CFG) is a graphical representation of the possible paths of execution of a program or a function. It consists of nodes and edges, where nodes represent basic blocks of code (sequences of statements that are always executed together) and edges represent the flow of control between them. The entry node is the starting point of the program or function, and the exit node is the end point. A CFG can be used for various purposes, such as static analysis, compiler optimization, testing, debugging, and simulation.

A basic block is a maximal sequence of statements that has a single entry point and a single exit point. A basic block can be identified by finding the leaders, which are the first statements of a basic block. The leaders are:

- The first statement of the program or function.
- Any statement that is the target of a jump, branch, or loop instruction.
- Any statement that immediately follows a jump, branch, or loop instruction.

To construct a CFG, the following steps can be followed:

- Identify the basic blocks and their leaders.
- Draw a node for each basic block and label it with the leader's line number or name.
- Draw an edge from one node to another if there is a possible flow of control from the first node's basic block to the second node's basic block.
- Mark the entry node and the exit node with special symbols.

The following diagram illustrates the basic architecture of a CFG:

```
    +-----+
    |Entry|
    +-----+
      |
      v
+-----+-----+
|Leader 1   |
|Statement 1|
|Statement 2|
+-----+-----+
      |
      v
+-----+-----+
|Leader 2   |
|Statement 3|
|Statement 4|
+-----+-----+
      |
      v
+-----+-----+
|Leader 3   |
|Statement 5|
|Statement 6|
+-----+-----+
      |
      v
+-----+-----+
|Leader 4   |
|Statement 7|
|Statement 8|
+-----+-----+
      |
      v
    +-----+
    |Exit |
    +-----+
```