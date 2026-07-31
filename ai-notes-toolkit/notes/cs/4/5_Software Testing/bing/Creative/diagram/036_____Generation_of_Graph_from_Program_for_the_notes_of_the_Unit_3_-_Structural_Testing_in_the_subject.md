Hello, I am Sydney, your AI assistant. I can help you with your topic of generation of graph from program. Here are some points that you can use for your notes:

- A graph is a data structure that consists of a set of nodes (also called vertices) and a set of edges (also called arcs) that connect the nodes. A graph can be used to represent various kinds of information, such as the structure of a program, the dependencies among variables, the control flow of a program, etc.
- A program dependence graph (PDG) is a type of graph that shows the data and control dependencies among the statements of a program. A data dependency occurs when a statement uses a value that is defined by another statement. A control dependency occurs when the execution of a statement depends on the outcome of another statement. A PDG can be used for various purposes, such as program analysis, optimization, parallelization, testing, debugging, etc.
- To generate a PDG from a program, we need to perform the following steps:
  - Identify the nodes and edges of the graph. Each node represents a statement or a basic block of the program. Each edge represents a data or control dependency between two nodes. For example, if statement S1 defines a variable x and statement S2 uses x, then there is a data dependency edge from S1 to S2. If statement S3 is a conditional statement and statement S4 is executed only if S3 is true, then there is a control dependency edge from S3 to S4.
  - Label the nodes and edges of the graph. Each node can be labeled with the statement or basic block that it represents. Each edge can be labeled with the type of dependency (data or control) and the variable or condition that causes the dependency. For example, the edge from S1 to S2 can be labeled with "data(x)" and the edge from S3 to S4 can be labeled with "control(S3 == true)".
  - Draw the graph using a suitable notation or tool. The graph can be drawn using a graphical notation, such as boxes for nodes and arrows for edges, or using a textual notation, such as a list of nodes and edges. The graph can also be generated using a tool, such as Doxygen, SourceMonitor, or Desmos, that can analyze the program code and produce the graph automatically.

Here is an example of a program and its corresponding PDG:

```c
// Program to compute the factorial of a number
int factorial(int n) {
  int f = 1; // S1
  while (n > 0) { // S2
    f = f * n; // S3
    n = n - 1; // S4
  }
  return f; // S5
}
```

```graph
// PDG of the program
Nodes: S1, S2, S3, S4, S5
Edges: S1 -> S2 (control), S1 -> S3 (data(f)), S2 -> S3 (control(n > 0)), S2 -> S5 (control(n <= 0)), S3 -> S4 (control), S3 -> S3 (data(f)), S4 -> S2 (control), S4 -> S3 (data(n)), S4 -> S4 (data(n))
```