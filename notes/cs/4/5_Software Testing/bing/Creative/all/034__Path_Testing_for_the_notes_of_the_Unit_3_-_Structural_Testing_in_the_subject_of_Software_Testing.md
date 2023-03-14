### Path Testing for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Path testing is a method that is used to design the test cases based on the source code of a program and its control flow graph.
- A control flow graph is a graphical representation of the program that shows the nodes and edges corresponding to the statements and branches of the code .
- The goal of path testing is to find a set of linearly independent paths of execution that cover all the possible branches in the program.
- A path is a sequence of nodes and edges that starts from an entry point and ends at an exit point of the program.
- A path is linearly independent if it introduces at least one new edge that is not included in any other paths.
- The number of linearly independent paths in a program is determined by the cyclomatic complexity, which is a metric that measures the complexity of the program based on the number of edges and nodes in the control flow graph .
- The cyclomatic complexity can be calculated by the following formula :

  ```
  McCabe's Cyclomatic Complexity = E - N + 2P
  ```

  Where,

  - E = Number of edges in control flow graph
  - N = Number of nodes in control flow graph
  - P = Program factor (number of connected components)

- The cyclomatic complexity indicates the minimum number of test cases required to achieve full branch coverage of the program .
- To generate the test cases, a basis set of paths is derived from the control flow graph by selecting one path from each linearly independent set of paths .
- A basis set of paths is a set of paths that covers all the edges in the control flow graph at least once .
- Each path in the basis set is then executed with appropriate input values and expected output values to verify the correctness of the program .

#### Example of Path Testing

Consider the following pseudocode of a program that calculates the average of three numbers:

```
Input: a, b, c
Output: avg

avg = 0
if a > 0 then
  avg = avg + a
  count = count + 1
endif
if b > 0 then
  avg = avg + b
  count = count + 1
endif
if c > 0 then
  avg = avg + c
  count = count + 1
endif
if count > 0 then
  avg = avg / count
endif
print avg
```

The control flow graph of the program is shown below:

```
  1
 / \
2   3
|   |
4   5
|   |
6   7
|   |
8   9
 \ /
  10
  |
  11
  |
  12
```

The cyclomatic complexity of the program is:

```
E = 12
N = 12
P = 1
McCabe's Cyclomatic Complexity = E - N + 2P = 12 - 12 + 2 = 2
```

The minimum number of test cases required to achieve full branch coverage is 2.

A possible basis set of paths is:

```
Path 1: 1-2-4-6-8-10-11-12
Path 2: 1-3-5-7-9-10-11-12
```

The test cases for each path are:

```
Path 1: a = 1, b = -1, c = -1, avg = 1
Path 2: a = -1, b = 2, c = 3, avg = 2.5
```

#### Advantages of Path Testing

- Path testing reduces the redundant tests by focusing on the logic of the program .
- Path testing facilitates analytical versus arbitrary case design by using a systematic approach.
- Path testing helps to determine all faults lying within a piece of code by executing all possible branches .
- Path testing is often used by software programmers to unit test the code of the software product.

#### Disadvantages of Path Testing

- Path testing can be very time