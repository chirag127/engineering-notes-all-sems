### Cyclomatic Complexity Measures

- Cyclomatic complexity is a software metric used to indicate the complexity of a program   .
- It is a quantitative measure of the number of linearly independent paths through a program's source code  .
- It was developed by Thomas J. McCabe, Sr. in 1976 .
- McCabe interprets a computer program as a set of a strongly connected directed graph, where the nodes represent the basic blocks of the program and the edges represent the control flow between them .
- The cyclomatic complexity of a program can be calculated by using the following formula :

```
V(G) = E - N + 2P
```

where,

- V(G) is the cyclomatic complexity of the program graph G
- E is the number of edges in the graph
- N is the number of nodes in the graph
- P is the number of connected components in the graph

- Alternatively, the cyclomatic complexity can be calculated by using the following formula :

```
V(G) = R + 1
```

where,

- V(G) is the cyclomatic complexity of the program graph G
- R is the number of regions in the graph

- The regions of a graph are the areas enclosed by the edges, including the area outside the graph .
- The cyclomatic complexity can also be calculated by counting the number of decision points in the program, such as if, while, for, case, etc., and adding one .

```
V(G) = D + 1
```

where,

- V(G) is the cyclomatic complexity of the program graph G
- D is the number of decision points in the program

- The cyclomatic complexity of a program can be used to measure the quality, maintainability, and testability of the code  .
- A lower cyclomatic complexity indicates a simpler program with fewer paths and less testing effort  .
- A higher cyclomatic complexity indicates a more complex program with more paths and more testing effort  .
- A general guideline is to keep the cyclomatic complexity of a program below 10  .
- There are various tools available to measure the cyclomatic complexity of a program, such as Visual Studio, SonarQube, CodeSonar, etc .