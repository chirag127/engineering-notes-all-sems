### BCNF

- BCNF stands for Boyce-Codd Normal Form, which is an advanced version of 3NF (Third Normal Form)   .
- A relation is in BCNF if it is in 3NF and for every functional dependency X -> Y, X is a super key or a candidate key    .
- A super key is a set of attributes that can uniquely identify a tuple in a relation .
- A candidate key is a minimal super key, that is, a super key that does not contain any redundant attribute .
- A functional dependency X -> Y means that the values of Y are determined by the values of X .
- A relation that is not in BCNF may have redundancy, inconsistency, and update anomalies   .
- To convert a relation into BCNF, we need to decompose it into smaller relations that satisfy the BCNF condition   .
- Decomposition should preserve the functional dependencies and the information of the original relation  .
- An example of a relation that is not in BCNF and how to decompose it into BCNF is given below :

| A | B | C | D | E |
|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 |
| 1 | 2 | 6 | 7 | 8 |
| 9 | 10| 3 | 4 | 5 |
| 9 | 10| 6 | 7 | 8 |

- The relation R(ABCDE) has the following functional dependencies: FD = {A -> BC, C -> DE}
- The candidate key is {A}
- The functional dependency C -> DE violates the BCNF condition, because C is not a super key or a candidate key
- To decompose R into BCNF, we can split it into two relations: R1(AC) and R2(CDE)
- R1 and R2 are in BCNF, because the only functional dependencies are A -> C and C -> DE, and both A and C are candidate keys in their respective relations
- R1 and R2 also preserve the functional dependencies and the information of R, because we can join them on the common attribute C to get back R

| A | C |
|---|---|
| 1 | 3 |
| 1 | 6 |
| 9 | 3 |
| 9 | 6 |

| C | D | E |
|---|---|---|
| 3 | 4 | 5 |
| 6 | 7 | 8 |

- The advantages of BCNF are that it reduces redundancy, inconsistency, and update anomalies, and ensures data integrity and normalization   .