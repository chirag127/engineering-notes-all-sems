## Unit 4 - Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database management system (DBMS).
- Database design involves identifying the data requirements, defining the entities and attributes, establishing the relationships and constraints, and choosing the appropriate data models and schemas.
- Normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into smaller and well-defined tables.
- Normalization involves applying a series of rules or normal forms to decompose a table into simpler tables that have minimal functional dependencies and anomalies.
- The main normal forms are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute is atomic (indivisible).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies that are not implied by the candidate keys.
- Normalization can improve the performance, maintainability, and security of a database, but it can also introduce some drawbacks, such as increased complexity, reduced efficiency, and loss of information. Therefore, it is important to balance the benefits and costs of normalization and choose the optimal level of normalization for a given database.