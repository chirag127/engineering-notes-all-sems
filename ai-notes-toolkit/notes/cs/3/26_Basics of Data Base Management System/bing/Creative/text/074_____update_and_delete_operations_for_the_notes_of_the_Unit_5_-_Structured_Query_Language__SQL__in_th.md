### Update and Delete Operations in SQL

- SQL stands for Structured Query Language, which is a standard language for manipulating data in relational databases.
- SQL has several commands for performing different operations on data, such as creating, retrieving, updating, and deleting data.
- SQL commands can be divided into two categories: Data Definition Language (DDL) and Data Manipulation Language (DML).
- DDL commands are used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, etc.
- DML commands are used to manipulate the data in the database, such as inserting, selecting, updating, and deleting data from tables and views.
- In this unit, we will focus on the update and delete operations in SQL, which are two of the most common DML commands.

#### Update Operation in SQL

- The update operation in SQL is used to modify the existing records in the database.
- The syntax of the update command is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- The table_name is the name of the table that contains the records to be updated.
- The SET clause specifies the columns and the new values to be assigned to them.
- The WHERE clause specifies the condition that identifies which records to be updated. If the WHERE clause is omitted, all the records in the table will be updated.
- The update command can modify one or more columns and one or more records at a time, depending on the SET and WHERE clauses.
- For example, the following update command will change the salary of the employee with id 101 to 5000 in the employees table:

```sql
UPDATE employees
SET salary = 5000
WHERE id = 101;
```

- The following update command will increase the salary of all the employees by 10% in the employees table:

```sql
UPDATE employees
SET salary = salary * 1.1;
```

#### Delete Operation in SQL

- The delete operation in SQL is used to delete the records in the database that are no longer required.
- The syntax of the delete command is:

```sql
DELETE FROM table_name
WHERE condition;
```

- The table_name is the name of the table that contains the records to be deleted.
- The WHERE clause specifies the condition that identifies which records to be deleted. If the WHERE clause is omitted, all the records in the table will be deleted.
- The delete command can delete one or more records at a time, depending on the WHERE clause.
- For example, the following delete command will delete the record of the employee with id 101 from the employees table:

```sql
DELETE FROM employees
WHERE id = 101;
```

- The following delete command will delete all the records from the employees table:

```sql
DELETE FROM employees;
```

- Note that the delete command only removes the data from the table, not the table itself. To delete the table, you need to use the drop command, which is a DDL command.