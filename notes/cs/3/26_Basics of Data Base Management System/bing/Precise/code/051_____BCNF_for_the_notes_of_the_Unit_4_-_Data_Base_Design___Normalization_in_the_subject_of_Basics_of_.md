### BCNF (Boyce-Codd Normal Form)

BCNF is a higher version of the Third Normal Form (3NF). It is a normal form used in database normalization to design a database schema that is free from unwanted dependencies and redundancies.

- BCNF is also known as 3.5 Normal Form.
- A relation is in BCNF if and only if every determinant in the relation is a candidate key.
- BCNF is stricter than 3NF and ensures that there are no non-trivial functional dependencies between non-prime attributes.
- To convert a relation into BCNF, we need to decompose it into smaller relations that satisfy the BCNF properties.
- BCNF decomposition may not always be dependency preserving, which means that the dependencies that held in the original relation may not hold in the decomposed relations.
- BCNF is mainly used in situations where the relation has more than one candidate key and there are dependencies between the non-prime attributes.
