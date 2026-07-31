# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, establishing the relationships and constraints, and choosing the appropriate data models and storage formats.
- Database design aims to achieve the following objectives:
  - Accuracy: The database should accurately represent the real-world domain and the business rules of the application.
  - Efficiency: The database should allow fast and easy access, retrieval, and modification of data, while minimizing the storage space and processing overhead.
  - Security: The database should protect the data from unauthorized access, modification, or deletion, and ensure the integrity and consistency of the data.
  - Scalability: The database should be able to accommodate the growth and changes in the data volume and complexity, without compromising the performance or functionality.
  - Maintainability: The database should be easy to update, modify, and extend, without affecting the existing functionality or data quality.

## Normalization
- Normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity and organization of data.
- Normalization helps in achieving the following benefits:
  - Improved Database Design: Normalization helps in improving the overall design of the database. By organizing the data in a structured and systematic way, normalization makes it easier to design and maintain the database. It also makes the database more flexible and adaptable to changing business needs.
  - Reduced Data Anomalies: Normalization helps in reducing the data anomalies, such as insertion, deletion, and update anomalies, that may arise due to the duplication and inconsistency of data. By eliminating the redundant and dependent data, normalization ensures that the data is stored only once and in one place, and that any changes to the data are reflected consistently throughout the database.
  - Enhanced Data Integrity: Normalization helps in enhancing the data integrity, by enforcing the constraints and rules on the data. By defining the primary keys, foreign keys, and other integrity constraints, normalization ensures that the data is valid, unique, and consistent, and that the relationships between the data are preserved and enforced.
  - Optimized Performance: Normalization helps in optimizing the performance of the database, by reducing the size and complexity of the data. By creating smaller and simpler tables, normalization reduces the storage space and the processing time required for the data operations. It also improves the query efficiency, by allowing the use of indexes and joins on the relevant tables and columns.

## Normal Forms
- Normal forms are the standards or rules that define the degree or level of normalization of a database schema.
- Normal forms are based on the concept of functional dependency, which is a relationship between two or more attributes, such that the value of one attribute determines the value of another attribute.
- Normal forms are applied sequentially, from the lowest to the highest, to a database schema, until it satisfies the desired level of normalization.
- The most common normal forms are:
  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values, i.e., each attribute has a single value for each record, and there are no repeating groups or arrays of values.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there are no partial dependencies or subsets of the primary key that determine the value of a non-key attribute.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there are no transitive dependencies or indirect relationships between the non-key attributes through another non-key attribute.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there are no non-trivial functional dependencies between two or more non-key attributes, or between a non-key attribute and a proper subset of a candidate key.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and there are no multi-valued dependencies, i.e., there are no attributes that have more than one independent value for a given record.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in