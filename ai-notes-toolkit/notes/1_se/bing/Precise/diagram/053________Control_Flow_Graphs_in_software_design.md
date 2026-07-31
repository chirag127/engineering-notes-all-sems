A Control Flow Graph (CFG) is a graphical representation of the control flow of a program. Each node in the graph represents a basic block, which is a sequence of instructions with a single entry point and a single exit point. The edges between the nodes represent the flow of control between the basic blocks.

Here is an example of a Control Flow Graph for a simple program that calculates the factorial of a number:

```
          +----------------+
          |  Start         |
          +-------+--------+
                  |
                  v
          +-------+--------+
          |  Input n       |
          +-------+--------+
                  |
                  v
          +-------+--------+
          |  fact = 1      |
          +-------+--------+
                  |
                  v
          +-------+--------+
          |  i = 1         |
          +-------+--------+
                  |
                  v
          +-------+--------+
          |  while i <= n  |
          +-------+--------+
                  |
          +-------+        +-------+
          v                v
+---------+------+  +------+--------+
| fact = fact * i |  |  Output fact  |
+---------+------+  +------+--------+
          |                |
          v                v
+---------+------+  +------+--------+
| i = i + 1      |  |  End          |
+----------------+  +---------------+
          |
          v
          +-------+--------+
          |  while i <= n  |
          +----------------+
```

###### Control Flow Graphs in software design
In software design, Control Flow Graphs are used to visualize the flow of control in a program, which can help in understanding the logic of the program and identifying potential issues such as infinite loops or unreachable code. They are also used in various software analysis and optimization techniques, such as data flow analysis and loop optimization.
