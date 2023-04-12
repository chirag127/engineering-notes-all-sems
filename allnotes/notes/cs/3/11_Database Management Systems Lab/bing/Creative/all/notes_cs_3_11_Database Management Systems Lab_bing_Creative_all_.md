

## Unit 1 - Installing Oracle/MySQL

Oracle and MySQL are two popular relational database management systems (RDBMS) that can be used to store, manage and manipulate data. In this unit, we will learn how to install Oracle and MySQL on Windows and Linux operating systems.

### Installing Oracle on Windows

To install Oracle on Windows, you need to follow these steps:

1. Download the Oracle Database installer from the official website: https://www.oracle.com/database/technologies/oracle-database-software-downloads.html
2. Choose the edition and version of Oracle that suits your needs and system requirements. For example, you can choose Oracle Database 19c Standard Edition 2 for Windows x64.
3. Run the installer as an administrator and follow the instructions on the screen. You will need to accept the license agreement, choose the installation type (typical or custom), specify the installation location, create an Oracle home user and password, configure the database options and review the summary.
4. Wait for the installation to complete and click Finish. You can verify the installation by opening the Oracle Database Configuration Assistant and checking the status of the database.
5. Optionally, you can also install Oracle SQL Developer, a graphical tool for developing and managing Oracle databases. You can download it from https://www.oracle.com/tools/downloads/sqldev-downloads.html and run the installer as an administrator.

### Installing Oracle on Linux

To install Oracle on Linux, you need to follow these steps:

1. Download the Oracle Database installer from the official website: https://www.oracle.com/database/technologies/oracle-database-software-downloads.html
2. Choose the edition and version of Oracle that suits your needs and system requirements. For example, you can choose Oracle Database 19c Enterprise Edition for Linux x86-64.
3. Transfer the installer to the Linux machine and unzip it. You can use a tool like WinSCP or FileZilla to transfer files between Windows and Linux.
4. Log in to the Linux machine as the root user or a user with sudo privileges. You will need to create an Oracle user and group, set the environment variables, install the required packages and configure the kernel parameters. You can follow the instructions in this guide: https://docs.oracle.com/en/database/oracle/oracle-database/19/ladbi/index.html
5. Run the installer as the Oracle user and follow the instructions on the screen. You will need to accept the license agreement, choose the installation type (typical or custom), specify the installation location, create an Oracle home user and password, configure the database options and review the summary.
6. Wait for the installation to complete and click Finish. You can verify the installation by opening the Oracle Database Configuration Assistant and checking the status of the database.
7. Optionally, you can also install Oracle SQL Developer, a graphical tool for developing and managing Oracle databases. You can download it from https://www.oracle.com/tools/downloads/sqldev-downloads.html and run the installer as the Oracle user.

### Installing MySQL on Windows

To install MySQL on Windows, you need to follow these steps:

1. Download the MySQL Installer from the official website: https://dev.mysql.com/downloads/installer/
2. Choose the edition and version of MySQL that suits your needs and system requirements. For example, you can choose MySQL Installer 8.0.27 for Windows.
3. Run the installer as an administrator and follow the instructions on the screen. You will need to accept the license agreement, choose the setup type (developer default, server only, client only or custom), specify the installation location, configure the MySQL server and products, create a root password and user accounts, apply the configuration and review the summary.
4. Wait for the installation to complete and click Finish. You can verify the installation by opening the MySQL Workbench and connecting to the MySQL server.
5. Optionally, you can also install other MySQL products, such as MySQL Shell, MySQL Router, MySQL Connector or MySQL Utilities. You can use the MySQL Installer to add or remove products as needed.

### Installing MySQL on Linux

To install MySQL on Linux, you need to follow these steps:

1. Download the MySQL repository package from the official website: https://dev.mysql.com/downloads/repo/
2. Choose the repository package that matches your Linux distribution and version. For example, you can choose MySQL 8.0 Community Server for Ubuntu 20.04.
3. Transfer the repository package to the Linux machine and install it. You can use a tool like WinSCP or FileZilla to transfer files between Windows and Linux.
4. Log in to the Linux machine as the root user or a user with sudo privileges. You will need to update the package index and install the MySQL server and client packages. You can follow the instructions in this guide



Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of installing Oracle/MySQL in the subject of Database Management Systems Lab. Here is the content in markdown format:

# Unit 1 - Installing Oracle/MySQL

## Oracle

Oracle is a relational database management system (RDBMS) that supports the SQL language for querying and manipulating data. Oracle can run on various operating systems, such as Windows, Linux, and Unix.

To install Oracle on your system, you need to follow these steps:

- Download the Oracle Database software from the official website: https://www.oracle.com/database/technologies/oracle-database-software-downloads.html
- Choose the edition and version that suits your needs and system requirements. For example, you can choose Oracle Database 19c Standard Edition 2 for Windows x64.
- Extract the downloaded zip file and run the setup.exe file as an administrator.
- Follow the installation wizard and provide the necessary information, such as the installation type, the Oracle base directory, the Oracle home directory, the database name, the password, and the pluggable database name.
- Wait for the installation to complete and verify that the Oracle Database service is running in the Windows Services panel.
- Optionally, you can install Oracle SQL Developer, a graphical tool for managing and developing Oracle databases, from this link: https://www.oracle.com/tools/downloads/sqldev-downloads.html
- To connect to your Oracle database, you can use SQL Developer, SQL*Plus, or any other client tool that supports Oracle.

## MySQL

MySQL is an open-source relational database management system (RDBMS) that supports the SQL language for querying and manipulating data. MySQL can run on various operating systems, such as Windows, Linux, and Unix.

To install MySQL on your system, you need to follow these steps:

- Download the MySQL Installer from the official website: https://dev.mysql.com/downloads/installer/
- Choose the installer type that suits your needs and system requirements. For example, you can choose MySQL Installer 8.0.27 for Windows (x86, 64-bit), MSI Installer.
- Run the installer file and follow the installation wizard and provide the necessary information, such as the setup type, the MySQL root password, the MySQL user accounts, and the MySQL server configuration.
- Wait for the installation to complete and verify that the MySQL service is running in the Windows Services panel.
- Optionally, you can install MySQL Workbench, a graphical tool for managing and developing MySQL databases, from this link: https://dev.mysql.com/downloads/workbench/
- To connect to your MySQL database, you can use MySQL Workbench, MySQL Shell, or any other client tool that supports MySQL.



## Unit 2 - Creating Entity-Relationship Diagram using case tools

- An entity-relationship diagram (ERD) is a graphical representation of the data and relationships in a database system.
- A case tool is a software application that supports the development and maintenance of software systems, such as databases, by providing features such as modeling, design, code generation, testing, and documentation.
- Creating an ERD using a case tool involves the following steps:
  - Identify the entities and attributes in the database system. An entity is a person, place, thing, or concept that can be uniquely identified and stored in the database. An attribute is a property or characteristic of an entity that can have a value. For example, in a student database, Student and Course are entities, and Student_ID, Name, and Grade are attributes.
  - Identify the relationships and cardinalities between the entities. A relationship is an association or link between two or more entities that expresses a business rule or requirement. A cardinality is the number of occurrences of one entity that can be related to another entity in a relationship. For example, in a student database, a student can enroll in many courses, and a course can have many students enrolled in it. This is a many-to-many relationship with a cardinality of M:N.
  - Draw the ERD using the case tool's graphical interface. The case tool provides symbols and notations to represent the entities, attributes, relationships, and cardinalities in the ERD. For example, a rectangle represents an entity, an oval represents an attribute, a diamond represents a relationship, and a line with a number or a symbol represents a cardinality. The case tool also allows the user to edit, modify, and validate the ERD.
  - Generate the database schema from the ERD using the case tool's code generation feature. The database schema is the logical structure and definition of the data and relationships in the database system. The case tool can generate the database schema in a specific database language, such as SQL, based on the ERD. The user can then execute the generated code to create the database tables and constraints.



# Unit 2 - Creating Entity-Relationship Diagram using case tools

- An entity-relationship diagram (ERD) is a graphical representation of the entities and relationships in a database system.
- An entity is a person, place, thing, or concept that can be uniquely identified and stored in a database. An entity has attributes that describe its properties or characteristics.
- A relationship is an association or connection between two or more entities. A relationship has a cardinality that specifies how many instances of each entity can participate in the relationship.
- A case tool is a software application that helps in the design, development, and maintenance of a database system. A case tool can provide features such as diagramming, modeling, documentation, code generation, testing, and debugging.
- Some of the benefits of using a case tool for creating an ERD are:
  - It can help in visualizing the database structure and the data flow.
  - It can help in validating the database design and ensuring its consistency and accuracy.
  - It can help in generating the database schema and the SQL code from the ERD.
  - It can help in documenting the database design and the business rules.
  - It can help in collaborating and communicating with other stakeholders and users.
- Some of the challenges of using a case tool for creating an ERD are:
  - It can be expensive and require a license or subscription fee.
  - It can be complex and require training and expertise to use effectively.
  - It can be incompatible or inconsistent with other tools or platforms.
  - It can be limited or inflexible in terms of customization and functionality.
- Some of the examples of case tools for creating an ERD are:
  - Lucidchart: A web-based diagramming and collaboration tool that supports various types of diagrams, including ERDs. It has a drag-and-drop interface, a library of templates and shapes, and a cloud-based storage and sharing feature.
  - Miro: A web-based visual collaboration platform that allows users to create and edit diagrams, including ERDs, on an infinite canvas. It has a variety of tools and widgets, such as sticky notes, shapes, icons, and images, and a real-time collaboration and feedback feature.
  - Dataedo: A web-based database documentation and data cataloging tool that can automatically generate an ERD from the current state of a database schema. It has a user-friendly interface, a rich set of metadata, and a data lineage and impact analysis feature.



## Unit 3 - Writing SQL statements Using ORACLE /MYSQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- ORACLE and MYSQL are two popular relational database management systems (RDBMS) that use SQL as their query language.
- To write SQL statements using ORACLE or MYSQL, one needs to follow some basic steps:
  - Connect to the database server using a client application, such as SQL*Plus for ORACLE or MySQL Workbench for MYSQL.
  - Specify the database name and the user credentials to access the data.
  - Write SQL statements in the query editor or the command-line interface, following the syntax and rules of SQL.
  - Execute the SQL statements by pressing a button or hitting the enter key, and view the results in the output window or the console.
  - Save, edit, or delete the SQL statements as needed.
- Some common types of SQL statements are:
  - Data Definition Language (DDL) statements, which are used to create, alter, or drop database objects, such as tables, views, indexes, etc.
  - Data Manipulation Language (DML) statements, which are used to insert, update, delete, or select data from database tables or views.
  - Data Control Language (DCL) statements, which are used to grant or revoke permissions or roles to users or groups on database objects or data.
  - Transaction Control Language (TCL) statements, which are used to control the transactions, such as commit, rollback, savepoint, etc.
