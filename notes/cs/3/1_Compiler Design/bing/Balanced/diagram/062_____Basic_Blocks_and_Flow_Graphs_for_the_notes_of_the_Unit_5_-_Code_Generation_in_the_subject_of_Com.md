### Basic Blocks and Flow Graphs

- A **basic block** is a set of statements that always executes in a sequence one after the other, without any branches or jumps in between  .
- A basic block can be entered only at the beginning and can be exited only at the end.
- A basic block can be identified by finding the **leaders**, which are the first statements of each basic block.
- A leader can be
  - The first statement of the program
  - The target of a jump or branch instruction
  - The statement immediately following a jump or branch instruction.
- A **flow graph** is a directed graph that represents the flow of control between basic blocks   .
- A flow graph has the following properties:
  - Each node is a basic block
  - There is an edge from node X to node Y if the control can pass from the last statement of X to the first statement of Y
  - There is a unique entry node with no incoming edges
  - There is a unique exit node with no outgoing edges .
- A flow graph is useful for
  - Performing data flow analysis
  - Optimizing the code
  - Generating target code .

Here is an example of a basic block and a flow graph:

```
// Basic block
a = b + c;
d = a * c;
e = d - a;

// Flow graph
    +-----+
    | a=1 |  <--- Entry node
    +-----+
      |
      v
    +-----+
    | b=2 |
    +-----+
      |
      v
    +-----+
    | c=3 |
    +-----+
      |
      v
    +-----+
    | d=4 |
    +-----+
      |
      v
    +-----+
    | e=5 |
    +-----+
      |
      v
    +-----+
    | f=6 |
    +-----+
      |
      v
    +-----+
    | g=7 |
    +-----+
      |
      v
    +-----+
    | h=8 |
    +-----+
      |
      v
    +-----+
    | i=9 |
    +-----+
      |
      v
    +-----+
    | j=10|  <--- Exit node
    +-----+
```