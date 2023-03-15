# Types of SQL Commands

SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases. SQL commands are divided into five broad categories based on their functionality:

- **DDL (Data Definition Language)**: These commands are used to create, modify, or delete the structure of database objects such as tables, views, indexes, etc. Some examples of DDL commands are:

  - CREATE: This command is used to create a new database object, such as a table, view, index, etc.
  - ALTER: This command is used to modify the structure or properties of an existing database object, such as adding, dropping, or renaming columns, constraints, etc.
  - DROP: This command is used to delete an existing database object, such as a table, view, index, etc.
  - TRUNCATE: This command is used to delete all the data from a table, but not the table itself.
  - RENAME: This command is used to change the name of a database object, such as a table, view, index, etc.

- **DML (Data Manipulation Language)**: These commands are used to insert, update, delete, or retrieve data from database tables. Some examples of DML commands are:

  - INSERT: This command is used to insert one or more rows of data into a table.
  - UPDATE: This command is used to modify the data of one or more rows in a table.
  - DELETE: This command is used to delete one or more rows of data from a table.
  - SELECT: This command is used to query data from one or more tables, based on certain criteria.

- **DCL (Data Control Language)**: These commands are used to grant or revoke permissions or access rights to database objects, such as tables, views, procedures, etc. Some examples of DCL commands are:

  - GRANT: This command is used to grant a specific privilege or role to a user or a group of users, such as SELECT, INSERT, UPDATE, DELETE, etc.
  - REVOKE: This command is used to revoke a specific privilege or role from a user or a group of users, such as SELECT, INSERT, UPDATE, DELETE, etc.

- **TCL (Transaction Control Language)**: These commands are used to manage the transactions in a database, such as committing, rolling back, or saving the changes made by a transaction. Some examples of TCL commands are:

  - COMMIT: This command is used to save the changes made by a transaction to the database permanently.
  - ROLLBACK: This command is used to undo the changes made by a transaction and restore the database to its previous state.
  - SAVEPOINT: This command is used to create a point in a transaction where the changes can be rolled back to, without affecting the entire transaction.

- **DQL (Data Query Language)**: This is not a separate category of SQL commands, but rather a subset of DML commands that are used to query data from the database. The most common DQL command is SELECT, which can be used with various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, LIMIT, etc. to filter, aggregate, sort, or limit the data returned by the query.