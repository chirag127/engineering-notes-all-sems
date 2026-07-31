A control flow graph (CFG) is a graphical representation of the possible paths of execution of a program or a function. It consists of nodes and edges, where nodes represent basic blocks of code (sequences of instructions that have a single entry and a single exit point) and edges represent the flow of control between them. A CFG can be used for various purposes, such as static analysis, compiler optimization, testing, debugging, and reverse engineering of software.

To draw a CFG in ASCII, you can use the following symbols:

- `o` for the start node
- `x` for the end node
- `[]` for a basic block node
- `->` for an edge
- `|` for a vertical line
- `/` or `\` for a diagonal line
- `?` for a conditional branch
- `:` for a label

For example, here is a CFG for a simple function that computes the factorial of a positive integer n:

```
o
|
[n = input()]
|
[n > 0 ?]
/     \
[1]   [n * factorial(n-1)]
|     /
x    /
 \  /
  \/
  x
```

The start node `o` leads to a basic block node `[n = input()]` that assigns the input value to n. Then, there is a conditional branch `?` that checks if n is greater than zero. If yes, the control flow goes to the left branch, where the node `[1]` returns 1 as the factorial of 0. If no, the control flow goes to the right branch, where the node `[n * factorial(n-1)]` recursively calls the function with n-1 as the argument and multiplies the result by n. Both branches end at the end node `x`, which represents the exit point of the function. The diagonal lines `/` and `\` are used to avoid crossing edges and to make the graph more readable.
