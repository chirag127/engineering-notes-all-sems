# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accurately represent the real-world domain and its information needs.
  - Ensure data integrity, consistency, and quality.
  - Minimize data redundancy and duplication.
  - Optimize data access and performance.
  - Facilitate data maintenance and evolution.
- Database design can be divided into three phases:
  - Conceptual design: The high-level description of the data and its relationships, using a conceptual data model such as the entity-relationship (ER) model or the unified modeling language (UML) class diagram.
  - Logical design: The translation of the conceptual design into a logical data model such as the relational model or the object-relational model, which defines the tables, columns, keys, and constraints.
  - Physical design: The implementation of the logical design in a specific database management system (DBMS), which defines the storage structures, indexes, views, and other physical aspects.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity in organizing data.
- Normalization also helps to avoid data anomalies, such as insertion, deletion, and update anomalies, which can cause data inconsistency and corruption.
- Normalization is based on the concept of normal forms, which are sets of rules or criteria that a table must satisfy to be considered well-structured and normalized.
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it contains only atomic values, i.e., each cell can hold only one value, and there are no repeating groups or arrays of values.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there are no partial dependencies.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there are no transitive dependencies.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there are no non-trivial functional dependencies that violate the key constraint.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies, i.e., there are no attributes that depend on a set of attributes rather than a single attribute.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, i.e., it cannot be decomposed into smaller tables without losing information.