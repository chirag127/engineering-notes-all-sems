# Normalization using FD

Normalization is the process of designing a relational database schema to minimize redundancy and anomalies. It involves decomposing a relation into smaller relations that satisfy certain properties or normal forms. Normal forms are defined based on the concept of functional dependencies (FDs).

A functional dependency (FD) for a relation R is a formula of the form X -> Y, where X and Y are sets of attributes of R. It means that the values of Y are determined by the values of X. In other words, two tuples in R that have the same values for X must also have the same values for Y.

For example, in a relation R(A, B, C, D), the FD A -> B means that the value of B depends on the value of A. If two tuples in R have the same value for A, they must also have the same value for B.

There are different types of FDs, such as trivial, full, partial, and transitive. A trivial FD is one where Y is a subset of X, such as A -> A. A full FD is one where Y is not a subset of X, and X is a candidate key of R, such as A -> B. A partial FD is one where Y is not a subset of X, and X is not a candidate key of R, but a proper subset of a candidate key, such as AB -> C. A transitive FD is one where Y is not a subset of X, and there exists another attribute Z such that X -> Z and Z -> Y, such as A -> B and B -> C.

Normalization using FDs involves applying a series of rules or tests to check whether a relation satisfies a certain normal form, and if not, how to decompose it into smaller relations that do. The most common normal forms are:

- First normal form (1NF): A relation is in 1NF if it has no multivalued or composite attributes. That is, each attribute value is atomic and indivisible.
- Second normal form (2NF): A relation is in 2NF if it is in 1NF and has no partial FDs. That is, each non-key attribute is fully dependent on the whole primary key.
- Third normal form (3NF): A relation is in 3NF if it is in 2NF and has no transitive FDs. That is, each non-key attribute is directly dependent on the primary key, and not on any other non-key attribute.
- Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and has no non-trivial FDs that violate the key constraint. That is, each attribute is fully dependent on a candidate key, and not on any other attribute.

The process of normalization using FDs can be summarized as follows:

- Start with a relation R and a set of FDs F that hold on R.
- Check whether R is in BCNF. If yes, stop. If no, find a non-trivial FD X -> Y that violates the key constraint, and decompose R into two relations: R1 = (X, Y) and R2 = (R - Y) + X. Preserve the FDs that hold on R1 and R2, and add any new FDs that are implied by F.
- Repeat step 2 for each relation until all relations are in BCNF.

The benefits of normalization using FDs are:

- It reduces data redundancy and storage space.
- It eliminates update, insertion, and deletion anomalies that may cause data inconsistency.
- It improves data integrity and query efficiency.