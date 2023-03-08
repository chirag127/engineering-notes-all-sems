 Here is the content in markdown format for the given topic:

### Writing basic SQL SELECT statements

1. SELECT - is used to retrieve data from a database table which returns this data in the form of a result table.

Syntax:
SELECT column1, column2, ...
FROM table_name;

Example:
SELECT name, age FROM users;

This will select the name and age columns from the users table.

2. DISTINCT - is used to return only distinct (different) values.

Syntax:
SELECT DISTINCT column1, column2, ...
FROM table_name;

Example:
SELECT DISTINCT city FROM users;

This will return only unique city values from the users table.

3. WHERE - is used to extract only those records that fulfill a specified condition.

Syntax:
SELECT column1, column2, ...
FROM table_name
WHERE condition;

Example:
SELECT * FROM users
WHERE age > 30;

This will select all rows from the users table where the age is greater than 30.

4. AND, OR and NOT - are used to combine two or more conditions.

AND - returns records where both conditions are true
OR - returns records where at least one of the conditions is true
NOT - returns records where the condition is false

Examples:
SELECT * FROM users WHERE age > 30 AND city = 'London'

SELECT * FROM users WHERE age > 30 OR city = 'London'

SELECT * FROM users WHERE NOT age = 27

[Detailed explanations, diagrams, examples and applications can be added here for better understanding.]