Halestead’s Software Science is a set of software metrics that measure the complexity and quality of a program based on the number and types of operators and operands used in the source code. The basic idea is that a program can be seen as a collection of tokens, which are either operators (symbols that perform some action) or operands (data or variables that are acted upon). Halestead’s Software Science defines the following measures:

- n1: the number of distinct operators
- n2: the number of distinct operands
- N1: the total number of operators
- N2: the total number of operands
- n: the program vocabulary, defined as n = n1 + n2
- N: the program length, defined as N = N1 + N2
- V: the program volume, defined as V = N * log2(n)
- D: the program difficulty, defined as D = (n1/2) * (N2/n2)
- E: the program effort, defined as E = D * V
- T: the program time, defined as T = E / S, where S is a constant that represents the speed of the programmer
- L: the program level, defined as L = 1 / D
- B: the program error estimate, defined as B = E^(2/3) / 3000

The following diagram illustrates the basic architecture of Halestead’s Software Science in software design using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
| Source code     |     | Operators and   |     | Halestead's     |
|                 |     | operands        |     | metrics         |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      |                        |                        |
      +------------------------+------------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |