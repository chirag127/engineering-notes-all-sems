### BCNF (Boyce-Codd Normal Form)
BCNF is a higher version of the Third Normal Form (3NF) and is used in database normalization. It is a slightly stronger version of the Third Normal Form. A relation is in BCNF if and only if every determinant in the relation is a candidate key. In other words, for every non-trivial functional dependency X -> Y, X must be a superkey.

#### Properties of BCNF:
- BCNF is a stronger version of 3NF.
- A relation in BCNF is also in 3NF, 2NF, and 1NF.
- A relation in 3NF is not necessarily in BCNF.
- BCNF eliminates redundancy and anomalies in the relation.

#### Advantages of BCNF:
- BCNF eliminates redundancy in the relation.
- BCNF eliminates update, insertion, and deletion anomalies in the relation.
- BCNF ensures data integrity and consistency in the relation.

#### Disadvantages of BCNF:
- BCNF may result in more relations compared to 3NF.
- BCNF may result in more complex queries compared to 3NF.

#### BCNF Decomposition:
BCNF decomposition is the process of decomposing a relation into multiple relations that are in BCNF. The goal of BCNF decomposition is to eliminate redundancy and anomalies in the relation while preserving the dependencies.

#### Steps for BCNF Decomposition:
1. Identify a non-trivial functional dependency X -> Y in the relation that violates BCNF.
2. Decompose the relation into two relations: one with XY attributes and the other with the remaining attributes.
3. Repeat the above steps for the decomposed relations until all the relations are in BCNF.

#### Example of BCNF Decomposition:
Consider a relation R(A, B, C, D) with the following functional dependencies:
- A -> B
- BC -> D

The candidate keys for this relation are AC and AD. The functional dependency A -> B violates BCNF because A is not a superkey. To decompose this relation into BCNF, we can create two relations: R1(A, B) and R2(A, C, D). The relation R1 is in BCNF because A is a candidate key. The relation R2 is also in BCNF because the only non-trivial functional dependency is BC -> D and BC is a candidate key.
