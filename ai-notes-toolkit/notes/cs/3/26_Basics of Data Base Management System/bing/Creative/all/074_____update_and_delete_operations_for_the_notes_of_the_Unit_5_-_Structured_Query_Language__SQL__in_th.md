# Update and Delete Operations in SQL

SQL is a language that allows you to manipulate data in relational databases. SQL has several commands that can perform different operations on data, such as inserting, selecting, updating, and deleting records. These commands are part of the Data Manipulation Language (DML) subset of SQL.

## Update Operation

The update operation is used to modify the existing records in a database table. The syntax of the update command is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

The update command requires the name of the table to be updated, the columns and values to be changed, and an optional condition to specify which records to update. If the condition is omitted, all the records in the table will be updated.

For example, to update the salary of an employee with id 101 to 5000, you can use the following command:

```sql
UPDATE employees
SET salary = 5000
WHERE id = 101;
```

You can also update multiple columns in one command, such as changing the name and department of an employee:

```sql
UPDATE employees
SET name = 'John Smith', department = 'Sales'
WHERE id = 101;
```

## Delete Operation

The delete operation is used to remove records from a database table. The syntax of the delete command is:

```sql
DELETE FROM table_name
WHERE condition;
```

The delete command requires the name of the table to be deleted from, and an optional condition to specify which records to delete. If the condition is omitted, all the records in the table will be deleted.

For example, to delete the record of an employee with id 101, you can use the following command:

```sql
DELETE FROM employees
WHERE id = 101;
```

You can also use more complex conditions to delete records, such as deleting all the employees who work in the IT department:

```sql
DELETE FROM employees
WHERE department = 'IT';
```

## Summary

- The update operation is used to modify the existing records in a database table. It requires the name of the table, the columns and values to be changed, and an optional condition to specify which records to update.
- The delete operation is used to remove records from a database table. It requires the name of the table and an optional condition to specify which records to delete.
- Both operations can use the WHERE clause to filter the records based on a condition. If the condition is omitted, all the records in the table will be affected.