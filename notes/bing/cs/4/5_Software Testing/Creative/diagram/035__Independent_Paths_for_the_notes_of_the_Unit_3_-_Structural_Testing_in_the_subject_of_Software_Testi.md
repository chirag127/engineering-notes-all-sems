The following diagram illustrates the basic architecture of a control flow graph for a simple program that calculates the factorial of a number. The control flow graph shows the independent paths that can be used for basis path testing, which is a type of structural testing that aims to cover all possible paths in the program. The independent paths are labeled as P1, P2, P3, and P4. The cyclomatic complexity of the graph is 4, which is equal to the number of independent paths.

```
+-----+       +-----+       +-----+       +-----+
|Start| ----> |Read | ----> |Fact | ----> |Print| ----> |End |
|     |       | n   |       | = 1 |       |Fact |       |    |
+-----+       +-----+       +-----+       +-----+       +-----+
                  |            |             ^
                  |            |             |
                  |            v             |
                  |          +-----+         |
                  |          | n>0 |         |
                  |          +-----+         |
                  |            |             |
                  |            |             |
                  |            v             |
                  |          +-----+         |
                  |          |Fact |         |
                  |          |*=n  |         |
                  |          +-----+         |
                  |            |             |
                  |            |             |
                  |            v             |
                  |          +-----+         |
                  |          | n-- |         |
                  |          +-----+         |
                  |            |             |
                  +------------+-------------+

P1: Start -> Read n -> Fact = 1 -> n > 0 -> Fact *= n -> n-- -> n > 0 -> Print Fact -> End
P2: Start -> Read n -> Fact = 1 -> n > 0 -> Fact *= n -> n-- -> n <= 0 -> Print Fact -> End
P3: Start -> Read n -> Fact = 1 -> n <= 0 -> Print Fact -> End
P4: Start -> Read n -> Fact = 1 -> n > 0 -> Fact *= n -> n-- -> n > 0 -> Fact *= n -> n-- -> n <= 0 -> Print Fact -> End
```