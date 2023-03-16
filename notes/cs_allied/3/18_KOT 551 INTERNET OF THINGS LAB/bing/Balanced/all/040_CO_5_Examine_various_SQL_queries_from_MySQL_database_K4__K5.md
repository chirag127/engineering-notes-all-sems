# CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- MySQL is one of the most popular open-source relational database management systems (RDBMS) that supports SQL.
- SQL queries are statements that specify what data to retrieve, insert, update, or delete from a database.
- SQL queries can be classified into four categories: Data Definition Language (DDL), Data Manipulation Language (DML), Data Query Language (DQL), and Data Control Language (DCL).
- DDL is used to define the structure and schema of the database, such as creating, altering, or dropping tables, indexes, views, etc.
- DML is used to manipulate the data in the database, such as inserting, updating, or deleting records, etc.
- DQL is used to query the data in the database, such as selecting, joining, filtering, sorting, grouping, etc.
- DCL is used to control the access and privileges of the database, such as granting, revoking, or denying permissions, etc.
- Some examples of SQL queries from MySQL database are:

  - To create a table named `students` with four columns: `id`, `name`, `age`, and `grade`:

    ```sql
    CREATE TABLE students (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      age INT,
      grade CHAR(1)
    );
    ```

  - To insert a record into the `students` table:

    ```sql
    INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 18, 'A');
    ```

  - To select all records from the `students` table:

    ```sql
    SELECT * FROM students;
    ```

  - To select only the `name` and `grade` columns from the `students` table:

    ```sql
    SELECT name, grade FROM students;
    ```

  - To select only the records from the `students` table where the `age` is greater than 20:

    ```sql
    SELECT * FROM students WHERE age > 20;
    ```

  - To select only the records from the `students` table where the `grade` is either 'A' or 'B':

    ```sql
    SELECT * FROM students WHERE grade IN ('A', 'B');
    ```

  - To select only the records from the `students` table where the `name` starts with 'A':

    ```sql
    SELECT * FROM students WHERE name LIKE 'A%';
    ```

  - To update the `grade` of the record with `id` 1 to 'B':

    ```sql
    UPDATE students SET grade = 'B' WHERE id = 1;
    ```

  - To delete the record with `id` 2 from the `students` table:

    ```sql
    DELETE FROM students WHERE id = 2;
    ```

  - To create a view named `top_students` that contains the `name` and `grade` of the students with grade 'A':

    ```sql
    CREATE VIEW top_students AS
    SELECT name, grade FROM students WHERE grade = 'A';
    ```

  - To grant the `SELECT` privilege on the `students` table to the user `bob`:

    ```sql
    GRANT SELECT ON students TO bob;
    ```

  - To revoke the `SELECT` privilege on the `students` table from the user `bob`:

    ```sql
    REVOKE SELECT ON students FROM bob;
    ```