### Types of SQL Commands

SQL stands for Structured Query Language and it is a standard language for storing, manipulating and retrieving data in databases. SQL commands can be grouped into five broad categories based on their functionality  . These are:

- **Data Definition Language (DDL)**: This category consists of SQL commands that can be used to define the database structure, such as creating, altering, dropping or renaming tables, views, indexes, schemas, etc. Some examples of DDL commands are:

  - CREATE: This command is used to create a new table, view, index, schema, etc. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a new table called students with three columns: id, name and age.
  - ALTER: This command is used to modify the structure of an existing table, view, index, schema, etc. For example, `ALTER TABLE students ADD COLUMN email VARCHAR(50);` adds a new column called email to the students table.
  - DROP: This command is used to delete an existing table, view, index, schema, etc. For example, `DROP TABLE students;` deletes the students table and all its data.
  - RENAME: This command is used to change the name of an existing table, view, index, schema, etc. For example, `RENAME TABLE students TO learners;` changes the name of the students table to learners.

- **Data Manipulation Language (DML)**: This category consists of SQL commands that can be used to manipulate the data in the database, such as inserting, updating, deleting or selecting data from tables, views, etc. Some examples of DML commands are:

  - INSERT: This command is used to insert new data into a table or view. For example, `INSERT INTO students (id, name, age, email) VALUES (1, 'Alice', 20, 'alice@example.com');` inserts a new row into the students table with the specified values.
  - UPDATE: This command is used to modify the existing data in a table or view. For example, `UPDATE students SET age = 21 WHERE id = 1;` updates the age of the student with id 1 to 21.
  - DELETE: This command is used to delete the existing data from a table or view. For example, `DELETE FROM students WHERE age > 25;` deletes all the rows from the students table where the age is greater than 25.
  - SELECT: This command is used to query or retrieve data from a table or view. For example, `SELECT name, email FROM students WHERE age < 22;` selects the name and email of the students whose age is less than 22.

- **Data Query Language (DQL)**: This category consists of SQL commands that can be used to query or retrieve data from the database, such as selecting, filtering, sorting, grouping, aggregating or joining data from tables, views, etc. Some examples of DQL commands are:

  - SELECT: This command is used to query or retrieve data from a table or view. For example, `SELECT name, email FROM students WHERE age < 22;` selects the name and email of the students whose age is less than 22.
  - WHERE: This clause is used to filter the data based on some condition. For example, `SELECT name, email FROM students WHERE age < 22;` selects the name and email of the students whose age is less than 22.
  - ORDER BY: This clause is used to sort the data in ascending or descending order. For example, `SELECT name, email FROM students ORDER BY name ASC;` selects the name and email of the students and sorts them by name in ascending order.
  - GROUP BY: This clause is used to group the data based on some column or expression. For example, `SELECT age, COUNT(*) FROM students GROUP BY age;` selects the age and the number of students for each age group.
  - HAVING: This clause is used to filter the data after grouping. For example, `SELECT age, COUNT(*) FROM students GROUP BY age HAVING COUNT(*) > 1;` selects the age and the number of students for each age group where the number of students is more than 1.
  - JOIN: This clause is used to combine data from two or more tables or views based on some common column or condition. For example, `SELECT s.name, s.email, c.name FROM students s