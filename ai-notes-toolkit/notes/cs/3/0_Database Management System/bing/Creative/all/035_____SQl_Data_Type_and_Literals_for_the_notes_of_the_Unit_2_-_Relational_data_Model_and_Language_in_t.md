# SQL Data Types and Literals

SQL data types are used to represent the nature of the data that can be stored in the database table. Every field or column in a table is given a data type when a table is defined . SQL data types can be categorized into the following groups:

- Numeric: These data types store numeric values, such as integers, decimals, and floating-point numbers. Examples are `INT`, `DECIMAL`, `FLOAT`, and `NUMERIC`.
- Character: These data types store character strings, such as names, addresses, and descriptions. Examples are `CHAR`, `VARCHAR`, `TEXT`, and `NCHAR`.
- Date and time: These data types store date and time values, such as birthdays, appointments, and timestamps. Examples are `DATE`, `TIME`, `DATETIME`, and `TIMESTAMP`.
- Binary: These data types store binary strings, such as images, files, and encryption keys. Examples are `BINARY`, `VARBINARY`, `BLOB`, and `IMAGE`.
- Boolean: These data types store logical values, such as true or false. Examples are `BIT`, `BOOLEAN`, and `TINYINT`.
- Special: These data types store special values, such as spatial data, XML data, JSON data, and variant data. Examples are `GEOMETRY`, `XML`, `JSON`, and `SQL_VARIANT`.

SQL literals are constants that represent fixed values in SQL statements . SQL literals can be of the following types:

- Character string: These literals are enclosed in single quotes, such as `'Hello'`, `'SQL'`, and `'2021-03-15'`.
- Bit string: These literals are binary values that are prefixed with `B` or `0b` and enclosed in single quotes, such as `B'1010'`, `0b1100`, and `B'1001'`.
- Exact numeric: These literals are decimal or integer values that can have an optional sign, such as `123`, `-456`, and `78.90`.
- Approximate numeric: These literals are floating-point values that can have an optional sign and an exponent, such as `1.23E4`, `-5.67E-8`, and `3.14`.