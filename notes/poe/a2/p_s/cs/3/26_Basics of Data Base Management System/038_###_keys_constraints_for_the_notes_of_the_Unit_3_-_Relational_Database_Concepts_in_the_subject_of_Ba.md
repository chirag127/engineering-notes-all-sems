 Here are the notes on ### keys constraints for the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System:

1. Keys: Keys are the attributes/columns of a table that uniquely identify each row in the table. They are used to establish and enforce relationships between data in tables. There are mainly two types of keys:

- Primary Key: A primary key is a column or set of columns that uniquely identifies each row in a table. It ensures that no duplicates exist in the key column(s), and it is used to link tables together. A table can only have one primary key.
- Foreign Key: A foreign key is a column or set of columns in a table that references the primary key of another table. It acts as a link between data in two tables, and ensures referential integrity between the tables.

2. Constraints: Constraints are rules applied on data in a table. They are used to limit the type of data that can be inserted into a column, and to enforce relationships between data. The main types of constraints are:

- NOT NULL: Prevents a column from having a NULL value
- UNIQUE: Ensures that all values in a column are different
- PRIMARY KEY: A combination of a NOT NULL and UNIQUE constraint. Uniquely identifies each row in a table
- FOREIGN KEY: Ensures that all values in a column exist in a column of another table (referential integrity)
- CHECK: Ensures that all values in a column satisfies a specific condition
- DEFAULT: Sets a default value for a column when no value is specified

Constraints can be specified when a table is created (table-level) or when a column is created (column-level). They are used to enforce data integrity in a database.

[Detailed diagrams, examples, advantages, disadvantages, applications, etc. can be added here if required.]