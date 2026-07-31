# Unit 3 - Relational Database Concepts: Key Constraints

- **Key constraints** are used to ensure the integrity and consistency of data in a relational database.
- A **key** is a column or a set of columns in a table that uniquely identifies a row in the table.
- There are several types of key constraints in a relational database, including:
  - **Primary key**: A primary key is a column or a set of columns that uniquely identifies a row in a table. A table can have only one primary key.
  - **Foreign key**: A foreign key is a column or a set of columns in a table that refers to the primary key of another table. The table containing the foreign key is called the referencing table, and the table containing the primary key is called the referenced table.
  - **Unique key**: A unique key is a column or a set of columns that uniquely identifies a row in a table. A table can have multiple unique keys.
  - **Candidate key**: A candidate key is a column or a set of columns that can uniquely identify a row in a table. A table can have multiple candidate keys, one of which is chosen as the primary key.
- Key constraints are used to enforce referential integrity, which ensures that the relationships between tables in a database are maintained.
- Key constraints can be enforced through the use of triggers, stored procedures, or declarative constraints.
- Violating a key constraint results in an error and the transaction is rolled back.