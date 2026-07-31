### Basic Blocks and Flow Graphs

- A **basic block** is a set of statements that always executes in a sequence one after the other, without any branches or jumps in between  .
- A basic block can be entered only at the beginning and can be exited only at the end.
- A basic block can be identified by the following rules:
  - The first statement is a leader (the target of a jump or the first statement of the program).
  - Any statement that follows an unconditional jump is a leader.
  - Any statement that is the target of a conditional jump is a leader.
- A **flow graph** is a directed graph that represents the flow of control between basic blocks   .
- A flow graph has the following properties:
  - Each node corresponds to a basic block.
  - There is an edge from node X to node Y if the control can pass from the last statement of X to the first statement of Y.
  - The node that contains the first statement of the program is the initial node and has no predecessors.
  - The nodes that contain return or exit statements are the final nodes and have no successors.
- A flow graph is useful for code optimization and code generation .