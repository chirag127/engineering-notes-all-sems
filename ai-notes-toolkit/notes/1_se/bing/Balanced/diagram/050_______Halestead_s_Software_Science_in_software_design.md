Halestead's Software Science is a set of software metrics that measure the complexity and quality of a program based on the number and types of operators and operands used in the code  . The metrics are derived from the following base measures:

- n1 = Number of distinct operators
- n2 = Number of distinct operands
- N1 = Total number of operators
- N2 = Total number of operands

The following diagram shows how these base measures are used to calculate other metrics such as program length, vocabulary, volume, difficulty, effort, time, bugs, and level :

##### Halestead’s Software Science in software design
```
+-----------------+     +-----------------+     +-----------------+
| n1              |     | n2              |     | N1              |
| Number of       |     | Number of       |     | Total number of |
| distinct        |     | distinct        |     | operators       |
| operators       |     | operands        |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
| N2              |     | n = n1 + n2     |     | N = N1 + N2     |
| Total number of |     | Program         |     | Program length  |
| operands        |     | vocabulary      |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
| V = N * log2(n) |     | D = (n1/2) *    |     | E = D * V       |
| Program volume  |     | (N2/n2)         |     | Program effort  |
|                 |     | Program         |     |                 |
|                 |     | difficulty      |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
| T = E / 18      |     | B = V / 3000    |     | L = 1 / D       |
| Program time    |     | Estimated bugs  |     | Program level   |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```