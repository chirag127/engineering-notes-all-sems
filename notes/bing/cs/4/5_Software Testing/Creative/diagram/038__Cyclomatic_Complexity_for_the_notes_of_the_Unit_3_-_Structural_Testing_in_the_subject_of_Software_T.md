Cyclomatic complexity is a software metric that measures the number of linearly independent paths through a program's source code. It is calculated using the control-flow graph of the program, where the nodes represent groups of commands and the edges represent the possible transitions between them. The formula for cyclomatic complexity is:

Cyclomatic complexity = E - N + 2*P

where,

E = number of edges in the flow graph.

N = number of nodes in the flow graph.

P = number of nodes that have exit points.

A higher cyclomatic complexity indicates a more complex and less maintainable program. A lower cyclomatic complexity indicates a simpler and more readable program.

The following diagram illustrates the basic concept of cyclomatic complexity using an example program:

```
+-----------------+       +-----------------+
| Start           |       | End             |
+-----------------+       +-----------------+
          |                         ^
          |                         |
          v                         |
+-----------------+                 |
| Print "Hello"   |                 |
+-----------------+                 |
          |                         |
          v                         |
+-----------------+                 |
| IF A > B        |                 |
+-----------------+                 |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          v                         |
+-----------------+                 |
| Print "A is big"|                 |
+-----------------+                 |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          v                         |
+-----------------+                 |
| ELSE            |                 |
+-----------------+                 |
          |                         |
          v                         |
+-----------------+                 |
| Print "B is big"|                 |
+-----------------+                 |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          v                         |
+-----------------+                 |
| ENDIF           |                 |
+-----------------+                 |
          |                         |
          v                         |
+-----------------+                 |
| Print "Goodbye" |-----------------+
+-----------------+
```

In this diagram, there are 8 nodes and 9 edges. There is only one node with an exit point, which is the End node. Therefore, the cyclomatic complexity of this program is:

Cyclomatic complexity = 9 - 8 + 2*1

Cyclomatic complexity = 3

This means that there are 3 linearly independent paths through this program, which are:

- Start -> Print "Hello" -> IF A > B -> Print "A is big" -> ENDIF -> Print "Goodbye" -> End
- Start -> Print "Hello" -> IF A > B -> ELSE -> Print "B is big" -> ENDIF -> Print "Goodbye" -> End
- Start -> Print "Hello" -> IF A > B -> ENDIF -> Print "Goodbye" -> End (This path is possible if A and B are equal)

I hope this diagram helps you understand the concept of cyclomatic complexity for the notes of the Unit 3 - Structural Testing in the subject of Software Testing.