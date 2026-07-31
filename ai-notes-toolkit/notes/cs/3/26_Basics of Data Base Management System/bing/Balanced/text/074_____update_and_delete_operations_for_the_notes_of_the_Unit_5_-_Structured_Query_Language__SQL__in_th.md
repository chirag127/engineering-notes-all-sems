### Update and Delete Operations for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- SQL is a language that allows users to view and manage data in a relational database system.
- SQL has several commands that can manipulate data, such as INSERT, UPDATE, DELETE, SELECT and MERGE. These commands are known as Data Manipulation Language (DML) statements.
- The UPDATE command is used to modify the existing records in the database. It can be used with a WHERE clause to specify which records to update.
- The syntax of the UPDATE command is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- The DELETE command is used to delete the records in the database that are no longer required. It can also be used with a WHERE clause to specify which records to delete.
- The syntax of the DELETE command is:

```sql
DELETE FROM table_name
WHERE condition;
```

- Some SQL best practices for deleting and updating data are:
  - Always backup the data before performing any delete or update operations.
  - Use transactions to ensure the data integrity and consistency.
  - Use the WHERE clause carefully to avoid deleting or updating the wrong records.
  - Test the delete or update statements on a sample data set before applying them to the actual data.
  - Use the ROLLBACK command to undo the changes if something goes wrong.