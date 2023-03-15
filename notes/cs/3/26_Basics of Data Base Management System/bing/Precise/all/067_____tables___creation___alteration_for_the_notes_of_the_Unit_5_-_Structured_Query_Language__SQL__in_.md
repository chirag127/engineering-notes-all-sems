# Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

### Tables – Creation & Alteration

- Tables are the basic structure in a relational database management system (RDBMS) where data is stored in rows and columns.
- The `CREATE TABLE` statement is used to create a new table in a database.
- The syntax for creating a table is: `CREATE TABLE table_name (column1 datatype, column2 datatype, column3 datatype, ...);`
- The `ALTER TABLE` statement is used to add, modify, or delete columns in an existing table, as well as to add and drop various constraints on an existing table.
- The syntax for adding a column to a table is: `ALTER TABLE table_name ADD column_name datatype;`
- The syntax for modifying a column in a table is: `ALTER TABLE table_name MODIFY column_name datatype;`
- The syntax for deleting a column from a table is: `ALTER TABLE table_name DROP COLUMN column_name;`
- Constraints such as `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, and `CHECK` can also be added or dropped using the `ALTER TABLE` statement.