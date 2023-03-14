###### Control Flow Graphs in software design

- A control flow graph (CFG) is a graphical representation of the possible paths of execution of a program or a function.
- A CFG consists of nodes and edges, where each node represents a basic block and each edge represents a possible transfer of control between basic blocks.
- A basic block is a sequence of instructions that has a single entry point and a single exit point, and does not contain any branches or jumps.
- A CFG can be used to analyze various properties of a program or a function, such as reachability, liveness, dominance, loop detection, data flow, etc.
- A CFG can also be used to optimize a program or a function, such as dead code elimination, constant propagation, common subexpression elimination, etc.
- A CFG can be constructed from the source code or the intermediate code of a program or a function, using various algorithms, such as the algorithm of Aho, Sethi and Ullman, or the algorithm of Cytron, Ferrante, Rosen, Wegman and Zadeck.
- A CFG can be represented in various ways, such as text, matrix, or graph. A common graphical representation of a CFG is to use rectangles for nodes, arrows for edges, and labels for instructions or conditions.
- A CFG can be modified to include additional information, such as loop headers, loop exits, loop invariants, loop variants, etc.
- A CFG can be simplified by applying various transformations, such as node splitting, node merging, edge splitting, edge merging, etc.

Here is an example of a CFG for a simple function that computes the factorial of a positive integer n:

```
int factorial(int n) {
  int result = 1;
  while (n > 1) {
    result = result * n;
    n = n - 1;
  }
  return result;
}
```

The CFG for this function is:

```
+-----------------+     +-----------------+
| Entry           |     | result = 1      |
|                 |---->|                 |
+-----------------+     +-----------------+
                             |
                             |     +-----------------+
                             |     | result = result |
                             |---->| * n             |
                             |     +-----------------+
                             |             |
                             |     +-----------------+
                             |     | n = n - 1       |
                             |---->|                 |
                             |     +-----------------+
                             |             |
                             |             v
+-----------------+     +-----------------+
| Exit            |<----| return result   |
|                 |     |                 |
+-----------------+     +-----------------+
                             ^
                             |
                             |     +-----------------+
                             |<----| n > 1           |
                             |     |                 |
                             |     +-----------------+
                             |
                             |
```

Some points to note about this CFG are:

- The entry node and the exit node are special nodes that do not correspond to any basic block in the source code. They are used to indicate the start and the end of the function.
- The node with the label `n > 1` is the loop header, which is the entry point of the loop. The edge from this node to the exit node is the loop exit, which is the exit point of the loop.
- The nodes with the labels `result = result * n` and `n = n - 1` are the loop body, which is the part of the loop that is executed repeatedly.
- The node with the label `result = 1` is the loop preheader, which is the part of the code that is executed before entering the loop.
- The node with the label `return result` is the loop postheader, which is the part of the code that is executed after exiting the loop.
- The loop invariant is a property that holds true before and after each iteration of the loop. For example, one loop invariant for this loop is `result = (n + 1)!`.
- The loop variant is a property that decreases with each iteration of the loop and eventually becomes false. For example, one loop variant for this loop is `n`.