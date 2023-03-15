### Built-in functions

Built-in functions are expressions that perform some operation using SQL keywords or special operators. They can be used in SQL SELECT statements to calculate values and manipulate data. They can also be used in other SQL clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, etc.

There are different types of built-in functions in SQL, depending on the purpose and the data type they operate on. Some of the common types are:

- **Aggregate functions**: These functions perform a calculation on a set of values and return a single value. They are often used with the GROUP BY clause to summarize data. Examples of aggregate functions are SUM, AVG, MIN, MAX, COUNT, etc.
- **Analytic functions**: These functions compute an aggregate value based on a group of rows, but unlike aggregate functions, they do not reduce the number of rows in the result. They are often used with the OVER clause to partition the data and apply a window function. Examples of analytic functions are RANK, ROW_NUMBER, LAG, LEAD, etc.
- **String functions**: These functions perform various operations on string values, such as concatenation, extraction, replacement, conversion, etc. Examples of string functions are CONCAT, SUBSTRING, REPLACE, UPPER, LOWER, etc.
- **Numeric functions**: These functions perform various operations on numeric values, such as arithmetic, rounding, truncation, conversion, etc. Examples of numeric functions are ABS, CEILING, FLOOR, POWER, SQRT, CAST, etc.
- **Date and time functions**: These functions perform various operations on date and time values, such as extraction, addition, subtraction, conversion, formatting, etc. Examples of date and time functions are GETDATE, DATEADD, DATEDIFF, DATEPART, FORMAT, etc.
- **Logical functions**: These functions perform various operations on logical values, such as comparison, negation, conjunction, disjunction, etc. Examples of logical functions are AND, OR, NOT, IF, CASE, etc.
- **Bit manipulation functions**: These functions perform various operations on bit values, such as shifting, rotating, masking, etc. Examples of bit manipulation functions are BITAND, BITOR, BITNOT, BITXOR, etc.

The syntax and usage of each built-in function may vary depending on the SQL dialect and the database system. Therefore, it is important to consult the documentation of the specific SQL server or database management system for more details and examples.