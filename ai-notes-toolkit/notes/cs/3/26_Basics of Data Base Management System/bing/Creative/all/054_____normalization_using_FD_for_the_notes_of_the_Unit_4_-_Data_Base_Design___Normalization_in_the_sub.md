# Normalization using FD

Normalization is the process of designing a relational database schema to minimize redundancy and anomalies. It involves decomposing a relation into smaller relations that satisfy certain properties or normal forms. Functional dependencies (FDs) are used to express the constraints between attributes in a relation. A functional dependency FD: X -> Y means that the values of Y are determined by the values of X. Two tuples sharing the same values of X will necessarily have the same values of Y.

Some of the common normal forms are:

- First normal form (1NF): A relation is in 1NF if every attribute is atomic, i.e., it cannot be further decomposed into smaller parts. For example, a relation with an attribute that stores a list of values is not in 1NF.
- Second normal form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., it does not depend on a proper subset of the primary key. For example, a relation with a composite primary key (A, B) and a non-key attribute C that depends only on A is not in 2NF.
- Third normal form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., it does not depend on another non-key attribute. For example, a relation with a primary key A and non-key attributes B and C, where B -> C, is not in 3NF.
- Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there is no non-trivial FD where the left-hand side is not a candidate key. For example, a relation with a candidate key A and a non-key attribute B, where A -> B and B -> A, is not in BCNF.

The process of normalization using FDs involves the following steps:

- Identify all the FDs that hold in the relation.
- Check if the relation satisfies the desired normal form. If not, proceed to the next step.
- Decompose the relation into smaller relations that preserve the FDs and satisfy the desired normal form. This may involve finding a minimal cover of the FDs, i.e., a set of FDs that is equivalent to the original set but has no redundant FDs.
- Repeat the process for each of the smaller relations until all of them are in the desired normal form.

Normalization using FDs can help to achieve a better database design that avoids redundancy and anomalies, such as insertion, deletion, and update anomalies. However, normalization may also have some drawbacks, such as loss of performance, increased complexity, and loss of semantic information. Therefore, normalization should be balanced with other design considerations, such as user requirements, query efficiency, and data integrity.