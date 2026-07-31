### Types of SQL Commands

SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases. SQL commands are divided into five broad categories based on their functionality:

- **Data Definition Language (DDL)**: These commands are used to create, modify, or delete the structure of database objects such as tables, views, indexes, etc. Some examples of DDL commands are:

  - `CREATE`: This command is used to create a new database object, such as a table, view, index, etc.
  - `ALTER`: This command is used to modify the structure or properties of an existing database object, such as adding or dropping columns, changing data types, renaming objects, etc.
  - `DROP`: This command is used to delete an existing database object, such as a table, view, index, etc.
  - `TRUNCATE`: This command is used to delete all the data from a table, but not the table itself.
  - `RENAME`: This command is used to rename an existing database object, such as a table, view, index, etc.

- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete, or retrieve data from database tables. Some examples of DML commands are:

  - `INSERT`: This command is used to insert new data into a table.
  - `UPDATE`: This command is used to modify the existing data in a table.
  - `DELETE`: This command is used to delete the existing data from a table.
  - `SELECT`: This command is used to query or retrieve data from one or more tables.

- **Data Control Language (DCL)**: These commands are used to grant or revoke permissions or access rights to database objects or users. Some examples of DCL commands are:

  - `GRANT`: This command is used to grant permissions or privileges to a user or a role to perform certain operations on database objects.
  - `REVOKE`: This command is used to revoke permissions or privileges from a user or a role to perform certain operations on database objects.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in a database, such as committing or rolling back the changes made by DML commands. Some examples of TCL commands are:

  - `COMMIT`: This command is used to save the changes made by DML commands to the database permanently.
  - `ROLLBACK`: This command is used to undo the changes made by DML commands to the database and restore the previous state.
  - `SAVEPOINT`: This command is used to create a point in a transaction where the changes can be rolled back to if needed.

- **Data Query Language (DQL)**: This is not a separate category of commands, but rather a subset of DML commands that are used to query or retrieve data from database tables. The most common DQL command is `SELECT`, which can be used with various clauses, operators, and functions to filter, sort, group, or aggregate the data. Some examples of DQL commands are:

  - `SELECT * FROM table_name`: This command is used to select all the columns and rows from a table.
  - `SELECT column1, column2 FROM table_name`: This command is used to select specific columns from a table.
  - `SELECT column1, column2 FROM table_name WHERE condition`: This command is used to select specific columns and rows that satisfy a condition from a table.
  - `SELECT column1, column2 FROM table_name ORDER BY column3`: This command is used to select specific columns and rows from a table and sort them by a column.
  - `SELECT column1, column2 FROM table_name GROUP BY column3`: This command is used to select specific columns and rows from a table and group them by a column.
  - `SELECT column1, column2 FROM table_name HAVING condition`: This command is used to select specific columns and rows from a table that satisfy a condition after grouping by a column.
  - `SELECT column1, column2 FROM table_name JOIN table2 ON condition`: This command is used to select specific columns and rows from two or more tables that are related by a condition.