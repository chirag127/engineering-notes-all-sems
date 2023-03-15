# Unit 4 - Normalization

Normalization is a process of organizing the data in a database to reduce redundancy and improve data integrity.

Normalization also simplifies the database design so that it achieves the optimal structure composed of atomic elements (i.e. elements that cannot be broken down into smaller parts).

There are different levels of normalization, called normal forms, that a database can achieve. Each normal form has a set of rules or criteria that must be met.

The most common normal forms are:

- First Normal Form (1NF): Each table cell should contain a single value. Each record needs to be unique.
- Second Normal Form (2NF): The table should be in 1NF and all the columns in the table should depend on the primary key.
- Third Normal Form (3NF): The table should be in 2NF and no column should depend on any other column except the primary key.
- Boyce-Codd Normal Form (BCNF): The table should be in 3NF and every determinant (a column or a set of columns that determines another column) should be a candidate key (a column or a set of columns that can uniquely identify a record).
- Fourth Normal Form (4NF): The table should be in BCNF and there should be no multi-valued dependencies (a situation where a column or a set of columns depends on another column or a set of columns, and both are independent of the primary key).
- Fifth Normal Form (5NF): The table should be in 4NF and there should be no join dependencies (a situation where a table can be decomposed into two or more tables and then joined back without losing any information).

The benefits of normalization are:

- It eliminates data anomalies (inconsistencies or errors that arise when data is inserted, updated, or deleted).
- It reduces data redundancy (duplication of data that wastes storage space and increases the risk of data inconsistency).
- It improves data integrity (accuracy and consistency of data).
- It facilitates data access and manipulation (by simplifying the database structure and relationships).

The drawbacks of normalization are:

- It may increase the number of tables and joins (which can affect the performance and complexity of queries).
- It may reduce data efficiency (by requiring more disk space and memory to store the normalized data).
- It may not reflect the business logic or requirements (by imposing a rigid structure that may not suit the real-world scenarios).