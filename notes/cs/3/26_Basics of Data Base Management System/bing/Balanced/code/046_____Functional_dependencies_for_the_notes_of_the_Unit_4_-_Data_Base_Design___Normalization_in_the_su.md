### Functional dependencies for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database.
- A functional dependency mathematically expresses the relation between different values in a database management system (DBMS).
- A functional dependency is denoted by an arrow, such as X -> Y, which means that the value of Y is determined by the value of X.
- There are four primary types of functional dependencies: multivalued, trivial, non-trivial and transitive .
- Multivalued dependency: A multivalued dependency occurs when there are two or more independent attributes in a relation that depend on a third attribute. For example, in a relation R(A, B, C), if A ->> B and A ->> C, then B and C are multivalued dependent on A.
- Trivial dependency: A trivial dependency occurs when the dependent attribute is a subset of the determinant attribute. For example, in a relation R(A, B, C), if A -> A or A -> AB, then these are trivial dependencies.
- Non-trivial dependency: A non-trivial dependency occurs when the dependent attribute is not a subset of the determinant attribute. For example, in a relation R(A, B, C), if A -> C, then this is a non-trivial dependency.
- Transitive dependency: A transitive dependency occurs when there is an indirect dependency between two attributes through a third attribute. For example, in a relation R(A, B, C), if A -> B and B -> C, then C is transitively dependent on A.
- Functional dependencies are used to establish relationships between attributes in a database and to ensure that the database is in a state of normalization .
- Normalization is the process of organizing the data in a database to minimize data redundancy and improve data integrity .
- There are several normal forms that a database can follow, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF) and fifth normal form (5NF) .
- Each normal form has a set of rules or conditions that the database must satisfy to be in that normal form .
- The higher the normal form, the more normalized the database is, and the less data redundancy and anomalies it has .
- However, higher normal forms may also result in more tables and joins, which may affect the performance and complexity of the database .
- Therefore, the choice of the normal form depends on the requirements and trade-offs of the database design .