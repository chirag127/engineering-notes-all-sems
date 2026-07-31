### Creating and managing tables for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

1. **Creating Tables**: Tables can be created using the `CREATE TABLE` statement in both ORACLE and MYSQL. The basic syntax for creating a table is:
```
CREATE TABLE table_name
(column1 datatype,
column2 datatype,
column3 datatype,
...);
```
2. **Data Types**: Both ORACLE and MYSQL support a variety of data types, including numeric, character, date/time, and binary data types. Some common data types include `INT`, `VARCHAR`, `DATE`, and `BLOB`.

3. **Constraints**: Constraints can be added to table columns to enforce data integrity. Some common constraints include `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, and `CHECK`.

4. **Altering Tables**: The structure of a table can be modified after it has been created using the `ALTER TABLE` statement. This can be used to add, modify, or drop columns, as well as to add or drop constraints.

5. **Dropping Tables**: Tables can be removed from the database using the `DROP TABLE` statement. This will permanently delete the table and all data stored in it.

6. **Managing Data**: Data can be inserted into a table using the `INSERT` statement, updated using the `UPDATE` statement, and deleted using the `DELETE` statement. Data can also be selected and retrieved from a table using the `SELECT` statement.

7. **Indexes**: Indexes can be created on table columns to improve query performance. Indexes can be created using the `CREATE INDEX` statement, and can be dropped using the `DROP INDEX` statement.

8. **Views**: Views can be created to provide a virtual table based on the result of a `SELECT` statement. Views can be created using the `CREATE VIEW` statement, and can be dropped using the `DROP VIEW` statement.

9. **Transactions**: Transactions can be used to ensure data consistency and integrity. Transactions can be started using the `BEGIN TRANSACTION` statement, and can be committed using the `COMMIT` statement or rolled back using the `ROLLBACK` statement.

10. **Backup and Recovery**: It is important to regularly backup database data to protect against data loss. Both ORACLE and MYSQL provide tools for backing up and restoring data.