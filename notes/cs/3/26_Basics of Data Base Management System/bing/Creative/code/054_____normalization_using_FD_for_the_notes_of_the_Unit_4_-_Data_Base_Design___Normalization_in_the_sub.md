### Normalization using FD

Normalization is the process of designing a relational database schema to minimize redundancy and anomalies. It involves decomposing a relation into smaller relations that satisfy certain properties or normal forms. Normal forms are defined based on the concept of functional dependencies (FDs).

A functional dependency (FD) is a constraint that describes the relationship between attributes in a relation. It has the form X -> Y, where X and Y are sets of attributes of the relation. It means that the values of Y are determined by the values of X, or equivalently, two tuples that agree on X must also agree on Y. For example, if we have a relation R(A, B, C) and a FD A -> B, it means that for any two tuples t1 and t2 in R, if t1[A] = t2[A], then t1[B] = t2[B].

The most common normal forms are:

- First normal form (1NF): A relation is in 1NF if it has no multivalued or composite attributes. That is, each attribute value is atomic and indivisible.
- Second normal form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. That is, there is no partial dependency of any attribute on a proper subset of the primary key.
- Third normal form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. That is, there is no transitive dependency of any attribute on a non-key attribute that is functionally dependent on the primary key.
- Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key. That is, there is no FD X -> Y where X is not a candidate key.

The process of normalization using FDs involves the following steps:

- Identify all the FDs that hold in the relation.
- Check if the relation satisfies the desired normal form. If not, proceed to the next step.
- Decompose the relation into smaller relations that preserve the FDs and satisfy the desired normal form. This can be done using various algorithms, such as synthesis or decomposition.
- Eliminate any redundant relations that can be obtained from other relations by applying the FDs.
- Check if the decomposition is dependency-preserving and lossless-join. If not, try to find a better decomposition or use other techniques, such as introducing artificial attributes or adding constraints.