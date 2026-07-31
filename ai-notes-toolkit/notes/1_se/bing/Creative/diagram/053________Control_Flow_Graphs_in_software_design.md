A control flow graph (CFG) is a graphical representation of the possible paths of execution of a program or a function. It consists of nodes and edges, where nodes represent basic blocks of code (sequences of statements that are always executed together) and edges represent the flow of control between them. A CFG can be used for various purposes, such as static analysis, optimization, testing, debugging, and documentation of software.

To draw a CFG, one needs to identify the basic blocks of code and the conditions that affect the control flow. Then, one can use symbols such as rectangles, diamonds, circles, and arrows to represent the nodes and edges of the graph. Here is an example of a CFG for a simple function that calculates the factorial of a positive integer n:

###### Control Flow Graphs in software design

```
+-----------------+
| Start           |
+-----------------+
        |
        v
+-----------------+
| int n, f = 1    |
+-----------------+
        |
        v
+-----------------+
| Read n          |
+-----------------+
        |
        v
+-----------------+       +-----------------+
| n > 0           |------>| Stop            |
+-----------------+       +-----------------+
        |
        v
+-----------------+
| f = f * n       |
+-----------------+
        |
        v
+-----------------+
| n = n - 1       |
+-----------------+
        |
        v
+-----------------+
| Print f         |
+-----------------+
        |
        v
+-----------------+
| Stop            |
+-----------------+
```