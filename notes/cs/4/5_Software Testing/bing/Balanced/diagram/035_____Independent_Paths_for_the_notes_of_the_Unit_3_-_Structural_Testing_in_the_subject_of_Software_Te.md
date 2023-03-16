### Independent Paths

- Independent paths are paths through a program's control flow graph that cannot be reproduced by combining other paths .
- Independent paths are important for path testing, a structural testing method that aims to cover all possible executable paths in a program .
- Path testing can help to find faults in the logic and design of a program, and reduce redundant tests .
- To find the independent paths, we can use the following steps  :

  1. Draw the control flow graph of the program, which shows the nodes (statements or blocks of code) and edges (transfers of control) of the program.
  2. Calculate the cyclomatic complexity of the graph, which is a measure of the number of linearly independent paths in the graph. There are several ways to calculate the cyclomatic complexity, such as:
     - V(G) = E - N + 2, where E is the number of edges and N is the number of nodes in the graph.
     - V(G) = P + 1, where P is the number of predicate nodes (nodes with two or more outgoing edges) in the graph.
     - V(G) = R, where R is the number of regions in the graph (a region is a closed area bounded by edges and nodes).
  3. Identify the basis set of independent paths, which is a set of paths that covers all the edges and nodes in the graph. The number of paths in the basis set should be equal to the cyclomatic complexity. A basis set is not unique, and there may be more than one way to choose the independent paths.
  4. Generate test cases for each path in the basis set, and execute them to test the program.

- Here is an example of path testing using independent paths :

  - Consider the following pseudocode of a program that calculates the average of three numbers:

    ```
    input a, b, c
    if a > 0 and b > 0 and c > 0
      avg = (a + b + c) / 3
      print avg
    else
      print "Invalid input"
    end if
    ```

  - The control flow graph of the program is:

    ```
    1. input a, b, c
       |
       V
    2. if a > 0 and b > 0 and c > 0
    /                    \
    |                      |
    V                      V
    3. avg = (a + b + c) / 3  4. print "Invalid input"
    |                      /
    V                    /
    5. print avg       /
    \                /
     \              /
      \            /
       V          V
        6. end if
    ```

  - The cyclomatic complexity of the graph is:

    - V(G) = E - N + 2 = 7 - 6 + 2 = 3
    - V(G) = P + 1 = 1 + 1 = 2
    - V(G) = R = 3

  - A possible basis set of independent paths is:

    - Path 1: 1-2-3-5-6
    - Path 2: 1-2-4-6
    - Path 3: 1-2-3-5-6-4-6

  - The test cases for each path are:

    - Path 1: a = 1, b = 2, c = 3 (valid input, average is calculated and printed)
    - Path 2: a = -1, b = 2, c = 3 (invalid input, error message is printed)
    - Path 3: a = 1, b = 2, c = 3, a = -1, b = 2, c = 3 (valid input followed by invalid input, average and error message are printed)

  - The test cases cover all the possible outcomes of the program, and can reveal any faults in the logic or design of the program.