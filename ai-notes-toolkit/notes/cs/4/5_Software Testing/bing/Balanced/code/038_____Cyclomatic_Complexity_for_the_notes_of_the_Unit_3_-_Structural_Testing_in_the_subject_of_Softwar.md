### Cyclomatic Complexity

Cyclomatic complexity is a software metric used to indicate the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a program's source code. It is computed using the control flow graph of the program.

Cyclomatic complexity can be used for the following purposes:

- To estimate the number of test cases required to cover all the possible paths of the program.
- To identify the high-risk modules or functions that may contain more errors or defects.
- To measure the maintainability and readability of the code by reducing the complexity.

Cyclomatic complexity can be calculated using the following formula :

Cyclomatic complexity = E – N + 2*P

where,

- E = represents the number of edges in the control flow graph.
- N = represents the number of nodes in the control flow graph.
- P = represents the number of connected components in the control flow graph.

Alternatively, cyclomatic complexity can also be calculated using the following formula:

Cyclomatic complexity = P + 1

where,

- P = represents the number of predicate nodes in the control flow graph.

A predicate node is a node that contains a condition, such as an if statement, a switch statement, a while loop, a for loop, etc.

The following example illustrates how to calculate the cyclomatic complexity of a simple program:

```c
// Program to find the maximum of two numbers
int max(int a, int b) {
  if (a > b) {
    return a;
  } else {
    return b;
  }
}
```

The control flow graph of the program is shown below:

![Control flow graph](https://www.softwaretestingclass.com/wp-content/uploads/2016/07/Control-Flow-Graph-Example.png)

Using the first formula, we can calculate the cyclomatic complexity as follows:

- E = 4 (the number of edges)
- N = 4 (the number of nodes)
- P = 1 (the number of connected components)

Cyclomatic complexity = E – N + 2*P
= 4 - 4 + 2*1
= 2

Using the second formula, we can calculate the cyclomatic complexity as follows:

- P = 1 (the number of predicate nodes, which is the if statement)

Cyclomatic complexity = P + 1
= 1 + 1
= 2

Therefore, the cyclomatic complexity of the program is 2, which means that there are two linearly independent paths in the program. To achieve 100% path coverage, we need to design two test cases that can execute both the paths. For example, one test case can be (a = 5, b = 3) and another test case can be (a = 2, b = 4).