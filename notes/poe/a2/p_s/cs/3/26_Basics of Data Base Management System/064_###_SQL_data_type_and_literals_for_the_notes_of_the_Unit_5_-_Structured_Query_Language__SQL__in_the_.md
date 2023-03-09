 Here is the content in markdown format for the topic ### SQL data type and literals for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System:

### SQL Data Types

The following data types are commonly used in SQL:

- INTEGER - Whole numbers, without decimals, such as 123 or -123
- FLOAT - Floating point numbers, with decimals, such as 19.99 or -19.99
- NUMERIC - Fixed precision and scale numbers, such as 19.99 or -19.99
- CHAR - Fixed length strings, such as 'Hello'
- VARCHAR - Variable length strings, such as 'Hello'
- DATE - Date values, such as '2019-06-15'
- TIME - Time values, such as '12:00:00'
- DATETIME - Date and time values, such as '2019-06-15 12:00:00'

### SQL Literals

Literals are fixed values that you literally include in your SQL statements.

Examples of literals:

- strings: 'Hello', 'SQL Tutorial'
- numeric: 12.3, 1000
- boolean: TRUE, FALSE
- date and time: '2019-06-15', '12:00:00'

Advantages of using literals:

- Easy to understand
- Increases readability of SQL statements
- Self documenting - the literal value explains the intent

Disadvantages of using literals:

- Lack of flexibility - the values cannot be easily changed
- Cannot reuse literal values
- Error prone if literals need to be updated in multiple places

In general, it is good practice to use literals for fixed, well known values, and variables or parameters for variable values.