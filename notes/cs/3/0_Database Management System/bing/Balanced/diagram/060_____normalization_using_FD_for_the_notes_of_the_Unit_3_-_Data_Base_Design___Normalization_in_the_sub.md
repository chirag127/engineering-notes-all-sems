### Normalization using FD

- Normalization is a process of organizing the data in a database to avoid data redundancy, insertion anomaly, update anomaly and deletion anomaly.
- Normalization is done by applying some rules or constraints on the database schema, which are called normal forms.
- Normal forms are based on the concept of functional dependencies (FDs), which capture the relationship between attributes in a relation.
- A functional dependency X -> Y means that the value of Y is determined by the value of X. In other words, if two tuples have the same value for X, they must also have the same value for Y.
- A relation is in a certain normal form if it satisfies the corresponding set of FDs or constraints.
- The most common normal forms are:

  - First normal form (1NF): A relation is in 1NF if it has no repeating groups or multivalued attributes. That is, each attribute value is atomic and indivisible.
  - Second normal form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. That is, there is no partial dependency of any attribute on a subset of the primary key.
  - Third normal form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. That is, there is no transitive dependency of any attribute on a non-key attribute that is functionally dependent on the primary key.
  - Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key. That is, there is no dependency of any attribute on a non-key attribute that is not a candidate key.

- To normalize a relation using FDs, we can follow these steps:

  - Identify all the candidate keys and the primary key of the relation.
  - Identify all the FDs that hold in the relation.
  - Check if the relation is in 1NF. If not, decompose it into 1NF relations by eliminating the repeating groups or multivalued attributes.
  - Check if the relation is in 2NF. If not, decompose it into 2NF relations by eliminating the partial dependencies.
  - Check if the relation is in 3NF. If not, decompose it into 3NF relations by eliminating the transitive dependencies.
  - Check if the relation is in BCNF. If not, decompose it into BCNF relations by eliminating the non-key dependencies.