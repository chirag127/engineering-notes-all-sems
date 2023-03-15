# Basic Blocks and Flow Graphs

- A **basic block** is a set of statements that always executes in a sequence one after the other, without any branches or jumps  .
- A basic block has a single entry point and a single exit point. It means the flow of control enters at the beginning and leaves at the end of the block .
- A basic block can be identified by finding the **leaders** of the statements. A leader is the first statement of a basic block.
- The leaders can be found by applying the following rules:
  - The first statement is a leader.
  - Any statement that is the target of a conditional or unconditional jump is a leader.
  - Any statement that immediately follows a jump statement is a leader.
- A **flow graph** is a directed graph that represents the flow of control between basic blocks  .
- A flow graph has the following properties  :
  - Each node in the graph corresponds to a basic block.
  - There is an edge from node X to node Y if the flow of control can pass from the end of block X to the beginning of block Y.
  - The node with no predecessors is the **entry node** of the graph. It corresponds to the first basic block of the program.
  - The node with no successors is the **exit node** of the graph. It corresponds to the last basic block of the program.
- A flow graph is useful for code optimization and code generation, as it shows the dependencies and the loops in the program .
- An example of a flow graph is shown below:

![Flow graph example](https://www.gatevidyalay.com/wp-content/uploads/2018/11/Basic-Blocks-and-Flow-Graphs-Example.png)