Boundary Value Analysis (BVA) is a software testing technique that focuses on testing the boundary values of valid and invalid partitions. The boundary values are the values at the edge of an equivalence partition or at the smallest and largest possible values of a range. The idea is that errors are more likely to occur at the boundaries than in the middle of the input domain.

A possible ASCII diagram for Boundary Value Analysis for the notes of the Unit 2 - Functional Testing in the subject of Software Testing is:

```
+-----------------+-----------------+-----------------+
| Invalid Input   | Valid Input     | Invalid Input   |
| Partition       | Partition       | Partition       |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|  <--------------|-----------------|---------------> |
|                 |                 |                 |
|  min - 1        |      min        |      max        |
|                 |                 |                 |
|  <--------------|-----------------|---------------> |
|                 |                 |                 |
|  min            |  min + 1        |      max + 1    |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
```

The diagram shows the boundary values for a valid input range of [min, max]. The invalid input partitions are the values below min and above max. The boundary values are min - 1, min, min + 1, max, and max + 1. These are the values that should be tested to check the functionality of the software.