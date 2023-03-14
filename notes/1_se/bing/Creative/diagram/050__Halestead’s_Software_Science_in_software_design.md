Halestead’s Software Science is a method of measuring the complexity of a software program based on the number and types of operators and operands used in the source code. It defines several metrics that can be calculated from the base measures of the number of distinct operators (n1), the number of distinct operands (n2), the total number of occurrences of operators (N1), and the total number of occurrences of operands (N2). These metrics include the program vocabulary (n), the program length (N), the estimated program length (N^), the program volume (V), the potential minimum volume (V*), the program level (L), the difficulty (D), the effort (E), the time required to program (T), and the number of delivered bugs (B).

The following diagram illustrates the basic architecture of Halestead’s Software Science in software design:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Source code    |----->|  Base measures  |----->|  Derived        |
|                 |      |  (n1, n2, N1,   |      |  metrics        |
|                 |      |  N2)            |      |  (n, N, N^, V,  |
+-----------------+      +-----------------+      |  V*, L, D, E,   |
                                                 |  T, B)          |
                                                 |                 |
                                                 +-----------------+
```