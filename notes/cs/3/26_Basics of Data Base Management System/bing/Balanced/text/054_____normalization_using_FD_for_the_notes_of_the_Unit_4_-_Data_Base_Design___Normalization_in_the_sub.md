### Normalization using FD

- Normalization is a process of organizing the data in a database to avoid data redundancy, insertion anomaly, update anomaly and deletion anomaly.
- Functional dependency (FD) is a constraint that describes the relationship between attributes in a relation.
- FDs are used to decompose relations into smaller relations that are in higher normal forms.
- Normal forms are the standards for evaluating the quality of a relation. The most common normal forms are 1NF, 2NF, 3NF and BCNF.
- 1NF: A relation is in 1NF if it has no repeating groups or multivalued attributes. Every attribute value must be atomic and unique within a tuple.
- 2NF: A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. That is, there is no partial dependency of any attribute on the primary key.
- 3NF: A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. That is, there is no transitive dependency of any attribute on the primary key.
- BCNF: A relation is in BCNF if it is in 3NF and every determinant is a candidate key. That is, there is no dependency of any attribute on a non-key attribute.
- The steps to normalize a relation using FDs are:
  - Identify all the candidate keys and the primary key of the relation.
  - Identify all the FDs that hold in the relation.
  - Check if the relation is in 1NF. If not, eliminate the repeating groups or multivalued attributes by creating new relations.
  - Check if the relation is in 2NF. If not, decompose the relation into smaller relations such that each relation is in 2NF.
  - Check if the relation is in 3NF. If not, decompose the relation into smaller relations such that each relation is in 3NF.
  - Check if the relation is in BCNF. If not, decompose the relation into smaller relations such that each relation is in BCNF.
  - Eliminate any redundant relations that may have been created during the decomposition process.