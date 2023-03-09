 Here is the content in markdown format for the topic ### data definition languages for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System:

### Data Definition Languages (DDL)

- DDLs are languages used to define the structure of a database. They are used to create and modify the structure of database objects.
- The main operations performed by DDLs are:

1. Creating a database schema: CREATE DATABASE
2. Creating a table: CREATE TABLE
3. Altering a table: ALTER TABLE (add/drop columns, add constraints, etc.)
4. Dropping a table: DROP TABLE
5. Creating an index: CREATE INDEX
6. Dropping an index: DROP INDEX

- Some examples of DDL commands in SQL are:

```
CREATE DATABASE myDB;

CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(20),
    age INT
);

ALTER TABLE student
    ADD grade VARCHAR(2);

DROP TABLE student;
```

- Advantages: Allows defining database structure efficiently. Used to modify database structure as per requirements.
- Disadvantages: Database schema has to be modified carefully as any error can corrupt the database.
- Applications: Commonly used in RDBMS to design database models.

- Here is an ASCII diagram showing the flow of DDL commands:

    ```
          CREATE/ALTER/DROP
           ^
           |
    +