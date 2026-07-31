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

  - To create a table named `students` with four columns: `id` (primary key), `name` (varchar), `age` (int), and `grade` (char):

    ```sql
    CREATE TABLE students (
      id INT NOT NULL AUTO_INCREMENT,
      name VARCHAR(50) NOT NULL,
      age INT NOT NULL,
      grade CHAR(1) NOT NULL,
      PRIMARY KEY (id)
    );
    ```

  - To insert a record into the `students` table with values: `1`, `Alice`, `20`, and `A`:

    ```sql
    INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 20, 'A');
    ```

  - To select all the records from the `students` table:

    ```sql
    SELECT * FROM students;
    ```

  - To select only the `name` and `grade` columns from the `students` table where the `age` is greater than `18` and order by the `grade` in descending order:

    ```sql
    SELECT name, grade FROM students WHERE age > 18 ORDER BY grade DESC;
    ```

  - To update the `grade` of the record with `id` equal to `1` to `B` in the `students` table:

    ```sql
    UPDATE students SET grade = 'B' WHERE id = 1;
    ```

  - To delete the record with `id` equal to `1` from the `students` table:

    ```sql
    DELETE FROM students WHERE id = 1;
    ```

  - To grant the `SELECT` and `UPDATE` privileges on the `students` table to the user `bob`:

    ```sql
    GRANT SELECT, UPDATE ON students TO bob;
    ```

  - To revoke the `UPDATE` privilege on the `students` table from the user `bob`:

    ```sql
    REVOKE UPDATE ON students FROM bob;
    ```