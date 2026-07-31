# Manipulating data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- SQL is a standard language for storing, manipulating and retrieving data in databases.
- SQL has two main categories of statements: Data Definition Language (DDL) and Data Manipulation Language (DML).
- DDL statements are used to create, alter, or drop database objects such as tables, views, indexes, etc.
- DML statements are used to insert, update, delete, and merge data in database tables.
- In this unit, we will focus on the following DML statements:
  - INSERT: to add one or more rows to a table.
  - UPDATE: to modify one or more rows in a table.
  - DELETE: to remove one or more rows from a table.
  - MERGE: to combine data from two tables based on a matching condition.
- The syntax and examples of these statements are given below.

## INSERT statement
- The INSERT statement is used to add one or more rows to a table.
- The basic syntax of the INSERT statement is:

```sql
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
```

- The table_name is the name of the table where the data will be inserted.
- The column1, column2, ... are the names of the columns in the table where the data will be inserted. If not specified, all the columns in the table will be used.
- The value1, value2, ... are the values to be inserted in the corresponding columns. They must match the data type and constraints of the columns.
- For example, to insert a new row into the EMPLOYEES table, we can write:

```sql
INSERT INTO EMPLOYEES (EMP_ID, NAME, SALARY, DEPT_ID) VALUES (101, 'Alice', 5000, 10);
```

- This will add a new row with the values 101, 'Alice', 5000, and 10 in the EMP_ID, NAME, SALARY, and DEPT_ID columns respectively.
- To insert multiple rows at once, we can use the following syntax:

```sql
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...), (value3, value4, ...), ...;
```

- For example, to insert two more rows into the EMPLOYEES table, we can write:

```sql
INSERT INTO EMPLOYEES (EMP_ID, NAME, SALARY, DEPT_ID) VALUES (102, 'Bob', 6000, 20), (103, 'Charlie', 7000, 30);
```

- This will add two more rows with the values 102, 'Bob', 6000, 20 and 103, 'Charlie', 7000, 30 in the EMP_ID, NAME, SALARY, and DEPT_ID columns respectively.

## UPDATE statement
- The UPDATE statement is used to modify one or more rows in a table.
- The basic syntax of the UPDATE statement is:

```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

- The table_name is the name of the table where the data will be updated.
- The column1, column2, ... are the names of the columns in the table that will be updated. The value1, value2, ... are the new values to be assigned to the corresponding columns. They must match the data type and constraints of the columns.
- The WHERE clause is used to specify the condition that identifies which rows will be updated. If not specified, all the rows in the table will be updated.
- For example, to update the salary of Alice in the EMPLOYEES table, we can write:

```sql
UPDATE EMPLOYEES SET SALARY = 5500 WHERE NAME = 'Alice';
```

- This will update the salary column of the row where the name column is 'Alice' to 5500.
- To update multiple columns at once, we can use the following syntax:

```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

- For example, to update the salary and department of Bob in the EMPLOYEES table, we can write:

```sql
UPDATE EMPLOYEES SET SALARY = 6500, DEPT_ID

```
