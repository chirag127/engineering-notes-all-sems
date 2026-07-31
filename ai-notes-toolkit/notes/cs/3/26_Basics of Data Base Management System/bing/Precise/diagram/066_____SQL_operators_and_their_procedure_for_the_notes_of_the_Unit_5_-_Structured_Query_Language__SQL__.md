### SQL Operators and their Procedure

SQL (Structured Query Language) is a standard language used to manage and manipulate data stored in relational databases. SQL operators are used to perform operations on data within the database. Here are some common SQL operators and their procedures:

1. **Arithmetic Operators**: These operators are used to perform mathematical operations on numeric data. The basic arithmetic operators in SQL are `+` (addition), `-` (subtraction), `*` (multiplication), and `/` (division). For example, to calculate the total salary of an employee, you can use the following SQL statement: `SELECT salary + bonus AS total_salary FROM employees;`

2. **Comparison Operators**: These operators are used to compare values in a database. The basic comparison operators in SQL are `=` (equal to), `<>` (not equal to), `>` (greater than), `<` (less than), `>=` (greater than or equal to), and `<=` (less than or equal to). For example, to find all employees with a salary greater than 50000, you can use the following SQL statement: `SELECT * FROM employees WHERE salary > 50000;`

3. **Logical Operators**: These operators are used to combine multiple conditions in a WHERE clause. The basic logical operators in SQL are `AND`, `OR`, and `NOT`. For example, to find all employees with a salary greater than 50000 and a bonus greater than 10000, you can use the following SQL statement: `SELECT * FROM employees WHERE salary > 50000 AND bonus > 10000;`

4. **Set Operators**: These operators are used to combine the results of two or more SELECT statements. The basic set operators in SQL are `UNION`, `INTERSECT`, and `EXCEPT`. For example, to find all employees who are either in the sales department or have a salary greater than 50000, you can use the following SQL statement: `(SELECT * FROM employees WHERE department = 'sales') UNION (SELECT * FROM employees WHERE salary > 50000);`

These are some of the basic SQL operators and their procedures. It is important to understand and use these operators correctly to effectively manipulate and manage data in a relational database.