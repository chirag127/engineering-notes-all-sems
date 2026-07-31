### Path Testing

Path testing is a white-box testing method that involves using the source code of a program in order to find every possible executable path. It helps to determine all faults lying within a piece of code .

Some of the path testing techniques are:

- Control Flow Graph: The program is converted into a control flow graph by representing the code into nodes and edges. The nodes represent the statements or blocks of code, and the edges represent the flow of control between them.
- Decision to Decision Path: The control flow graph can be broken into various decision to decision paths and then test cases can be generated for each path. A decision to decision path is a path that starts and ends at a decision node, such as a conditional statement or a loop.
- Independent Paths: Independent path is a path that introduces at least one new edge that is not included in any other paths. The number of independent paths in a program can be calculated using the cyclomatic complexity metric .
- Basis Path Testing: Basis path testing is a path testing method that uses the cyclomatic complexity to determine the number of independent paths and then test cases are generated for each path. The objective of basis path testing is to define the number of test cases needed to maximize test coverage .

The steps for basis path testing are :

- Draw a control flow graph for the program or module.
- Calculate the cyclomatic complexity of the graph using one of the following formulas:

  - V(G) = E - N + 2
  - V(G) = P + 1
  - V(G) = Number of decision nodes + 1

  where V(G) is the cyclomatic complexity, E is the number of edges, N is the number of nodes, and P is the number of connected components in the graph.
- Find a basis set of paths that covers all the edges in the graph. A basis set is a set of independent paths that can be used to construct any other path in the graph by combining them.
- Generate test cases to exercise each path in the basis set.

An example of basis path testing is shown below:

```python
# A simple program to calculate the average of two numbers
def average(a, b):
  if a > 0 and b > 0: # Decision node 1
    return (a + b) / 2
  elif a < 0 and b < 0: # Decision node 2
    return -((abs(a) + abs(b)) / 2)
  else: # Decision node 3
    return 0
```

The control flow graph for this program is:

![Control flow graph](https://i.imgur.com/4Q0l0Xy.png)

The cyclomatic complexity of the graph is:

- V(G) = 7 - 6 + 2 = 3
- V(G) = 1 + 1 = 2
- V(G) = 3 + 1 = 4

The basis set of paths for this graph is:

- Path 1: 1-2-3-6
- Path 2: 1-2-4-6
- Path 3: 1-2-5-6

The test cases for each path are:

- Path 1: a = 1, b = 2
- Path 2: a = -1, b = -2
- Path 3: a = 0, b = 0