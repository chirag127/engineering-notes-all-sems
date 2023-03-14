Cyclomatic complexity is a software metric used to indicate the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a program's source code. It was developed by Thomas J. McCabe, Sr. in 1976.

Cyclomatic complexity is computed using the control-flow graph of the program: the nodes of the graph correspond to indivisible groups of commands of a program, and a directed edge connects two nodes if the second command might be executed immediately after the first command.

Cyclomatic complexity can be calculated using the following formula:

Cyclomatic complexity = E - N + 2*P

where,

E = number of edges in the flow graph.

N = number of nodes in the flow graph.

P = number of nodes that have exit points.

Here is an example of a simple program and its control-flow graph:

```
IF A = 10 THEN
   IF B > C THEN
      A = B
   ELSE
      A = C
   ENDIF
ENDIF
Print A
Print B
Print C
```

```
    +-----------------+
    | A = 10          |
    +-----------------+
          |
          v
    +-----------------+
    | B > C           |
    +-----------------+
     /             \
    /               \
   v                 v
+------+         +------+
| A = B |         | A = C |
+------+         +------+
   \                 /
    \               /
     v             v
+-----------------+
| Print A         |
+-----------------+
          |
          v
+-----------------+
| Print B         |
+-----------------+
          |
          v
+-----------------+
| Print C         |
+-----------------+
```

In this example, the number of edges is 9, the number of nodes is 8, and the number of exit points is 1. Therefore, the cyclomatic complexity is 9 - 8 + 2*1 = 3.

Cyclomatic complexity can be used to measure the structural complexity of a program, the difficulty of testing and maintaining it, and the likelihood of errors in it. Generally, lower values of cyclomatic complexity are desirable, as they indicate simpler and more readable code. A common threshold for cyclomatic complexity is 10, although some organizations may use higher or lower limits.