### Control Flow Graphs

A control flow graph (CFG) is a graphical representation of the control flow or computation during the execution of a program or an application. A CFG consists of nodes and edges, where each node represents a basic block of code (a sequence of instructions that always execute together) and each edge represents a possible flow of control from one node to another. A CFG can be used for various purposes, such as static analysis, compiler optimization, testing, debugging, and program understanding.

Some basic concepts and terminologies related to CFGs are:

- **Entry node**: The node that represents the starting point of the program or the function. There is only one entry node in a CFG.
- **Exit node**: The node that represents the end point of the program or the function. There can be more than one exit node in a CFG, depending on the number of return statements or exit points in the code.
- **Branch node**: A node that has more than one outgoing edge, indicating a conditional or unconditional jump in the code. For example, an if-else statement, a switch-case statement, a loop statement, or a goto statement can create a branch node.
- **Join node**: A node that has more than one incoming edge, indicating a convergence of control flow from different paths. For example, the end of an if-else statement, a switch-case statement, or a loop statement can create a join node.
- **Path**: A sequence of nodes and edges that can be traversed during the execution of the program. A path can be complete (from the entry node to an exit node) or partial (from any node to any other node).
- **Cyclomatic complexity**: A metric that measures the complexity of a program or a function based on the number of independent paths in its CFG. It can be calculated as:

  - Cyclomatic complexity = Number of edges - Number of nodes + 2
  - Cyclomatic complexity = Number of branch nodes + 1

  A higher cyclomatic complexity indicates a higher complexity and a lower testability of the program or the function.

To draw a CFG for a given program or a function, the following steps can be followed:

- Identify the entry and exit nodes of the program or the function and label them as `start` and `end` respectively.
- Identify the basic blocks of code and label them with unique identifiers, such as `B1`, `B2`, etc.
- Draw a node for each basic block and an edge for each possible flow of control between them.
- Label the edges with the conditions or expressions that determine the flow of control, if any.
- Check the correctness and completeness of the CFG by tracing all possible paths from the entry node to the exit nodes.

For example, consider the following pseudocode for a function that calculates the factorial of a given number:

```
function factorial(n)
  if n < 0 then
    return -1
  else
    f = 1
    while n > 0 do
      f = f * n
      n = n - 1
    end while
    return f
  end if
end function
```

The CFG for this function can be drawn as:

```
start
  |
  v
 B1: if n < 0 then
  |            |
  |            v
  |          B2: return -1
  |            |
  v            v
B3: else     end
  |
  v
B4: f = 1
  |
  v
B5: while n > 0 do
  |            |
  |            v
  |          B6: f = f * n
  |            |
  |            v
  |          B7: n = n - 1
  |            |
  v            |
B8: end while |
  |            |
  v<-----------
B9: return f
  |
  v
 end
```

Some properties of this CFG are:

- The entry node is `start` and the exit nodes are `end` and `B2`.
- The branch nodes are `B1` and `B5`.
- The join nodes are `B3` and `B8`.
- The cyclomatic complexity is 4 (4 edges - 6 nodes + 2) or 3 (2 branch nodes + 1).