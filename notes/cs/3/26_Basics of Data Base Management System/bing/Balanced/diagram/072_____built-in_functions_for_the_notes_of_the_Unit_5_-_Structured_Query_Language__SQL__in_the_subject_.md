### Built-in functions

- Built-in functions are expressions in SQL that perform some operation on one or more values and return a single value.
- Built-in functions can be used in SQL SELECT expressions, WHERE clauses, ORDER BY clauses, and other SQL statements.
- Built-in functions can be categorized into different types based on their functionality and input/output data types.
- Some of the common types of built-in functions are:

  - **String functions**: These functions manipulate character data, such as concatenating, trimming, replacing, or converting strings. Examples of string functions are `CONCAT`, `LEFT`, `REPLACE`, and `UPPER`.
  - **Numeric functions**: These functions perform mathematical calculations on numeric data, such as finding the absolute value, rounding, or trigonometric functions. Examples of numeric functions are `ABS`, `ROUND`, `SIN`, and `SQRT`.
  - **Date and time functions**: These functions manipulate date and time data, such as extracting parts of a date, adding or subtracting intervals, or formatting dates. Examples of date and time functions are `DATEPART`, `DATEDIFF`, `GETDATE`, and `FORMAT`.
  - **Conversion functions**: These functions convert data from one data type to another, such as converting a string to a number, or a date to a string. Examples of conversion functions are `CAST`, `CONVERT`, `PARSE`, and `TRY_CONVERT`.
  - **Aggregate functions**: These functions perform a calculation on a set of values and return a single value, such as finding the sum, average, minimum, or maximum of a column. Examples of aggregate functions are `SUM`, `AVG`, `MIN`, and `MAX`.
  - **Analytic functions**: These functions compute an aggregate value based on a group of rows, but unlike aggregate functions, they return multiple rows with the same or different values. Examples of analytic functions are `ROW_NUMBER`, `RANK`, `LAG`, and `LEAD`.
  - **Bit manipulation functions**: These functions perform bitwise operations on binary data, such as shifting, rotating, or masking bits. Examples of bit manipulation functions are `BITAND`, `BITOR`, `BITNOT`, and `BITXOR`.
  - **System functions**: These functions return information about the system, such as the current user, session, database, or server. Examples of system functions are `USER`, `SESSION_ID`, `DB_NAME`, and `SERVERPROPERTY`.

- To use a built-in function, you need to specify the function name followed by parentheses, and optionally provide one or more arguments inside the parentheses, separated by commas. For example:

  - `SELECT UPPER(name) FROM customers;` -- This uses the `UPPER` string function to convert the name column to uppercase.
  - `SELECT ROUND(price, 2) FROM products;` -- This uses the `ROUND` numeric function to round the price column to two decimal places.
  - `SELECT FORMAT(order_date, 'yyyy-MM-dd') FROM orders;` -- This uses the `FORMAT` date and time function to format the order_date column as a string in the specified format.
  - `SELECT CAST(age AS VARCHAR) FROM employees;` -- This uses the `CAST` conversion function to convert the age column from an integer to a string.
  - `SELECT SUM(quantity) FROM order_details;` -- This uses the `SUM` aggregate function to calculate the total quantity of all order details.
  - `SELECT RANK() OVER (ORDER BY salary DESC) FROM employees;` -- This uses the `RANK` analytic function to assign a rank to each employee based on their salary in descending order.
  - `SELECT BITAND(flags, 1) FROM settings;` -- This uses the `BITAND` bit manipulation function to perform a bitwise AND operation on the flags column and the value 1.
  - `SELECT USER();` -- This uses the `USER` system function to return the current user name.