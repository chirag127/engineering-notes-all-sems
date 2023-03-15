### Normalization using FD

- Normalization is the process of designing a relational database schema to minimize redundancy and anomalies.
- Functional dependency (FD) is a constraint that describes the relationship between attributes in a relation.
- A FD X -> Y means that the values of Y are determined by the values of X. Two tuples sharing the same values of X will necessarily have the same values of Y.
- A FD is trivial if Y is a subset of X, or full if Y is not a subset of X.
- A FD is called a partial dependency if there is a proper subset of X that can also determine Y.
- A FD is called a transitive dependency if there is an attribute Z that is not part of the candidate key and X -> Z and Z -> Y.
- Normalization uses FDs to decompose a relation into smaller relations that satisfy certain normal forms.
- Normal forms are defined based on the types of FDs that a relation can or cannot have.
- The most common normal forms are:

  - First normal form (1NF): A relation is in 1NF if it has no multivalued or composite attributes. All attributes are atomic.
  - Second normal form (2NF): A relation is in 2NF if it is in 1NF and has no partial dependencies.
  - Third normal form (3NF): A relation is in 3NF if it is in 2NF and has no transitive dependencies.
  - Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key.

- Normalization can be done by applying a series of decomposition rules based on the FDs of a relation.
- Decomposition rules aim to preserve the information and the dependencies of the original relation.
- Decomposition rules include:

  - Decomposition by projection: Given a relation R and a FD X -> Y, decompose R into two relations R1(X,Y) and R2(X,Z), where Z is the set of attributes of R that are not in X or Y.
  - Decomposition by synthesis: Given a relation R and a set of FDs F, decompose R into a set of relations that are in BCNF and whose FDs are logically implied by F.
  - Decomposition by analysis: Given a relation R and a set of FDs F, decompose R into a set of relations that are in 3NF and whose FDs are logically implied by F.