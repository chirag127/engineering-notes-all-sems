### BCNF

- BCNF stands for **Boyce-Codd Normal Form** and it is an advanced version of 3NF (Third Normal Form).
- A relation is in BCNF if it is already in 3NF and for every functional dependency X -> Y, X is a super key or a candidate key of the relation  .
- A super key is a set of attributes that can uniquely identify a tuple in a relation. A candidate key is a minimal super key, meaning that no proper subset of the candidate key is a super key.
- BCNF is stricter than 3NF, as it eliminates the possibility of having a non-prime attribute (an attribute that is not part of any candidate key) on the right-hand side of a functional dependency .
- The purpose of BCNF is to reduce redundancy and anomalies in the data, such as insertion, deletion and update anomalies .
- To convert a relation into BCNF, we need to identify the functional dependencies that violate the BCNF condition and decompose the relation into smaller relations that preserve the dependencies and the data .
- For example, consider a relation R with attributes A, B, C, D and E, and the following functional dependencies:

  - A -> BC
  - C -> DE

- The candidate key for this relation is A, as it can uniquely determine all the other attributes. However, this relation is not in BCNF, as C is not a super key but it determines DE, which are non-prime attributes.
- To convert this relation into BCNF, we can decompose it into two relations:

  - R1(A, B, C) with functional dependency A -> BC
  - R2(C, D, E) with functional dependency C -> DE

- Both R1 and R2 are in BCNF, as the left-hand side of each functional dependency is a super key. The decomposition also preserves the original dependencies and the data.