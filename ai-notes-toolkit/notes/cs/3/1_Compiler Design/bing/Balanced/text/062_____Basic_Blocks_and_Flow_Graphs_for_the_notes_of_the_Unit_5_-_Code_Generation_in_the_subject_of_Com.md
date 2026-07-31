### Basic Blocks and Flow Graphs

- A **basic block** is a set of statements that always executes in a sequence one after the other, without any branches or jumps  .
- A basic block has a single entry point and a single exit point. It means the flow of control enters at the beginning and leaves at the end of the block .
- A basic block can be identified by finding the **leaders** of the statements. A leader is the first statement of a basic block.
- The leaders are:
  - The first statement of the program.
  - Any statement that is the target of a jump or branch instruction.
  - Any statement that immediately follows a jump or branch instruction.
- A **flow graph** is a directed graph that represents the flow of control between basic blocks  .
- A flow graph has the following properties:
  - Each node in the graph corresponds to a basic block.
  - There is an edge from node X to node Y if the flow of control can transfer from the end of block X to the beginning of block Y.
  - The initial node has no incoming edges and the final node has no outgoing edges  .
- A flow graph is useful for code optimization and code generation, as it shows the dependencies and the order of execution of the basic blocks .
- An example of a basic block and a flow graph is shown below:

```
// A sequence of three-address code
a = b + c
d = a - b
if d == 0 goto L1
a = a + 1
goto L2
L1: d = b - c
L2: e = a + d
```

```
// The basic blocks are:

B1: a = b + c
    d = a - b
    if d == 0 goto L1

B2: a = a + 1
    goto L2

B3: d = b - c

B4: e = a + d

// The leaders are:

a = b + c // first statement of the program
if d == 0 goto L1 // target of a jump instruction
a = a + 1 // follows a jump instruction
d = b - c // target of a jump instruction
e = a + d // follows a jump instruction
```

```
// The flow graph is:

    B1
   /  \
  /    \
B2      B3
 \     /
  \   /
   B4
```