## Unit 4 - Normalization

- Normalization is a process of organizing the data in a database to reduce redundancy and improve data integrity.
- Normalization also simplifies the database design so that it achieves the optimal structure composed of atomic elements (i.e. elements that cannot be broken down into smaller parts).
- There are different levels of normalization, called normal forms, that a database can achieve. Each normal form has a set of rules or criteria that must be met.
- The most common normal forms are:

  - First Normal Form (1NF): Each table has a primary key and each column contains atomic values, and there are no repeating groups of columns.
  - Second Normal Form (2NF): The table is in 1NF and all the columns depend on the primary key.
  - Third Normal Form (3NF): The table is in 2NF and all the columns depend only on the primary key and not on other columns.
  - Boyce-Codd Normal Form (BCNF): The table is in 3NF and every determinant is a candidate key.
  - Fourth Normal Form (4NF): The table is in BCNF and has no multi-valued dependencies.
  - Fifth Normal Form (5NF): The table is in 4NF and has no join dependencies.

- Normalization can be done by following a set of steps that help in decomposing the original table into well-structured tables. The steps are:

  - Identify all the candidate keys of the table.
  - Identify all the functional dependencies in the table.
  - Identify the highest normal form that the table satisfies.
  - If the table is not in the desired normal form, decompose the table into smaller tables that satisfy the dependency and the normal form.
  - Repeat the process for each smaller table until all the tables are in the desired normal form.