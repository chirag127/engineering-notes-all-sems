# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, establishing the relationships and constraints, and choosing the appropriate data models and storage formats.
- Database design aims to achieve the following objectives:
  - Accuracy: The database should accurately represent the real-world domain and the business rules of the application.
  - Efficiency: The database should allow fast and easy access, insertion, update, and deletion of data, while minimizing the storage space and processing overhead.
  - Security: The database should protect the data from unauthorized access, modification, or deletion, and ensure the integrity and consistency of the data.
  - Scalability: The database should be able to accommodate the growth and changes in the data volume and complexity, without compromising the performance or functionality.
  - Maintainability: The database should be easy to modify, debug, and enhance, without affecting the existing functionality or data quality.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity and organization of data.
- Normalization also helps to avoid the following problems that may arise from a poorly designed schema:
  - Anomalies: Inconsistencies or errors in the data that occur due to the duplication or omission of data in different tables.
  - Update anomalies: When a change in one table is not reflected in another table, leading to data inconsistency or loss.
  - Insertion anomalies: When a new record cannot be inserted into a table without violating some constraint or creating redundant data.
  - Deletion anomalies: When deleting a record from a table causes the loss of related data in another table.
- Normalization is based on the concept of functional dependency, which is a relationship between two sets of attributes, such that the value of one set determines the value of the other set.
- Normalization applies a series of rules or normal forms to a schema, each of which reduces the degree of redundancy and dependency in the schema.
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute has a single value for each record.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, or in other words, there are no transitive dependencies between non-key attributes.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, or in other words, there are no partial dependencies between candidate keys and non-key attributes.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies, or in other words, there are no non-key attributes that depend on a subset of a composite key.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, or in other words, it cannot be decomposed into smaller tables without losing information.