# Unit 4 - Data Base Design & Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database.
- Database design involves identifying the entities, attributes, and relationships that are relevant to the data requirements and organizing them into tables and columns.
- Database design also involves defining the constraints, indexes, views, triggers, and other features that ensure the integrity, performance, and security of the database.
- Database design follows a set of principles and guidelines that help in creating a well-structured and normalized database.

## Database Normalization
- Database normalization is a method in relational database design which helps properly organize data tables.
- The process aims to create a system that faithfully represents information and relationships without data loss or redundancy.
- Database normalization involves decomposing tables into smaller and simpler ones based on the functional dependencies and the level of data redundancy.
- Database normalization reduces the chances of data anomalies, such as insertion, deletion, and update anomalies, that can compromise the consistency and accuracy of the database.
- Database normalization also improves the efficiency and flexibility of the database by reducing the storage space and the number of joins required for querying the data.

## Normal Forms
- Normal forms are the standards or rules that define the level of normalization of a database or a table.
- Normal forms are based on the concept of functional dependency, which is a relationship between two sets of attributes such that the value of one set determines the value of the other set.
- Normal forms are hierarchical, meaning that a higher normal form implies that the lower normal forms are also satisfied.
- The most common normal forms are:

  - First Normal Form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute has a single value for each record.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key or the candidate key.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key or the candidate key, meaning that there are no functional dependencies between non-key attributes.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning that there are no partial or transitive dependencies on non-key attributes.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies, meaning that there are no attributes that depend on a set of attributes rather than a single attribute.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, meaning that it cannot be decomposed into smaller tables without losing information.