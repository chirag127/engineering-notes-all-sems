## Data Definition Language (DDL) Statements

Data Definition Language (DDL) is a subset of SQL (Structured Query Language) used to define and manage the structure of a database. DDL statements are used to create, alter, and drop database objects such as tables, views, indexes, and procedures.

Here are some common DDL statements used in Database Management Systems:

1. **CREATE**: This statement is used to create a new database object, such as a table, view, index, or procedure. For example, to create a new table named `students`, the following statement can be used:
```
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT
);
```

2. **ALTER**: This statement is used to modify the structure of an existing database object. For example, to add a new column `email` to the `students` table, the following statement can be used:
```
ALTER TABLE students ADD COLUMN email VARCHAR(255);
```

3. **DROP**: This statement is used to delete a database object. For example, to delete the `students` table, the following statement can be used:
```
DROP TABLE students;
```

4. **TRUNCATE**: This statement is used to delete all data from a table, but not the table itself. For example, to delete all data from the `students` table, the following statement can be used:
```
TRUNCATE TABLE students;
```

These are some of the common DDL statements used in Database Management Systems. It is important to note that the syntax and usage of these statements may vary slightly depending on the specific database management system being used.