# Normalization using FD

- Normalization is a process of organizing the data in a database to avoid data redundancy, insertion anomaly, update anomaly and deletion anomaly.
- Normalization is done by applying some rules or constraints called normal forms on the database schema.
- Normal forms are based on the concept of functional dependencies (FDs), which capture the relationships between the attributes of a relation.
- A functional dependency X -> Y means that the value of Y is determined by the value of X. In other words, if two tuples have the same value for X, they must also have the same value for Y.
- A relation is in a certain normal form if it satisfies the corresponding set of conditions or constraints based on the FDs.
- The most common normal forms are:

  - First normal form (1NF): A relation is in 1NF if it has no repeating groups or multivalued attributes. That is, each attribute must have a single atomic value.
  - Second normal form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. That is, there is no partial dependency of any attribute on a subset of the primary key.
  - Third normal form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. That is, there is no transitive dependency of any attribute on a non-key attribute that is functionally dependent on the primary key.
  - Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key. That is, there is no dependency of any attribute on a non-key attribute that is not a candidate key.
  - Fourth normal form (4NF): A relation is in 4NF if it is in BCNF and has no multivalued dependencies. That is, there is no dependency of one set of attributes on another set of attributes that is not functionally dependent on the primary key.
  - Fifth normal form (5NF): A relation is in 5NF if it is in 4NF and has no join dependencies. That is, the relation cannot be decomposed into two or more relations that can be joined together to produce the original relation.

- To normalize a relation using FDs, we can follow these steps:

  - Identify all the FDs that hold in the relation and find the candidate keys.
  - Check if the relation is in 1NF and eliminate any repeating groups or multivalued attributes by creating new relations.
  - Check if the relation is in 2NF and eliminate any partial dependencies by creating new relations.
  - Check if the relation is in 3NF and eliminate any transitive dependencies by creating new relations.
  - Check if the relation is in BCNF and eliminate any dependencies that violate the BCNF condition by creating new relations.
  - Check if the relation is in 4NF and eliminate any multivalued dependencies by creating new relations.
  - Check if the relation is in 5NF and eliminate any join dependencies by creating new relations.