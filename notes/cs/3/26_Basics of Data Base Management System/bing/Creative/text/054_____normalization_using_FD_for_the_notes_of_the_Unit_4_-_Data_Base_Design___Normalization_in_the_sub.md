### Normalization using FD

- Normalization is the process of designing a relational database schema to minimize redundancy and anomalies.
- Functional dependency (FD) is a constraint that describes the relationship between attributes in a relation.
- A FD X -> Y means that the values of Y are determined by the values of X. Two tuples sharing the same values of X will necessarily have the same values of Y.
- A FD is trivial if Y is a subset of X, or full if Y is not a subset of X.
- A FD is called a superkey if X is a superkey of the relation, or a candidate key if X is a candidate key of the relation.
- A FD is called a partial dependency if there is a proper subset of X that determines Y, or a transitive dependency if there is an attribute Z that is not part of any candidate key and X -> Z and Z -> Y.
- Normalization using FD involves applying a series of normal forms to a relation, each with a specific condition that must be satisfied.
- The normal forms are:

  - First normal form (1NF): A relation is in 1NF if it has no multivalued or composite attributes. All attributes must be atomic.
  - Second normal form (2NF): A relation is in 2NF if it is in 1NF and has no partial dependencies. All non-key attributes must depend on the whole candidate key.
  - Third normal form (3NF): A relation is in 3NF if it is in 2NF and has no transitive dependencies. All non-key attributes must depend only on the candidate keys.
  - Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and has no FDs that violate the candidate keys. All FDs must have a candidate key on the left hand side.
  - Fourth normal form (4NF): A relation is in 4NF if it is in BCNF and has no multivalued dependencies. A multivalued dependency X ->> Y means that for each value of X, there is a set of values of Y that are associated with it.
  - Fifth normal form (5NF): A relation is in 5NF if it is in 4NF and has no join dependencies. A join dependency means that the relation can be decomposed into two or more relations that can be joined back to get the original relation.

- Normalization using FD can be done by following these steps:

  - Identify all the FDs that hold in the relation.
  - Check if the relation is in 1NF. If not, decompose it into 1NF relations.
  - Check if the relation is in 2NF. If not, decompose it into 2NF relations by eliminating partial dependencies.
  - Check if the relation is in 3NF. If not, decompose it into 3NF relations by eliminating transitive dependencies.
  - Check if the relation is in BCNF. If not, decompose it into BCNF relations by eliminating FDs that violate the candidate keys.
  - Check if the relation is in 4NF. If not, decompose it into 4NF relations by eliminating multivalued dependencies.
  - Check if the relation is in 5NF. If not, decompose it into 5NF relations by eliminating join dependencies.
  - Check if the decomposition is lossless and dependency-preserving. If not, try to find a better decomposition or use other techniques to ensure data integrity.