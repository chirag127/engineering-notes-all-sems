### BCNF

- BCNF stands for Boyce-Codd Normal Form, which is an advanced version of 3NF (Third Normal Form)   .
- A relation is in BCNF if it is in 3NF and for every functional dependency X -> Y, X is a superkey or a candidate key  .
- A superkey is a set of attributes that uniquely identifies a tuple in a relation. A candidate key is a minimal superkey, meaning that no proper subset of it is a superkey .
- BCNF is stricter than 3NF, as it eliminates the possibility of having a non-prime attribute (an attribute that is not part of any candidate key) on the right-hand side of a functional dependency  .
- BCNF ensures that there are no anomalies (such as redundancy, inconsistency, or update anomalies) in the relation, and that every attribute depends only on the candidate keys   .

#### Example

- Consider a relation R with attributes A, B, C, D, and E, and the following functional dependencies:

  - A -> BC
  - C -> DE

- The candidate keys are {A} and {C}.
- This relation is in 3NF, as for every functional dependency, the left-hand side is a superkey or the right-hand side is a prime attribute.
- However, this relation is not in BCNF, as the functional dependency C -> DE violates the condition that the left-hand side must be a superkey. C is not a superkey, as it is not a minimal set of attributes that uniquely identifies a tuple.
- To convert this relation into BCNF, we need to decompose it into two relations:

  - R1(A, B, C) with the functional dependency A -> BC
  - R2(C, D, E) with the functional dependency C -> DE

- Both relations are now in BCNF, as for every functional dependency, the left-hand side is a superkey.