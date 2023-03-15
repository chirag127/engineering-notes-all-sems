# SQL Data Types and Literals

## SQL Data Types
- SQL data types are used to represent the nature of the data that can be stored in the database table .
- Every field or column in a table is given a data type when a table is defined .
- SQL data types can be categorized into the following groups:
  - Numeric: for storing numbers, such as `INT`, `FLOAT`, `DECIMAL`, etc.
  - Character: for storing text, such as `CHAR`, `VARCHAR`, `TEXT`, etc.
  - Date and time: for storing date and time values, such as `DATE`, `TIME`, `DATETIME`, etc.
  - Binary: for storing binary data, such as `BINARY`, `VARBINARY`, `IMAGE`, etc.
  - Other: for storing special types of data, such as `BOOLEAN`, `XML`, `JSON`, etc.
- Different database systems may support different data types or have different names for the same data type.
- For example, SQL Server supports a data type called `sql_variant` that can store up to 8,000 bytes of data of various data types.
- SQL data types are important for ensuring data integrity, performance, and compatibility.

## SQL Literals
- SQL literals are constants that represent fixed values in SQL statements .
- SQL literals can be used in expressions, conditions, assignments, or as arguments to functions .
- There are four kinds of literal values supported in SQL :
  - Character string: for representing text values, enclosed in single quotes, such as `'Hello'`, `'SQL'`, etc.
  - Bit string: for representing binary values, prefixed with `B` or `0b`, such as `B'1010'`, `0b1100`, etc.
  - Exact numeric: for representing integer or decimal values, such as `42`, `3.14`, etc.
  - Approximate numeric: for representing floating-point values, using scientific notation, such as `1.23E4`, `6.02E-23`, etc.
- SQL literals can also be modified by collation, which specifies the rules for sorting and comparing character data.
- For example, `'SQL' COLLATE Latin1_General_CS_AS` is a character string literal with a case-sensitive and accent-sensitive collation.