### Identification of Independent Paths for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Structural testing, also known as white-box testing, is a technique of testing the internal structure and logic of the software code.
- Structural testing aims to cover all the possible paths of execution in the software code, which are also called independent paths.
- An independent path is a path that introduces at least one new set of processing statements or a new condition.
- Identifying independent paths is important for designing test cases that can achieve maximum coverage of the code.
- There are different methods for identifying independent paths, such as cyclomatic complexity, basis path testing, and control flow graph.

#### Cyclomatic Complexity
- Cyclomatic complexity is a metric that measures the number of linearly independent paths in the software code.
- Cyclomatic complexity can be calculated using the following formula:

  - V(G) = E - N + 2P
  - Where V(G) is the cyclomatic complexity, E is the number of edges, N is the number of nodes, and P is the number of connected components in the control flow graph of the code.
- Cyclomatic complexity can also be calculated using the following formula:

  - V(G) = R + 1
  - Where V(G) is the cyclomatic complexity and R is the number of regions in the control flow graph of the code.
- Cyclomatic complexity can also be calculated using the following formula:

  - V(G) = D + 1
  - Where V(G) is the cyclomatic complexity and D is the number of decision points in the code.
- Cyclomatic complexity can be used to determine the minimum number of test cases required to cover all the independent paths in the code.
- Cyclomatic complexity can also be used to measure the complexity and maintainability of the code. A higher cyclomatic complexity indicates a higher risk of errors and defects in the code.

#### Basis Path Testing
- Basis path testing is a technique of designing test cases based on the independent paths identified by the cyclomatic complexity.
- Basis path testing involves the following steps:

  - Draw the control flow graph of the code.
  - Calculate the cyclomatic complexity of the code using any of the formulas mentioned above.
  - Identify the basis set of independent paths in the code. A basis set is a set of independent paths that covers all the edges and nodes in the control flow graph.
  - Design test cases for each independent path in the basis set. Each test case should exercise one and only one independent path.
  - Execute the test cases and verify the expected outputs.

#### Control Flow Graph
- A control flow graph is a graphical representation of the flow of control in the software code.
- A control flow graph consists of nodes and edges. Nodes represent statements or blocks of code, and edges represent the flow of control between the nodes.
- A control flow graph can be used to identify the independent paths in the code by tracing the possible paths of execution from the entry node to the exit node.
- A control flow graph can also be used to calculate the cyclomatic complexity of the code by counting the number of edges, nodes, regions, or decision points in the graph.

#### Example
- Consider the following pseudocode for a function that calculates the factorial of a given number:

  - function factorial(n)
    - if n == 0 or n == 1 then
      - return 1
    - else
      - return n * factorial(n-1)
    - end if
  - end function

- The control flow graph of the code is shown below:

```
    +-----+
    | n=0 |<----+
    +-----+     |
      |         |
      |         |
      v         |
    +-----+     |
    | n=1 |<----+
    +-----+     |
      |         |
      |         |
      v         |
    +-----+     |
    |return 1|  |
    +-----+     |
      |         |
      |         |
      v         |
    +-----+     |
    |else|      |
    +-----+     |
      |         |
      |         |
      v         |
    +-----+     |
    |return n*  |
    |factorial  |
    |(n-1)      |
    +-----+-----+
```

- The cyclomatic complexity of the code can be calculated using any of the formulas:

  - V(G) = E - N + 2P = 9 - 7 + 2 = 4
  - V(G) = R + 1 = 3 + 1 = 4
  - V(G) = D + 1 =