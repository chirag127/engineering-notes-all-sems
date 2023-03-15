# Types of SQL Commands

SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases. SQL commands are divided into five broad categories based on their functionality:

- **Data Definition Language (DDL)**: These commands are used to create, modify, or delete the structure of database objects such as tables, views, indexes, etc. Some examples of DDL commands are:

  - `CREATE`: This command is used to create a new database object, such as a table, view, index, etc.
  - `ALTER`: This command is used to modify the structure or properties of an existing database object, such as adding, dropping, or renaming columns, constraints, etc.
  - `DROP`: This command is used to delete an existing database object, such as a table, view, index, etc.
  - `RENAME`: This command is used to change the name of an existing database object, such as a table, view, index, etc.
  - `TRUNCATE`: This command is used to delete all the data from a table, but not the table structure itself.

- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete, or retrieve data from database tables. Some examples of DML commands are:

  - `INSERT`: This command is used to insert new data into a table.
  - `UPDATE`: This command is used to modify the existing data in a table.
  - `DELETE`: This command is used to delete the existing data from a table.
  - `SELECT`: This command is used to retrieve data from one or more tables based on certain criteria.

- **Data Query Language (DQL)**: This is a subset of DML commands that are used to query data from database tables. The most common DQL command is `SELECT`, which can be used with various clauses, such as `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`, etc. to filter, aggregate, sort, or limit the data returned by the query.

- **Data Control Language (DCL)**: These commands are used to control the access and permissions of database users and roles. Some examples of DCL commands are:

  - `GRANT`: This command is used to grant privileges or permissions to a user or role to perform certain operations on database objects, such as `SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc.
  - `REVOKE`: This command is used to revoke or remove the privileges or permissions granted to a user or role on database objects.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in a database, which are a set of logical operations that are performed as a single unit. Some examples of TCL commands are:

  - `BEGIN`: This command is used to start a new transaction.
  - `COMMIT`: This command is used to end and save the changes made by a transaction.
  - `ROLLBACK`: This command is used to undo and discard the changes made by a transaction.
  - `SAVEPOINT`: This command is used to create a point in a transaction that can be used to rollback to in case of an error.