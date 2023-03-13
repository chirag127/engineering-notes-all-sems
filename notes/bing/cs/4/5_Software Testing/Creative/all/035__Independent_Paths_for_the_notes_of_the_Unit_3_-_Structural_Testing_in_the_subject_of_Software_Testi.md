### Independent Paths for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Independent paths are paths through a program's control flow graph that cannot be reproduced by combining other paths .
- Independent paths are important for path testing, which is a structural testing method that aims to cover all possible executable paths in a program .
- Path testing can help to find faults in the logic and structure of a program, and reduce redundant tests .
- To find the independent paths, we can use the following steps  :
  - Draw the control flow graph of the program, which is a graphical representation of the program's flow of control, with nodes representing statements or blocks of code, and edges representing transitions or branches.
  - Calculate the cyclomatic complexity of the graph, which is a measure of the number of linearly independent paths in the graph. There are several ways to calculate the cyclomatic complexity, such as:
    - V(G) = E - N + 2, where E is the number of edges, and N is the number of nodes.
    - V(G) = P + 1, where P is the number of predicate nodes, which are nodes with two or more outgoing edges.
    - V(G) = R, where R is the number of regions in the graph, which are areas enclosed by edges and nodes.
  - Identify the basis set of paths, which is a set of linearly independent paths that can form any other path in the graph by combination. The basis set should have the same number of paths as the cyclomatic complexity. To identify the basis set, we can use the following rules :
    - Start from the entry node of the graph, and follow any edge to the next node.
    - If the current node is a predicate node, choose one of the outgoing edges that has not been traversed before, and follow it to the next node.
    - If the current node is not a predicate node, follow the only outgoing edge to the next node.
    - Repeat the above steps until reaching the exit node of the graph, or a node that has already been visited in the current path.
    - If the exit node is reached, record the current path as one of the basis paths, and go back to the last predicate node that has an untraversed outgoing edge, and follow it to the next node.
    - If a node that has already been visited is reached, go back to the last predicate node that has an untraversed outgoing edge, and follow it to the next node.
    - Repeat the above steps until all the edges have been traversed, and all the basis paths have been identified.
  - Generate test cases for each path in the basis set, using appropriate input values and expected output values.
  - Execute the test cases and verify the results.

- Here is an example of finding the independent paths for a simple program that calculates the factorial of a given number:

```c
// Program to calculate the factorial of a given number
int factorial(int n) {
  int result = 1;
  if (n < 0) {
    return -1; // invalid input
  }
  while (n > 0) {
    result = result * n;
    n = n - 1;
  }
  return result;
}
```

- The control flow graph of the program is:

```
    +-----+     +-----+     +-----+     +-----+
    |  1  |---->|  2  |---->|  3  |---->|  4  |
    +-----+     +-----+     +-----+     +-----+
                /     \     /     \
               /       \   /       \
              /         \ /         \
             /           X           \
            /           / \           \
           /           /   \           \
          /           /     \           \
         /           /       \           \
        /           /         \           \
       /           /           \           \
      /           /             \           \
     /           /               \           \
    /           /                 \           \
   /           /                   \           \
  /           /                     \           \
 /           /                       \           \
+-----+     +-----+     +-----+     +-----+     +-----+
|  5  |