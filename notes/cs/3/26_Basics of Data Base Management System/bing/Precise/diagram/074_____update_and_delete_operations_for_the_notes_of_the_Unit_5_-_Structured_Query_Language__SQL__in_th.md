### Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

#### Update and Delete Operations

- The `UPDATE` statement is used to modify existing records in a table.
- The `DELETE` statement is used to delete existing records from a table.
- The `WHERE` clause is used to specify which records to update or delete.
- If the `WHERE` clause is not specified, all records in the table will be updated or deleted.
- The `SET` keyword is used to specify the new values for the columns to be updated.
- The `UPDATE` statement can be used to update one or more columns at a time.
- The `DELETE` statement can be used to delete one or more rows at a time.
- It is important to be cautious when using the `UPDATE` and `DELETE` statements, as they can permanently modify or delete data in the database.

Example of an `UPDATE` statement:
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

Example of a `DELETE` statement:
```
DELETE FROM table_name
WHERE condition;
```