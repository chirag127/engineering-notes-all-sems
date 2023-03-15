# Built-in functions

Built-in functions are expressions in which an SQL keyword or special operator executes some operation. They can be used in SQL SELECT expressions to calculate values and manipulate data. They can also be used in other SQL statements, such as WHERE, GROUP BY, HAVING, ORDER BY, etc.

There are different types of built-in functions in SQL, such as:

- **String functions**: These functions perform operations on string values, such as concatenation, extraction, conversion, etc. Some examples are ASCII, CHAR, CHARINDEX, CONCAT, LEFT, RIGHT, etc.
- **Numeric functions**: These functions perform calculations on numeric values, such as arithmetic, rounding, trigonometry, etc. Some examples are ABS, CEILING, FLOOR, POWER, SQRT, SIN, COS, etc.
- **Date and time functions**: These functions perform operations on date and time values, such as extraction, conversion, addition, subtraction, etc. Some examples are DATEADD, DATEDIFF, DATEPART, GETDATE, YEAR, MONTH, DAY, etc.
- **Conversion functions**: These functions convert values from one data type to another, such as numeric, string, date, etc. Some examples are CAST, CONVERT, PARSE, TRY_CAST, TRY_CONVERT, etc.
- **Aggregate functions**: These functions perform a calculation on a set of values and return a single value. They are often used with the GROUP BY clause to group rows into categories and apply a summary function to each group. Some examples are AVG, COUNT, MAX, MIN, SUM, etc.
- **Analytic functions**: These functions compute an aggregate value based on a group of rows. However, unlike aggregate functions, they do not reduce the number of rows returned by the query. They are often used with the OVER clause to specify the partitioning and ordering of the rows. Some examples are ROW_NUMBER, RANK, DENSE_RANK, NTILE, LAG, LEAD, etc.
- **Bit manipulation functions**: These functions perform bitwise operations on binary values, such as AND, OR, XOR, NOT, etc. Some examples are BITAND, BITOR, BITXOR, BITNOT, etc.
- **System functions**: These functions return information about the system, such as the current user, database, session, etc. Some examples are CURRENT_USER, DB_NAME, HOST_NAME, SESSION_USER, etc.