### Generation of Graph from Program

- A graph is a mathematical structure that consists of a set of vertices (nodes) and a set of edges (arcs) that connect pairs of vertices.
- A graph can be used to represent the flow of control in a program, where each vertex corresponds to a statement or a block of statements, and each edge corresponds to a possible transfer of control between statements.
- A graph can help in designing test cases for a program, by identifying different paths of execution that cover different aspects of the program logic and behavior.
- There are different types of graphs that can be derived from a program, such as:
  - Program graph: A graph that shows all the possible paths of execution in a program, including loops and branches. A program graph can be obtained by analyzing the source code or the intermediate code of a program.
  - Decision graph: A graph that shows the logical conditions that determine the branching of a program. A decision graph can be obtained by simplifying the program graph and removing the edges that do not affect the branching.
  - Data dependency graph: A graph that shows the dependencies between the variables and the statements that use or modify them. A data dependency graph can be obtained by analyzing the data flow of a program.
  - Cyclomatic graph: A graph that shows the linearly independent paths of execution in a program. A cyclomatic graph can be obtained by applying the cyclomatic complexity metric to the program graph.
- To generate a graph from a program, the following steps can be followed:
  - Identify the vertices and the edges of the graph based on the type of graph desired.
  - Label the vertices and the edges with appropriate identifiers, such as statement numbers, condition expressions, variable names, etc.
  - Draw the graph using a graphical tool or a notation, such as dot or matrix.
  - Verify the correctness and completeness of the graph by comparing it with the program code and logic.
- An example of generating a program graph from a program is shown below:

```python
# Program to compute the factorial of a positive integer n
n = int(input("Enter a positive integer: ")) # Statement 1
fact = 1 # Statement 2
i = 1 # Statement 3
while i <= n: # Statement 4
  fact = fact * i # Statement 5
  i = i + 1 # Statement 6
print("The factorial of", n, "is", fact) # Statement 7
```

The program graph for the above program is:

```
1 -> 2 -> 3 -> 4
4 -> 5 -> 6 -> 4
4 -> 7
```

The program graph can also be represented as a matrix, where each row and column corresponds to a statement number, and each entry indicates the presence or absence of an edge between the statements:

```
  1 2 3 4 5 6 7
1 0 1 0 0 0 0 0
2 0 0 1 0 0 0 0
3 0 0 0 1 0 0 0
4 0 0 0 0 1 0 1
5 0 0 0 0 0 1 0
6 0 0 0 1 0 0 0
7 0 0 0 0 0 0 0
```

The program graph can also be drawn using a graphical tool, such as:

![Program graph](https://i.imgur.com/8wZ0f1L.png)