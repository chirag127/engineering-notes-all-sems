## Unit 4 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database normalization is a technique of database design that organizes data into tables and columns to reduce redundancy and improve data integrity.
- Normalization also simplifies the database design by creating atomic elements, i.e., elements that cannot be broken down into smaller parts.
- Normalization is based on a series of normal forms, which are rules that define the level of normalization of a database. The higher the normal form, the more normalized the database is.
- The most common normal forms are:

  - First normal form (1NF): A table is in 1NF if it contains only atomic values and no repeating groups of data.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies.

- The benefits of normalization are:

  - It eliminates data anomalies, such as insertion, deletion, and update anomalies, that can cause data inconsistency and corruption.
  - It reduces data redundancy and storage space, which improves performance and efficiency.
  - It enhances data integrity and security, which ensures data accuracy and reliability.
  - It facilitates data manipulation and querying, which makes it easier to access and analyze data.

- The drawbacks of normalization are:

  - It can increase the number of tables and joins, which can complicate the database design and query processing.
  - It can reduce data availability and performance, especially for complex and large databases that require frequent transactions and queries.
  - It can require more effort and expertise to design and maintain a normalized database, which can increase the cost and time of development.

- The process of normalization involves the following steps:

  - Identify the entities and attributes of the database and define the functional dependencies among them.
  - Create a preliminary design by representing the entities and attributes as tables and columns, and assign a primary key to each table.
  - Apply the normal forms to the preliminary design and check for violations. If any violation is found, decompose the table into smaller tables that satisfy the normal form.
  - Repeat the process until the highest level of normalization is achieved or desired.
  - Review and refine the final design and test it for functionality and performance.