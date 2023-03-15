### BCNF

- BCNF stands for Boyce-Codd Normal Form     .
- It is an advanced version of 3NF (Third Normal Form)   .
- It is also sometimes referred to as 3.5NF or 3.5 Normal Form.
- It is based on functional dependencies that take into account all candidate keys in a relation .
- A relation is in BCNF if and only if for every functional dependency X -> Y, X is a superkey    .
- A superkey is a set of attributes that uniquely identifies a tuple in a relation.
- A candidate key is a minimal superkey, that is, a superkey that has no proper subset that is also a superkey.
- A prime attribute is an attribute that belongs to any candidate key.
- BCNF eliminates the possibility of having non-trivial functional dependencies of attributes on anything other than a superset of a candidate key .
- BCNF ensures that every determinant is a candidate key.
- BCNF helps to reduce redundancy and anomalies in a relation.

#### Example of BCNF

- Consider a relation R with attributes A, B, C, D, E and the following functional dependencies:

  - A -> BC
  - C -> DE

- The candidate keys are {A} and {C}.
- The relation R is in 3NF, but not in BCNF, because the functional dependency A -> BC violates the BCNF condition, as A is not a superkey.
- To convert R into BCNF, we need to decompose it into two relations:

  - R1(A, B, C) with the functional dependency A -> BC
  - R2(C, D, E) with the functional dependency C -> DE

- Both R1 and R2 are in BCNF, as the left-hand side of each functional dependency is a superkey.
- The decomposition preserves the functional dependencies and reduces redundancy and anomalies.