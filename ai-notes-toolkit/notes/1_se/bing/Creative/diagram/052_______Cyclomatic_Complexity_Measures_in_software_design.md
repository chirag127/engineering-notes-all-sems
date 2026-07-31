Cyclomatic complexity is a software metric used to measure the complexity of a program. It is a count of the number of independent paths through the program source code. An independent path is a path that has at least one edge that has not been traversed before in any other paths. The cyclomatic complexity can be calculated from the control flow graph of the program, using the formula:

Cyclomatic complexity = E - N + 2

where E is the number of edges and N is the number of nodes in the graph.

The cyclomatic complexity can be used to determine the number of test cases needed to cover all the possible paths of the program, as well as to identify the areas of high complexity that may be prone to errors or difficult to maintain.

Here is an example of a control flow graph and its cyclomatic complexity:

```text
    +-----+       +-----+       +-----+
    |  A  |       |  B  |       |  C  |
    +-----+       +-----+       +-----+
       |             |             |
       |             |             |
       |             |             |
       |             |             |
       |             |             |
       |             |             |
       |             |             |
       |             |             |
       |             |             |
       |             |             |
       |             |             |
       |             |             |
       |             |             |
       +-----------> | <-----------+
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
                     |
                     +-----+       +-----+
                     |  D  |       |  E  |
                     +-----+       +-----+
                        |             |
                        |             |
                        |             |
                        |             |
                        |             |
                        |             |
                        |             |
                        |             |
                        |             |
                        |             |
                        |             |
                        |             |
                        |             |
                        +-----------> |
```

The graph has 5 nodes and 6 edges, so the cyclomatic complexity is 6 - 5 + 2 = 3. This means there are 3 independent paths in the program, which are:

- A -> B -> D -> E
- A -> B -> C -> B -> D -> E
- A -> B -> C -> B -> C -> B -> D -> E

To test the program, we need at least 3 test cases to cover all the paths.