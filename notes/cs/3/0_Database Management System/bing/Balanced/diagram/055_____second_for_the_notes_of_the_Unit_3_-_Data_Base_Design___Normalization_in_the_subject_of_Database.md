### Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database system.
- Database normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into tables and columns that follow certain rules or normal forms.
- Normalization also simplifies the database design and makes it easier to query, update, and maintain the data.
- There are several levels of normalization, each with a specific goal and criteria. The most common levels are:

  - First normal form (1NF): A table is in 1NF if it has no repeating groups or arrays of data, and every column has a single value for each row. This means that each attribute or column should be atomic, or indivisible.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key column depends on the whole primary key. This means that there should be no partial dependencies, or columns that depend on only a part of the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key column depends only on the primary key. This means that there should be no transitive dependencies, or columns that depend on other non-key columns.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key. A determinant is a column or a set of columns that determines the value of another column. A candidate key is a column or a set of columns that can uniquely identify a row in a table.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies. A multi-valued dependency occurs when a column or a set of columns can have more than one value for a given primary key value.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies. A join dependency occurs when a table can be decomposed into two or more tables and then reconstructed by joining them on their primary keys.

- To normalize a database, one can follow these steps:

  - Identify the entities and attributes that need to be stored in the database.
  - Create a table for each entity and assign a primary key to each table.
  - Identify the relationships and cardinalities among the entities and add foreign keys to the tables as needed.
  - Check if the tables are in 1NF and eliminate any repeating groups or arrays of data by creating new tables or columns.
  - Check if the tables are in 2NF and eliminate any partial dependencies by creating new tables or moving columns to existing tables.
  - Check if the tables are in 3NF and eliminate any transitive dependencies by creating new tables or moving columns to existing tables.
  - Check if the tables are in BCNF and eliminate any determinants that are not candidate keys by creating new tables or moving columns to existing tables.
  - Check if the tables are in 4NF and eliminate any multi-valued dependencies by creating new tables or moving columns to existing tables.
  - Check if the tables are in 5NF and eliminate any join dependencies by creating new tables or moving columns to existing tables.

- Here is an example of a database that stores information about students, courses, and grades. The database is normalized from 1NF to 3NF.

  - Unnormalized table:

    | Student ID | Student Name | Course ID | Course Name | Grade |
    |------------|--------------|-----------|-------------|-------|
    | 101        | Alice        | C1, C2    | Math, CS    | A, B  |
    | 102        | Bob          | C2, C3    | CS, English | B, C  |
    | 103        | Charlie      | C1, C3    | Math, English | C, A |

  - 1NF table:

    | Student ID | Student Name | Course ID | Course Name | Grade |
    |------------|--------------|-----------|-------------|-------|
    | 101        | Alice        | C1        | Math        | A     |
    | 101        | Alice        | C2        | CS          | B     |
    | 102        | Bob          | C2        | CS          | B     |
    | 102        | Bob          | C3        | English     |