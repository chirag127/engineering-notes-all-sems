The following is a detailed ASCII diagram for Impracticality of Testing AllPaths for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing.

```
+-----------------+         +-----------------+         +-----------------+
|                 |         |                 |         |                 |
|  Test Case 1    |         |  Test Case 2    |         |  Test Case 3    |
|                 |         |                 |         |                 |
+-----------------+         +-----------------+         +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       V                         V                         V
+-----------------+         +-----------------+         +-----------------+
|                 |         |                 |         |                 |
|  Program        |         |  Program        |         |  Program        |
|                 |         |                 |         |                 |
+-----------------+         +-----------------+         +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       V                         V                         V
+-----------------+         +-----------------+         +-----------------+
|                 |         |                 |         |                 |
|  Output 1       |         |  Output 2       |         |  Output 3       |
|                 |         |                 |         |                 |
+-----------------+         +-----------------+         +-----------------+
```

The diagram shows that for each test case, the program produces a different output. However, this does not mean that the program has covered all possible paths in its code. There may be some paths that are not executed by any of the test cases, or some paths that are executed by more than one test case. Therefore, testing all paths is impractical, because it would require an infinite number of test cases, or at least a very large number that is not feasible to generate or execute.