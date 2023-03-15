# SQL data type and literals

- SQL data types are the attributes that define the kind of value that can be stored in a column of a table or a variable in a program.
- SQL data types can be categorized into numeric, character, date and time, interval, boolean, and large object types.
- SQL literals are the constant values that can be assigned to a column or a variable, or used in expressions or conditions.
- SQL literals can be classified into numeric, character, date and time, interval, and boolean literals.
- SQL literals are written in a specific format depending on the data type they represent.

## Numeric data types and literals

- Numeric data types are used to store numbers, such as integers, decimals, fractions, and real numbers.
- Numeric data types can be further divided into exact and approximate numeric types.
- Exact numeric types are used to store numbers with a fixed precision and scale, such as integers, decimals, and numeric.
- Approximate numeric types are used to store numbers with a floating-point representation, such as floats, doubles, and reals.
- Numeric literals are written as a sequence of digits, optionally with a decimal point, a sign, and an exponent.
- Examples of numeric literals are: 42, -3.14, 6.02E23, +0.5.

## Character data types and literals

- Character data types are used to store strings of characters, such as letters, symbols, and spaces.
- Character data types can be further divided into fixed-length and variable-length character types.
- Fixed-length character types are used to store strings of a fixed size, such as char and nchar.
- Variable-length character types are used to store strings of a variable size, such as varchar, nvarchar, text, and clob.
- Character literals are written as a sequence of characters enclosed in single quotes, optionally with escape sequences for special characters.
- Examples of character literals are: 'Hello', 'SQL', 'It''s a sunny day', 'This is a newline\n'.

## Date and time data types and literals

- Date and time data types are used to store values that represent dates, times, or both.
- Date and time data types can be further divided into date, time, timestamp, and interval types.
- Date types are used to store values that represent calendar dates, such as date and year.
- Time types are used to store values that represent clock times, such as time and time with time zone.
- Timestamp types are used to store values that represent both date and time, such as timestamp and timestamp with time zone.
- Interval types are used to store values that represent a duration of time, such as interval year to month and interval day to second.
- Date and time literals are written in a specific format depending on the data type they represent, using keywords, separators, and delimiters.
- Examples of date and time literals are: DATE '2021-03-15', TIME '22:11:25', TIMESTAMP '2021-03-15 22:11:25', INTERVAL '1' YEAR, INTERVAL '10:30:00' HOUR TO SECOND.

## Boolean data types and literals

- Boolean data types are used to store values that represent logical truth values, such as boolean and bit.
- Boolean literals are written as the keywords TRUE, FALSE, or UNKNOWN, or as the digits 1, 0, or NULL for bit data types.
- Examples of boolean literals are: TRUE, FALSE, UNKNOWN, 1, 0, NULL.