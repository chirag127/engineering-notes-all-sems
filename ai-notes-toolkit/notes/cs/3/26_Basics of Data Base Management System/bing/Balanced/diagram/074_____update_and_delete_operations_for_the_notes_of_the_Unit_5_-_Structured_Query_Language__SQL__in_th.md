### Update and Delete Operations in SQL

SQL is a language that allows you to manipulate data in relational databases. SQL has several commands that let you perform different operations on data, such as inserting, updating, deleting, and selecting records. These commands are known as Data Manipulation Language (DML) statements .

#### Update Operation

The UPDATE command is used to modify the existing records in a database table. You can use the SET clause to specify the new values for the columns that you want to update. You can also use the WHERE clause to filter the records that you want to update based on some condition .

The syntax of the UPDATE command is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

For example, if you want to update the salary of the employee with id 101 to 5000 in the employees table, you can write:

```sql
UPDATE employees
SET salary = 5000
WHERE id = 101;
```

#### Delete Operation

The DELETE command is used to delete the records from a database table that are no longer required. You can use the WHERE clause to specify the condition that determines which records to delete. If you omit the WHERE clause, all the records in the table will be deleted .

The syntax of the DELETE command is:

```sql
DELETE FROM table_name
WHERE condition;
```

For example, if you want to delete the employee with id 102 from the employees table, you can write:

```sql
DELETE FROM employees
WHERE id = 102;
```

#### Summary

- SQL is a language that allows you to manipulate data in relational databases using DML statements.
- The UPDATE command is used to modify the existing records in a database table. You can use the SET and WHERE clauses to specify the new values and the condition for the update operation.
- The DELETE command is used to delete the records from a database table that are no longer required. You can use the WHERE clause to specify the condition for the delete operation.