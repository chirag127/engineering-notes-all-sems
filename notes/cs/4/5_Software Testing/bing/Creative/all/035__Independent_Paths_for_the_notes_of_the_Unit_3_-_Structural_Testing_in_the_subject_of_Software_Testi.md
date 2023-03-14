### Independent Paths for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Independent paths are a set of paths through a program that are linearly independent, meaning that they introduce at least one new edge or node that is not included in any other path .
- Independent paths are useful for designing test cases that cover the logic of the program and reduce the redundancy of testing the same paths repeatedly .
- Independent paths can be derived from the control flow graph of the program, which is a graphical representation of the code using nodes and edges to show the flow of execution .
- One way to calculate the number of independent paths is to use McCabe's cyclomatic complexity, which is a measure of the complexity of a program based on the number of edges, nodes, and connected components in the control flow graph .
- McCabe's cyclomatic complexity can be computed using the formula: `V(G) = E - N + 2P`, where `V(G)` is the cyclomatic complexity, `E` is the number of edges, `N` is the number of nodes, and `P` is the number of connected components in the graph .
- Another way to calculate the number of independent paths is to use the decision-to-decision path technique, which involves breaking the control flow graph into segments that start and end with a decision node (a node that has more than one outgoing edge) and then collapsing each segment into a single node .
- The number of independent paths is then equal to the number of nodes in the collapsed graph .
- To create test cases for each independent path, the tester needs to identify the input values and expected output values that will cause the program to execute the path .
- The test cases should cover all the edges and nodes in the path, as well as any boundary conditions or error conditions that may arise .

#### Example

Consider the following pseudocode for a program that calculates the factorial of a positive integer:

```
function factorial(n):
  if n < 0:
    return -1
  else if n == 0 or n == 1:
    return 1
  else:
    result = 1
    for i = 1 to n:
      result = result * i
    return result
```

The control flow graph for this program is shown below:

```
    +---+
    | n |
    +---+
      |
      v
+-----------+
| n < 0 ?   |
+-----------+
  |     |
  |     | No
  v     v
+---+ +-----------+
| 1 | | n == 0 ?  |
+---+ +-----------+
  |     |     |
  |     |     | No
  v     v     v
+---+ +---+ +-----------+
| 2 | | 1 | | n == 1 ?  |
+---+ +---+ +-----------+
  |     |     |     |
  |     |     |     | No
  v     v     v     v
+---+ +---+ +---+ +-------+
| 3 | | 2 | | 2 | | i = 1 |
+---+ +---+ +---+ +-------+
  |     |     |     |
  |     |     |     v
  |     |     | +-----------+
  |     |     | | i <= n ?  |
  |     |     | +-----------+
  |     |     |   |     |
  |     |     |   |     | No
  |     |     |   v     v
  |     |     | +-------+ +---+
  |     |     | | r = r | | 4 |
  |     |     | | * i   | +---+
  |     |     | +-------+   |
  |     |     |   |         |
  |     |     |   v         |
  |     |     | +-------+   |
  |     |     | | i = i |   |
  |     |     | | + 1   |   |
  |     |     | +-------+   |
  |     |     |