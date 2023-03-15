## Unit 4 - Normalization

- Normalization is a process of organizing the data in a database to reduce redundancy and improve data integrity.
- Normalization also simplifies the database design so that it achieves the optimal structure composed of atomic elements (i.e. elements that cannot be broken down into smaller parts).
- There are different levels of normalization, called normal forms, that a database can conform to. Each normal form has a set of rules or criteria that must be met.
- The most common normal forms are:

  - First Normal Form (1NF): Each table has a primary key and each column contains atomic values, and there are no repeating groups of columns.
  - Second Normal Form (2NF): The table is in 1NF and all the columns depend on the primary key.
  - Third Normal Form (3NF): The table is in 2NF and all the columns are directly dependent on the primary key and not on other columns.
  - Boyce-Codd Normal Form (BCNF): The table is in 3NF and every determinant is a candidate key.
  - Fourth Normal Form (4NF): The table is in BCNF and has no multi-valued dependencies.
  - Fifth Normal Form (5NF): The table is in 4NF and has no join dependencies.

- Normalization helps to eliminate anomalies in the data, such as insertion, deletion, and update anomalies.
- Normalization can also improve query performance, as it reduces the size of the tables and the number of joins required.
- However, normalization can also have some drawbacks, such as increased complexity, reduced performance for some types of queries, and possible loss of data semantics.