## Unit 3 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into tables and columns that follow certain rules or normal forms.
- Normalization also simplifies the database design and makes it easier to query, update, and maintain the data.
- There are several levels of normalization, each with a specific goal and criteria. The most common levels are:
  - First normal form (1NF): Each table has a primary key and each column contains atomic values (i.e., values that cannot be further divided).
  - Second normal form (2NF): Each table is in 1NF and each non-key column depends on the whole primary key (i.e., there are no partial dependencies).
  - Third normal form (3NF): Each table is in 2NF and each non-key column depends only on the primary key (i.e., there are no transitive dependencies).
  - Boyce-Codd normal form (BCNF): Each table is in 3NF and every determinant (i.e., a set of columns that determines another column) is a candidate key (i.e., a minimal set of columns that uniquely identifies a row).
  - Fourth normal form (4NF): Each table is in BCNF and there are no multi-valued dependencies (i.e., situations where a column can have more than one value for a given primary key).
  - Fifth normal form (5NF): Each table is in 4NF and there are no join dependencies (i.e., situations where a table can be decomposed into two or more tables and then reconstructed by joining them on their primary keys).
- To normalize a database, one can follow these steps:
  - Identify the entities and attributes that need to be stored in the database and create a conceptual model (e.g., an entity-relationship diagram).
  - Convert the conceptual model into a logical model (e.g., a relational schema) and assign primary keys and foreign keys to the tables.
  - Apply the normalization rules to the logical model and check if it satisfies the desired level of normalization. If not, decompose the tables into smaller ones and repeat the process until the desired level is reached.
  - Convert the logical model into a physical model (e.g., a SQL script) and implement the database on the RDBMS.