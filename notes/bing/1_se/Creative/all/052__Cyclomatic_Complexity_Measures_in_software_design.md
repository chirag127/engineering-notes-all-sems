##### Cyclomatic Complexity Measures in software design

- Cyclomatic complexity is a software metric used to measure the complexity of a program .
- It is a quantitative measure of the number of independent paths through the program source code .
- An independent path is a path that has at least one edge (branch or condition) that has not been traversed before in any other paths .
- Cyclomatic complexity can be calculated from the control flow graph of the program, which is a graphical representation of the program structure and flow of control .
- The formula for cyclomatic complexity is:

  - V(G) = E - N + 2
  - where V(G) is the cyclomatic complexity, E is the number of edges, and N is the number of nodes in the graph .

- Alternatively, cyclomatic complexity can be calculated from the number of decision points (such as if, while, for, switch, etc.) and exit points (such as return, break, etc.) in the program:

  - V(G) = D + 1
  - where V(G) is the cyclomatic complexity, and D is the number of decision points and exit points .

- Cyclomatic complexity can be used for various purposes, such as:

  - Determining the number of independent paths and test cases for the program .
  - Estimating the effort and time required for developing, testing, and maintaining the program .
  - Evaluating the quality and readability of the program .
  - Identifying the potential risks and defects in the program .
  - Refactoring the program to reduce the complexity and improve the performance .

- A general guideline for cyclomatic complexity is:

  - V(G) <= 10: The program is simple and easy to understand and test .
  - V(G) > 10 and <= 20: The program is moderately complex and may require more testing and documentation .
  - V(G) > 20: The program is highly complex and difficult to understand and test. It should be refactored or divided into smaller modules .

- An example of calculating cyclomatic complexity from the control flow graph is shown below:

  - The program is a simple function that checks if a number is even or odd and prints the result.

```c
void checkEvenOdd(int n) {
  if (n % 2 == 0) {
    printf("Even\n");
  } else {
    printf("Odd\n");
  }
}
```

  - The control flow graph of the program is:

```
    +-----+
    |  n  |
    +-----+
      |
      v
+-----------+
| n % 2 == 0|
+-----------+
  |     |
  |     | No
  |     v
  |  +-------+
  |  | Odd   |
  |  +-------+
  |     |
Yes    |
  v    v
+-------+
| Even  |
+-------+
  |
  v
+-----+
| End |
+-----+
```

  - The cyclomatic complexity of the program is:

    - V(G) = E - N + 2
    - V(G) = 7 - 6 + 2
    - V(G) = 3

  - The program has three independent paths:

    - Path 1: n -> n % 2 == 0 -> Even -> End
    - Path 2: n -> n % 2 == 0 -> Odd -> End
    - Path 3: n -> End

  - The program has a low cyclomatic complexity and is easy to understand and test.