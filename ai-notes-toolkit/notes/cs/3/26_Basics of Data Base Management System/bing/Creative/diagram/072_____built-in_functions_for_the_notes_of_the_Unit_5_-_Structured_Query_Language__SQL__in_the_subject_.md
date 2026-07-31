Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on SQL built-in functions for your notes.

### Built-in functions

- Built-in functions are expressions that perform some operation using SQL keywords or special operators.
- Built-in functions can be used anywhere expressions are allowed, such as in SELECT, WHERE, GROUP BY, HAVING, ORDER BY clauses.
- Built-in functions can be categorized into different types based on their functionality and input/output data types   .
- Some of the common types of built-in functions are:

  - **String functions**: These functions manipulate character data, such as concatenating, searching, replacing, converting, etc. Some examples are ASCII, CHAR, CHARINDEX, CONCAT, LEFT, RIGHT, LEN, LOWER, UPPER, REPLACE, SUBSTRING, etc  .
  - **Numeric functions**: These functions perform mathematical operations on numeric data, such as rounding, truncating, calculating absolute value, logarithm, power, etc. Some examples are ABS, CEILING, FLOOR, ROUND, SQRT, LOG, POWER, RAND, etc  .
  - **Date and time functions**: These functions manipulate date and time data, such as extracting, adding, subtracting, formatting, converting, etc. Some examples are DATEADD, DATEDIFF, DATEPART, GETDATE, GETUTCDATE, SYSDATETIME, CONVERT, FORMAT, etc  .
  - **Conversion functions**: These functions convert data from one data type to another, such as from string to numeric, from numeric to date, from date to string, etc. Some examples are CAST, CONVERT, PARSE, TRY_CAST, TRY_CONVERT, TRY_PARSE, etc  .
  - **Aggregate functions**: These functions perform a calculation on a set of values and return a single value, such as sum, average, count, minimum, maximum, etc. Some examples are SUM, AVG, COUNT, MIN, MAX, etc   .
  - **Analytic functions**: These functions compute an aggregate value based on a group of rows, but unlike aggregate functions, they do not reduce the number of rows returned. They can also perform ranking, windowing, and lag/lead operations. Some examples are ROW_NUMBER, RANK, DENSE_RANK, NTILE, LAG, LEAD, FIRST_VALUE, LAST_VALUE, etc   .
  - **Bit manipulation functions**: These functions perform bitwise operations on binary data, such as shifting, rotating, anding, oring, xoring, etc. Some examples are BITAND, BITOR, BITXOR, BITNOT, BITLSHIFT, BITRSHIFT, etc .
  - **System functions**: These functions return information about the system, such as the current user, the current database, the current session, the server name, the version, etc. Some examples are USER, DATABASE, SESSION_USER, @@SPID, @@SERVERNAME, @@VERSION, etc  .

- The syntax and usage of each built-in function may vary depending on the SQL server and version. It is advisable to check the official documentation for the specific function before using it   .