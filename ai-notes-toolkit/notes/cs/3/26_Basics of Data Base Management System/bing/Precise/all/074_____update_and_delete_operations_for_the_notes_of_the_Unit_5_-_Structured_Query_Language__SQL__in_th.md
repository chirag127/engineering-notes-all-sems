# Update and Delete Operations in SQL

Structured Query Language (SQL) is a standard language for managing and querying relational databases. In this section, we will discuss the `UPDATE` and `DELETE` operations in SQL.

## UPDATE
The `UPDATE` statement is used to modify existing records in a table. The basic syntax for the `UPDATE` statement is as follows:

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- `table_name`: The name of the table to update.
- `column1`, `column2`, ...: The columns to update.
- `value1`, `value2`, ...: The new values to set for the specified columns.
- `condition`: The condition that specifies which records to update.

It is important to include a `WHERE` clause in the `UPDATE` statement to specify which records to update. If the `WHERE` clause is omitted, all records in the table will be updated.

## DELETE
The `DELETE` statement is used to delete existing records from a table. The basic syntax for the `DELETE` statement is as follows:

```
DELETE FROM table_name
WHERE condition;
```

- `table_name`: The name of the table to delete from.
- `condition`: The condition that specifies which records to delete.

Like the `UPDATE` statement, it is important to include a `WHERE` clause in the `DELETE` statement to specify which records to delete. If the `WHERE` clause is omitted, all records in the table will be deleted.

These are the basics of the `UPDATE` and `DELETE` operations in SQL. It is important to use these statements carefully, as they can modify or delete data permanently from the database.