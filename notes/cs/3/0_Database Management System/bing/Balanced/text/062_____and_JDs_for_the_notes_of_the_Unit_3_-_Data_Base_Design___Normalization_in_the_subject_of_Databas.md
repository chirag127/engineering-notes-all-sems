# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accuracy: The database should accurately represent the real-world domain and the business rules of the application.
  - Efficiency: The database should allow fast and easy access, insertion, update, and deletion of data, while minimizing the storage space and processing overhead.
  - Security: The database should protect the data from unauthorized access, modification, or deletion, and ensure the integrity and consistency of the data.
  - Flexibility: The database should be able to accommodate changing data requirements and business needs, without requiring major modifications or redesigns.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity in organizing data.
- Normalization helps in achieving the following benefits:
  - Improved Database Design: Normalization helps in improving the overall design of the database. By organizing the data in a structured and systematic way, normalization makes it easier to design and maintain the database. It also makes the database more flexible and adaptable to changing business needs.
  - Reduced Data Anomalies: Normalization helps in reducing the data anomalies, such as insertion, update, and deletion anomalies, that may arise due to redundant or dependent data. Data anomalies can lead to data inconsistency, data loss, or data corruption.
  - Enhanced Data Integrity: Normalization helps in enhancing the data integrity, by enforcing the constraints and relationships between the data. Data integrity ensures that the data is valid, accurate, and consistent throughout the database.
  - Optimized Performance: Normalization helps in optimizing the performance of the database, by reducing the size of the data, avoiding unnecessary joins, and facilitating the use of indexes and query optimization techniques.

## Normal Forms
- Normal forms are the rules or standards that define the level of normalization of a database schema. The higher the normal form, the more normalized the schema is.
- There are several normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF). Each normal form has a set of criteria or conditions that must be satisfied by the schema.
- The process of normalization involves applying the normal forms in a sequential order, starting from 1NF and moving up to the highest applicable normal form. Each normal form builds on the previous one, and removes a certain type of redundancy or dependency from the schema.
- The following is a brief overview of the normal forms and their criteria:

  - 1NF: A table is in 1NF if it contains only atomic values, i.e., each cell can hold only one value, and there are no repeating groups or arrays of values within a row or column.
  - 2NF: A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there are no partial dependencies.
  - 3NF: A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there are no transitive dependencies.
  - BCNF: A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there are no non-trivial functional dependencies that violate the key constraint.
  - 4NF: A table is in 4NF if it is in BCNF and has no multi-valued dependencies, i.e., there are no attributes that depend on a set of attributes rather than a single attribute.
  - 5NF: A table is in 5NF if it is in 4NF and has no join dependencies, i.e., there are no subsets of attributes that can be projected out and joined back without loss of information.

## References
: https://www.w3schools.in/DBMS/database-normalization/
[^