### Types of SQL Commands

SQL (Structured Query Language) is a standard language for manipulating and querying data in relational databases. SQL commands can be classified into four main categories:

- **Data Definition Language (DDL)**: These commands are used to create, modify, or delete the structure of database objects, such as tables, views, indexes, etc. Some examples of DDL commands are:

  - CREATE: This command is used to create a new database object, such as a table, view, index, etc.
  - ALTER: This command is used to modify the structure or properties of an existing database object, such as adding, deleting, or renaming columns, constraints, etc.
  - DROP: This command is used to delete an existing database object, such as a table, view, index, etc.
  - RENAME: This command is used to change the name of an existing database object, such as a table, view, index, etc.
  - TRUNCATE: This command is used to delete all the data from a table, but not the table structure itself.

- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete, or retrieve data from database tables. Some examples of DML commands are:

  - INSERT: This command is used to insert one or more rows of data into a table.
  - UPDATE: This command is used to modify one or more rows of data in a table.
  - DELETE: This command is used to delete one or more rows of data from a table.
  - SELECT: This command is used to retrieve data from one or more tables, based on certain criteria or conditions.

- **Data Control Language (DCL)**: These commands are used to control the access and permissions of users and roles on database objects, such as granting or revoking privileges, creating or dropping users, etc. Some examples of DCL commands are:

  - GRANT: This command is used to grant one or more privileges to a user or a role on a database object, such as SELECT, INSERT, UPDATE, DELETE, etc.
  - REVOKE: This command is used to revoke one or more privileges from a user or a role on a database object, such as SELECT, INSERT, UPDATE, DELETE, etc.
  - CREATE USER: This command is used to create a new user in the database, with a username and a password.
  - DROP USER: This command is used to delete an existing user from the database, along with their privileges and objects.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in the database, such as committing or rolling back the changes made by DML commands, setting the isolation level, etc. Some examples of TCL commands are:

  - COMMIT: This command is used to save the changes made by DML commands in the database permanently.
  - ROLLBACK: This command is used to undo the changes made by DML commands in the database, and restore the previous state.
  - SAVEPOINT: This command is used to create a point in the transaction, where the changes can be rolled back to, without affecting the entire transaction.
  - SET TRANSACTION: This command is used to set the isolation level of the transaction, which determines how the transaction is affected by other concurrent transactions. The isolation levels are: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, and SERIALIZABLE.