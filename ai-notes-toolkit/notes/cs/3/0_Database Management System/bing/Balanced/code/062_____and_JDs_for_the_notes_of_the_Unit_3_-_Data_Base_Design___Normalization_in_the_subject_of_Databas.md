# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, establishing the relationships and constraints, and choosing the appropriate data models and storage options.
- Database design aims to achieve the following objectives:
  - Accurately represent the real-world domain and its rules
  - Ensure data integrity, consistency, and quality
  - Support efficient data access and manipulation
  - Facilitate data security and privacy
  - Allow for data scalability and maintainability
- Database design can be divided into three phases:
  - Conceptual design: The high-level description of the data and its relationships, using a conceptual data model such as the Entity-Relationship (ER) model.
  - Logical design: The translation of the conceptual design into a logical data model such as the Relational model, which specifies the tables, columns, keys, and constraints.
  - Physical design: The implementation of the logical design in a specific database management system (DBMS), which involves choosing the physical storage structures, indexes, and performance tuning parameters.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization split a large table into smaller tables and define relationships between them to increases the clarity in organizing data.
- Normalization helps in improving the overall design of the database by:
  - Reducing data anomalies, such as insertion, deletion, and update anomalies, that may arise due to data duplication and inconsistency.
  - Enhancing data integrity and consistency by enforcing the atomicity, domain, entity, and referential integrity constraints.
  - Simplifying data manipulation and querying by reducing the complexity and ambiguity of the data and its relationships.
  - Saving storage space and improving performance by eliminating unnecessary data and optimizing the table structures and indexes.
- Normalization is based on the concept of normal forms, which are the levels of quality or refinement that a database schema can achieve. The most common normal forms are:
  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values, i.e., each cell can hold only one value, and there are no repeating groups or arrays within a row.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there are no partial dependencies.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there are no transitive dependencies.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there are no non-trivial functional dependencies that violate the key constraint.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and there are no multi-valued dependencies, i.e., there are no attributes that depend on a set of attributes rather than a single attribute.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and there are no join dependencies, i.e., there are no subsets of attributes that can be projected out and joined back without loss of information.