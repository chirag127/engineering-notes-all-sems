### BCNF

- BCNF stands for **Boyce-Codd Normal Form**     .
- It is an advanced version of **Third Normal Form (3NF)**    .
- A table or a relation is in BCNF if it satisfies the following conditions    :
  - It is already in 3NF.
  - For every functional dependency X -> Y, X is a **super key** or a **candidate key** of the table or relation.
- A super key is a set of attributes that can uniquely identify a tuple in a relation .
- A candidate key is a minimal super key, that is, a super key that does not have any redundant attribute .
- The purpose of BCNF is to **reduce redundancy** and **eliminate anomalies** in the data    .
- Anomalies are inconsistencies or errors that may occur when inserting, updating, or deleting data in a table .
- BCNF is also sometimes referred to as **3.5 Normal Form** or **3.5NF**.

#### Example of BCNF

- Consider a relation R with five attributes: R(ABCDE).
- The functional dependencies are: FD = {A -> BC, C -> DE}.
- The candidate key is: {A}.
- To check if R is in BCNF, we inspect each of the functional dependencies:
  - A -> BC: This satisfies BCNF, because A is a candidate key.
  - C -> DE: This violates BCNF, because C is not a super key or a candidate key.
- To convert R into BCNF, we decompose it into two relations:
  - R1(ABC) with FD = {A -> BC}.
  - R2(CDE) with FD = {C -> DE}.
- Both R1 and R2 are in BCNF, because for each functional dependency, the left-hand side is a candidate key.
- The decomposition preserves the functional dependencies and reduces the redundancy in the data.