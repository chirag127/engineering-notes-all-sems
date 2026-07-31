# Second

## Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database normalization is a technique of database design that aims to reduce data redundancy and dependency by splitting a large table into smaller tables and defining relationships between them.
- Normalization helps to improve the quality, consistency, and performance of the database, as well as to make it more flexible and maintainable.
- Normalization is based on a set of rules or normal forms that define the criteria for a well-designed database. The most common normal forms are:

  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values, i.e., each cell can hold only one value, and there are no repeating groups of columns.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there are no partial dependencies.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, i.e., there are no transitive dependencies.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, i.e., there are no non-trivial functional dependencies that violate the key constraint.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies, i.e., there are no attributes that depend on a set of values rather than a single value.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, i.e., it cannot be decomposed into smaller tables without losing information.

- The process of normalization involves applying the normal forms to a table until it reaches the desired level of normalization. The steps are:

  - Identify the functional dependencies and candidate keys of the table.
  - Check if the table is in 1NF and eliminate any repeating groups or composite values.
  - Check if the table is in 2NF and eliminate any partial dependencies by creating new tables with the dependent attributes and referencing the primary key of the original table.
  - Check if the table is in 3NF and eliminate any transitive dependencies by creating new tables with the dependent attributes and referencing the primary key of the original table.
  - Check if the table is in BCNF and eliminate any non-trivial functional dependencies that violate the key constraint by creating new tables with the dependent attributes and referencing the determinant of the original table.
  - Check if the table is in 4NF and eliminate any multi-valued dependencies by creating new tables with the dependent attributes and referencing the primary key of the original table.
  - Check if the table is in 5NF and eliminate any join dependencies by creating new tables with the dependent attributes and referencing the primary keys of the original tables.

- The benefits of normalization are:

  - It reduces data duplication and storage space.
  - It prevents data anomalies and inconsistencies.
  - It facilitates data integrity and security.
  - It simplifies data manipulation and querying.
  - It enhances data scalability and adaptability.

- The drawbacks of normalization are:

  - It may increase the number of tables and joins, which can affect the performance and complexity of the database.
  - It may lose some information or business rules that are implicit in the original table.
  - It may not suit some applications or scenarios that require denormalized data for efficiency or analysis.

- The level of normalization depends on the requirements and objectives of the database system. There is no single optimal level of normalization for all databases. Some factors that influence the choice of normalization level are:

  - The size and nature of the data and the transactions.
  - The frequency and type of data updates and queries.
  - The trade-off between data quality and performance.
  - The availability and cost of resources and technology.