# SQL Data Types and Literals

## Data Types
- SQL data types are used to represent the nature of the data that can be stored in the database table  .
- Every field or column in a table is given a data type when a table is defined .
- Data types can be categorized into numeric, character, date and time, and binary types .
- Some common data types are:

| Data Type | Description | Example |
| --- | --- | --- |
| INT | Integer numbers | 42 |
| DECIMAL | Decimal numbers with a fixed precision and scale | 3.14 |
| FLOAT | Floating-point numbers with an approximate precision | 1.23E4 |
| CHAR | Fixed-length character strings | 'Hello' |
| VARCHAR | Variable-length character strings | 'World' |
| DATE | Dates in the format YYYY-MM-DD | '2021-12-15' |
| TIME | Times in the format HH:MM:SS | '22:11:27' |
| DATETIME | Dates and times in the format YYYY-MM-DD HH:MM:SS | '2021-12-15 22:11:27' |
| BIT | Binary values | 0 or 1 |
| BLOB | Binary large objects | Image files |

## Literals
- Literals are constant values that can be used in SQL statements .
- Literals can be of four kinds: character string, bit string, exact numeric, and approximate numeric.
- Character string literals are written as a sequence of characters enclosed in single quotes . For example, 'Hello'.
- Bit string literals are written as a sequence of 0s and 1s preceded by a B and enclosed in single quotes. For example, B'1010'.
- Exact numeric literals are written as a sequence of digits, optionally with a decimal point and a sign . For example, 42, -3.14, +100.
- Approximate numeric literals are written as a sequence of digits, with a decimal point, a sign, and an exponent . For example, 1.23E4, -6.78E-2, +9.0E+3.