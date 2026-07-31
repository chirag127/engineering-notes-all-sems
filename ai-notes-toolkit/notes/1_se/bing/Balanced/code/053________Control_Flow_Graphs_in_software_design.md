###### Control Flow Graphs in software design

A control flow graph (CFG) is a graphical representation of the possible paths of execution of a program or a function. It consists of nodes that represent basic blocks of code, and edges that represent the flow of control between them. A basic block is a sequence of instructions that has a single entry point and a single exit point. A control flow graph can be used for various purposes, such as static analysis, optimization, testing, and debugging of software.

To create a control flow graph, one can follow these steps:

- Identify the basic blocks of the program or function. A basic block starts with a label, a function call, or a branch target, and ends with a return, a branch, or a function exit.
- Draw a node for each basic block, and label it with the block number or name.
- Draw an edge from one node to another if there is a possible flow of control from the first block to the second block. For example, if the first block ends with a conditional branch, draw two edges from it, one for the true branch and one for the false branch. If the first block ends with an unconditional branch, draw only one edge from it to the target block.
- Mark the entry and exit nodes of the graph. The entry node is the node that corresponds to the first basic block of the program or function. The exit node is the node that corresponds to the return or exit statement of the program or function.

Here is an example of a control flow graph for a simple function that computes the factorial of a given number:

```mermaid
graph TD
A[Entry] --> B[n = input()]
B --> C[if n < 0]
C -->|Yes| D[return -1]
C -->|No| E[if n == 0]
E -->|Yes| F[return 1]
E -->|No| G[f = 1]
G --> H[i = 1]
H --> I[while i <= n]
I -->|Yes| J[f = f * i]
J --> K[i = i + 1]
K --> I
I -->|No| L[return f]
L --> M[Exit]
D --> M
F --> M
```