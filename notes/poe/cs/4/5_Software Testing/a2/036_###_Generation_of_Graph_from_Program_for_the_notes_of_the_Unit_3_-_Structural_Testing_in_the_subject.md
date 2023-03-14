 Here is the content in markdown format for the given topic:

### Generation of Graph from Program for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

To generate graph from a program for structural testing, follow the below steps:

1. Tokenize the program into basic blocks: Break the program into basic blocks i.e. sequence of statements with only one entry and exit point. The basic blocks can be obtained by splitting the program at decision points or loop constructs.

2. Identify the flow of control between basic blocks: Identify how the control flows from one basic block to another. This can be done by analyzing the logical conditions and loops in the program. Note down the control flow in terms of edges between the basic blocks.

3. Generate graph from basic blocks and control flow: Represent each basic block as a node and the control flow between basic blocks as directed edges. This generates a directed graph with nodes as basic blocks and edges as control flow between them. This graph is known as the control flow graph (CFG) or flow graph.

 Advantages of generating graph from program:
- It provides a visual representation of the program which makes it easy to analyze the program structure.
- It helps in identifying the independent paths in the program which aids in structural testing.
- It is useful for calculating cyclomatic complexity and identifying the maximum number of test cases needed.

Disadvantages:
- The graph generation process can become complex for large programs with many loops and conditions.
- The basic blocks are not always distinctly identifiable which can lead to issues in graph generation.

Examples and applications: Control flow graph is commonly used in structural testing, static analysis, calculating cyclomatic complexity, program slicing, etc. It provides a systematic way to analyze the structure of programs.