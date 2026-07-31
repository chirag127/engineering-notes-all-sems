### SQL Data Types and Literals

- SQL data types are used to represent the nature of the data that can be stored in the database table. Every field or column in a table is given a data type when a table is defined .
- SQL data types can be categorized into the following groups:
  - Numeric: These data types store numeric values, such as integers, decimals, and floating-point numbers. Examples are `INT`, `DECIMAL`, `FLOAT`, etc.
  - Character: These data types store character strings, such as names, addresses, and descriptions. Examples are `CHAR`, `VARCHAR`, `TEXT`, etc.
  - Date and time: These data types store date and time values, such as birthdays, appointments, and timestamps. Examples are `DATE`, `TIME`, `DATETIME`, etc.
  - Binary: These data types store binary data, such as images, files, and encryption keys. Examples are `BINARY`, `VARBINARY`, `IMAGE`, etc.
  - Other: These data types store special values, such as Boolean, XML, JSON, and spatial data. Examples are `BIT`, `XML`, `JSON`, `GEOMETRY`, etc.
- SQL literals are constants that represent fixed values in SQL statements, such as numbers, strings, dates, and booleans .
- SQL literals can be classified into the following types:
  - Character string literals: These literals are enclosed in single quotes (`'`) or double quotes (`"`) and represent text values. Examples are `'Hello'`, `"World"`, `'2021-03-15'`, etc.
  - Bit string literals: These literals are prefixed with `B` or `X` and represent binary values. Examples are `B'1010'`, `X'0A'`, `B'00000000'`, etc.
  - Exact numeric literals: These literals represent exact numeric values, such as integers and decimals. Examples are `42`, `3.14`, `0`, etc.
  - Approximate numeric literals: These literals represent approximate numeric values, such as floating-point numbers and scientific notation. Examples are `1.23E4`, `6.02E-23`, `0.0`, etc.
- SQL literals can be used in various contexts, such as assignments, comparisons, calculations, and expressions. Examples are:

```sql
-- Assign a character string literal to a variable
DECLARE @name VARCHAR(20);
SET @name = 'Sydney';

-- Compare a date literal with a column value
SELECT * FROM orders
WHERE order_date = '2021-03-15';

-- Calculate the area of a circle using a numeric literal
SELECT 3.14 * radius * radius AS area
FROM circles;

-- Concatenate two string literals using a plus operator
SELECT 'Hello' + 'World' AS greeting;
```