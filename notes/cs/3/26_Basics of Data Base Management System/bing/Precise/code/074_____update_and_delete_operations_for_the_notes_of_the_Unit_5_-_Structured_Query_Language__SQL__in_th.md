### Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System: Update and Delete Operations

- The `UPDATE` statement is used to modify existing records in a table.
- The `DELETE` statement is used to delete existing records from a table.
- The `WHERE` clause is used in both `UPDATE` and `DELETE` statements to specify which records to modify or delete.
- The `SET` keyword is used in the `UPDATE` statement to specify the new values for the columns being updated.
- The `UPDATE` statement can be used to update one or more columns at a time.
- The `DELETE` statement can be used to delete one or more rows at a time.
- It is important to use the `WHERE` clause carefully in `UPDATE` and `DELETE` statements to avoid accidentally modifying or deleting the wrong records.
- It is recommended to use the `SELECT` statement first to verify the records that will be affected by the `UPDATE` or `DELETE` statement before executing it.

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