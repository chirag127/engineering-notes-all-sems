# Types of SQL Commands

SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases. SQL commands are instructions that can be used to perform various operations on the data, such as creating, modifying, querying, or controlling the database.

SQL commands are divided into five broad categories, based on their functionality:

- **Data Definition Language (DDL)**: These commands are used to define the structure and schema of the database, such as creating, altering, or dropping tables, views, indexes, or constraints. Some examples of DDL commands are:

  - CREATE: This command is used to create a new table, view, index, or database in the database server.
  - ALTER: This command is used to modify the structure or schema of an existing table, view, index, or database in the database server.
  - DROP: This command is used to delete an existing table, view, index, or database from the database server.
  - RENAME: This command is used to change the name of an existing table, view, index, or database in the database server.
  - TRUNCATE: This command is used to remove all the data from an existing table, but not the table structure or schema.

- **Data Manipulation Language (DML)**: These commands are used to manipulate the data stored in the database, such as inserting, updating, deleting, or merging data. Some examples of DML commands are:

  - INSERT: This command is used to insert new data into a table in the database server.
  - UPDATE: This command is used to modify the existing data in a table in the database server.
  - DELETE: This command is used to remove the existing data from a table in the database server.
  - MERGE: This command is used to combine the data from two or more tables into one table in the database server.

- **Data Query Language (DQL)**: These commands are used to query or retrieve the data from the database, such as selecting, filtering, sorting, or grouping data. Some examples of DQL commands are:

  - SELECT: This command is used to select or extract data from one or more tables or views in the database server.
  - WHERE: This command is used to filter the data based on some conditions or criteria in the database server.
  - ORDER BY: This command is used to sort the data in ascending or descending order based on some columns or expressions in the database server.
  - GROUP BY: This command is used to group the data based on some columns or expressions and apply some aggregate functions on them in the database server.
  - HAVING: This command is used to filter the data after grouping them based on some conditions or criteria in the database server.

- **Data Control Language (DCL)**: These commands are used to control the access and permissions of the data in the database, such as granting, revoking, or denying privileges or roles to users or groups. Some examples of DCL commands are:

  - GRANT: This command is used to grant some privileges or roles to a user or a group in the database server.
  - REVOKE: This command is used to revoke some privileges or roles from a user or a group in the database server.
  - DENY: This command is used to deny some privileges or roles to a user or a group in the database server.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in the database, such as committing, rolling back, or saving the changes made by the transactions. Some examples of TCL commands are:

  - COMMIT: This command is used to save the changes made by a transaction to the database server.
  - ROLLBACK: This command is used to undo the changes made by a transaction to the database server.
  - SAVEPOINT: This command is used to create a point in the transaction where the changes can be rolled back to in the database server.