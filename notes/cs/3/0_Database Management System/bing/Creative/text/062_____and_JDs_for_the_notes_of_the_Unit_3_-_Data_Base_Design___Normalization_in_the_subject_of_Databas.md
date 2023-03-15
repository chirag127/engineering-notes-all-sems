# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database design involves identifying the entities, attributes, and relationships that represent the information and business rules of a domain.
- Database design also involves choosing appropriate data types, constraints, indexes, and other properties for the tables and columns.
- Database design aims to achieve the following objectives:
  - Reduce data redundancy and inconsistency by avoiding duplication and conflicts.
  - Ensure data integrity and accuracy by enforcing rules and constraints on the data.
  - Enhance data security and privacy by restricting access and manipulation of the data.
  - Improve data performance and scalability by optimizing the storage and retrieval of the data.
  - Facilitate data maintenance and evolution by allowing changes and updates to the data structure.

## Database Normalization
- Database normalization is a technique of database design that organizes the data into tables and columns that are related and independent of each other.
- Database normalization reduces data redundancy and inconsistency by eliminating repeating groups, partial dependencies, and transitive dependencies among the data elements.
- Database normalization also simplifies the database design by ensuring that each table has a single purpose and a clear definition of its primary key and foreign keys.
- Database normalization is based on the concept of normal forms, which are rules and criteria that define the level of normalization of a database.
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it contains only atomic values (i.e., values that cannot be further divided) and has no repeating groups (i.e., columns that store multiple values of the same type).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key column depends on the whole primary key (i.e., there are no partial dependencies).
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key column depends only on the primary key (i.e., there are no transitive dependencies).
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant (i.e., a column or a set of columns that uniquely determines another column) is a candidate key (i.e., a minimal set of columns that can uniquely identify a row).
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies (i.e., dependencies among two or more columns that are not caused by the primary key).
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies (i.e., dependencies that require joining two or more tables to represent the data).
- Database normalization has the following benefits:
  - It reduces data anomalies (i.e., errors or inconsistencies that occur when inserting, updating, or deleting data) by ensuring that each piece of data is stored in one place and is updated consistently.
  - It improves data quality and reliability by enforcing data integrity and accuracy through constraints and rules.
  - It increases data efficiency and flexibility by minimizing the storage space and maximizing the query performance of the data.
  - It facilitates data evolution and maintenance by allowing changes and updates to the data structure without affecting the existing data and applications.