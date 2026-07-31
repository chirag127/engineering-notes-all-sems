# SQL Data Types and Literals

SQL data types are used to represent the nature of the data that can be stored in the database table. Every field or column in a table is given a data type when a table is defined. SQL data types can be broadly classified into the following categories :

- String: These data types are used to store character data, such as text, names, addresses, etc. Examples of string data types are CHAR, VARCHAR, TEXT, etc.
- Numeric: These data types are used to store numeric data, such as integers, decimals, fractions, etc. Examples of numeric data types are INT, FLOAT, DECIMAL, etc.
- Date and Time: These data types are used to store date and time values, such as year, month, day, hour, minute, second, etc. Examples of date and time data types are DATE, TIME, DATETIME, etc.
- Binary: These data types are used to store binary data, such as images, files, etc. Examples of binary data types are BINARY, VARBINARY, BLOB, etc.

SQL literals are the values that are used to represent a constant value in a SQL statement. SQL literals can be of four kinds:

- Character string: These literals are enclosed in single quotes (' ') and can contain any character. For example, 'Hello', 'SQL', '123', etc.
- Bit string: These literals are prefixed with a B or b and enclosed in single quotes (' '). They can contain only 0 or 1. For example, B'1010', b'0011', etc.
- Exact numeric: These literals are composed of digits and an optional sign (+ or -). They can also have a decimal point (.) and a scale (the number of digits after the decimal point). For example, 12, -34, 5.67, etc.
- Approximate numeric: These literals are composed of digits, an optional sign (+ or -), a decimal point (.), and an exponent (E or e followed by an integer). They are used to represent very large or very small numbers. For example, 1.23E4, -6.78e-2, etc.

Some SQL data types also have their own literals, such as money, uniqueidentifier, etc. For example, $12, $-23, 6F9619FF-8B86-D011-B42D-00C04FC964FF, etc.