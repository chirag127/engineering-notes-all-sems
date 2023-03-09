 Here is the content in markdown format for the topic ### SQL Operators and Their Procedure for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System:

### SQL Operators and Their Procedure

1. Comparison Operators:
- =: Equal
- <> or !=: Not Equal
- >: Greater Than
- <: Less Than
- >=: Greater Than or Equal To
- <=: Less Than or Equal To

These operators are used to compare values and return a boolean result (true/false). They can be used in WHERE clause to filter records.

2. Logical Operators:
- AND: Returns true if both operands are true
- OR: Returns true if any of the operands is true
- NOT: Inverts the boolean value (true becomes false and vice-versa)

These operators are used to combine comparison operators and return a boolean value. They can be used in WHERE clause to filter records with multiple conditions.

3. Arithmetic Operators:
- +: Addition
- -: Subtraction
- *: Multiplication
- /: Division
- %: Modulus (Returns the remainder of a division)

These operators are used to perform mathematical calculations on numeric data and return numeric values. They can be used in SELECT clause to calculate columns values.

4. BETWEEN:

The BETWEEN operator is used to filter records within a certain range. The values can be numbers, text or dates.

The BETWEEN operator is inclusive: it includes the values you specify.

Syntax:
column_name BETWEEN value1 AND value2

Example:
SELECT * FROM products WHERE price BETWEEN 10 AND 20

This will return all products with a price between 10 and 20 (inclusive).

[You can include additional details, diagrams, examples, etc. here if needed.]