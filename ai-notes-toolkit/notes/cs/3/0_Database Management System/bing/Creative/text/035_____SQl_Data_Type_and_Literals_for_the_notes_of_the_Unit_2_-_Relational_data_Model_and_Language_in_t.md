### SQL Data Types and Literals

SQL data types are used to represent the nature of the data that can be stored in the database table. Every field or column in a table is given a data type when a table is defined. These data types describe the kind of information which can be stored in a column .

SQL literals are the values that are used to represent a constant value in a SQL statement. They are also known as constants. There are four kinds of literal values supported in SQL. They are:

- Character string: A sequence of characters enclosed by single quotes, such as 'Hello' or 'SQL'.
- Bit string: A sequence of binary digits (0 or 1) enclosed by single quotes, such as '1010' or '0011'.
- Exact numeric: A decimal number with a fixed precision and scale, such as 123.45 or 0.01.
- Approximate numeric: A floating-point number with an approximate precision and scale, such as 1.23E4 or 3.14E-2.

Some examples of SQL literals are:

- SELECT 'Hello' AS Greeting;
- SELECT '1010' AS BitString;
- SELECT 123.45 AS ExactNumeric;
- SELECT 1.23E4 AS ApproximateNumeric;

Some of the common SQL data types are :

- CHAR(n): A fixed-length character string of n characters, where n is a positive integer.
- VARCHAR(n): A variable-length character string of up to n characters, where n is a positive integer.
- INT: An integer number with a range of -2,147,483,648 to 2,147,483,647.
- DECIMAL(p, s): A decimal number with a precision of p digits and a scale of s digits, where p and s are positive integers.
- FLOAT(n): A floating-point number with a precision of n bits, where n is a positive integer.
- DATE: A date value in the format of YYYY-MM-DD, such as 2021-12-31.
- TIME: A time value in the format of HH:MM:SS, such as 23:59:59.
- DATETIME: A combination of date and time values, such as 2021-12-31 23:59:59.

Some examples of SQL data types are:

- CREATE TABLE Employee (Name CHAR(20), Salary DECIMAL(10, 2));
- INSERT INTO Employee VALUES ('Alice', 5000.00);
- SELECT Name, Salary FROM Employee WHERE Salary > 4000.00;