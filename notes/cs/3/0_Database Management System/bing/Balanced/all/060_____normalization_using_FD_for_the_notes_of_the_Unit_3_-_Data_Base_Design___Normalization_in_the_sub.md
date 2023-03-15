# Normalization using FD

Normalization is the process of designing a relational database schema to minimize redundancy and anomalies. It involves decomposing a relation into smaller relations that satisfy certain properties or normal forms. Normal forms are defined based on the concept of functional dependencies (FDs).

A functional dependency (FD) is a constraint that describes the relationship between attributes in a relation. It has the form X -> Y, where X and Y are sets of attributes of the relation. It means that the values of Y are determined by the values of X, or equivalently, two tuples that agree on X must also agree on Y. X is called the determinant and Y is called the dependent.

For example, in a relation R(A, B, C, D) with the following FDs:

- A -> B
- B -> C
- A, C -> D

We can say that B is functionally dependent on A, C is functionally dependent on B, and D is functionally dependent on A and C.

There are different normal forms that a relation can satisfy, depending on the properties of its FDs. The most common ones are:

- First normal form (1NF): A relation is in 1NF if it has no multivalued or composite attributes. This is the basic requirement for a relation to be well-formed.
- Second normal form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. This means that there is no partial dependency, where a non-key attribute depends on only part of the primary key.
- Third normal form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. This means that there is no transitive dependency, where a non-key attribute depends on another non-key attribute that depends on the primary key.
- Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key. This means that there is no dependency where a non-key attribute determines another non-key attribute.

Normalization using FDs is the process of applying these normal forms to a relation to reduce redundancy and anomalies. It involves finding the minimal cover of FDs for the relation, identifying the candidate keys, and decomposing the relation into smaller relations that satisfy the desired normal form. The minimal cover of FDs is a set of FDs that is equivalent to the original set of FDs, but has no redundant FDs or attributes. A candidate key is a minimal set of attributes that uniquely identifies each tuple in the relation.

For example, consider the relation R(A, B, C, D) with the following FDs:

- A -> B
- B -> C
- A, C -> D

The minimal cover of FDs for R is:

- A -> B
- B -> C
- A -> D

The candidate keys for R are:

- A
- B, D

To normalize R into 3NF, we can decompose it into the following relations:

- R1(A, B) with FD A -> B
- R2(B, C) with FD B -> C
- R3(A, D) with FD A -> D

To normalize R into BCNF, we can decompose it further into the following relations:

- R1(A, B) with FD A -> B
- R2(B, C) with FD B -> C
- R3(A, D) with FD A -> D
- R4(B, D) with no FDs

Normalization using FDs can help improve the quality and efficiency of a database design by eliminating redundancy and anomalies. However, it may also introduce some drawbacks, such as loss of information, increased number of joins, and reduced performance. Therefore, normalization should be balanced with other design considerations, such as user requirements, query patterns, and data integrity.