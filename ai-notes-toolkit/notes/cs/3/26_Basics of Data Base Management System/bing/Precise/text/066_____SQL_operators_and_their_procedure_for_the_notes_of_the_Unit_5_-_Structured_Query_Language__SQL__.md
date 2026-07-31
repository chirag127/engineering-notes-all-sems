### SQL Operators and their Procedure

SQL operators are used to perform operations on data stored in a database. These operators can be used in the `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements. Here are some common SQL operators and their procedures:

1. **Arithmetic Operators**: These operators are used to perform mathematical calculations on numeric data. The arithmetic operators in SQL are `+`, `-`, `*`, and `/`. For example, to calculate the total salary of an employee, including a bonus, you could use the following statement: `SELECT salary + bonus AS total_salary FROM employees;`

2. **Comparison Operators**: These operators are used to compare values in a database. The comparison operators in SQL are `=`, `<>`, `>`, `<`, `>=`, and `<=`. For example, to find all employees with a salary greater than 50000, you could use the following statement: `SELECT * FROM employees WHERE salary > 50000;`

3. **Logical Operators**: These operators are used to combine multiple conditions in a `WHERE` clause. The logical operators in SQL are `AND`, `OR`, and `NOT`. For example, to find all employees with a salary greater than 50000 and a bonus greater than 1000, you could use the following statement: `SELECT * FROM employees WHERE salary > 50000 AND bonus > 1000;`

4. **String Operators**: These operators are used to manipulate string data. The string operators in SQL are `||` (concatenation), `LENGTH()`, `UPPER()`, `LOWER()`, `LTRIM()`, `RTRIM()`, and `SUBSTR()`. For example, to concatenate the first and last name of an employee, you could use the following statement: `SELECT first_name || ' ' || last_name AS full_name FROM employees;`

These are some of the common SQL operators and their procedures. They can be used in various combinations to perform complex operations on data stored in a database. It is important to understand the use of these operators to effectively retrieve and manipulate data in a database.