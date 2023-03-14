### Generation of Graph from Program

- A graph is a visual representation of the structure and flow of a program.
- A graph consists of nodes and edges, where nodes represent statements or blocks of code, and edges represent the possible transitions between nodes.
- A graph can help in understanding the logic and complexity of a program, as well as in designing and executing test cases.
- There are different types of graphs that can be generated from a program, such as control flow graph, data flow graph, call graph, etc.
- A control flow graph (CFG) shows the sequence of execution of statements or blocks in a program, along with the branching and looping conditions.
- A data flow graph (DFG) shows the dependencies and interactions of variables and data in a program, along with the definitions and uses of variables.
- A call graph (CG) shows the relationships and invocations of functions or procedures in a program, along with the parameters and return values.
- To generate a graph from a program, the following steps are usually followed:
  - Identify the nodes and edges of the graph based on the type of graph and the level of abstraction.
  - Label the nodes and edges with appropriate information, such as statement numbers, variable names, function names, etc.
  - Draw the graph using a standard notation, such as boxes for nodes, arrows for edges, diamonds for branching conditions, etc.
  - Verify the correctness and completeness of the graph by checking the correspondence between the graph and the program.
- An example of generating a control flow graph from a program is shown below:

```c
// Program to calculate the factorial of a number
int factorial(int n) {
  int f = 1; // 1
  while (n > 0) { // 2
    f = f * n; // 3
    n = n - 1; // 4
  }
  return f; // 5
}
```

The control flow graph for the above program is:

![CFG](https://i.imgur.com/0Z6w1Zl.png)

The nodes are numbered according to the statement numbers in the program. The edges represent the possible transitions between the nodes. The diamond node represents the branching condition of the while loop. The node with double borders represents the exit point of the function.