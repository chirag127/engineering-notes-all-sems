### Data Definition Language

Data Definition Language (DDL) is a subset of SQL (Structured Query Language) that is used to define and manage the structure of a database. It includes commands for creating, altering, and deleting database objects such as tables, views, indexes, and stored procedures.

Some common DDL commands include:

- `CREATE`: This command is used to create a new database object, such as a table or view. For example, the command `CREATE TABLE Students (ID INT, Name VARCHAR(255))` creates a new table named `Students` with two columns: `ID` and `Name`.

- `ALTER`: This command is used to modify the structure of an existing database object. For example, the command `ALTER TABLE Students ADD COLUMN Age INT` adds a new column named `Age` to the `Students` table.

- `DROP`: This command is used to delete a database object. For example, the command `DROP TABLE Students` deletes the `Students` table from the database.

- `TRUNCATE`: This command is used to delete all data from a table, but it does not delete the table itself. For example, the command `TRUNCATE TABLE Students` deletes all data from the `Students` table, but the table itself remains in the database.

It is important to note that DDL commands are used to manage the structure of the database, not the data itself. Data manipulation is done using a different subset of SQL called Data Manipulation Language (DML).