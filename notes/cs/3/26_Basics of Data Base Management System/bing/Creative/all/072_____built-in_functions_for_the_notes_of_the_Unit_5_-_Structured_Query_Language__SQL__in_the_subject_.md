# Built-in functions

Built-in functions are expressions in which an SQL keyword or special operator executes some operation. They can be used in SQL SELECT expressions to calculate values and manipulate data. They can also be used in other SQL statements, such as WHERE, GROUP BY, HAVING, ORDER BY, etc.

There are different types of built-in functions in SQL, such as:

- **String functions**: These functions perform operations on string values, such as concatenation, extraction, conversion, etc. Some examples of string functions are ASCII, CHAR, CHARINDEX, CONCAT, LEFT, RIGHT, etc.
- **Numeric functions**: These functions perform mathematical operations on numeric values, such as rounding, truncating, finding the absolute value, etc. Some examples of numeric functions are ABS, CEILING, FLOOR, POWER, ROUND, SQRT, etc.
- **Date and time functions**: These functions perform operations on date and time values, such as extracting parts of a date, adding or subtracting intervals, converting formats, etc. Some examples of date and time functions are DATEADD, DATEDIFF, DATEPART, GETDATE, YEAR, MONTH, DAY, etc.
- **Conversion functions**: These functions convert a value from one data type to another, such as from string to numeric, from numeric to date, etc. Some examples of conversion functions are CAST, CONVERT, PARSE, TRY_CAST, TRY_CONVERT, etc.
- **Aggregate functions**: These functions perform a calculation on a set of values and return a single value. They are often used with the GROUP BY clause to summarize data. Some examples of aggregate functions are AVG, COUNT, MAX, MIN, SUM, etc.
- **Analytic functions**: These functions compute an aggregate value based on a group of rows. However, unlike aggregate functions, they do not reduce the number of rows returned by the query. They are often used with the OVER clause to partition the data and apply a window function. Some examples of analytic functions are ROW_NUMBER, RANK, DENSE_RANK, NTILE, LAG, LEAD, etc.
- **Bit manipulation functions**: These functions perform bitwise operations on binary values, such as shifting, rotating, anding, oring, etc. Some examples of bit manipulation functions are BITAND, BITOR, BITXOR, BITNOT, BITLSHIFT, BITRSHIFT, etc.
- **System functions**: These functions return information about the system, such as the current user, the current database, the current session, etc. Some examples of system functions are USER, DATABASE, SESSION_USER, @@VERSION, @@ROWCOUNT, @@ERROR, etc.

: https://www.tutorialsteacher.com/sqlserver/builtin-functions