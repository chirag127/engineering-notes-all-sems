### BCNF

- BCNF stands for Boyce-Codd Normal Form, which is an advanced version of 3NF (Third Normal Form).
- A relation is in BCNF if it is already in 3NF and for every functional dependency X -> Y, X is a superkey or a candidate key of the relation  .
- A superkey is a set of attributes that can uniquely identify a tuple in a relation. A candidate key is a minimal superkey, meaning that no proper subset of it is a superkey.
- BCNF is stricter than 3NF, as it eliminates the possibility of having a non-prime attribute (an attribute that is not part of any candidate key) on the right-hand side of a functional dependency.
- BCNF ensures that there are no anomalies or redundancies in the relation, and that every attribute is fully dependent on the key.
- To check if a relation is in BCNF, we need to find all the functional dependencies and candidate keys in the relation, and then verify that the left-hand side of every functional dependency is a superkey or a candidate key.
- To convert a relation that is not in BCNF to BCNF, we need to decompose it into smaller relations that are in BCNF, by using the functional dependencies that violate the BCNF condition.

#### Example

- Consider a relation R with attributes A, B, C, D, and E, and the following functional dependencies:

  - A -> BC
  - C -> DE

- The candidate keys of R are {A} and {C}.
- The functional dependency A -> BC violates the BCNF condition, as A is not a superkey of R (it is only a candidate key).
- To convert R to BCNF, we need to decompose it into two relations:

  - R1(A, B, C) with the functional dependency A -> BC
  - R2(C, D, E) with the functional dependency C -> DE

- Both R1 and R2 are in BCNF, as the left-hand side of every functional dependency is a superkey or a candidate key of the relation.