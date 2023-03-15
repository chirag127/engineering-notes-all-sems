# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accuracy: The data stored in the database should reflect the real-world facts and events as accurately as possible.
  - Efficiency: The database should allow fast and easy access, retrieval, and modification of data, while minimizing the storage space and processing time.
  - Security: The database should protect the data from unauthorized access, modification, or deletion, and ensure the integrity and consistency of the data.
  - Flexibility: The database should be able to accommodate changing data requirements and business needs, and support new functionalities and features.

## Normalization
- Normalization is a database schema design technique that reduces data redundancy and dependency by splitting a large table into smaller tables and defining relationships between them.
- Normalization helps to improve the database design by:
  - Eliminating data anomalies: Data anomalies are inconsistencies or errors that occur when data is inserted, updated, or deleted in a database. Normalization prevents data anomalies by ensuring that each piece of data is stored only once and in one place.
  - Reducing data duplication: Data duplication is the storage of the same data in multiple places, which wastes storage space and increases the risk of data inconsistency. Normalization reduces data duplication by separating the data into different tables based on their logical categories and dependencies.
  - Enhancing data integrity: Data integrity is the quality and reliability of the data in a database. Normalization enhances data integrity by enforcing the rules and constraints that govern the data and their relationships, such as primary keys, foreign keys, and referential integrity.
  - Simplifying data maintenance: Data maintenance is the process of updating, modifying, or deleting data in a database. Normalization simplifies data maintenance by reducing the number of places where data changes need to be made, and by making the data structure more understandable and manageable.

## Normal Forms
- Normal forms are the standards or rules that define the level of normalization of a database schema. There are several normal forms, each with a specific criterion that must be satisfied to achieve that level of normalization. The most common normal forms are:
  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values, that is, values that cannot be further divided into smaller parts. This means that each column should store only one value of a single data type, and there should be no repeating groups or arrays of values in a table.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, that is, the value of a non-key attribute is determined by the value of the primary key and nothing else. This means that there should be no partial dependencies or subsets of the primary key that can determine the value of a non-key attribute.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, that is, the value of a non-key attribute is determined by the value of the primary key and not by the value of any other non-key attribute. This means that there should be no transitive dependencies or indirect relationships between the non-key attributes.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, that is, every attribute or set of attributes that can uniquely identify a row in a table is a potential primary key. This means that there should be no non-trivial functional dependencies or dependencies that do not involve a candidate key.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies, that is, dependencies where a single attribute or set of attributes can have more than one value for a given primary key. This means that there should be no repeating groups or arrays of values in a table.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, that is, dependencies where a table can be decomposed into two or more tables and then reconstructed by joining them on their primary keys. This means that there should be no