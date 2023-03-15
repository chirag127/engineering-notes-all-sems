 Here is the content in markdown format for the given topic:

### Generation of Graph from Program for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

To generate graph from a program, follow the below steps:

1. Analyze the program and identify the basic blocks. The basic blocks are sequence of statements which have only one entry and one exit point.
2. Identify the conditional statements like if-else, switch-case, etc. and draw connections from the output of these statements to the basic blocks that follow them. This forms the nodes and edges of the graph.
3. Identify the loops like for loop, while loop, do-while loop, etc. and draw connections from the end of the loop to the start of the loop. This completes the graph formation.
4. Name the nodes of the graph with the labels of the basic blocks. The graph formed is called the control flow graph (CFG) of the program.

*Advantages of generating graph from a program:*

- It is easy to visualize the flow of control in a program through the graph.
- It helps in conducting structural testing of the program. The graph can be traversed to identify paths and coverage criteria can be applied.
- The complexity of a program can be analyzed by calculating metrics like cyclomatic complexity from the graph.

*Disadvantages of generating graph from a program:*

- The graph formation can become complex for larger programs with many nested conditional statements and loops.
- The nodes and edges of the graph do not provide the actual logic of the program. They just show the control flow. The data flow cannot be depicted from the graph.

*Examples:*

Here is a simple C program and its corresponding control flow graph:

Program:
if (x == 0)
  x = 1;
else
  x = 2;

Graph:

[A diagram showing 2 nodes 'If (x == 0)' and 'Else' with an edge from 'If (x == 0)' to 'Else']