- Some examples of SQL statements using ORACLE or MYSQL are:

  - To create a table named `employees` with four columns: `emp_id`, `emp_name`, `emp_salary`, and `emp_dept`, one can write:

    ```sql
    -- ORACLE syntax
    CREATE TABLE employees (
      emp_id NUMBER(10) PRIMARY KEY,
      emp_name VARCHAR2(50) NOT NULL,
      emp_salary NUMBER(10,2) CHECK (emp_salary > 0),
      emp_dept VARCHAR2(20)
    );

    -- MYSQL syntax
    CREATE TABLE employees (
      emp_id INT(10) PRIMARY KEY,
      emp_name VARCHAR(50) NOT NULL,
      emp_salary DECIMAL(10,2) CHECK (emp_salary > 0),
      emp_dept VARCHAR(20)
    );
    ```

  - To insert a row into the `employees` table with the values `101`, `Alice`, `5000`, and `Sales`, one can write:

    ```sql
    -- ORACLE and MYSQL syntax
    INSERT INTO employees (emp_id, emp_name, emp_salary, emp_dept)
    VALUES (101, 'Alice', 5000, 'Sales');
    ```

  - To update the salary of the employee with the id `101` to `6000`, one can write:

    ```sql
    -- ORACLE and MYSQL syntax
    UPDATE employees
    SET emp_salary = 6000
    WHERE emp_id = 101;
    ```

  - To delete the employee with the id `101` from the `employees` table, one can write:

    ```sql
    -- ORACLE and MYSQL syntax
    DELETE FROM employees
    WHERE emp_id = 101;
    ```

  - To select all the columns and rows from the `employees` table, one can write:

    ```sql
    -- ORACLE and MYSQL syntax
    SELECT * FROM employees;
    ```

  - To select only the name and salary of the employees who work in the `Sales` department, one can write:

    ```sql
    -- ORACLE and MYSQL syntax
    SELECT emp_name, emp_salary FROM employees
    WHERE emp_dept = 'Sales';
    ```



Hello, I am Sydney, your AI assistant. I can help you with writing basic SQL SELECT statements for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab. Here are some points to remember:

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- A SELECT statement is used to query data from one or more tables or views in a database. The basic syntax of a SELECT statement is:

```sql
SELECT column1, column2, ... FROM table1, table2, ... WHERE condition;
```

- The SELECT clause specifies which columns to return in the result set. You can use * to select all columns from a table or view.
- The FROM clause specifies which tables or views to query data from. You can use aliases to give a table or view a different name in the query.
- The WHERE clause specifies a condition that filters the rows in the result set. You can use logical operators such as AND, OR, and NOT to combine multiple conditions.
- You can use various clauses to modify the result set of a SELECT statement, such as:

  - The ORDER BY clause to sort the rows by one or more columns in ascending or descending order.
  - The GROUP BY clause to group the rows by one or more columns and apply aggregate functions such as SUM, AVG, COUNT, etc.
  - The HAVING clause to filter the groups by a condition.
  - The LIMIT clause to limit the number of rows returned by the query.
  - The JOIN clause to combine data from two or more tables or views based on a common column or condition.

- You can use various functions and operators to manipulate the data in a SELECT statement, such as:

  - Arithmetic operators such as +, -, *, /, and % to perform calculations on numeric values.
  - String functions such as CONCAT, SUBSTR, LENGTH, UPPER, LOWER, etc. to manipulate character values.
  - Date functions such as SYSDATE, TO_DATE, TO_CHAR, EXTRACT, etc. to manipulate date and time values.
  - Conversion functions such as CAST, TO_NUMBER, TO_CHAR, etc. to convert data from one type to another.
  - Conditional expressions such as CASE, DECODE, NVL, etc. to return different values based on a condition.

- You can use subqueries to nest one SELECT statement inside another SELECT statement. A subquery can return a single value, a single row, a single column, or a table. You can use subqueries in various clauses of a SELECT statement, such as:

  - The SELECT clause to return a value or a column as a part of the result set.
  - The FROM clause to return a table as a source of data for the query.
  - The WHERE clause to return a condition for filtering the rows.
  - The HAVING clause to return a condition for filtering the groups.
  - The ORDER BY clause to return a column for sorting the rows.

- You can use comments to add explanatory notes to your SQL statements. Comments can be either single-line or multi-line. The syntax for comments is:

```sql
-- This is a single-line comment
/* This is a multi-line comment */
```

- You can use a semicolon (;) to end a SQL statement. You can also use a slash (/) on a new line to execute a SQL statement in some SQL tools.



# Restricting and Sorting Data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Restricting data means limiting the rows that are retrieved by a query based on some conditions.
- Sorting data means arranging the rows that are retrieved by a query in a specific order.
- Both restricting and sorting data can be done by using clauses in the SQL statement, such as WHERE, ORDER BY, and LIMIT.

## Restricting Data

- The WHERE clause is used to filter the rows that match a given condition or expression.
- The WHERE clause can be used with any SQL statement that returns rows, such as SELECT, UPDATE, or DELETE.
- The WHERE clause can contain single or multiple conditions, which can be combined with logical operators such as AND, OR, and NOT.
- The WHERE clause can also use comparison operators such as =, <, >, <=, >=, <>, LIKE, IN, BETWEEN, and IS NULL to compare values.
- The WHERE clause can also use functions, subqueries, and variables to evaluate conditions.

### Examples of Restricting Data

- To display the name and salary of all employees whose salary is not in the range of $10,000 to $15,000, we can use the following query in MySQL:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary NOT BETWEEN 10000 AND 15000;
```

- To display the name and department of all employees who work in either department 10 or 20, we can use the following query in Oracle:

```sql
SELECT first_name, last_name, department_id
FROM employees
WHERE department_id IN (10, 20);
```

- To display the name and hire date of all employees who were hired in the year 2020, we can use the following query in Oracle:

```sql
SELECT first_name, last_name, hire_date
FROM employees
WHERE EXTRACT(YEAR FROM hire_date) = 2020;
```

## Sorting Data

- The ORDER BY clause is used to sort the rows that are retrieved by a query in ascending or descending order.
- The ORDER BY clause can be used with any SQL statement that returns rows, such as SELECT or UNION.
- The ORDER BY clause can sort the rows by one or more columns or expressions, which can be specified by name, alias, or position.
- The ORDER BY clause can also use the ASC or DESC keywords to specify the sort order for each column or expression. The default order is ascending.
- The ORDER BY clause can also use the NULLS FIRST or NULLS LAST keywords to specify how null values are treated in the sort order.

### Examples of Sorting Data

- To display the name and salary of all employees in descending order of salary, we can use the following query in MySQL:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;
```

- To display the name and department of all employees in ascending order of department and then in descending order of name, we can use the following query in Oracle:

```sql
SELECT first_name, last_name, department_id
FROM employees
ORDER BY department_id ASC, last_name DESC;
```

- To display the name and hire date of all employees in ascending order of hire date and then in ascending order of name, with null values last, we can use the following query in Oracle:

```sql
SELECT first_name, last_name, hire_date
FROM employees
ORDER BY hire_date ASC NULLS LAST, first_name ASC;
```

## Limiting Rows

- The LIMIT clause is used to limit the number of rows that are retrieved by a query to a specified range.
- The LIMIT clause can be used with any SQL statement that returns rows, such as SELECT or UNION.
- The LIMIT clause can specify the offset and the count of the rows to be retrieved, or the percentage of the rows to be retrieved.
- The LIMIT clause can also use the WITH TIES option to include additional rows that have the same values as the last row in the result set.

### Examples of Limiting Rows

- To display the name and salary of the top 5 highest paid employees, we can use the following query in MySQL:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;
```

- To display the name and department of the employees from the 11th to the 20th position in ascending order of department, we can use the following query in Oracle:

```sql
SELECT first

```




# Displaying data from multiple tables

- One of the main features of SQL is the ability to query data from multiple tables and combine the results into a single result set.
- This is useful for retrieving related information from different sources and presenting a comprehensive view of the data.
- There are different ways to display data from multiple tables using SQL statements, such as:
  - Joining columns in two or more tables
  - Merging data from multiple tables into a single column
  - Creating a subquery to retrieve data from more than one table
  - Using set operators to combine result sets from different queries

## Joining columns in two or more tables

- A join is a SQL operation that allows you to combine data from two or more tables based on a common column or condition.
- The common column is usually a primary key in one table and a foreign key in another table, which establishes a relationship between the tables.
- There are different types of joins, such as:
  - Inner join: returns only the rows that match the join condition in both tables.
  - Left join: returns all the rows from the left table and the matching rows from the right table, or NULL if there is no match.
  - Right join: returns all the rows from the right table and the matching rows from the left table, or NULL if there is no match.
  - Full join: returns all the rows from both tables, regardless of whether they match the join condition or not.
  - Cross join: returns the Cartesian product of the rows from both tables, which means every row from the left table is paired with every row from the right table.
- The syntax for joining tables in SQL is:

```sql
SELECT column_list
FROM table1
JOIN table2
ON join_condition;
```

- For example, if we have two tables, `employees` and `departments`, and we want to display the employee name, department name, and salary for each employee, we can use an inner join as follows:

```sql
SELECT e.name, d.name, e.salary
FROM employees e
JOIN departments d
ON e.department_id = d.id;
```

- The result would look something like this:

| name | name | salary |
| --- | --- | --- |
| Alice | Sales | 5000 |
| Bob | Marketing | 4000 |
| Charlie | IT | 6000 |
| David | HR | 3000 |

## Merging data from multiple tables into a single column

- Sometimes, we may want to display data from multiple tables into a single column, rather than multiple columns.
- This can be useful for concatenating values, aggregating data, or creating a list of values.
- To merge data from multiple tables into a single column, we can use the following techniques:
  - Concatenation operator: allows us to combine two or more values into a single string. The operator varies depending on the database system, but it is usually `||` or `+`.
  - Aggregate functions: allow us to perform calculations on a set of values and return a single value. Some common aggregate functions are `SUM`, `AVG`, `MIN`, `MAX`, `COUNT`, etc.
  - Subquery: allows us to nest a query inside another query and use the result as a value or a table. A subquery can be used in the `SELECT`, `FROM`, `WHERE`, `HAVING`, or `ORDER BY` clauses of the main query.
  - GROUP_CONCAT function: allows us to concatenate values from a group of rows into a single string, separated by a delimiter. This function is specific to MySQL and SQLite databases.
- For example, if we have two tables, `students` and `courses`, and we want to display the student name and the list of courses they are enrolled in, we can use a subquery and the `GROUP_CONCAT` function as follows:

```sql
SELECT s.name, 
(SELECT GROUP_CONCAT(c.name) FROM courses c WHERE c.student_id = s.id) AS courses
FROM students s;
```

- The result would look something like this:

| name | courses |
| --- | --- |
| Emma | Math, Physics, Chemistry |
| Noah | History, Geography, Literature |
| Olivia | Art, Music, Drama |
| Liam | Biology, Computer Science, Engineering |



# Aggregating data using group function for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Aggregate functions are functions that operate on a set of values and return a single value. They are commonly used to perform calculations or summaries on groups of rows in a table or view. Some examples of aggregate functions are `SUM`, `MAX`, `MIN`, `COUNT`, `AVG`, `LISTAGG`, `JSON_ARRAYAGG`, etc.    
- Group functions are aggregate functions that can be used with the `GROUP BY` clause in a `SELECT` statement. The `GROUP BY` clause divides the rows of a table or view into groups based on the values of one or more columns. The aggregate functions are then applied to each group and return a single result row for each group.    
- The syntax of using group functions with the `GROUP BY` clause is as follows:

```sql
SELECT column1, column2, ..., aggregate_function(column)
FROM table
WHERE condition
GROUP BY column1, column2, ...
ORDER BY column1, column2, ...
```

- The columns in the `SELECT` list must be either the columns used in the `GROUP BY` clause or the aggregate functions. The columns in the `ORDER BY` clause must be the same as the columns in the `SELECT` list. The `WHERE` clause can be used to filter the rows before grouping them.    
- The `HAVING` clause can be used to filter the groups after applying the aggregate functions. The `HAVING` clause can only contain aggregate functions or columns used in the `GROUP BY` clause. The syntax of using the `HAVING` clause is as follows:

```sql
SELECT column1, column2, ..., aggregate_function(column)
FROM table
WHERE condition
GROUP BY column1, column2, ...
HAVING aggregate_function(column) condition
ORDER BY column1, column2, ...
```

- The `HAVING` clause is similar to the `WHERE` clause, but it operates on groups rather than rows. The `HAVING` clause can be used to eliminate groups that do not satisfy the condition.    
- Some examples of using group functions with the `GROUP BY` and `HAVING` clauses are as follows:

```sql
-- Find the total sales amount for each product category
SELECT category, SUM(amount) AS total_sales
FROM sales
GROUP BY category
ORDER BY category;

