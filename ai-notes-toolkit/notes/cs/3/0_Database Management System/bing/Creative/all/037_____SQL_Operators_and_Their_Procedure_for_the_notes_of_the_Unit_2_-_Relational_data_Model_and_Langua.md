# SQL Operators and Their Procedure

SQL operators are symbols or keywords that are used to perform operations on values or expressions in SQL statements. They are used to specify conditions, filter results, perform calculations, or manipulate strings. SQL operators can be classified into six types:

- Arithmetic operators: These operators are used for mathematical operations on numerical data, such as adding, subtracting, multiplying, or dividing. For example, `SELECT 10 + 10;` returns 20.
- Comparison operators: These operators are used to compare two values or expressions and return a Boolean value (true or false). For example, `SELECT 10 > 5;` returns true.
- Logical operators: These operators are used to combine two or more conditions and return a Boolean value. For example, `SELECT 10 > 5 AND 10 < 20;` returns true.
- Bitwise operators: These operators are used to perform bitwise operations on binary data, such as AND, OR, XOR, or NOT. For example, `SELECT 10 & 5;` returns 0.
- String operators: These operators are used to manipulate strings, such as concatenating, extracting, or replacing. For example, `SELECT 'Hello' + 'World';` returns HelloWorld.
- Set operators: These operators are used to combine the results of two or more queries into one result set, such as UNION, INTERSECT, or EXCEPT. For example, `SELECT name FROM table1 UNION SELECT name FROM table2;` returns the names from both tables without duplicates.

The procedure for using SQL operators is to place them between the values or expressions that they operate on, and follow the syntax rules of the SQL clause that they are used in. For example, in the WHERE clause, the operators must be enclosed in parentheses if they have lower precedence than other operators. For example, `SELECT * FROM table WHERE (10 + 10) > 15;` returns the rows where the sum of 10 and 10 is greater than 15.