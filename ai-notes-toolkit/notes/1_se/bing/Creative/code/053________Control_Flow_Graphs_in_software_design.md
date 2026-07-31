###### Control Flow Graphs in software design

A control flow graph (CFG) is a graphical representation of the possible paths of execution of a program or a function. It consists of nodes and edges, where nodes represent basic blocks of code (sequences of statements that are always executed together) and edges represent the flow of control between them. A basic block has a single entry point and a single exit point, and it does not contain any jumps or branches. A control flow graph can be used for various purposes, such as static analysis, optimization, testing, debugging, and verification of software.

To create a control flow graph, one can follow these steps:

- Identify the entry and exit points of the program or function. These will be the start and end nodes of the graph.
- Divide the code into basic blocks. A basic block starts with a label, a jump, or a branch, and ends with a jump, a branch, or a return statement. A basic block can also be a single statement that does not affect the control flow, such as an assignment or a function call.
- Draw the nodes for each basic block and label them with the corresponding code.
- Draw the edges between the nodes according to the control flow. An edge from node A to node B means that the execution can go from the end of A to the start of B. For conditional branches, use different colors or shapes to indicate the true and false branches. For loops, use back edges to connect the end of the loop body to the start of the loop condition.

Here is an example of a control flow graph for a simple function that calculates the factorial of a positive integer n:

```mermaid
graph TD
    A[Start] --> B[n = input()]
    B --> C[if n < 0]
    C -->|True| D[print("Invalid input")]
    D --> E[End]
    C -->|False| F[if n == 0 or n == 1]
    F -->|True| G[return 1]
    G --> E
    F -->|False| H[f = 1]
    H --> I[i = 1]
    I --> J[while i <= n]
    J -->|True| K[f = f * i]
    K --> L[i = i + 1]
    L --> J
    J -->|False| M[return f]
    M --> E
```