## Data Manipulation Language(DML) Statements

Data Manipulation Language (DML) statements are used to manipulate data within the database. These statements allow users to insert, update, delete and retrieve data from the database.

### INSERT Statement

The INSERT statement is used to add new rows to a table. The syntax for the INSERT statement is as follows:

```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...)
```

### UPDATE Statement

The UPDATE statement is used to modify existing data in a table. The syntax for the UPDATE statement is as follows:

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

### DELETE Statement

The DELETE statement is used to remove rows from a table. The syntax for the DELETE statement is as follows:

```
DELETE FROM table_name
WHERE condition;
```

### SELECT Statement

The SELECT statement is used to retrieve data from one or more tables. The syntax for the SELECT statement is as follows:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### Transaction Management

DML statements can be grouped into transactions, which allow multiple statements to be treated as a single unit of work. Transactions ensure that if one statement fails, the entire transaction is rolled back, so that the database is left in a consistent state.

### Advantages

- DML statements provide a flexible and powerful way to manipulate data within a database.
- Transactions ensure that data is consistent and reliable.
- DML statements can be used to automate common data management tasks.

### Disadvantages

- DML statements can be complex and difficult to write correctly.
- Transactions can have a performance impact on the database.

### Examples

```
-- Insert a new row into the employees table
INSERT INTO employees (employee_id, first_name, last_name, email)
VALUES (1001, 'John', 'Doe', 'jdoe@example.com');

-- Update the salary of all employees in the sales department
UPDATE employees
SET salary = salary * 1.1
WHERE department = 'Sales';

-- Delete all employees who have left the company
DELETE FROM employees
WHERE end_date IS NOT NULL;

-- Retrieve the names and salaries of all employees in the marketing department
SELECT first_name, last_name, salary
FROM employees
WHERE department = 'Marketing';
```

### Applications

DML statements are used in a wide variety of applications, including:

- Web applications that interact with databases.
- Business intelligence and reporting applications that extract data from databases.
- Data warehousing applications that transform and load data into databases.