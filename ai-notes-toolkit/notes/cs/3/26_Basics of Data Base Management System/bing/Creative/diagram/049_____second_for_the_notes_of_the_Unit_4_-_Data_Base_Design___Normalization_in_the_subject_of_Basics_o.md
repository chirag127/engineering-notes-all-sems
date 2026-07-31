### Second

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database system.
- Database normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into tables and columns that follow certain rules or normal forms.
- Normalization also simplifies the database design and makes it easier to maintain and query.
- There are several levels of normalization, each with a specific goal and criteria. The most common levels are:

  - First normal form (1NF): Eliminate repeating groups or arrays by creating separate tables for each set of related data and identifying each set with a primary key.
  - Second normal form (2NF): Eliminate partial dependencies by ensuring that every non-key attribute depends on the whole primary key and not on a subset of it.
  - Third normal form (3NF): Eliminate transitive dependencies by ensuring that every non-key attribute depends only on the primary key and not on any other non-key attribute.
  - Boyce-Codd normal form (BCNF): Eliminate anomalies caused by functional dependencies that violate 3NF by ensuring that every determinant is a candidate key.
  - Fourth normal form (4NF): Eliminate multivalued dependencies by ensuring that no table contains two or more independent and multivalued facts about an entity.
  - Fifth normal form (5NF): Eliminate join dependencies by ensuring that every join dependency is implied by the candidate keys of the table.

- Normalization is a progressive process, and a higher level of normalization cannot be achieved unless the previous levels have been satisfied.
- Normalization has some advantages and disadvantages, such as:

  - Advantages: It reduces data duplication, improves data consistency, avoids update anomalies, facilitates data retrieval, and enhances data security.
  - Disadvantages: It increases the number of tables and joins, which may affect performance and complexity. It may also result in data loss or redundancy if not done properly.