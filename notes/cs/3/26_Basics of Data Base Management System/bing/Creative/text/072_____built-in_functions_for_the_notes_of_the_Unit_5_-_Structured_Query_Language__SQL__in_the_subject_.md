### Built-in functions for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- A built-in function is an expression in which an SQL keyword or special operator executes some operation.
- Built-in functions use keywords that are case-insensitive and can be used anywhere expressions are allowed.
- Built-in functions can be categorized into different types based on their functionality and input/output data types   .
- Some of the common types of built-in functions are:

  - **String functions**: These functions perform operations on string values, such as concatenation, extraction, conversion, searching, etc. Some examples are ASCII, CHAR, CHARINDEX, CONCAT, LEFT, RIGHT, REPLACE, etc .
  - **Numeric functions**: These functions perform calculations on numeric values, such as rounding, truncating, finding absolute value, etc. Some examples are ABS, CEILING, FLOOR, POWER, ROUND, SQRT, etc .
  - **Date and time functions**: These functions manipulate or extract information from date and time values, such as finding the current date, adding or subtracting intervals, formatting, etc. Some examples are DATEADD, DATEDIFF, DATEPART, GETDATE, YEAR, MONTH, DAY, etc .
  - **Conversion functions**: These functions convert values from one data type to another, such as converting a string to a number, a date to a string, etc. Some examples are CAST, CONVERT, PARSE, TRY_CAST, TRY_CONVERT, etc .
  - **Logical functions**: These functions evaluate logical expressions and return a Boolean value (TRUE, FALSE, or UNKNOWN), such as checking for null values, comparing values, etc. Some examples are COALESCE, IIF, ISNULL, NULLIF, etc .
  - **Aggregate functions**: These functions perform a calculation on a set of values and return a single value, such as finding the sum, average, count, minimum, maximum, etc. Some examples are AVG, COUNT, MAX, MIN, SUM, etc  .
  - **Analytic functions**: These functions compute an aggregate value based on a group of rows, but unlike aggregate functions, they do not reduce the number of rows returned. They can also perform ranking, windowing, and other complex calculations. Some examples are CUME_DIST, DENSE_RANK, LAG, LEAD, NTILE, PERCENT_RANK, RANK, ROW_NUMBER, etc .
  - **Bit manipulation functions**: These functions perform bitwise operations on binary values, such as shifting, rotating, anding, oring, etc. Some examples are BITAND, BITOR, BITXOR, BITNOT, etc.
  - **System functions**: These functions return information about the system, such as the current user, the current database, the current session, etc. Some examples are CURRENT_USER, DB_NAME, HOST_NAME, SESSION_USER, etc .

- To use a built-in function, you need to specify the function name followed by parentheses, and optionally provide arguments inside the parentheses, depending on the function.
- For example, to use the CONCAT function to concatenate two strings, you can write:

  ```sql
  SELECT CONCAT('Hello', 'World');
  ```

- To use the AVG function to find the average salary of employees, you can write:

  ```sql
  SELECT AVG(salary) FROM employees;
  ```

- To use the RANK function to rank the employees by their salary, you can write:

  ```sql
  SELECT name, salary, RANK() OVER (ORDER BY salary DESC) AS rank FROM employees;
  ```