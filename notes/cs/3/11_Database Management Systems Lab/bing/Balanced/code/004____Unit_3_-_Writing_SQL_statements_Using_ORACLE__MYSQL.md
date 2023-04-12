## Unit 3 - Writing SQL statements Using ORACLE /MYSQL

SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases. SQL can be used to perform various tasks, such as creating tables, inserting records, updating data, deleting data, querying data, joining tables, and performing calculations.

ORACLE and MYSQL are two popular relational database management systems (RDBMS) that support SQL. ORACLE is a proprietary software developed by Oracle Corporation, while MYSQL is an open-source software developed by MySQL AB (now owned by Oracle Corporation). Both ORACLE and MYSQL have their own features and extensions to the SQL standard, but they also share many common SQL syntax and commands.

In this unit, we will learn how to write basic SQL statements using ORACLE or MYSQL, such as:

- SELECT: to query data from one or more tables
- INSERT: to insert new records into a table
- UPDATE: to modify existing records in a table
- DELETE: to remove records from a table
- CREATE TABLE: to create a new table in the database
- ALTER TABLE: to modify the structure of an existing table
- DROP TABLE: to delete a table from the database
- JOIN: to combine data from two or more tables based on a common column
- GROUP BY: to group records with the same values and apply aggregate functions
- HAVING: to filter groups based on a condition
- ORDER BY: to sort the query results by one or more columns
- LIMIT: to limit the number of rows returned by a query

The general syntax of a SQL statement is:

```sql
SQL_command
[parameters]
[conditions]
[modifiers];
```

The SQL_command is the keyword that specifies the action to be performed, such as SELECT, INSERT, UPDATE, etc. The parameters are the arguments that provide the details of the action, such as the table name, column name, values, etc. The conditions are the clauses that specify the criteria for selecting, modifying, or deleting data, such as WHERE, JOIN, GROUP BY, etc. The modifiers are the keywords that modify the behavior of the SQL_command, such as DISTINCT, AS, ASC, DESC, etc. The semicolon (;) is the statement terminator that marks the end of a SQL statement.

Here are some examples of SQL statements using ORACLE or MYSQL:

- To query all the records from the table employees:

```sql
SELECT * FROM employees;
```

- To query the first name, last name, and salary of the employees who work in the department 10:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE department_id = 10;
```

- To query the first name, last name, and salary of the employees who work in the department 10 or 20, and sort the results by salary in descending order:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE department_id IN (10, 20)
ORDER BY salary DESC;
```

- To insert a new record into the table employees with the values 101, 'John', 'Smith', 5000, and 10 for the columns employee_id, first_name, last_name, salary, and department_id, respectively:

```sql
INSERT INTO employees (employee_id, first_name, last_name, salary, department_id)
VALUES (101, 'John', 'Smith', 5000, 10);
```

- To update the salary of the employee with the employee_id 101 to 6000:

```sql
UPDATE employees
SET salary = 6000
WHERE employee_id = 101;
```

- To delete the record of the employee with the employee_id 101 from the table employees:

```sql
DELETE FROM employees
WHERE employee_id = 101;
```

- To create a new table called departments with the columns department_id, department_name, and location_id, and specify the data types and constraints for each column:

```sql
CREATE TABLE departments (
  department_id NUMBER(4) PRIMARY KEY,
  department_name VARCHAR2(30) NOT NULL,
  location_id NUMBER(4) REFERENCES locations(location_id)
);
```

- To add a new column called manager_id to the table employees, and specify the data type and constraint for the column:

```sql
ALTER TABLE employees
ADD manager_id NUMBER(4) REFERENCES employees(employee_id);
```

- To drop the table departments from the database:

```sql
DROP TABLE departments;
```

- To query the first name, last name, and department name of the employees who work in the departments located in the city 'New York', and join the tables employees, departments, and locations based on the common columns:

```sql
SELECT e.first

```
