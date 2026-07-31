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

  - Create a table named `students` with four columns: `id`, `name`, `age`, and `grade`:

    ```sql
    CREATE TABLE students (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      age INT,
      grade CHAR(1)
    );
    ```

  - Insert three records into the `students` table:

    ```sql
    INSERT INTO students (id, name, age, grade) VALUES
    (1, 'Alice', 18, 'A'),
    (2, 'Bob', 19, 'B'),
    (3, 'Charlie', 20, 'C');
    ```

  - Select all the records from the `students` table:

    ```sql
    SELECT * FROM students;
    ```

  - Select the name and grade of the students who are older than 18:

    ```sql
    SELECT name, grade FROM students WHERE age > 18;
    ```

  - Update the grade of Bob to 'A':

    ```sql
    UPDATE students SET grade = 'A' WHERE name = 'Bob';
    ```

  - Delete the record of Charlie from the `students` table:

    ```sql
    DELETE FROM students WHERE name = 'Charlie';
    ```

  - Create a view named `top_students` that shows the name and grade of the students who have grade 'A':

    ```sql
    CREATE VIEW top_students AS
    SELECT name, grade FROM students WHERE grade = 'A';
    ```

  - Grant the SELECT privilege on the `students` table to a user named `user1`:

    ```sql
    GRANT SELECT ON students TO user1;
    ```

  - Revoke the SELECT privilege on the `students` table from `user1`:

    ```sql
    REVOKE SELECT ON students FROM user1;
    ```