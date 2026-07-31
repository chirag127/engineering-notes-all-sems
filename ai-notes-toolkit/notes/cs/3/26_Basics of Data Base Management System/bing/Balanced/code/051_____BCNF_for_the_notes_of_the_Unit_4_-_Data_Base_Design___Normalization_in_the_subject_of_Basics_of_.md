### BCNF

- BCNF stands for Boyce-Codd Normal Form, which is an advanced version of 3NF (Third Normal Form)   .
- A relation is in BCNF if it is already in 3NF and for every functional dependency X -> Y, X is a super key or a candidate key  .
- A super key is a set of attributes that can uniquely identify a tuple in a relation. A candidate key is a minimal super key, meaning that no proper subset of it is a super key .
- BCNF is stricter than 3NF, as it eliminates the possibility of having a non-prime attribute (an attribute that is not part of any candidate key) on the right-hand side of a functional dependency  .
- BCNF ensures that there are no anomalies (such as redundancy, inconsistency, or update anomalies) in the relation, and that every attribute is fully dependent on the key  .

#### Example

- Consider a relation R with attributes A, B, C, D, and E, and the following functional dependencies:

  - A -> BC
  - C -> DE

- The candidate key for this relation is A, as it can uniquely determine all other attributes .
- This relation is in 3NF, as for every functional dependency, the left-hand side is a super key or the right-hand side is a prime attribute .
- However, this relation is not in BCNF, as C -> DE violates the condition that the left-hand side must be a super key .
- To convert this relation into BCNF, we need to decompose it into two relations, R1 and R2, as follows:

  - R1 (A, B, C)
  - R2 (C, D, E)

- Now, both R1 and R2 are in BCNF, as the only functional dependencies are A -> BC and C -> DE, and in both cases, the left-hand side is a candidate key .