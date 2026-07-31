# Creating and managing tables for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- A table is a collection of related data organized in rows and columns in a database.
- To create a table in Oracle SQL, you use the `CREATE TABLE` statement, followed by the table name and the column definitions .
- The basic syntax of the `CREATE TABLE` statement is:

```sql
CREATE TABLE schema_name.table_name (
  column_1 data_type column_constraint,
  column_2 data_type column_constraint,
  ...
  table_constraint
);
```

- The `schema_name` is optional and specifies the schema where the table belongs. If you omit it, the table will be created in your own schema.
- The `table_name` is the name of the table that you want to create. It must be unique within the schema.
- The `column_1`, `column_2`, etc. are the names of the columns in the table. Each column must have a data type and an optional column constraint.
- The `data_type` specifies the type of data that the column can store, such as `NUMBER`, `VARCHAR2`, `DATE`, etc.
- The `column_constraint` specifies the rules that the column values must follow, such as `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, etc.
- The `table_constraint` specifies the rules that the table as a whole must follow, such as `PRIMARY KEY`, `UNIQUE`, `FOREIGN KEY`, `CHECK`, etc.

- To manage tables in Oracle SQL, you can use various commands, such as:
  - `ALTER TABLE` to modify the structure or properties of an existing table, such as adding, dropping, renaming, or modifying columns, constraints, indexes, partitions, etc.
  - `DROP TABLE` to delete an existing table and its data from the database.
  - `TRUNCATE TABLE` to remove all the data from an existing table without deleting the table itself.
  - `RENAME TABLE` to change the name of an existing table.
  - `COMMENT ON TABLE` to add or modify a comment on an existing table or its columns.
  - `ANALYZE TABLE` to collect statistics on an existing table and its indexes for the optimizer.
  - `LOCK TABLE` to prevent other users from modifying an existing table or its data while you perform a transaction.
  - `GRANT` and `REVOKE` to grant or revoke privileges on an existing table to other users or roles.

- To view the information about the tables in Oracle SQL, you can use various commands, such as:
  - `DESCRIBE` to display the column names, data types, and constraints of an existing table.
  - `SELECT` to query the data from an existing table or multiple tables using various clauses, such as `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `JOIN`, etc.
  - `INSERT` to add new rows of data to an existing table.
  - `UPDATE` to modify the existing rows of data in an existing table.
  - `DELETE` to remove the existing rows of data from an existing table.
  - `MERGE` to insert, update, or delete rows of data in an existing table based on the data from another table or subquery.
  - `EXPLAIN PLAN` to display the execution plan of a `SELECT` statement on an existing table or tables.

- To create and manage tables in Oracle SQL using a graphical user interface, you can use various tools, such as:
  - Oracle SQL Developer, which is a free and integrated development environment for Oracle Database.
  - Oracle Application Express (APEX), which is a low-code development platform for building web applications on Oracle Database.
  - Oracle SQL*Plus, which is a command-line tool for interacting with Oracle Database.