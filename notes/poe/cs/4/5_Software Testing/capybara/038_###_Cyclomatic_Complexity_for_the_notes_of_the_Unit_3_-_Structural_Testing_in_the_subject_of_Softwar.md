### Cyclomatic Complexity for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

Cyclomatic complexity is a software metric that measures the complexity of a program. It is used to determine the number of independent paths through a program's source code. The concept of cyclomatic complexity was first introduced by Thomas McCabe in 1976.

#### Calculating Cyclomatic Complexity

Cyclomatic complexity can be calculated using the following formula:

```
M = E - N + 2P
```
where:
- M = Cyclomatic complexity
- E = Number of edges in the control flow graph
- N = Number of nodes in the control flow graph
- P = Number of connected components in the control flow graph

#### Control Flow Graph

To calculate the cyclomatic complexity of a program, we first need to construct its control flow graph. A control flow graph is a graphical representation of a program's control flow. It consists of nodes, which represent the program's basic blocks, and edges, which represent the program's control flow.

#### Advantages of Cyclomatic Complexity

- Cyclomatic complexity can be used to measure the quality of a program's design.
- It can be used to identify parts of a program that are difficult to test.
- It can be used to identify parts of a program that are likely to contain errors.

#### Disadvantages of Cyclomatic Complexity

- Cyclomatic complexity can be time-consuming to calculate for large programs.
- It can be difficult to interpret the results of a cyclomatic complexity calculation.

#### Mnemonics and Learning Tricks

There are several mnemonics and learning tricks that can be used to remember the concept of cyclomatic complexity. One mnemonic is "V = E - N + 2", which represents the formula for the cyclomatic complexity of a program without considering the number of connected components in the control flow graph. Another learning trick is to remember that a program with a high cyclomatic complexity is like a maze, with many different paths that can be taken.

#### Examples of Cyclomatic Complexity

Consider the following code snippet:

```
if (x > y) {
  z = x + y;
} else {
  z = x - y;
}
```

The control flow graph for this code snippet has two nodes and two edges, resulting in a cyclomatic complexity of 2.

Consider the following code snippet:

```
for (i = 0; i < n; i++) {
  for (j = 0; j < m; j++) {
    if (a[i][j] == x) {
      printf("Found at (%d, %d)\n", i, j);
    }
  }
}
```

The control flow graph for this code snippet has three nodes and four edges, resulting in a cyclomatic complexity of 2.

#### Applications of Cyclomatic Complexity

Cyclomatic complexity can be used in software development to identify parts of a program that are likely to contain errors. It can also be used to measure the quality of a program's design and to identify parts of a program that are difficult to test.