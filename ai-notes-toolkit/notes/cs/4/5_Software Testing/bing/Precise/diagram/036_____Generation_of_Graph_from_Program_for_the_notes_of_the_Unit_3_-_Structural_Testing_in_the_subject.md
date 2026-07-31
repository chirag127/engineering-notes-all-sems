### Generation of Graph from Program

1. The first step in generating a graph from a program is to identify the control flow of the program. This can be done by analyzing the source code and identifying the different paths that can be taken during execution.
2. Once the control flow has been identified, a control flow graph (CFG) can be created. This is a graphical representation of the program's control flow, where each node represents a basic block of code and edges represent the flow of control between these blocks.
3. The CFG can then be used to generate other types of graphs, such as a program dependency graph (PDG) or a system dependence graph (SDG). These graphs provide additional information about the program's structure and can be used for various types of analysis, such as data flow analysis or slicing.
4. In the context of structural testing, these graphs can be used to identify test cases that provide good coverage of the program's control flow and data flow. By analyzing the graphs, testers can identify paths through the program that need to be tested and generate test cases accordingly.
