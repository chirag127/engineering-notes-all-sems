 Here is the content in markdown format for the topic -

### DAG representation of basic blocks for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

- A Directed Acyclic Graph(DAG) is used to represent the basic blocks of a flow graph.
- In a DAG, each node represents a basic block and each edge represents a possible flow of control from one basic block to another.
- The edges are directed from the predecessor basic block to the successor basic block.
- The DAG does not contain any cycles as it is an Acyclic Graph.
- The DAG representation simplifies many compiler analyses like finding dominators, reachable blocks, etc.
- The DAG can be constructed from the flow graph by collapsing all the nodes within a basic block into a single node and eliminating the edges within the basic block.
- Example: The flow graph and corresponding DAG representation is shown below -

Flow Graph:

[A flow graph diagram showing basic blocks and control flows is shown here]

DAG:

[A DAG diagram showing nodes as basic blocks and directed edges as control flows is shown here]

- Advantages:
    - Simpler representation than flow graph.
    - Aids compiler optimizations and analyses.
- Disadvantages:
    - Information about statements and expressions within a basic block is lost.
    - Additional information may be required to construct the original flow graph back from the DAG.
- Applications: DAG representation is commonly used in compilers to perform control flow analysis and optimization techniques like graph colouring register allocation, etc.