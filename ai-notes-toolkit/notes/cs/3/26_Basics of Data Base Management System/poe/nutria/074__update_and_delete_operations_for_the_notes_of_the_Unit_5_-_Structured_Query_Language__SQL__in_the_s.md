
### Update and Delete Operations for Unit 5 - Structured Query Language (SQL)

1. Update Operation: The update operation is used to modify existing data in a database. It can be used to change the values of one or more columns in a table. It can also be used to add new rows or delete existing rows.

2. Delete Operation: The delete operation is used to remove data from a database. It can be used to delete one or more rows from a table. It can also be used to delete entire tables or columns.

3. SQL Statements: SQL statements are used to perform update and delete operations. The syntax for update and delete statements is similar. The syntax for an update statement is as follows:

```
UPDATE table_name
SET column_name1 = new_value1, 
    column_name2 = new_value2, 
    ...
WHERE condition;
```

The syntax for a delete statement is as follows:

```
DELETE FROM table_name
WHERE condition;
```

4. Limiting Update and Delete Operations: It is important to limit update and delete operations to only the necessary rows or columns. This can be done by using the WHERE clause to specify the conditions for the operation.