-- Find the average salary for each department that has more than 10 employees
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 10
ORDER BY department;

-- Find the name and email of the customers who have placed more than 5 orders
SELECT name, email
FROM customers
JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id, name, email
HAVING COUNT(orders.id) > 5
ORDER BY name, email;

-- Find the name and price of the most expensive product in each category
SELECT category, name, MAX(price) AS max_price
FROM products
GROUP BY category
ORDER BY category;
```

- Oracle and MySQL support different aggregate functions and have some differences in how they handle the `GROUP BY` clause. For example, Oracle supports the `LISTAGG` function to concatenate values from a group into a single string, while MySQL supports the `JSON_ARRAYAGG` and `JSON_OBJECTAGG` functions to aggregate values from a group into a JSON array or object.   
- Another difference is that Oracle requires that all columns in the `SELECT` list must be either the columns used in the `GROUP BY` clause or the aggregate functions, while MySQL allows columns that are not in the `GROUP BY` clause or the aggregate functions, but the values of those columns are indeterminate and may vary for each execution of the query.   
- Therefore, it is important to check the documentation of the specific database system before using the group functions and the `GROUP BY` clause.



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




# Creating and managing tables for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- A table is a collection of related data organized in rows and columns in a database.
- To create a table in Oracle SQL, you use the `CREATE TABLE` statement, followed by the table name and the column definitions .
- The basic syntax of the `CREATE TABLE` statement is:

```sql
CREATE TABLE schema_name.table_name (
  column_1 data_type column_constraint,
  column_2 data_type column_constraint,
  ...
  table_constraint
);
```

- The `schema_name` is optional and specifies the schema where the table belongs. If you omit it, the table will be created in your own schema.
- The `table_name` is the name of the table that you want to create. It must be unique within the schema.
- The `column_1`, `column_2`, etc. are the names of the columns in the table. Each column must have a data type and an optional column constraint.
- The `data_type` specifies the type of data that the column can store, such as `NUMBER`, `VARCHAR2`, `DATE`, etc.
- The `column_constraint` specifies the rules that the column values must follow, such as `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, etc.
- The `table_constraint` specifies the rules that the table as a whole must follow, such as `PRIMARY KEY`, `UNIQUE`, `FOREIGN KEY`, `CHECK`, etc.

- To manage tables in Oracle SQL, you can use various commands, such as:
  - `ALTER TABLE` to modify the structure or properties of an existing table, such as adding, dropping, renaming, or modifying columns, constraints, indexes, partitions, etc.
  - `DROP TABLE` to delete an existing table and its data from the database.
  - `TRUNCATE TABLE` to remove all the data from an existing table without deleting the table itself.
  - `RENAME TABLE` to change the name of an existing table.
  - `COMMENT ON TABLE` to add or modify a comment on an existing table or its columns.
  - `ANALYZE TABLE` to collect statistics on an existing table and its indexes for the optimizer.
  - `LOCK TABLE` to prevent other users from modifying an existing table or its data while you perform a transaction.
  - `GRANT` and `REVOKE` to grant or revoke privileges on an existing table to other users or roles.

- To view the information about the tables in Oracle SQL, you can use various commands, such as:
  - `DESCRIBE` to display the column names, data types, and constraints of an existing table.
  - `SELECT` to query the data from an existing table or multiple tables using various clauses, such as `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `JOIN`, etc.
  - `INSERT` to add new rows of data to an existing table.
  - `UPDATE` to modify the existing rows of data in an existing table.
  - `DELETE` to remove the existing rows of data from an existing table.
  - `MERGE` to insert, update, or delete rows of data in an existing table based on the data from another table or subquery.
  - `EXPLAIN PLAN` to display the execution plan of a `SELECT` statement on an existing table or tables.

- To create and manage tables in Oracle SQL using a graphical user interface, you can use various tools, such as:
  - Oracle SQL Developer, which is a free and integrated development environment for Oracle Database.
  - Oracle Application Express (APEX), which is a low-code development platform for building web applications on Oracle Database.
  - Oracle SQL*Plus, which is a command-line tool for interacting with Oracle Database.



## Unit 4 - Normalization

- Normalization is a process of organizing the data in a database to reduce redundancy and improve data integrity.
- Normalization also simplifies the database design so that it achieves the optimal structure composed of atomic elements (i.e. elements that cannot be broken down into smaller parts).
- There are two goals of the normalization process: 
  - Eliminating redundant data (for example, storing the same data in more than one table) and 
  - Ensuring data dependencies make sense (only storing related data in a table). Both of these are worthy goals as they reduce the amount of space a database consumes and ensure that data is logically stored.
- The most common forms of normalization applied to databases are called the normal forms. They are numbered from one (the lowest form of normalization, referred to as first normal form or 1NF) through five (the highest, fifth normal form or 5NF). In practical applications, you'll often see 1NF, 2NF, and 3NF along with the occasional 4NF. Fifth normal form is very rarely seen and won't be discussed in this course.
- The normal forms are cumulative. In other words, to qualify for second normal form, a table must first satisfy the requirements for first normal form. To qualify for third normal form, a table must first satisfy the requirements for second normal form, and so on.
- The following are the definitions and examples of each normal form:

### First Normal Form (1NF)
- A table is in 1NF if it contains no repeating groups of data.
- A repeating group is a set of two or more fields that can occur any number of times in a single record.
- For example, consider the following table that stores the courses taken by students:

| Student ID | Name | Course 1 | Course 2 | Course 3 |
|------------|------|----------|----------|----------|
| 1001       | John | Math     | English  | History  |
| 1002       | Mary | Science  | Art      | NULL     |
| 1003       | Bob  | Music    | NULL     | NULL     |

- This table is not in 1NF because it contains a repeating group of fields: Course 1, Course 2, and Course 3. These fields can store multiple values for each student, but they are not atomic.
- To convert this table into 1NF, we need to remove the repeating group and create a separate table for courses, with a foreign key that references the student table. For example:

| Student ID | Name |
|------------|------|
| 1001       | John |
| 1002       | Mary |
| 1003       | Bob  |

| Student ID | Course |
|------------|--------|
| 1001       | Math   |
| 1001       | English|
| 1001       | History|
| 1002       | Science|
| 1002       | Art    |
| 1003       | Music  |

- Now, each table is in 1NF as it contains only atomic values and no repeating groups.

### Second Normal Form (2NF)
- A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
- A non-key attribute is an attribute that is not part of the primary key.
- A functional dependency is a relationship between two attributes, such that the value of one attribute (the determinant) uniquely determines the value of another attribute (the dependent).
- A full functional dependency is a functional dependency where the entire primary key is the determinant. In other words, removing any attribute from the primary key would make the dependency invalid.
- For example, consider the following table that stores the grades of students in different courses:

| Student ID | Course | Grade | Instructor |
|------------|--------|-------|------------|
| 1001       | Math   | A     | Smith      |
| 1001       | English| B     | Jones      |
| 1002       | Science| C     | Lee        |
| 1002       | Art    | A     | Chen       |
| 1003       | Music  | B     | Davis      |

- The primary key of this table is a composite key of Student ID and Course, as they uniquely identify each record.
- This table is in 1NF, but not in 2NF, because there are some non-key attributes that are not fully functionally dependent on the primary key. For instance, the attribute Instructor is functionally dependent on the attribute Course, but not on the attribute Student ID. This means that the instructor of a course does not



# Unit 4 - Normalization in Database Management Systems Lab

## Normalization

- Normalization is a technique to reduce data redundancy and remove anomalies related to insertion, deletion and updation from the database .
- Normalization of the database is a process of arranging the data in the database.
- The core idea of database normalization is to divide the tables into smaller subtables and store pointers to data rather than replicating it.
- Normalization is a process used for data modelling or database creation, where you organise your data and tables so it can be added and updated efficiently.
- Normalization is something a person does manually, as opposed to a system or a tool doing it.

## Keys

- Keys are column attributes that identify a database record uniquely.
- Keys are used to establish and identify relationships between tables and also to uniquely identify any record or row of data inside a table.
- There are different types of keys, such as primary key, foreign key, candidate key, alternate key, composite key, super key, etc.

## Functional Dependencies

- Functional dependencies are constraints between two attributes in a relation.
- A functional dependency is a relationship that exists when one attribute uniquely determines another attribute.
- For example, if A and B are attributes of a relation R, and every value of A is associated with exactly one value of B, then we say that B is functionally dependent on A, or A determines B, denoted by A -> B.

## Normal Forms

- Normal forms are steps to accomplish a certain quality of a database.
- Normal forms are based on the concept of functional dependencies and keys.
- There are different levels of normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), etc.
- Each normal form has a set of rules or criteria that a relation must satisfy to be in that normal form.
- The higher the normal form, the less redundancy and anomalies in the database.

## References

: https://medium.com/geekculture/normalization-in-database-management-system-82a5f14e117
: https://www.includehelp.com/dbms/normalization-in-database-management-system.aspx
: https://hackr.io/blog/dbms-normalization
: https://www.databasestar.com/database-normalization/
: https://phoenixnap.com/kb/database-normalization



## Unit 5 - Creating cursor

- A cursor is a temporary work area created in the system memory when a SQL statement is executed.
- A cursor contains information on a select statement and the rows of data accessed by it.
- A cursor can be used to manipulate data in a row-by-row manner.
- There are two types of cursors: implicit and explicit.
- An implicit cursor is automatically created by Oracle whenever a SQL statement is executed, when there is no explicit cursor for the statement.
- An explicit cursor is a cursor that is defined by the programmer in the declaration section of a PL/SQL block.
- An explicit cursor can be used to process multiple rows returned by a select statement.
- An explicit cursor has four attributes: %FOUND, %NOTFOUND, %ROWCOUNT, and %ISOPEN, which provide information about the execution of a data manipulation statement.
- An explicit cursor can be created using the following steps:
  - Declare the cursor using the CURSOR keyword and assign a name to it.
  - Define the query for the cursor using the SELECT statement.
  - Open the cursor using the OPEN statement to allocate memory and execute the query.
  - Fetch the data from the cursor into variables or records using the FETCH statement.
  - Close the cursor using the CLOSE statement to release the memory.
- An example of creating an explicit cursor is:

```sql
DECLARE
  CURSOR c_emp IS
    SELECT empno, ename, sal FROM emp;
  v_empno NUMBER(4);
  v_ename VARCHAR2(10);
  v_sal NUMBER(7,2);
BEGIN
  OPEN c_emp;
  LOOP
    FETCH c_emp INTO v_empno, v_ename, v_sal;
    EXIT WHEN c_emp%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(v_empno || ' ' || v_ename || ' ' || v_sal);
  END LOOP;
  CLOSE c_emp;
