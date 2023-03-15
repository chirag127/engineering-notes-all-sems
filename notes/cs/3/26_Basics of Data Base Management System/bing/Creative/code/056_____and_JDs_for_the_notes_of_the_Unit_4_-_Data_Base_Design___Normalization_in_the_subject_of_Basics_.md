# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database design involves the following steps:
  - Identifying the purpose and scope of the database
  - Analyzing the data requirements and business rules
  - Creating an entity-relationship (ER) diagram or a data model
  - Converting the ER diagram or data model into a relational schema
  - Implementing the relational schema in a RDBMS
  - Testing and refining the database
- Database design aims to achieve the following goals:
  - Minimize data redundancy and inconsistency
  - Ensure data integrity and security
  - Facilitate data access and manipulation
  - Enhance database performance and scalability
  - Support future changes and enhancements

## Normalization
- Normalization is a database design technique, which is used to design a relational database table up to higher normal form.
- Normalization helps to reduce data redundancy and inconsistency, and improve data integrity and efficiency.
- Normalization involves the following steps:
  - Identifying the functional dependencies and candidate keys of a table
  - Applying the normalization rules or normal forms to decompose the table into smaller and simpler tables
  - Assigning appropriate primary keys and foreign keys to the tables
  - Checking the lossless join and dependency preservation properties of the decomposition
- Normalization rules or normal forms are based on the concept of functional dependency, which is a relationship between two sets of attributes in a table, such that the values of one set determine the values of the other set.
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it contains only atomic values and no repeating groups.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and it has no multi-valued dependencies.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and it has no join dependencies.
- Normalization is a progressive process, and a higher level of database normalization cannot be achieved unless the previous levels have been satisfied.
- Normalization is not always desirable or feasible, as it may introduce some drawbacks, such as:
  - Increased number of tables and joins, which may affect the performance and complexity of the database
  - Loss of some desirable dependencies or constraints, which may affect the data quality and consistency
  - Trade-off between normalization and denormalization, which may depend on the specific requirements and objectives of the database

: Database normalization - Wikipedia
: What is Normalization? - database.guide
: What is Database Normalization? How to Normalize a Database
: A Step-By-Step Guide to Normalization in DBMS With Examples - Database Star
: Database design basics - Microsoft Support