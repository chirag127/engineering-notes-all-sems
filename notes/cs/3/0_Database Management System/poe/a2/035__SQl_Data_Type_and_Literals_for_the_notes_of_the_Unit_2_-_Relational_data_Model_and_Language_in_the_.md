 Here is the formal notes on the topic **SQL Data Types and Literals** for the Unit 2 - Relational Data Model and Language in Database Management System:

### SQL Data Types and Literals

1. SQL supports following data types:
- Numeric: INT, FLOAT, REAL, DOUBLE PRECISION, NUMERIC
- Character: CHAR, VARCHAR, NCHAR, NVARCHAR
- Temporal: DATE, TIME, TIMESTAMP
- Binary: BINARY, VARBINARY
- Boolean: BOOLEAN

2. Literals are fixed values assigned to variables.
- Numeric literals: 123, 123.45, -45
- Character literals: 'Hello', 'DBMS'
- Boolean literals: TRUE, FALSE
- Date/Time literals: '2020-12-25', '12:30:45'

3. Each literal has a corresponding data type. The database system implicitly converts literals to their data types.
- For example, literal 123 is converted to INT, 123.45 is converted to FLOAT, 'Hello' is converted to VARCHAR.

4. The size specification is required for fixed length character and binary types (CHAR and BINARY) to specify the number of characters or bytes respectively.
- For example, CHAR(10) specifies a character string of length 10 characters.

5. Apostrophes (') are used to enclose character literals and delimiters (,) are used to separate literals in a list.
- For example, 'Hello', 'World'

6. SQL is case-insensitive by default. CHARSET and Collation sequence can be used to specify case-sensitivity.

This notes cover the key points about SQL data types and literals. Let me know if you would like me to explain anything in more detail.