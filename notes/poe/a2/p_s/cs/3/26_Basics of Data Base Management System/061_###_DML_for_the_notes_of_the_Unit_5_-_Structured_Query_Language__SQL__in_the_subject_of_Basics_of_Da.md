 Here is the content in markdown format for the topic -

### DML for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

**Data Manipulation Language (DML)** is used to manipulate data in a database. The common DML commands are:

- **INSERT**: Adds new data to a table. Syntax: INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
- **UPDATE**: Updates existing data in a table. Syntax: UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
- **DELETE**: Deletes existing data from a table. Syntax: DELETE FROM table_name WHERE condition;

**Advantages of DML**:
- Allows to easily modify data in a database.
- Provides flexibility to add, remove or update data.
- Increases data consistency and accuracy.

**Disadvantages of DML**:
- If not used properly, it can destroy data or make it inconsistent.
- It can impact performance if a large amount of data is modified.
- It requires careful use of WHERE clause to avoid unwanted data modifications.

**Examples of DML commands**:

`INSERT INTO students (name, age) VALUES ('John', 20);`

`UPDATE students SET age = 21 WHERE name = 'John';`

`DELETE FROM students WHERE age > 20;`

DML is commonly used in web applications to update database information based on user actions like adding a product to cart, updating profile information, etc. It allows to easily manage data in databases and keep it up-to-date. Overall, DML provides a convenient way to manipulate data in a database through SQL commands.