END;
```



# Unit 5 - Creating cursor in the subject of Database Management Systems Lab

## What is a cursor?

- A cursor is a temporary memory area that holds the result set of a query and allows row-by-row processing of the data.
- A cursor can be used to perform operations on each row of the result set, such as updating, deleting, or fetching data.
- A cursor can also be used to handle complex logic that cannot be expressed in a single SQL statement.

## Types of cursors

- There are two types of cursors: implicit and explicit.
- An implicit cursor is automatically created and managed by the database system for every SQL statement that returns a result set. For example, a SELECT statement creates an implicit cursor.
- An explicit cursor is created and controlled by the user using the DECLARE, OPEN, FETCH, and CLOSE statements. An explicit cursor can be named and customized according to the user's needs.

## How to create an explicit cursor

- The following steps are involved in creating an explicit cursor:

  1. Declare the cursor name and the SQL statement that defines the result set. For example:

     ```sql
     DECLARE cursor_name CURSOR FOR SELECT * FROM table_name;
     ```

  2. Open the cursor to execute the SQL statement and populate the result set in the memory. For example:

     ```sql
     OPEN cursor_name;
     ```

  3. Fetch the data from the cursor one row at a time and perform the desired operations on each row. For example:

     ```sql
     FETCH cursor_name INTO variable1, variable2, ...;
     ```

  4. Close the cursor to release the memory and resources associated with it. For example:

     ```sql
     CLOSE cursor_name;
     ```

## Examples of creating cursors in different databases

- The syntax and features of cursors may vary slightly depending on the database system. Here are some examples of creating cursors in different databases:

  - SQL Server:

    ```sql
    -- Declare the cursor
    DECLARE employee_cursor CURSOR FOR
    SELECT id, name, salary FROM employee;

    -- Declare variables to hold the fetched data
    DECLARE @id INT, @name VARCHAR(50), @salary DECIMAL(10,2);

    -- Open the cursor
    OPEN employee_cursor;

    -- Fetch the first row
    FETCH NEXT FROM employee_cursor INTO @id, @name, @salary;

    -- Loop through the cursor until no more rows are available
    WHILE @@FETCH_STATUS = 0
    BEGIN
      -- Perform some operation on each row, for example, print the data
      PRINT 'ID: ' + CAST(@id AS VARCHAR) + ', Name: ' + @name + ', Salary: ' + CAST(@salary AS VARCHAR);

      -- Fetch the next row
      FETCH NEXT FROM employee_cursor INTO @id, @name, @salary;
    END

    -- Close the cursor
    CLOSE employee_cursor;

    -- Deallocate the cursor
    DEALLOCATE employee_cursor;
    ```

  - Oracle:

    ```sql
    -- Declare the cursor
    DECLARE
      CURSOR employee_cursor IS
      SELECT id, name, salary FROM employee;

      -- Declare variables to hold the fetched data
      v_id employee.id%TYPE;
      v_name employee.name%TYPE;
      v_salary employee.salary%TYPE;
    BEGIN
      -- Open the cursor
      OPEN employee_cursor;

      -- Loop through the cursor until no more rows are available
      LOOP
        -- Fetch the next row
        FETCH employee_cursor INTO v_id, v_name, v_salary;

        -- Exit the loop if no more rows are available
        EXIT WHEN employee_cursor%NOTFOUND;

        -- Perform some operation on each row, for example, print the data
        DBMS_OUTPUT.PUT_LINE('ID: ' || v_id || ', Name: ' || v_name || ', Salary: ' || v_salary);
      END LOOP;

      -- Close the cursor
      CLOSE employee_cursor;
    END;
    ```

  - MySQL:

    ```sql
    -- Declare the cursor
    DECLARE employee_cursor CURSOR FOR
    SELECT id, name, salary FROM employee;

    -- Declare a variable to indicate the end of the cursor
    DECLARE done INT DEFAULT FALSE;

    -- Declare variables to hold the fetched data
    DECLARE v_id INT;
    DECLARE v_name VARCHAR(50);
    DECLARE v_salary DECIMAL(10,2);

    -- Declare a handler to set the done variable to true when no more rows are available
    DECLARE CONTINUE HANDLER

```




## Unit 6 - Creating procedure and functions

- A procedure is a named block of code that performs a specific task and can be executed by other parts of the program.
- A function is a named block of code that returns a value and can be used as an expression in other parts of the program.
- Both procedures and functions can have parameters, which are variables that receive values from the caller.
- Procedures and functions can be created using the `CREATE PROCEDURE` and `CREATE FUNCTION` statements, respectively.
- Procedures and functions can be executed using the `CALL` and `SELECT` statements, respectively, or by using their names as expressions in other statements.
- Procedures and functions can be modified using the `ALTER PROCEDURE` and `ALTER FUNCTION` statements, respectively.
- Procedures and functions can be deleted using the `DROP PROCEDURE` and `DROP FUNCTION` statements, respectively.
- Procedures and functions can be nested, meaning that one procedure or function can call another procedure or function within its code block.
- Procedures and functions can improve the readability, modularity, and reusability of the code, as well as reduce duplication and errors.



# Unit 6 - Creating procedure and functions in the subject of Database Management Systems Lab

## Introduction

- A database management system (DBMS) is a software that allows users to create, manipulate, and manage data in a structured way.
- A DBMS consists of several components, such as data, database schema, database engine, database access language, and procedures.
- Procedures refer to general instructions to use a DBMS, such as how to install, login, logout, backup, restore, and generate reports.
- Procedures can also refer to specific instructions to perform certain operations on data, such as how to insert, update, delete, and select data.
- Procedures that perform operations on data are also called stored procedures, views, and functions.

## Stored procedures

- A stored procedure is a set of SQL statements that can be executed as a single unit.
- A stored procedure can accept input parameters and return output parameters or result sets.
- A stored procedure can be created using the CREATE PROCEDURE statement, and executed using the EXECUTE or EXEC statement.
- A stored procedure can improve the performance, security, and maintainability of a database application, by reducing the network traffic, enforcing access control, and encapsulating the business logic.
- A stored procedure can be modified using the ALTER PROCEDURE statement, and deleted using the DROP PROCEDURE statement.

## Views

- A view is a virtual table that contains the result of a SQL query.
- A view can be created using the CREATE VIEW statement, and queried using the SELECT statement.
- A view can simplify the access to complex or frequently used queries, by hiding the underlying tables and columns, and providing a meaningful name.
- A view can also provide a level of abstraction and security, by restricting the access to certain columns or rows of the underlying tables.
- A view can be modified using the ALTER VIEW statement, and deleted using the DROP VIEW statement.

## Functions

- A function is a named set of SQL statements that returns a single value or a table of values.
- A function can be created using the CREATE FUNCTION statement, and invoked using the SELECT statement or as part of an expression.
- A function can be used to perform calculations, validations, conversions, or manipulations on data, by encapsulating the logic and reusing the code.
- A function can be classified into two types: scalar functions and table-valued functions.
- A scalar function returns a single value of a specific data type, while a table-valued function returns a table of values.
- A function can be modified using the ALTER FUNCTION statement, and deleted using the DROP FUNCTION statement.



## Unit 7 - Creating packages and triggers

In this unit, you will learn how to create packages and triggers in Oracle Database. Packages and triggers are two types of PL/SQL program units that can enhance the functionality and performance of your database applications.

### Packages

A package is a collection of related PL/SQL objects, such as procedures, functions, variables, constants, cursors, and types, that are stored together in the database. A package has two parts: a specification and a body. The specification declares the public objects that can be accessed by other program units, while the body defines the private objects and the implementation of the public objects.

Some benefits of using packages are:

- Modularity: You can organize your PL/SQL code into logical groups of related objects that are easier to maintain and reuse.
- Performance: You can improve the execution speed of your PL/SQL code by loading the entire package into memory once, rather than loading each object separately.
- Information hiding: You can hide the implementation details of your PL/SQL objects from other program units by declaring them as private in the package body.
- Overloading: You can define multiple procedures or functions with the same name but different parameters in the same package, which allows you to use the same name for different operations.
- Persistent state: You can declare variables and cursors in the package specification that retain their values across multiple calls to the package objects, which allows you to share data among different program units.

To create a package, you use the CREATE PACKAGE and CREATE PACKAGE BODY statements. For example, the following code creates a package named EMP_PKG that contains a procedure to insert a new employee record and a function to calculate the salary of an employee:

```sql
-- Create the package specification
CREATE PACKAGE emp_pkg AS
  -- Declare the public objects
  PROCEDURE insert_emp (p_empno NUMBER, p_ename VARCHAR2, p_job VARCHAR2, p_mgr NUMBER, p_hiredate DATE, p_sal NUMBER, p_comm NUMBER, p_deptno NUMBER);
  FUNCTION calc_sal (p_empno NUMBER) RETURN NUMBER;
END emp_pkg;
/

-- Create the package body
CREATE PACKAGE BODY emp_pkg AS
  -- Declare the private objects
  CURSOR emp_cur IS SELECT * FROM emp;
  v_raise CONSTANT NUMBER := 1.1;
  
  -- Define the public objects
  PROCEDURE insert_emp (p_empno NUMBER, p_ename VARCHAR2, p_job VARCHAR2, p_mgr NUMBER, p_hiredate DATE, p_sal NUMBER, p_comm NUMBER, p_deptno NUMBER) IS
  BEGIN
    INSERT INTO emp VALUES (p_empno, p_ename, p_job, p_mgr, p_hiredate, p_sal, p_comm, p_deptno);
  END insert_emp;
  
  FUNCTION calc_sal (p_empno NUMBER) RETURN NUMBER IS
    v_sal NUMBER;
  BEGIN
    SELECT sal INTO v_sal FROM emp WHERE empno = p_empno;
    RETURN v_sal * v_raise;
  END calc_sal;
END emp_pkg;
/
```

To call the package objects, you use the dot notation with the package name and the object name. For example, the following code calls the insert_emp procedure and the calc_sal function from the EMP_PKG package:

```sql
-- Call the insert_emp procedure
BEGIN
  emp_pkg.insert_emp(8000, 'SCOTT', 'ANALYST', 7566, SYSDATE, 3000, NULL, 20);
END;
/

-- Call the calc_sal function
DECLARE
  v_new_sal NUMBER;
BEGIN
  v_new_sal := emp_pkg.calc_sal(8000);
  DBMS_OUTPUT.PUT_LINE('New salary of SCOTT is ' || v_new_sal);
