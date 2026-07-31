### BCNF

- BCNF stands for **Boyce-Codd Normal Form**     .
- It is an advanced version of **Third Normal Form (3NF)**    .
- A table or a relation is in BCNF if it satisfies the following conditions    :
  - It is already in 3NF.
  - For every functional dependency X -> Y, X is either a **super key** or a **candidate key**    .
- A super key is a set of attributes that can uniquely identify a tuple in a relation .
- A candidate key is a minimal super key, that is, a super key that does not have any redundant attribute .
- The purpose of BCNF is to eliminate **anomalies** and **redundancies** that may arise due to **transitive dependencies** or **partial dependencies**    .
- Anomalies are inconsistencies or errors that may occur when inserting, updating, or deleting data in a relation .
- Redundancies are duplication of data that may waste storage space and cause inconsistency .
- A transitive dependency is a functional dependency X -> Y -> Z, where X is not a super key and Z is not a prime attribute .
- A partial dependency is a functional dependency X -> Y, where X is a proper subset of a candidate key and Y is not a prime attribute .
- A prime attribute is an attribute that belongs to any candidate key .
- BCNF can be achieved by **decomposing** the relation into smaller relations that satisfy the BCNF conditions    .
- Decomposition should preserve the **functional dependencies** and the **lossless join property**    .
- Functional dependencies are constraints that specify the relationship between attributes in a relation .
- Lossless join property ensures that the original relation can be reconstructed from the decomposed relations without losing any information .