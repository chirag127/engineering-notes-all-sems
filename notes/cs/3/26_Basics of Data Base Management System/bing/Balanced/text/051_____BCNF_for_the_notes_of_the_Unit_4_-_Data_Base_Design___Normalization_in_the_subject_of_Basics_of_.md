### BCNF

- BCNF stands for Boyce-Codd Normal Form, which is an advanced version of 3NF (Third Normal Form).
- A relation is in BCNF if it is in 3NF and for every functional dependency X -> Y, X is a superkey or a candidate key of the relation  .
- A superkey is a set of attributes that uniquely identifies a tuple in a relation. A candidate key is a minimal superkey, meaning that no proper subset of it is a superkey.
- BCNF is stricter than 3NF, as it eliminates the possibility of having a non-prime attribute (an attribute that is not part of any candidate key) on the right-hand side of a functional dependency.
- The purpose of BCNF is to reduce redundancy and anomalies in the data, such as insertion, deletion and update anomalies.
- To convert a relation into BCNF, we need to decompose it into smaller relations that satisfy the BCNF condition, while preserving the functional dependencies and the data.
- An example of BCNF decomposition is as follows:

  - Consider a relation R(ABCDE) with the following functional dependencies: FD = {A -> BC, C -> DE}.
  - The candidate key of R is A, as it determines all the other attributes.
  - The relation R is not in BCNF, as the functional dependency C -> DE violates the BCNF condition, since C is not a superkey or a candidate key.
  - To convert R into BCNF, we need to decompose it into two relations: R1(ABC) and R2(CDE), such that R1 has the functional dependency A -> BC and R2 has the functional dependency C -> DE.
  - The relations R1 and R2 are in BCNF, as the left-hand side of each functional dependency is a candidate key of the relation.
  - The decomposition preserves the functional dependencies and the data of R, as we can reconstruct R by joining R1 and R2 on the attribute C.