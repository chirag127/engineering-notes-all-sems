The generation of graph from program is a technique of structural testing that uses the program's control flow as a model. The graph consists of nodes and edges, where nodes represent basic blocks of code and edges represent the possible transitions between them. The graph can be used to measure the coverage of test cases and to design new test cases that cover all the paths or branches in the graph.

A basic block is a sequence of statements that has only one entry point and one exit point. A basic block can be identified by finding the leaders, which are the first statements of a basic block. The leaders are:

- The first statement of the program.
- Any statement that is the target of a jump, branch, or loop.
- Any statement that immediately follows a jump, branch, or loop.

The following diagram illustrates the basic architecture of a graph from program using ASCII characters:

    +-----------------+     +-----------------+     +-----------------+
    | Leader:         |     | Leader:         |     | Leader:         |
    | Statement 1     |     | Statement 4     |     | Statement 7     |
    | Statement 2     |     | Statement 5     |     | Statement 8     |
    | Statement 3     |     | Statement 6     |     | Statement 9     |
    +-----------------+     +-----------------+     +-----------------+
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             v                     v                     v
    +-----------------+     +-----------------+     +-----------------+
    | Leader:         |     | Leader:         |     | Leader:         |
    | Statement 10    |     | Statement 11    |     | Statement 12    |
    | Statement 11    |     | Statement 12    |     | Statement 13    |
    | Statement 12    |     | Statement 13    |     | Statement 14    |
    +-----------------+     +-----------------+     +-----------------+
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             |                     |                     |
             +----------+----------+----------+----------+
                        |                     |
                        |                     |
                        |                     |
                        |                     |
                        |                     |
                        |                     |
                        |                     |
                        |                     |
                        |                     |
                        |                     |
                        |                     |
                        |                     |
                        |                     |
                        |                     |
                        v                     v
    +-----------------+     +-----------------+
    | Leader:         |     | Leader:         |
    | Statement 15    |     | Statement 16    |
    | Statement 16    |     | Statement 17    |
    | Statement 17    |     | Statement 18    |
    +-----------------+     +-----------------+
             |                     |
             |                     |
             |                     |
             |                     |
             |                     |
             |                     |
             |                     |
             |                     |
             +----------+----------+
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        v
    +-----------------+
    | Leader:         |
    | Statement 19    |
    | Statement 20    |
    | Statement 21    |
    +-----------------+
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             v
    +-----------------+
    | Leader:         |
    | Statement 22    |
    | Statement 23    |
    | Statement 24    |
    +-----------------+
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             |
             v
    +-----------------+
    | Leader:         |
    | Statement