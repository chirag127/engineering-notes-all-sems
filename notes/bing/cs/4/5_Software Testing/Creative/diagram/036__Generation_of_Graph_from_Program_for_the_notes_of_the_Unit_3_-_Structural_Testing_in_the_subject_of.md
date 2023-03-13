The following is a detailed ASCII diagram for Generation of Graph from Program for the notes of the Unit 3 - Structural Testing in the subject of Software Testing.

### Generation of Graph from Program

The process of generating a graph from a program involves the following steps:

1. Identify the nodes of the graph, which represent the basic blocks of the program. A basic block is a sequence of statements that has a single entry point and a single exit point. A basic block can be identified by using the following rules:

  - The first statement of the program is the first statement of a basic block.
  - Any statement that is the target of a jump, branch, or loop is the first statement of a basic block.
  - Any statement that immediately follows a jump, branch, or loop is the first statement of a basic block.
  - The last statement of the program is the last statement of a basic block.

2. Identify the edges of the graph, which represent the possible transitions between the basic blocks. An edge can be identified by using the following rules:

  - If a basic block B1 ends with an unconditional jump to another basic block B2, then there is an edge from B1 to B2.
  - If a basic block B1 ends with a conditional branch to another basic block B2, then there are two edges from B1, one to B2 and one to the basic block that follows B1 in the program order.
  - If a basic block B1 ends with a loop statement, then there is an edge from B1 to itself, and an edge from B1 to the basic block that follows B1 in the program order.

3. Label the nodes and edges of the graph with the corresponding statements and conditions of the program.

For example, consider the following program:

```
1. read x
2. if x > 0 then
3.   y = x + 1
4. else
5.   y = x - 1
6. end if
7. print y
8. stop
```

The graph generated from this program is:

```
    +-----------------+
    | 1. read x       |
    +-----------------+
            |
            | x > 0
            v
    +-----------------+       +-----------------+
    | 3. y = x + 1    |       | 5. y = x - 1    |
    +-----------------+       +-----------------+
            |                         |
            |                         |
            +---------> +-----------------+
                        | 7. print y      |
                        +-----------------+
                                |
                                |
                                v
                        +-----------------+
                        | 8. stop         |
                        +-----------------+
```