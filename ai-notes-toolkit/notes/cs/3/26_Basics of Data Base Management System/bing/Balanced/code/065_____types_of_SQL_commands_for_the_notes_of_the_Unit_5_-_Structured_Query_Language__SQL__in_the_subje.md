### Types of SQL Commands

SQL commands are instructions that are used to communicate with the database and perform various tasks. SQL commands can be classified into five main categories, based on their functionality:

- **Data Definition Language (DDL)**: These commands are used to create, modify, or delete the structure of the database objects, such as tables, views, indexes, etc. Some examples of DDL commands are:

  - `CREATE`: This command is used to create a new database object, such as a table, view, index, etc.
  - `ALTER`: This command is used to modify the structure or attributes of an existing database object, such as adding, dropping, or renaming columns, constraints, etc.
  - `DROP`: This command is used to delete an existing database object, such as a table, view, index, etc.
  - `RENAME`: This command is used to change the name of an existing database object, such as a table, view, index, etc.
  - `TRUNCATE`: This command is used to delete all the data from a table, but not the table structure.

- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete, or retrieve data from the database tables. Some examples of DML commands are:

  - `INSERT`: This command is used to insert new data into a table.
  - `UPDATE`: This command is used to modify the existing data in a table.
  - `DELETE`: This command is used to delete the existing data from a table.
  - `SELECT`: This command is used to query data from one or more tables, based on certain criteria.

- **Data Query Language (DQL)**: This is a subset of DML commands that are used to query data from the database tables. The main DQL command is:

  - `SELECT`: This command is used to query data from one or more tables, based on certain criteria. It can also be used to perform various operations on the data, such as sorting, filtering, grouping, aggregating, joining, etc.

- **Data Control Language (DCL)**: These commands are used to control the access and permissions of the database users and roles. Some examples of DCL commands are:

  - `GRANT`: This command is used to grant privileges or permissions to a user or role, such as the ability to select, insert, update, or delete data from a table, view, etc.
  - `REVOKE`: This command is used to revoke or remove the privileges or permissions that were previously granted to a user or role.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in the database, such as committing, rolling back, or saving the changes made by the DML commands. Some examples of TCL commands are:

  - `COMMIT`: This command is used to save the changes made by the DML commands in the database permanently.
  - `ROLLBACK`: This command is used to undo the changes made by the DML commands in the database and restore the previous state.
  - `SAVEPOINT`: This command is used to create a point in the transaction where the changes can be rolled back to, in case of any error or failure.