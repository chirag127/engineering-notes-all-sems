### Generation of Graph from Program for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Structural testing is a type of software testing that focuses on the internal design and implementation of the software, rather than its functionality.
- Structural testing uses the program's control flow and data flow as models to design test cases and measure test coverage.
- Generation of graph from program is a technique to represent the program's structure and logic in a graphical form, such as a flowchart or a control flow graph.
- A flowchart is a diagram that shows the sequence of steps and decisions in a program using symbols and arrows.
- A control flow graph is a directed graph that shows the possible paths of execution in a program using nodes and edges.
- A node represents a basic block, which is a sequence of statements that can be executed without branching.
- An edge represents a transfer of control from one basic block to another.
- A control flow graph can be generated from a program by following these steps:
  - Identify the basic blocks in the program and label them with numbers or letters.
  - Draw a node for each basic block and write the label inside the node.
  - Draw an edge from one node to another if there is a transfer of control between the corresponding basic blocks.
  - Mark the entry and exit nodes of the graph with special symbols, such as a circle or a square.
- For example, consider the following program:

```c
// Program to calculate the factorial of a number
#include <stdio.h>
int main()
{
  int n, i, f = 1;
  printf("Enter a positive integer: ");
  scanf("%d", &n);
  if (n < 0)
    printf("Invalid input.\n");
  else
  {
    for (i = 1; i <= n; i++)
      f = f * i;
    printf("Factorial of %d = %d\n", n, f);
  }
  return 0;
}
```

- The control flow graph for this program is:

```
    +---+
    | 1 |
    +---+
      |
      v
    +---+
    | 2 |
    +---+
      |
      v
    +---+
    | 3 |
    +---+
      |
      v
    +---+
    | 4 |
    +---+
      |
      v
    +---+
    | 5 |
    +---+
    / \
   /   \
  v     v
+---+  +---+
| 6 |  | 7 |
+---+  +---+
  |      |
  v      v
+---+  +---+
| 8 |  | 9 |
+---+  +---+
  |      |
  v      v
+---+  +---+
|10 |  |11 |
+---+  +---+
  |      |
  v      v
+---+  +---+
|12 |  |13 |
+---+  +---+
  |      |
  v      v
+---+  +---+
|14 |  |15 |
+---+  +---+
  |      |
  v      v
+---+  +---+
|16 |  |17 |
+---+  +---+
  |      |
  v      v
+---+  +---+
|18 |  |19 |
+---+  +---+
  |      |
  v      v
+---+  +---+
|20 |  |21 |
+---+  +---+
  |      |
  v      v
+---+  +---+
|22 |  |23 |
+---+  +---+
  |      |
  v      v
+---+  +---+
|24 |  |25 |
+---+  +---+
  |      |
  v      v
+---+  +---+
|26 |  |27 |
+---+  +---+
  |      |
  v      v
+---+  +---+
|28 |  |29 |
+---+  +---+
  |      |
  v      v
+---+  +---+
|30 |  |31 |
+---+  +---+
  |      |
  v      v
+---+  +---+