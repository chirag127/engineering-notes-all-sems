### Generation of Graph from Program

- A graph is a mathematical structure that represents the relationships between entities, such as nodes and edges.
- A graph can be used to model the control flow of a program, which is the sequence of execution of statements and branches.
- A control flow graph (CFG) is a type of graph that shows the possible paths of execution of a program, where each node represents a basic block (a sequence of statements with no branches) and each edge represents a transfer of control between basic blocks.
- A CFG can be derived from the source code of a program by identifying the entry and exit points, the basic blocks, and the branching conditions.
- A CFG can be used for various purposes in software testing, such as measuring the complexity of a program, generating test cases, and evaluating the coverage of test cases.
- A CFG can be represented in different ways, such as using adjacency matrices, adjacency lists, or graphical diagrams.
- A graphical diagram is a visual representation of a CFG, where each node is drawn as a circle or a rectangle, and each edge is drawn as a line or an arrow.
- A graphical diagram can be generated from a program by following these steps:
  - Identify the entry and exit points of the program and label them as START and END nodes.
  - Identify the basic blocks of the program and label them with numbers or letters.
  - Identify the branching conditions of the program and label them with true (T) or false (F) values.
  - Draw the nodes and edges of the CFG according to the program structure and the branching conditions.
  - Optionally, annotate the nodes and edges with additional information, such as statement numbers, variable values, or test cases.
- An example of a graphical diagram generated from a program is shown below:

```text
// Program to compute the maximum of three numbers
int max(int a, int b, int c) {
  int m;
  if (a > b) {
    m = a;
  } else {
    m = b;
  }
  if (c > m) {
    m = c;
  }
  return m;
}
```

```text
START
  |
  | a, b, c
  V
  1. int m;
  |
  | a > b
  V
  +----T----> 2. m = a; ----+
  |                         |
  F                         |
  V                         V
  3. m = b;                 | c > m
  |                         V
  +-----------------------> +----T----> 4. m = c; ----+
                            |                         |
                            F                         |
                            V                         V
                            5. return m; <------------+
                              |
                              V
                             END
```