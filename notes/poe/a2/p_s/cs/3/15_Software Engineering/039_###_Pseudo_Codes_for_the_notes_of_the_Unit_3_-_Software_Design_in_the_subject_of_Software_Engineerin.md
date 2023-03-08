 Here is the content in Markdown format:

### Spanning Tree Algorithms in Local Area Network

- A spanning tree is a subset of edges of a graph that connects all nodes without any cycles and with minimum cost.
- Spanning tree algorithms are used in local area networks to prevent routing loops and ensure that there is only one path between any two nodes.
- The most common spanning tree algorithms are:
    - Prim's algorithm: Starts from an arbitrary root node and greedily adds the lowest cost edge that doesn't create a cycle.
    - Kruskal's algorithm: Sorts all edges by cost and adds them in order if they don't create a cycle.
    - Reverse-delete algorithm: Starts with a complete graph and deletes edges to avoid cycles.
- Advantages: Prevent routing loops, ensure unique path.
- Disadvantages: May not find optimal cost spanning tree, can be slow for large networks.
- Applications: LAN protocols like STP, RSTP, MSTP.

Markdown table:

Algorithm    How it works                        Advantages                     Disadvantages
Prim's      Greedy, add lowest cost edge        Simple, efficient              May not find optimal cost
Kruskal's   Sort edges by cost, add in order    Usually finds lowest cost      Sorting edges can be slow
Reverse-delete  Start with complete graph, delete edges  Guaranteed to find lowest cost  Slow, not practical for large networks

[Detailed diagrams and examples can be added if required]

### Pseudo Codes for the notes of the Unit 3 - Software Design in the subject of Software Engineering

- Pseudo code is an informal way to express the design of a computer program. It uses a combination of natural language and programming language to describe the steps required to solve a problem.
- Some key points about pseudo code:
    - It should be easy to understand, like plain English.
    - It can use programming constructs like if-else, for loops, while loops, functions, etc. but does not require strict syntax.
    - It focuses on the logic of the algorithm rather than precise code.
    - It can be used to outline the structure of a program before writing the actual code.
    - It should have clear indentation and formatting to represent the control flow.
- Examples of pseudo code:

Function to find maximum of two numbers:

Function max(a, b)
    if a > b
        return a
    else
        return b

For loop to print numbers from 1 to 10:

For i = 1 to 10
    Print i

[Detailed examples and markdown tables can be added if required]