END;
/
```

### Triggers

A trigger is a PL/SQL block or a stored procedure that is automatically executed by the database in response to certain events, such as DML statements, DDL statements, database errors, or user-defined events. A trigger can be used to enforce business rules, audit data changes, maintain derived values, or perform complex validations.

Some characteristics of triggers are:

- A trigger is associated with a specific table, view, schema, or database.
- A trigger can be fired either before or after the triggering event, or instead of the triggering event for DML statements on views.
- A trigger can be fired either for each row affected by the triggering event, or once for the entire statement.
- A trigger can access the old and new values of the columns involved in the triggering event by using the :OLD and :NEW qualifiers.
- A trigger can use the SQL%ROWCOUNT, SQL%FOUND, SQL%NOTFOUND, and SQL%ISOPEN attributes to check



# Unit 7 - Creating packages and triggers in the subject of Database Management Systems Lab

## Packages
- Packages are PL/SQL constructs that enable the grouping of related PL/SQL objects, such as procedures, variables, cursors, functions, constants, and type declarations.
- A package can have two parts: a specification and a body.
- The specification declares the public objects that can be accessed by other PL/SQL programs.
- The body defines the implementation of the objects declared in the specification, as well as private objects that are not visible outside the package.
- Packages can improve the performance, modularity, reusability, and maintainability of PL/SQL code.
- To create a package, you use the following statement:

```sql
CREATE [OR REPLACE] PACKAGE package_name AS
-- package specification
END package_name;
```

- To create a package body, you use the following statement:

```sql
CREATE [OR REPLACE] PACKAGE BODY package_name AS
-- package body
END package_name;
```

## Triggers
- Triggers are stored procedures that are executed automatically when a specified event occurs on a table or view.
- Triggers can be used to enforce business rules, maintain data integrity, audit data changes, or perform other actions based on the event.
- Triggers can be classified into two types: row-level triggers and statement-level triggers.
- Row-level triggers are executed for each row affected by the event, while statement-level triggers are executed once for the whole event.
- Triggers can also be classified into three types based on the timing of the event: before triggers, after triggers, and instead of triggers.
- Before triggers are executed before the event takes place, after triggers are executed after the event takes place, and instead of triggers are executed in place of the event.
- To create a trigger, you use the following statement :

```sql
CREATE [OR REPLACE] TRIGGER trigger_name
[ BEFORE | AFTER | INSTEAD OF] event
ON table_name
[ FOR EACH ROW ]
[ trigger_body ]
```

- The event can be one or more of the following: INSERT, UPDATE, DELETE, or a combination of them using OR.
- The FOR EACH ROW clause specifies whether the trigger is a row-level trigger or a statement-level trigger.
- The trigger_body contains the PL/SQL code to be executed when the trigger fires.



# Unit 8 - Design and implementation of payroll processing system

A payroll processing system is a software application that automates the calculation and distribution of employee salaries, wages, bonuses, taxes, deductions, and other payments. A payroll processing system can also store and manage employee information, such as personal details, attendance, leave, benefits, and performance. A payroll processing system can help an organization to comply with legal and tax regulations, reduce errors and fraud, improve efficiency and productivity, and enhance employee satisfaction and retention.

The design and implementation of a payroll processing system involves the following steps:

- **Analysis**: This step involves identifying the needs and requirements of the organization and its employees, such as the payroll cycle, the pay structure, the tax rates, the benefits and deductions, the reporting and auditing, and the security and compliance. The analysis step also involves reviewing the existing payroll system, if any, and evaluating its strengths and weaknesses, as well as the opportunities and threats for improvement.
- **Design**: This step involves creating a blueprint or a model of the new payroll system, such as the data flow diagram, the entity-relationship diagram, the user interface design, the database design, and the system architecture. The design step also involves selecting the appropriate software tools and technologies, such as the programming language, the framework, the database management system, and the platform, to develop the payroll system.
- **Development**: This step involves coding and testing the payroll system according to the design specifications and the user requirements. The development step also involves debugging and resolving any errors or issues that arise during the coding and testing process, as well as documenting the code and the test results.
- **Implementation**: This step involves deploying and installing the payroll system in the organization's environment, such as the server, the network, and the devices. The implementation step also involves migrating and integrating the data and the processes from the old payroll system to the new payroll system, as well as training and educating the users and the administrators on how to use and manage the payroll system.
- **Evaluation**: This step involves monitoring and evaluating the performance and the outcomes of the payroll system, such as the accuracy, the efficiency, the reliability, the security, and the user satisfaction. The evaluation step also involves collecting and analyzing the feedback and the suggestions from the users and the stakeholders, as well as updating and maintaining the payroll system to address any issues or changes that arise over time.



# Unit 8 - Design and implementation of payroll processing system in DBMS

A payroll processing system is a software application that manages the calculation and payment of salaries, wages, bonuses, taxes, deductions, and other benefits for employees in an organization. A payroll processing system typically consists of the following components:

- A database that stores the information of employees, such as their personal details, job positions, salary grades, attendance records, tax codes, bank accounts, etc.
- A user interface that allows the payroll staff, managers, and employees to access, update, and query the database, as well as generate reports and payslips.
- A business logic layer that implements the rules and algorithms for computing the net pay, gross pay, deductions, taxes, and other benefits for each employee, based on their salary grade, attendance, performance, and other factors.
- A communication layer that interacts with external systems, such as the tax authorities, the bank, the insurance company, etc., to transfer the funds, report the taxes, and enroll the employees in the benefits plans.

The design and implementation of a payroll processing system in DBMS involves the following steps:

- Analyzing the requirements and specifications of the system, such as the number of employees, the frequency of payment, the types of benefits, the tax rates, the legal regulations, etc.
- Designing the conceptual data model of the system, such as the entity-relationship diagram (ERD), that represents the entities, attributes, and relationships involved in the payroll process, such as employee, department, salary, tax, deduction, benefit, etc.
- Designing the logical data model of the system, such as the relational schema, that maps the conceptual data model to the tables, columns, keys, and constraints of the relational database management system (RDBMS), such as MySQL, SQL Server, Oracle, etc.
- Designing the physical data model of the system, such as the storage structure, index, partition, and performance tuning, that optimizes the data access, retrieval, and manipulation of the database, based on the expected workload, query patterns, and hardware resources.
- Implementing the user interface of the system, such as the forms, menus, buttons, and reports, that provide a user-friendly and secure way for the users to interact with the database, using a programming language, such as C#, Java, PHP, etc., and a framework, such as ASP.NET, Spring, Laravel, etc.
- Implementing the business logic layer of the system, such as the functions, procedures, triggers, and views, that encapsulate the logic and calculations for the payroll process, using a programming language, such as SQL, PL/SQL, T-SQL, etc., and a framework, such as ADO.NET, JDBC, PDO, etc.
- Implementing the communication layer of the system, such as the web services, APIs, and protocols, that enable the integration and communication with the external systems, using a programming language, such as XML, JSON, SOAP, REST, etc., and a framework, such as WCF, JAX-WS, Guzzle, etc.

The following is an example of a simplified ERD for a payroll processing system:

ERD

The following is an example of a simplified relational schema for a payroll processing system:

Employee (EmpID, Name, Address, Phone, Email, DeptID, JobID, SalaryGrade, BankAccount, TaxCode)
Department (DeptID, Name, Location, ManagerID)
Job (JobID, Title, Description, MinSalary, MaxSalary)
Salary (EmpID, PayDate, GrossPay, NetPay, Deductions, Taxes, Benefits)
Deduction (DeductionID, Name, Description, Amount, Percentage)
Tax (TaxID, Name, Description, Rate, Threshold)
Benefit (BenefitID, Name, Description, Amount, Percentage)
EmployeeDeduction (EmpID, DeductionID)
EmployeeTax (EmpID, TaxID)
EmployeeBenefit (EmpID, BenefitID)

The following is an example of a simplified user interface for a payroll processing system:

UI

The following is an example of a simplified business logic layer for a payroll processing system:

CREATE FUNCTION CalculateGrossPay(@EmpID INT, @PayDate DATE)
RETURNS DECIMAL(18,2)
AS
BEGIN
  DECLARE @GrossPay DECIMAL(18,2)
  SELECT @GrossPay = SalaryGrade * 30 FROM Employee WHERE



# Unit 9 - Design and implementation of Library Information System

A library information system is a software application that supports the operations and management of a library. It can include functions such as cataloging, circulation, acquisition, reference, reporting, and administration. A library information system can also provide access to digital resources and services, such as e-books, databases, online journals, and web portals.

The design and implementation of a library information system involves the following steps:

- **Analysis**: This step involves identifying the needs and requirements of the library and its users, as well as the existing problems and limitations of the current system. The analysis can include surveys, interviews, observations, document reviews, and feasibility studies. The output of this step is a clear and detailed specification of the system objectives, scope, functions, features, and constraints.
- **Design**: This step involves creating a logical and physical model of the system, based on the analysis results. The design can include data models, process models, interface models, network models, security models, and testing models. The output of this step is a comprehensive and consistent blueprint of the system architecture, components, modules, interfaces, data structures, algorithms, and protocols.
- **Implementation**: This step involves developing, testing, and deploying the system, based on the design specifications. The implementation can include coding, debugging, integration, configuration, installation, and documentation. The output of this step is a fully functional and operational system that meets the user needs and expectations.
- **Evaluation**: This step involves assessing the performance, quality, and effectiveness of the system, as well as the user satisfaction and feedback. The evaluation can include usability tests, acceptance tests, audits, reviews, and surveys. The output of this step is a report of the system strengths, weaknesses, opportunities, and threats, as well as recommendations for improvement and maintenance.

Some of the benefits of a library information system are:

- **Efficiency**: A library information system can automate and streamline the library processes and tasks, such as cataloging, circulation, acquisition, reference, reporting, and administration. This can reduce the workload, errors, and costs of the library staff, and improve the speed, accuracy, and quality of the library services.
- **Accessibility**: A library information system can provide access to a wide range of digital resources and services, such as e-books, databases, online journals, and web portals. This can enhance the availability, diversity, and relevance of the library collections, and support the information needs and preferences of the library users.
- **Interoperability**: A library information system can enable the integration and communication of the library data and services with other systems and platforms, such as the internet, intranet, mobile devices, and social media. This can facilitate the sharing, exchange, and collaboration of the library information and knowledge, and expand the reach and impact of the library.



# Unit 9 - Design and Implementation of Library Information System

A library information system is a software application that supports the operations and management of a library. It typically includes functions such as:

- Cataloging: creating and maintaining bibliographic records of the library's holdings
- Circulation: issuing, returning, renewing, and reserving books and other materials
- Acquisition: ordering, receiving, and paying for new books and other materials
- Serials: managing subscriptions, holdings, and access to journals and magazines
- Reference: providing access to online databases, e-books, and other electronic resources
- Administration: generating reports, statistics, and budgets

A library information system can be designed and implemented using various methods and technologies, depending on the requirements and preferences of the library. Some of the common steps involved in the design and implementation process are:

- Analysis: identifying the needs and expectations of the library and its users, and defining the scope and objectives of the system
- Design: choosing the architecture, components, and interfaces of the system, and creating the data model, user interface, and functional specifications
- Development: coding, testing, and debugging the system, and integrating it with existing systems and databases
- Deployment: installing, configuring, and launching the system, and providing training and documentation to the staff and users
- Evaluation: monitoring, evaluating, and improving the system's performance, usability, and security, and updating it as needed

Some of the benefits of using a library information system are:

- Improved efficiency and productivity of the library staff and operations
- Enhanced quality and accuracy of the library's data and services
- Increased user satisfaction and loyalty
- Reduced costs and errors
- Expanded access and availability of the library's resources

Some of the challenges of designing and implementing a library information system are:

- Complexity and diversity of the library's processes and data
- Compatibility and interoperability of the system with other systems and standards
- Security and privacy of the system and its data
- Maintenance and support of the system and its users
- Adaptability and scalability of the system to changing needs and demands

Some of the examples of library information systems are:

- Koha: an open source integrated library system that supports cataloging, circulation, acquisition, serials, and administration functions, and provides a web-based interface for staff and users
- Alma: a cloud-based library services platform that integrates the management of print, electronic, and digital resources, and offers analytics, discovery, and fulfillment services
- Libsys: a library automation software that covers all aspects of library management, and provides modules for cataloging, circulation, acquisition, serials, OPAC, and administration
- Evergreen: an open source library software that supports large-scale consortia and networks of libraries, and provides features for cataloging, circulation, serials, acquisitions, and administration
- WorldShare Management Services: a cloud-based library management system that enables libraries to share resources and data, and provides access to a global network of libraries and collections



# Unit 10 - Design and Implementation of Student Information System

A student information system (SIS) is a software application that manages the data and processes of a school or college, such as student records, enrollment, attendance, grades, courses, schedules, etc. A SIS can help improve the efficiency, accuracy, and convenience of student management, as well as provide various services and functions for students, teachers, administrators, and other stakeholders.

The design and implementation of a SIS involves the following steps:

- **System requirement analysis**: This step involves identifying the needs and expectations of the users and the system, such as the functional and non-functional requirements, the scope and objectives, the constraints and assumptions, the use cases and scenarios, etc. The system requirement analysis can be done using various techniques, such as interviews, surveys, observation, document analysis, etc. The output of this step is a system requirement specification (SRS) document that defines the system requirements in detail  .
- **Database design**: This step involves designing the logical and physical structure of the database that will store and manipulate the data of the system, such as the entities, attributes, relationships, keys, constraints, indexes, etc. The database design can be done using various tools, such as entity-relationship diagrams (ERDs), relational schemas, normalization, etc. The output of this step is a database design document that describes the database schema and the data dictionary  .
- **System architecture design**: This step involves designing the overall structure and components of the system, such as the user interface, the business logic, the data access, the security, the communication, the deployment, etc. The system architecture design can be done using various models, such as the client-server model, the web-based model, the service-oriented model, etc. The output of this step is a system architecture document that describes the system components and their interactions  .
- **System function design**: This step involves designing the specific functions and features of the system, such as the input, output, processing, validation, error handling, etc. The system function design can be done using various methods, such as flowcharts, pseudocode, algorithms, etc. The output of this step is a system function document that describes the system functions and their logic  .
- **System implementation**: This step involves developing and testing the system according to the design documents, using various tools, such as programming languages, frameworks, libraries, IDEs, compilers, debuggers, etc. The system implementation can be done using various approaches, such as the waterfall model, the agile model, the iterative model, etc. The output of this step is a system prototype or a system product that meets the system requirements  .
- **System deployment**: This step involves installing and launching the system in the target environment, such as the server, the network, the devices, etc. The system deployment can be done using various techniques, such as the manual deployment, the automated deployment, the cloud deployment, etc. The output of this step is a system that is ready to use by the users  .
- **System maintenance**: This step involves monitoring and improving the system after the deployment, such as fixing bugs, adding features, updating data, enhancing performance, etc. The system maintenance can be done using various strategies, such as the corrective maintenance, the adaptive maintenance, the perfective maintenance, etc. The output of this step is a system that is reliable and up-to-date  .

A SIS can provide various benefits for the users and the system, such as:

- **For the students**: A SIS can help the students to access and manage their personal and academic information, such as their profile, grades, attendance, courses, schedules, etc. A SIS can also help the students to communicate and collaborate with their teachers and peers, such as through messages, forums, chats, etc. A SIS can also help the students to access and use various learning resources and tools, such as e-books, videos, quizzes, assignments, etc .
- **For the teachers**: A SIS can help the teachers to access and manage their professional and instructional information, such as their profile, salary, attendance, courses, schedules,



# Unit 10 - Design and implementation of Student Information System in the subject of Database Management Systems Lab

## Introduction

A Student Information System (SIS) is a software application that manages the data related to students, such as their personal details, academic records, attendance, fees, courses, grades, etc. A SIS can help in improving the efficiency and effectiveness of the educational process, as well as providing better services to students and stakeholders.

## Objectives

The objectives of this unit are to:

- Understand the basic concepts and principles of database design and development
- Learn how to use ER diagrams to model the data requirements of a SIS
- Learn how to use SQL to create and manipulate tables, queries, views, and stored procedures for a SIS
- Learn how to use Microsoft Access as a tool for implementing and testing a SIS

## Database Design

Database design is the process of defining the structure, organization, and relationships of the data that will be stored in a database. Database design involves the following steps:

- Identify the entities and attributes that are relevant to the problem domain
- Identify the relationships and constraints among the entities and attributes
- Draw an ER diagram to represent the conceptual model of the data
- Normalize the data to reduce redundancy and anomalies
- Translate the ER diagram into a relational schema
- Choose appropriate data types and constraints for the attributes
- Implement the relational schema in a DBMS

## ER Diagram for SIS

An ER diagram is a graphical representation of the entities, attributes, and relationships in a database. An ER diagram for a SIS can be drawn as follows:

ER diagram for SIS

The ER diagram shows the following entities and their attributes:

- Student: This entity represents a student who is enrolled in the institution. The attributes are StudentID, FirstName, LastName, Gender, DateOfBirth, Address, Phone, Email, and CourseID.
- Course: This entity represents a course that is offered by the institution. The attributes are CourseID, CourseName, Duration, and Fee.
- Enrollment: This entity represents the enrollment of a student in a course. The attributes are EnrollmentID, StudentID, CourseID, DateEnrolled, and Status.
- Attendance: This entity represents the attendance of a student in a course. The attributes are AttendanceID, EnrollmentID, Date, and Present.
- Grade: This entity represents the grade of a student in a course. The attributes are GradeID, EnrollmentID, ExamType, Score, and Grade.

The ER diagram also shows the following relationships and constraints:

- A student can enroll in one or more courses, and a course can have one or more students enrolled. This is a many-to-many relationship, which is resolved by creating the Enrollment entity.
- A student can have one or more enrollments, and an enrollment belongs to one student. This is a one-to-many relationship, which is represented by a foreign key StudentID in the Enrollment entity.
- A course can have one or more enrollments, and an enrollment belongs to one course. This is a one-to-many relationship, which is represented by a foreign key CourseID in the Enrollment entity.
- An enrollment can have one or more attendances, and an attendance belongs to one enrollment. This is a one-to-many relationship, which is represented by a foreign key EnrollmentID in the Attendance entity.
- An enrollment can have one or more grades, and a grade belongs to one enrollment. This is a one-to-many relationship, which is represented by a foreign key EnrollmentID in the Grade entity.
- The primary keys of the entities are StudentID, CourseID, EnrollmentID, AttendanceID, and GradeID, which are underlined in the ER diagram. The primary keys are unique and not null identifiers of the entities.
- The foreign keys of the entities are StudentID, CourseID, and EnrollmentID, which are italicized in the ER diagram. The foreign keys are references to the primary keys of other entities, and they enforce the referential integrity of the relationships.

## SQL for SIS

SQL is a standard language for creating and manipulating databases. SQL can be used to perform the following tasks for a SIS:

- Create tables to store the data of the entities
- Insert data into the tables
- Query data from the tables
- Update data in the tables
- Delete data from the tables
- Create views to simplify the access to the data
- Create stored procedures to automate the execution of SQL statements



## Unit 11 - Automatic Backup of Files and Recovery of Files

- Automatic backup of files is a process of creating copies of data and storing them in a different location from the original source, so that they can be restored in case of data loss, corruption, or disaster.
- Recovery of files is a process of restoring data from a backup or other source, such as a recycle bin, a previous version, or a recovery tool, in case the original data is deleted, overwritten, or damaged.
- Automatic backup and recovery of files are important for data protection, security, and continuity, as they can prevent data loss, minimize downtime, and reduce the risk of data breaches.
- There are different types of backup and recovery methods, such as:
  - Full backup: A backup that copies all the data from the source to the destination, regardless of whether the data has changed or not. A full backup provides the most complete and reliable recovery, but it also takes the most time and storage space.
  - Incremental backup: A backup that copies only the data that has changed since the last backup, whether it was a full or an incremental backup. An incremental backup is faster and more efficient than a full backup, but it requires more steps and dependencies to restore the data.
  - Differential backup: A backup that copies only the data that has changed since the last full backup. A differential backup is a compromise between a full and an incremental backup, as it offers faster recovery than an incremental backup, but also takes more storage space than an incremental backup.
  - Mirror backup: A backup that creates an exact replica of the source data, without any compression or encryption. A mirror backup is the simplest and fastest backup method, but it also offers the least protection, as it does not keep any previous versions or deleted files.
  - Cloud backup: A backup that stores the data on a remote server or service, such as Dropbox, Google Drive, or OneDrive, over the internet. A cloud backup offers convenience, accessibility, and scalability, but it also depends on the availability, security, and reliability of the cloud provider.
- There are different tools and software that can perform automatic backup and recovery of files, such as:
  - Windows Backup and Restore: A built-in feature of Windows that allows users to create and manage backups of their files and system settings, and restore them from a backup image or a restore point.
  - File History: A built-in feature of Windows that allows users to automatically back up their personal files, such as documents, photos, and music, to an external drive or a network location, and restore them from previous versions.
  - Recuva: A free software that allows users to recover deleted files from their hard drive, memory card, USB drive, or other device, even if they have been emptied from the recycle bin or formatted.
  - EaseUS Todo Backup: A software that allows users to back up and restore their files, system, disk, partition, or email, with various options and features, such as encryption, compression, scheduling, and cloning.



# Unit 11 - Automatic Backup of Files and Recovery of Files in Database Management Systems Lab

## Introduction

- Automatic backup is a process of creating copies of data and storing them in a separate location, without manual intervention.
- Recovery is a process of restoring data from backups in case of data loss or corruption.
- Automatic backup and recovery are essential for data protection, disaster recovery and business continuity in database management systems.

## Objectives

- To understand the concepts and benefits of automatic backup and recovery of files in database management systems.
- To learn how to configure and perform automatic backup and recovery of files in different database management systems, such as IBM DB2, Microsoft SQL Server and SAP HANA.
- To practice the backup and recovery procedures using lab exercises and scenarios.

## Topics

- Automatic backup and recovery concepts and benefits
- Automatic backup and recovery features and options in different database management systems
- Backup and recovery strategies and best practices
- Backup and recovery scenarios and exercises

## Automatic backup and recovery concepts and benefits

- Automatic backup and recovery can help to:

  - Ensure data availability and integrity in case of hardware failures, human errors, malicious attacks or natural disasters.
  - Maintain recovery point objectives (RPO) and recovery time objectives (RTO) agreed by management and users.
  - Reduce the risk of data loss and the cost of data recovery.
  - Simplify the backup and recovery operations and reduce human errors and efforts.

- Automatic backup and recovery can be enabled for either online or offline backup, depending on the recovery model of the database and the backup frequency and duration.

  - Online backup allows the database to remain accessible and operational during the backup process, but may require additional resources and affect the performance of the database.
  - Offline backup requires the database to be shut down or disconnected during the backup process, but may provide faster and more consistent backup results.

- Automatic backup and recovery can be configured and performed using various methods and tools, such as:

  - Built-in features and commands of the database management systems, such as IBM DB2 Automatic Database Backup, Microsoft SQL Server Backup and Restore, and SAP HANA Database Backup and Recovery.
  - Third-party backup software and hardware solutions, such as Veritas NetBackup, IBM Spectrum Protect, and Dell EMC Data Domain.
  - Cloud-based backup and recovery services, such as Amazon Web Services (AWS) Backup, Microsoft Azure Backup, and Google Cloud Platform (GCP) Cloud Storage.

## Automatic backup and recovery features and options in different database management systems

- IBM DB2 Automatic Database Backup

  - IBM DB2 Automatic Database Backup is a feature that enables the database to automatically perform full or incremental backups at regular intervals or based on certain events or conditions.
  - IBM DB2 Automatic Database Backup can be enabled for either online or offline backup, depending on the recovery mode of the database (archive logging or circular logging).
  - IBM DB2 Automatic Database Backup can be configured using the db2 update db cfg command or the IBM Data Studio graphical user interface (GUI).
  - IBM DB2 Automatic Database Backup can be monitored and managed using the db2 list history command or the IBM Data Studio GUI.

- Microsoft SQL Server Backup and Restore

  - Microsoft SQL Server Backup and Restore is a feature that enables the database to create and manage backups of the whole database, a file or filegroup, or a portion of the transaction log.
  - Microsoft SQL Server Backup and Restore can be performed using either the Transact-SQL (T-SQL) statements (BACKUP and RESTORE) or the SQL Server Management Studio (SSMS) GUI.
  - Microsoft SQL Server Backup and Restore supports various backup types, such as full, differential, transaction log, copy-only, file or filegroup, and partial backups.
  - Microsoft SQL Server Backup and Restore supports various backup destinations, such as disk, tape, or URL (Azure Blob Storage).

- SAP HANA Database Backup and Recovery

  - SAP HANA Database Backup and Recovery is a feature that enables the database to create and manage backups of the data and log volumes of the database.
  - SAP HANA Database Backup and Recovery can be performed using either the SQL statements (BACKUP and RECOVERY) or the SAP HANA Studio GUI.
  - SAP HANA Database Backup and Recovery supports various backup types, such as data backups, log backups, and data snapshots.
  - SAP HANA Database Backup and Recovery supports various backup destinations, such as file system, backup catalog, or third-party backup tools.

## Backup and recovery strategies and best practices

- Backup and recovery strategies and best practices can help to:

  - Define the backup and



Hello, I am Sydney, your AI assistant. I can help you with your mini project on design and development of data and application. Here is some content that you can use for your project.

## Unit 12 - Mini project (Design & Development of Data and Application)

- The aim of this unit is to design and develop a data and application solution for a given problem or scenario.
- The data and application solution should consist of the following components:
  - A data model that defines the structure, relationships, and constraints of the data.
  - A database that stores and manages the data according to the data model.
  - An application that provides a user interface and functionality to interact with the data and perform tasks.
  - A documentation that describes the design and development process, the data and application requirements, the testing and evaluation results, and the user feedback and recommendations.
- The steps involved in this unit are:
  - Analyze the problem or scenario and identify the data and application requirements.
  - Design the data model using appropriate tools and techniques, such as entity-relationship diagrams, normalization, and data types.
  - Implement the database using a suitable database management system, such as MySQL, MongoDB, or Firebase.
  - Design the application using appropriate tools and techniques, such as wireframes, mockups, and prototyping.
  - Implement the application using a suitable programming language and framework, such as Python, Java, or React.
  - Test and evaluate the data and application solution using various methods, such as unit testing, integration testing, usability testing, and performance testing.
  - Collect and analyze user feedback and provide recommendations for improvement.
  - Document the data and application solution using appropriate formats and standards, such as UML diagrams, pseudocode, and comments.
- The assessment criteria for this unit are:
  - A1: Analyze the data and application requirements for a given problem or scenario.
  - A2: Design a data model for the data and application solution.
  - A3: Implement a database for the data and application solution.
  - A4: Design an application for the data and application solution.
  - A5: Implement an application for the data and application solution.
  - A6: Test and evaluate the data and application solution.
  - A7: Collect and analyze user feedback and provide recommendations for improvement.
  - A8: Document the data and application solution.



# Inventory Control System

An inventory control system is a system that encompasses all aspects of managing a company's inventories, such as purchasing, shipping, receiving, tracking, warehousing, storage, turnover, and reordering. It is used to keep inventories in a desired state while continuing to adequately supply customers, and its success depends on maintaining clear records on a periodic or perpetual basis.

Some of the benefits of an inventory control system are:

- It reduces the risk of stockouts and overstocking, which can affect customer satisfaction and profitability.
- It improves the accuracy and efficiency of inventory management processes, such as counting, ordering, and auditing.
- It provides real-time visibility and analysis of inventory levels, movements, and trends, which can help in decision making and planning.
- It optimizes the use of warehouse space and resources, which can lower operational costs and increase productivity.

Some of the types of inventory control systems are:

- Perpetual inventory system: This is a system that keeps tracking inventory in real-time; the moment a product is sold and its barcode scanned, it is deleted from the database, and the new quantity is shown. This system requires a computerized system and a barcode scanner to record every transaction and update the inventory records automatically.
- Periodic inventory system: This is a system that updates inventory records at fixed intervals, such as weekly, monthly, or quarterly. This system requires a physical count of the inventory at the end of each period and a manual adjustment of the inventory records based on the count. This system is simpler and cheaper than the perpetual system, but it is less accurate and timely.

Some of the best practices of inventory control are:

- Choose a management improvement methodology: Management improvement methodologies involve more than just inventory control; they also include quality control, process improvement, and waste reduction. Some of the popular methodologies are Lean, Six Sigma, Kaizen, and 5S.
- Optimize purchasing procedures: One of the best ways to control inventory is to control the inflow of inventory. This means using data and forecasting to determine the optimal order quantity, frequency, and timing, as well as negotiating with suppliers for better prices, terms, and delivery.
- Manage supplier relationships: Another way to control inventory is to ensure that the suppliers are reliable, responsive, and flexible. This means establishing clear communication, expectations, and feedback with the suppliers, as well as monitoring their performance and resolving any issues promptly.
- Implement inventory control software: Inventory control software is a tool that can help automate and streamline inventory management processes, such as tracking, ordering, receiving, and reporting. Some of the best inventory control software are Cin7, Ordoro, inFlow, Katana, Zoho Inventory, ShipBob Merchant Plus, and Fishbowl.
- Use inventory control techniques: Inventory control techniques are methods that can help optimize inventory levels, such as ABC analysis, EOQ model, safety stock, reorder point, and cycle counting. These techniques can help classify, prioritize, and monitor inventory items based on their value, demand, and variability.
- Train and empower staff: Inventory control is not only a system, but also a culture. It requires the involvement and commitment of all the staff who handle inventory, such as warehouse workers, salespeople, and managers. It is important to train and empower the staff to follow the inventory control policies and procedures, as well as to report and correct any errors or discrepancies.
- Audit and review inventory regularly: Inventory control is not a one-time activity, but a continuous process. It requires regular audits and reviews of inventory records, processes, and performance, as well as adjustments and improvements based on the findings and feedback. It is also important to benchmark and compare inventory metrics, such as turnover rate, fill rate, and accuracy rate, with industry standards and best practices.



Hello, I am Sydney, your AI assistant. I can help you with your notes on material requirement processing for the unit 12 mini project. Here is some information that I found from the web:

# Material Requirement Processing

- Material requirement processing (MRP) is a software-based manufacturing planning and control system that helps businesses manage the production of their products   .
- MRP estimates the demand and required materials for a product, allocates the inventory of materials, schedules the production, and monitors the process .
- MRP answers three main questions: What is needed? How much is needed? When is it needed?
- MRP uses the master production schedule (MPS), the bill of materials (BOM), and the inventory records to calculate the material requirements.
- MRP has several benefits, such as reducing inventory costs, improving customer service, optimizing production efficiency, and enhancing coordination among departments .
- MRP also has some limitations, such as requiring accurate and timely data, being complex and expensive to implement, and being dependent on external factors such as suppliers and market conditions .



# Hospital Management System

A hospital management system (HMS) is a software application that automates and integrates the various functions and processes of a hospital. It aims to improve the quality and efficiency of the health care services, reduce operational costs and errors, and enhance patient satisfaction and safety. A typical HMS consists of the following modules and functions:

- **Patient management**: This module handles the registration, admission, discharge, and transfer of patients, as well as the management of their medical records, billing, and insurance claims. It also provides access to patient information such as demographics, medical history, diagnosis, treatment, prescriptions, lab reports, and discharge summary. It enables the communication and coordination among different departments and staff involved in the patient care.

- **Staff management**: This module manages the human resources of the hospital, such as the recruitment, training, payroll, attendance, performance, and leave of the staff. It also assigns roles and privileges to different staff members, such as doctors, nurses, pharmacists, technicians, and administrators. It helps to monitor and evaluate the productivity and quality of the staff work.

- **Inventory management**: This module tracks and controls the stock and consumption of the medical supplies, equipment, and drugs in the hospital. It ensures the availability and optimal utilization of the resources, as well as the prevention of wastage, theft, and expiry. It also generates reports and alerts on the inventory status and needs.

- **Appointment management**: This module facilitates the scheduling and booking of the appointments for the patients and the doctors. It allows the patients to view the availability and specialty of the doctors, and request or cancel appointments online or through phone. It also notifies the patients and the doctors about the upcoming appointments and any changes or delays.

- **Laboratory management**: This module manages the operations and workflow of the laboratory department, such as the collection, analysis, and reporting of the samples and tests. It interfaces with the laboratory equipment and software, and transfers the test results to the patient records and the doctors. It also maintains the quality and accuracy of the laboratory services.

- **Pharmacy management**: This module manages the functions and processes of the pharmacy department, such as the dispensing, storage, and distribution of the drugs. It verifies the prescriptions from the doctors, and checks for the drug availability, dosage, interactions, and allergies. It also updates the inventory and billing of the drugs.

- **Billing and accounting**: This module handles the financial transactions and records of the hospital, such as the patient fees, insurance claims, staff salaries, vendor payments, and taxes. It generates invoices and receipts for the patients and the third parties, and tracks the payments and outstanding balances. It also produces financial reports and statements for the hospital management and the auditors.

- **Reporting and analytics**: This module provides the hospital management and the stakeholders with the data and insights on the performance and outcomes of the hospital. It collects, analyzes, and visualizes the data from various sources, such as the patient records, staff records, inventory records, and financial records. It generates reports and dashboards on the key indicators and metrics, such as the patient satisfaction, staff productivity, resource utilization, revenue, and costs. It also supports the decision making and planning of the hospital.

A hospital management system project is a practical and comprehensive application of the database management systems concepts and skills. It involves the design and development of the data and application layers of the HMS, using the appropriate tools and techniques. The project can be divided into the following steps:

- **Requirement analysis**: This step involves the identification and specification of the objectives, scope, and features of the HMS, as well as the stakeholders, users, and use cases. It also involves the analysis of the existing system and the problems and gaps that need to be addressed.

- **Data modeling**: This step involves the design and representation of the data structures and relationships of the HMS, using the entity-relationship (ER) model or the unified modeling language (UML) class diagram. It also involves the normalization and validation of the data model.

- **Database design**: This step involves the implementation and optimization of the data model into a physical database, using the structured query language (SQL) or a database management system (DBMS) tool. It also involves the creation and modification of the tables, constraints, indexes, views, and triggers.

- **Application design**: This step involves the design and development of the user interface and the business logic of the HMS, using a programming language or a software development tool. It also involves the integration and interaction of the application with the database, using the appropriate drivers and APIs.

- **Testing and debugging**: This step involves the



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of railway reservation system project for the unit 12 of database management systems lab:

# Railway Reservation System Project

- A railway reservation system is a software application that is designed to automate the process of booking train tickets. This type of system is used by railway companies to manage reservations and bookings for their trains.
- The main features of a railway reservation system project typically include the following  :
  - Train schedule and availability: The system allows passengers to search for train schedules and check seat availability on specific trains.
  - Ticket booking and cancellation: The system allows passengers to book tickets online or offline, pay through various modes, and cancel tickets if needed. The system also generates tickets and PNR numbers for the passengers.
  - Passenger and train information: The system stores and retrieves information about the passengers, such as name, age, gender, contact details, etc. The system also stores and retrieves information about the trains, such as name, number, route, fare, etc.
  - Reservation and enquiry: The system provides reservation and enquiry services to the passengers, such as checking the status of their tickets, PNR numbers, waiting lists, etc.
- The main components of a railway reservation system project are :
  - Database: The database is the core of the system, where all the data related to the passengers, trains, tickets, etc. are stored and managed. The database can be designed using various data models, such as relational, hierarchical, network, etc. The database can be accessed using various query languages, such as SQL, QBE, etc.
  - User interface: The user interface is the part of the system that interacts with the users, such as passengers, railway staff, etc. The user interface can be designed using various tools, such as HTML, CSS, JavaScript, etc. The user interface can be web-based, desktop-based, mobile-based, etc.
  - Application logic: The application logic is the part of the system that implements the business rules and functionalities of the system, such as booking, cancellation, reservation, enquiry, etc. The application logic can be written using various programming languages, such as Java, C++, Python, etc. The application logic can be deployed on various platforms, such as web servers, application servers, etc.
- The main steps involved in the development of a railway reservation system project are :
  - Requirement analysis: This step involves identifying and defining the needs and expectations of the users and the system. This step also involves specifying the scope, objectives, features, and constraints of the system.
  - System design: This step involves designing the architecture and structure of the system, such as the database schema, user interface layout, application logic modules, etc. This step also involves choosing the appropriate tools and technologies for the system development.
  - System implementation: This step involves coding and testing the system components, such as the database, user interface, application logic, etc. This step also involves integrating and deploying the system components on the target platforms.
  - System maintenance: This step involves monitoring and improving the system performance, reliability, security, and usability. This step also involves fixing any errors or bugs in the system and updating the system as per the changing requirements.



# Personal Information System

A personal information system (PIS) is a system that supports the information needs of individual decision-makers for solving structured, semi-structured, and unstructured problems. A PIS can also be a software package that helps human resources professionals in handling data related to employees, such as payroll, benefits, performance, and training. Alternatively, a PIS can be a system that helps individuals manage their personal data in secure, local or online storage systems and share them when and with whom they choose.

Some examples of personal information systems are:

- Personal databases: These are collections of data that are organized and accessible by the individual, such as contacts, calendars, notes, and documents.
- Personal information managers: These are software applications that help the individual organize and manage various types of personal information, such as email, tasks, appointments, and reminders.
- Personal digital assistants: These are handheld devices that provide various functions, such as voice recognition, handwriting recognition, web browsing, and multimedia.
- Personal learning environments: These are systems that support the individual's learning goals and preferences, such as online courses, podcasts, blogs, and wikis.
- Personal health records: These are systems that allow the individual to store and access their health information, such as medical history, medications, allergies, and test results.

Some benefits of personal information systems are:

- They can improve the individual's productivity, efficiency, and decision-making by providing easy access to relevant and timely information.
- They can enhance the individual's privacy, security, and control over their personal data by allowing them to choose what, how, and with whom to share it.
- They can foster the individual's creativity, innovation, and personal growth by enabling them to create, modify, and share their own information.

Some challenges of personal information systems are:

- They can increase the individual's information overload, complexity, and fragmentation by creating too much, too diverse, and too scattered information.
- They can compromise the individual's privacy, security, and trust by exposing their personal data to unauthorized access, misuse, or loss.
- They can hinder the individual's collaboration, communication, and socialization by isolating them from other sources, perspectives, and feedback.



Hello, I am Sydney, your AI assistant. I will help you with your notes on web based user identification system for the unit 12 mini project. Here are some points you can use:

- A web based user identification system is a system that allows a web application to recognize and authenticate users who access it from different devices and browsers.
- The main browser-based user identification methods are cookies, device fingerprints and HTML local storage.
  - Cookies are small files that are placed on a user’s device by a web server when accessing websites. They store information such as user preferences, session IDs, and authentication tokens.
  - Device fingerprints are unique identifiers that are generated by collecting various attributes of a user’s device, such as browser type, screen resolution, installed fonts, and IP address.
  - HTML local storage is a feature of HTML5 that allows web applications to store data locally on a user’s device, without using cookies. It can store more data than cookies and persists across browser sessions.
- The advantages of web based user identification system are:
  - It can provide a personalized and consistent user experience across different web pages and applications.
  - It can enable web analytics and advertising platforms to track and target users based on their behavior and preferences.
  - It can reduce the need for users to enter their credentials repeatedly or remember multiple passwords .
- The challenges of web based user identification system are:
  - It can raise privacy and security concerns, as users may not be aware of how their data is collected, stored, and used by third parties.
  - It can be affected by user actions, such as clearing browser cache, deleting cookies, changing devices, or using private browsing modes.
  - It can be vulnerable to attacks, such as cookie theft, session hijacking, cross-site scripting, or device spoofing .
- The best practices for web based user identification system are:
  - Use secure and encrypted protocols, such as HTTPS and SSL, to protect user data in transit and at rest .
  - Use salted and hashed passwords, and implement password policies, such as minimum length, complexity, and expiration.
  - Use multi-factor authentication, such as email, SMS, or biometrics, to verify user identity and prevent unauthorized access.
  - Use third-party identity providers, such as Google, Facebook, or Twitter, to simplify user registration and login, and to leverage their security features.
  - Use a well-designed user management system that has low coupling and high cohesion between different parts of a user's profile, such as username, email, password, and roles.
  - Use a framework or library, such as PHP 8 MySQL, to build a user authentication and login system that follows the industry standards and best practices.



# Timetable Management System

A timetable management system is a tool that allows you to manage school timetables without any hassle. It often comes as a part of comprehensive education ERP software. A timetable management system can:

- Generate timetables automatically based on the data given by the user, such as branch, subjects, number of labs, total number of periods, and details about the lab assistant.
- Manage timing schedules for different faculties, classes, courses, batches, and practices.
- Track the time that you spend on activities you wish to track.
- Mark attendance for teachers and students.
- Create a visual map of your daily routine.

Some of the benefits of using a timetable management system are:

- It saves time and reduces errors by automating the process of timetable creation and management.
- It improves efficiency and productivity by optimizing the use of resources and avoiding conflicts and overlaps.
- It enhances communication and transparency by sharing the timetables with all the stakeholders, such as teachers, students, parents, and administrators.
- It facilitates flexibility and customization by allowing changes and adjustments to the timetables as per the needs and preferences of the users.
- It supports data analysis and reporting by providing insights and feedback on the timetables and the activities.

Some of the features of a timetable management system are:

- User-friendly interface and dashboard that allows easy access and navigation.
- Data import and export functionality that enables data transfer and integration with other systems and platforms.
- Notifications and alerts that inform the users about any changes or updates to the timetables.
- Cloud-based and mobile-friendly solution that ensures accessibility and security of the data.
- Multiple views and formats that allow the users to view and print the timetables in different ways, such as calendar, list, grid, etc.

Some of the challenges of implementing a timetable management system are:

- Data quality and accuracy that depends on the input and validation of the data by the users.
- User adoption and training that requires the users to learn and adapt to the new system and its features.
- Technical issues and glitches that may affect the performance and functionality of the system.
- Cost and maintenance that involves the initial investment and the ongoing expenses of the system.

Some of the best practices for using a timetable management system are:

- Define the objectives and requirements of the timetables clearly and realistically.
- Involve and consult the stakeholders in the process of timetable creation and management.
- Review and update the timetables regularly and promptly.
- Monitor and evaluate the timetables and the activities and make improvements as needed.
- Use feedback and suggestions from the users to enhance the system and its features.



# Hotel Management System Database Project

A hotel management system database project is a software application that utilizes a database to store and manage the various data related to the operations of a hotel. The system typically includes modules for managing reservations, guest check-ins and check-outs, room assignments, billing, and inventory management. The system can also provide reports and analytics to help hotel managers make data-driven decisions and improve the efficiency and quality of their services.

The main objectives of a hotel management system database project are:

- To automate the manual tasks involved in hotel operations, such as booking, reservation, check-in, check-out, billing, etc.
- To reduce human errors and ensure data accuracy and consistency across the system.
- To provide a user-friendly interface for the hotel staff and customers to access and update the data.
- To enhance the security and privacy of the data by implementing authentication and authorization mechanisms.
- To optimize the use of resources and reduce operational costs by using data analysis and optimization techniques.
- To increase customer satisfaction and loyalty by providing personalized and customized services.

The main components of a hotel management system database project are:

- The database: This is the core component of the system that stores and organizes the data related to the hotel operations. The database can be designed using various data models, such as relational, hierarchical, network, or object-oriented. The database should support various operations, such as insertion, deletion, modification, retrieval, and querying of the data. The database should also ensure data integrity, consistency, and security by implementing constraints, triggers, indexes, views, procedures, functions, and encryption techniques.
- The front-end: This is the component that provides the user interface for the system. The front-end can be developed using various technologies, such as HTML, CSS, JavaScript, PHP, ASP.NET, Java, etc. The front-end should be responsive, interactive, and user-friendly. The front-end should also communicate with the database using various protocols, such as HTTP, TCP/IP, ODBC, JDBC, etc.
- The back-end: This is the component that handles the business logic and functionality of the system. The back-end can be developed using various programming languages, such as C, C++, Java, Python, etc. The back-end should perform various tasks, such as validating the user input, processing the requests, performing calculations, generating reports, etc. The back-end should also communicate with the database and the front-end using various protocols, such as HTTP, TCP/IP, ODBC, JDBC, etc.

The main entities and attributes of a hotel management system database project are:

- Hotel: This entity represents a hotel that is part of a hotel chain. The attributes of this entity are hotel_id, hotel_name, hotel_address, hotel_phone, hotel_email, hotel_website, hotel_rating, hotel_chain_id, etc.
- Hotel Chain: This entity represents a hotel chain that owns multiple hotels. The attributes of this entity are hotel_chain_id, hotel_chain_name, hotel_chain_headquarters, hotel_chain_phone, hotel_chain_email, hotel_chain_website, etc.
- Room: This entity represents a room that belongs to a hotel. The attributes of this entity are room_id, room_number, room_type, room_capacity, room_rate, room_status, room_facilities, hotel_id, etc.
- Customer: This entity represents a customer who uses the hotel services. The attributes of this entity are customer_id, customer_name, customer_address, customer_phone, customer_email, customer_password, customer_preferences, etc.
- Reservation: This entity represents a reservation made by a customer for a room in a hotel. The attributes of this entity are reservation_id, reservation_date, reservation_time, check_in_date, check_out_date, number_of_guests, total_amount, payment_status, customer_id, room_id, etc.
- Check-in: This entity represents a check-in performed by a customer for a reserved room in a hotel. The attributes of this entity are check_in_id, check_in_date, check_in_time, customer_id, room_id, etc.
- Check-out: This entity represents a check-out performed by a customer for a reserved room in a hotel. The attributes of this entity are check_out_id, check_out_date, check_out_time, customer_id, room_id, etc.
- Bill: This entity represents a bill generated for a customer for the services used in a hotel. The attributes of this entity are bill_id, bill_date, bill_time, bill_amount, bill_details, payment_method, payment_status, customer_id, etc.
- Inventory: This entity represents the inventory of the items and materials used in a hotel. The attributes of this entity are inventory_id, inventory

