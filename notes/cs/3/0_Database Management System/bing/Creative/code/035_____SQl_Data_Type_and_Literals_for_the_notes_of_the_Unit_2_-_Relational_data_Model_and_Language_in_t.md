Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of SQL Data Type and Literals for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System.

```markdown
### SQL Data Type and Literals

- SQL data types are the attributes that define the kind of data that can be stored in a column of a table or a variable in a program.
- SQL data types can be categorized into four main groups: numeric, character, date and time, and boolean.
- SQL literals are the constant values that can be assigned to a column of a table or a variable in a program.
- SQL literals can be of different types, such as numeric, character, date and time, boolean, null, and interval.

#### Numeric Data Types

- Numeric data types are used to store numbers, such as integers, decimals, fractions, and floating-point numbers.
- Numeric data types can have different ranges and precisions, depending on the implementation of the SQL system.
- Some common numeric data types are:

  - INTEGER: A whole number, such as 1, -5, or 1000.
  - DECIMAL(p, s): A fixed-point number, where p is the precision (the total number of digits) and s is the scale (the number of digits after the decimal point), such as 3.14, -0.01, or 123.456.
  - FLOAT(p): A floating-point number, where p is the precision (the number of significant digits), such as 1.23e4, -3.14e-2, or 6.02e23.
  - REAL: A synonym for FLOAT.
  - DOUBLE PRECISION: A synonym for FLOAT with a higher precision.

- Numeric literals are written as the number itself, optionally with a sign (+ or -) and a decimal point (.), such as 42, -3.14, or +1.23e4.

#### Character Data Types

- Character data types are used to store strings, such as words, sentences, or symbols.
- Character data types can have different lengths and character sets, depending on the implementation of the SQL system.
- Some common character data types are:

  - CHAR(n): A fixed-length string, where n is the number of characters, such as 'A', 'Hello', or 'SQL'.
  - VARCHAR(n): A variable-length string, where n is the maximum number of characters, such as 'A', 'Hello', or 'SQL'.
  - TEXT: A large variable-length string, such as 'This is a long text.'.

- Character literals are written as the string enclosed in single quotes ('), such as 'Hello', 'SQL', or 'This is a character literal.'.

#### Date and Time Data Types

- Date and time data types are used to store values that represent dates, times, or both.
- Date and time data types can have different formats and precisions, depending on the implementation of the SQL system.
- Some common date and time data types are:

  - DATE: A value that represents a calendar date, such as '2021-03-15', '15/03/2021', or 'March 15, 2021'.
  - TIME: A value that represents a time of day, such as '20:08:12', '08:08:12 PM', or '8:08:12 PM'.
  - TIMESTAMP: A value that represents a date and time, such as '2021-03-15 20:08:12', '15/03/2021 08:08:12 PM', or 'March 15, 2021 8:08:12 PM'.
  - DATETIME: A synonym for TIMESTAMP.

- Date and time literals are written as the date and/or time value enclosed in single quotes ('), using a format that is supported by the SQL system, such as '2021-03-15', '20:08:12', or '2021-03-15 20:08:12'.

#### Boolean Data Types

- Boolean data types are used to store values that represent logical truth, such as true or false.
- Boolean data types can have different representations, depending on the implementation of the SQL system.
- Some common boolean data types are:

  - BOOLEAN: A value that can be either true or false, such as true, false, or unknown.
  - BIT: A value that can be either 1 or 0, such as 1, 0, or null.

- Boolean literals are written as the keyword TRUE, FALSE, or UNKNOWN, such as TRUE,

```
