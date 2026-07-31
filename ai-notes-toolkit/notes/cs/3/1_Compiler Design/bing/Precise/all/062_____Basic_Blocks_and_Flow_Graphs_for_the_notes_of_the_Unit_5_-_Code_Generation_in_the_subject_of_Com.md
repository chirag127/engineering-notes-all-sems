### Basic Blocks and Flow Graphs

Unit 5 - Code Generation in the subject of Compiler Design

- A **basic block** is a sequence of consecutive statements in which flow of control enters at the beginning and leaves at the end without halt or possibility of branching except at the end.
- Basic blocks form the vertices or nodes in a **flow graph**, which represents the flow of control in a program.
- An edge from one basic block to another indicates that control may pass from the first to the second.
- The flow graph provides a useful intermediate representation of the program for optimization and code generation.
- To construct a flow graph, the program is first divided into basic blocks.
- This is done by identifying the **leaders**, which are the first statements of basic blocks.
- Leaders are identified by the following rules:
  1. The first statement is a leader.
  2. Any statement that is the target of a conditional or unconditional jump is a leader.
  3. Any statement that immediately follows a conditional or unconditional jump is a leader.
- Once the leaders have been identified, the basic blocks can be constructed by placing all statements between two leaders in the same basic block.
- The flow graph is then constructed by adding edges between basic blocks according to the flow of control in the program.
