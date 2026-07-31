 Here is the content in Markdown format without any emojis or external links, written in points and in a formal tone:

### SQL Operators and Their Procedure

1. Arithmetic Operators: Used to perform arithmetic operations like addition, subtraction, multiplication, division, modulus.
eg: SELECT col1, col2, col1 + col2 FROM table;

2. Comparison Operators: Used to compare values for equal, not equal, greater than, less than, greater than or equal to, less than or equal to.
eg: SELECT * FROM table WHERE col1 = 5;

3. Logical Operators: Used to combine multiple conditions or manipulate the output of Boolean expressions. The operators are AND, OR, and NOT.
eg: SELECT * FROM table WHERE col1 = 5 AND col2 = 10;

4. BETWEEN Operator: Used to filter values within a certain range.
eg: SELECT * FROM table WHERE col1 BETWEEN 5 AND 10;

5. IN Operator: Used to specify multiple values in a WHERE clause.
eg: SELECT * FROM table WHERE col1 IN (5, 10, 15);

6. LIKE Operator: Used to search for a specific pattern in a column.
eg: SELECT * FROM table WHERE col1 LIKE 'a%';   //will find any values that start with "a"

7. IS NULL and IS NOT NULL: Used to check for null values.
eg: SELECT * FROM table WHERE col1 IS NOT NULL;

The above are some common SQL operators and their usage in procedures. Let me know if you would like me to elaborate on any of the points or add more operators and examples.