### Data Definition Language

Data Definition Language (DDL) is a subset of SQL (Structured Query Language) used to define and manage the structure of a database. It includes commands to create, alter, and delete database objects such as tables, views, indexes, and stored procedures.

Some common DDL commands include:

- `CREATE`: used to create a new database object, such as a table or view.
- `ALTER`: used to modify the structure of an existing database object.
- `DROP`: used to delete a database object.
- `TRUNCATE`: used to remove all data from a table, but not the table itself.

DDL commands are used to define the structure of the database and its objects, and do not directly manipulate the data stored within those objects. That is the role of Data Manipulation Language (DML) commands, such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

It is important to note that DDL commands are typically irreversible, meaning that once a command is executed, it cannot be undone. For this reason, it is important to carefully plan and review DDL commands before executing them.