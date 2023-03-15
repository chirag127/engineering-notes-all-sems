### Basic Blocks and Flow Graphs

- A basic block is a sequence of consecutive statements in which the flow of control enters at the beginning and leaves at the end without halt or possibility of branching except at the end.
- A flow graph is a directed graph in which the nodes are basic blocks and the edges indicate the flow of control between the blocks.
- Basic blocks and flow graphs are useful for code generation because they allow the compiler to identify and optimize the frequently executed parts of the program.
- To construct basic blocks and flow graphs, the compiler can use the following steps:
  - Divide the intermediate code into basic blocks by finding the leaders, which are the first statements of each basic block. A statement is a leader if:
    - It is the first statement in the intermediate code, or
    - It is the target of a jump, or
    - It immediately follows a jump.
  - Create a node for each basic block and add an edge from block B to block C if the execution of B can be followed by the execution of C. This can happen if:
    - C immediately follows B in the intermediate code and B does not end with an unconditional jump, or
    - B ends with a conditional or unconditional jump to C.