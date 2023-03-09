 Here is the content in markdown format for the topic ### SQl Data Type and Literals for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System:

### SQL Data Types and Literals

1. Numeric Types
- INTEGER: Whole numbers, without fractions.
- SMALLINT: Whole numbers, without fractions. Range is smaller than INTEGER.
- DECIMAL or NUMERIC: Fixed precision and scale numbers. Allows fractions.
- FLOAT or REAL: Floating point numbers, allowing fractions. Precision can be lost.

2. String Types
- CHAR: Fixed length strings. Declared width.
- VARCHAR: Variable length strings. Declared maximum width.
- TEXT: Variable unlimited length strings.

3. Date and Time Types
- DATE: YYYY-MM-DD
- TIME: HH:MM:SS
- TIMESTAMP: YYYY-MM-DD HH:MM:SS
- INTERVAL: Used for time differences

4. Boolean Type
- BOOLEAN: Stores TRUE or FALSE logical values.

5. Literals
- Numeric: 1234, 12.34
- String: 'Hello', ' Single quotes for strings '
- Date and Time: '2020-01-01', '12:30:45'
- Boolean: TRUE, FALSE

Advantages:
- Appropriate data type can be chosen based on the nature of data which leads to efficient storage.
- Data validity can be ensured by restricting input to specific data types.
- Security can be enforced by allowing only certain data types for sensitive data.

Disadvantages:
- Inappropriate data type choice can lead to wastage of storage space.
- Data type restrictions can limit flexibility.
- Conversion between data types may be required in some cases leading to overhead.

[Detailed diagrams and examples can be added here]

Applications:
- Choosing appropriate data types for database design based on the data to be stored.
- Designing input forms and validation based on data types.
- Processing and manipulating data based on data types.