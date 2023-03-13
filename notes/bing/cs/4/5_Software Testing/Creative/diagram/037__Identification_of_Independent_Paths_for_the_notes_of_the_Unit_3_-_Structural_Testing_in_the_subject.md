Identification of independent paths is a technique for path testing, which is a type of structural testing that focuses on the logic of the program. Path testing aims to cover all the possible paths in the control flow graph of the program or module. An independent path is one that introduces at least one new edge that has not been traversed before the path is defined. The number of independent paths in a control flow graph is given by the cyclomatic complexity, which can be calculated by the formula:

Cyclomatic complexity = Edges - Nodes + 2

or

Cyclomatic complexity = Regions + 1

or

Cyclomatic complexity = Decisions + 1

where Edges are the number of edges in the graph, Nodes are the number of nodes in the graph, Regions are the number of enclosed areas in the graph, and Decisions are the number of conditional statements in the graph.

To identify the independent paths, we can use the following steps:

1. Draw the control flow graph of the program or module, with each node representing a statement or a group of statements, and each edge representing a transfer of control.
2. Calculate the cyclomatic complexity of the graph using any of the formulas above.
3. Identify a basis set of independent paths by choosing paths that cover all the nodes and edges in the graph. The number of paths in the basis set should be equal to the cyclomatic complexity.
4. Design test cases that will execute each path in the basis set.

As an example, consider the following pseudocode of a program that calculates the factorial of a number:

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

The control flow graph of this program is:

```
    +---+     +---+     +---+     +---+
    | 1 | --> | 2 | --> | 3 | --> | 4 |
    +---+     +---+     +---+     +---+
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      v         v         v         v
    +---+     +---+     +---+     +---+
    | 5 | <-- | 6 | <-- | 7 | <-- | 8 |
    +---+     +---+     +---+     +---+
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      |         |         |         |
      v         v         v         v
    +---+     +---+     +---+     +---+
    | 9 |     |10 |     |11 |     |12 |
    +---+     +---+     +---+     +---+
```

The cyclomatic complexity of this graph is:

Cyclomatic complexity = Edges - Nodes + 2

= 16 - 12 + 2

= 6

The basis set of independent paths is:

Path 1: 1-2-3-4-5-9
Path 2: 1-2-3-4-8-7-6-10
Path 3: 1-2-3-4-8-7-11
Path 4: 1-2-3-4-8-12
Path 5: 4-8-7-6-10-6-7-11
Path 6: 4-8-7-6-10-6-7-6-10

The test cases that will execute each path are:

Test case 1: n = -1
Test case 2: n = 0
Test case 3: n = 1
Test case 4: n = 2
Test case 5: n = 3
Test case 6: n = 4