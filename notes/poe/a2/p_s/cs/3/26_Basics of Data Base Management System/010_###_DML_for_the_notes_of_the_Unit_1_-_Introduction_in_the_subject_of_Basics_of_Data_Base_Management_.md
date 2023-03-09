 Here is the content in markdown format for the given topic:

### DML for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System

- DML stands for Data Manipulation Language. It is used to manipulate the data in a database.
- The common DML commands are:

1. INSERT - Used to insert new data into a table.
Syntax: INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);

2. UPDATE - Used to modify existing data within a table.
Syntax: UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;

3. DELETE - Used to remove existing data from a table.
Syntax: DELETE FROM table_name WHERE condition;

- Examples of DML:

INSERT INTO students (name, age) VALUES ('John', 20);

UPDATE students SET age = 21 WHERE name = 'John';

DELETE FROM students WHERE name = 'John';

- Advantages:

- Easy to use and learn.
- Flexible to modify data.
- Disadvantages:

- Does not provide data security.
- Does not maintain data integrity.
- May lead to inconsistent data if not used properly.

- Applications:

- Used by database applications to modify data as required.
- Used for data entry, data update and data deletion purposes.

[Detailed diagrams and codes can be included if required.]