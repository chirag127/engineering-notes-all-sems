 Here is the content in markdown format for the topic ### Types of SQL Commands for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System:

#### Data Definition Language (DDL)
- CREATE - to create a new database, table, index, etc.
- ALTER - alters an existing database object
- DROP - deletes an existing database object

Examples:
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(20),
    salary INT
);

ALTER TABLE employees
ADD age INT;

DROP TABLE employees;
```

Advantages: Used to define the database schema.

Disadvantages: Data loss may occur if used incorrectly.

Applications: Used in the initial design and development phase of a database.

#### Data Manipulation Language (DML)
- INSERT - inserts new data into a table
- UPDATE - updates existing data in a table
- DELETE - deletes existing data from a table

Examples:
```sql
INSERT INTO employees (id, name, salary)
VALUES (1, 'John', 5000);

UPDATE employees
SET salary = 6000
WHERE name = 'John';

DELETE FROM employees
WHERE name = 'John';
```

Advantages: Used to manage data in the database.

Disadvantages: Data loss/inconsistency may occur if used incorrectly.

Applications: Used for regular data operations on a database.

[Detailed explanations, diagrams and more examples can be added wherever required to make the notes comprehensive and easy to understand.]