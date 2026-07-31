### Update and Delete Operations

#### Update Operation
- The `UPDATE` statement is used to modify the existing records in a table.
- The `SET` clause specifies the column to be updated and the new value to be set.
- The `WHERE` clause specifies which record or records should be updated. If the `WHERE` clause is not specified, all records in the table will be updated.
- Syntax:
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

#### Delete Operation
- The `DELETE` statement is used to delete existing records in a table.
- The `WHERE` clause specifies which record or records should be deleted. If the `WHERE` clause is not specified, all records in the table will be deleted.
- Syntax:
```
DELETE FROM table_name WHERE condition;
```
- To delete all records from a table, the `TRUNCATE` statement can be used. This is faster than using the `DELETE` statement without a `WHERE` clause.
- Syntax:
```
TRUNCATE TABLE table_name;
```