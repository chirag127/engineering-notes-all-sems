According to the web search results, independent paths are a set of paths in the control flow graph of a program that are linearly independent, meaning that no path can be constructed by combining other paths. Independent paths are used to measure the cyclomatic complexity of a program, which is the number of linearly independent paths through the program. Cyclomatic complexity can be calculated by using the formula V(G) = e - n + 2P, where e is the number of edges, n is the number of nodes, and P is the number of connected components in the graph.

The following diagram illustrates the basic architecture of a control flow graph for a program with four independent paths:

```
    A
   / \
  B   C
 / \ / \
D   E   F
 \ / \ /
  G   H
   \ /
    I
```

The four independent paths are:

- A-B-D-G-I
- A-B-E-G-I
- A-C-F-H-I
- A-C-E-H-I

The cyclomatic complexity of this graph is V(G) = 12 - 9 + 2 = 5.