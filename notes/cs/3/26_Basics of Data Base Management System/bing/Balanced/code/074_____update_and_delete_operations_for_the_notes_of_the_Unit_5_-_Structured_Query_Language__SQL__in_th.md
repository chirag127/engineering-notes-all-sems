### Update and Delete Operations for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- SQL is a language that allows users to view and manage data in a relational database system.
- Data Manipulation Language (DML) is a subset of SQL that deals with inserting, updating, deleting, and selecting data from tables and views.
- The UPDATE command is used to modify the existing records in the database. It has the following syntax:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- The SET clause specifies which columns to update and what values to assign to them.
- The WHERE clause is optional and filters the records that match the condition. If the WHERE clause is omitted, all the records in the table will be updated.
- The UPDATE command can also use expressions, subqueries, and joins to update data from multiple tables or sources.
- The DELETE command is used to remove the records from the table that are no longer required. It has the following syntax:

```sql
DELETE FROM table_name
WHERE condition;
```

- The WHERE clause is optional and filters the records that match the condition. If the WHERE clause is omitted, all the records in the table will be deleted.
- The DELETE command can also use subqueries and joins to delete data from multiple tables or sources.
- Both the UPDATE and DELETE commands can use the TOP keyword to limit the number of rows affected by the operation. For example:

```sql
UPDATE TOP (10) table_name
SET column1 = value1
WHERE condition;

DELETE TOP (10) FROM table_name
WHERE condition;
```

- The above commands will update or delete only the first 10 rows that match the condition.
- Both the UPDATE and DELETE commands can use the OUTPUT clause to return the modified or deleted rows as a result set. For example:

```sql
UPDATE table_name
SET column1 = value1
OUTPUT inserted.column1, deleted.column1
WHERE condition;

DELETE FROM table_name
OUTPUT deleted.*
WHERE condition;
```

- The above commands will return the new and old values of column1 for the updated rows, and the entire deleted rows, respectively.
- Both the UPDATE and DELETE commands can be customized by using stored procedures, triggers, or user-defined functions to implement business logic or validation rules. For example, a trigger can be defined to audit the changes made by the UPDATE or DELETE commands, or a stored procedure can be used to perform complex calculations or validations before updating or deleting data.
- Both the UPDATE and DELETE commands should be used with caution, as they can cause data loss or inconsistency if not performed correctly. Some of the best practices for using these commands are:

  - Always use a WHERE clause to limit the scope of the operation, unless you want to affect all the rows in the table.
  - Always test the WHERE clause with a SELECT statement before executing the UPDATE or DELETE command, to verify that the correct rows are selected.
  - Always use transactions to ensure the atomicity and consistency of the operation, and to be able to roll back the changes in case of errors or exceptions.
  - Always use appropriate locking or isolation levels to prevent concurrency issues or data corruption, especially when updating or deleting data from multiple tables or sources.
  - Always backup the database or the table before performing the UPDATE or DELETE operation, to be able to restore the data in case of accidental or unwanted changes.