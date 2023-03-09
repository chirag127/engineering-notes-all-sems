### Normal Forms for the Notes of the Unit 3 - Database Design & Normalization in the Subject of Database Management System

Normalization is an important concept in database design that helps reduce data redundancy and improve data integrity. It involves breaking down a larger table into smaller tables to reduce data redundancy and improve data consistency. Normalization is achieved through a series of normal forms, which are guidelines for designing a database schema that is well-structured and efficient.

#### First Normal Form (1NF)

- Each table cell should contain a single value.
- Each column should have a unique name.
- The order of the columns should not matter.

#### Second Normal Form (2NF)

- The table should be in 1NF.
- All columns in the table should depend on the primary key.
- If a column does not depend on the primary key, it should be moved to a new table.

#### Third Normal Form (3NF)

- The table should be in 2NF.
- There should be no transitive dependencies.
- Transitive dependencies occur when a non-key column depends on another non-key column that is not part of the primary key.

#### Boyce-Codd Normal Form (BCNF)

- The table should be in 3NF.
- Every determinant should be a candidate key.
- Determinants are the columns that determine the values of other columns.

#### Fourth Normal Form (4NF)

- The table should be in BCNF.
- There should be no multi-valued dependencies.
- Multi-valued dependencies occur when a single value in one column determines multiple values in another column.

#### Fifth Normal Form (5NF)

- The table should be in 4NF.
- There should be no join dependencies.
- Join dependencies occur when two or more tables can be joined in more than one way.

Normalization helps to ensure that a database is efficient and scalable. By reducing data redundancy and improving data consistency, it becomes easier to maintain and update the database. However, there are some disadvantages to normalization, such as increased complexity and a potential loss of performance when querying the database.

Overall, understanding the different normal forms is essential for designing a well-structured and efficient database schema. By following these guidelines, it is possible to create a database that is both easy to use and maintain.