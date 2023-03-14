Boundary Value Analysis is a functional testing technique that is based on testing the boundary values of valid and invalid partitions. It is used to check the behavior of the system at the edge of the equivalence partition, where errors are more likely to occur. It involves testing the minimum, maximum, just above the minimum, just below the maximum, and nominal values of each input variable.

The following is a possible ASCII diagram for Boundary Value Analysis for the notes of the Unit 2 - Functional Testing in the subject of Software Testing:

```
+-----------------+-----------------+-----------------+
| Invalid         | Valid           | Invalid         |
| Partition       | Partition       | Partition       |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
| Min-1           | Min             | Max+1           |
| (Boundary Value)| (Boundary Value)| (Boundary Value)|
+-----------------+-----------------+-----------------+
|                 | Min+1           |                 |
|                 | (Boundary Value)|                 |
|                 +-----------------+                 |
|                 | Nominal         |                 |
|                 | (Boundary Value)|                 |
|                 +-----------------+                 |
|                 | Max-1           |                 |
|                 | (Boundary Value)|                 |
+-----------------+-----------------+-----------------+
```