#### CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- MySQL is an open-source relational database management system (RDBMS) that supports SQL as its primary interface.
- A SQL query is a statement that specifies what data to retrieve, modify, insert, delete, or update from a database.
- SQL queries can be classified into four categories: Data Definition Language (DDL), Data Manipulation Language (DML), Data Query Language (DQL), and Data Control Language (DCL).
- DDL is used to define the structure and schema of the database, such as creating, altering, or dropping tables, indexes, views, or triggers.
- DML is used to manipulate the data in the database, such as inserting, updating, deleting, or merging records.
- DQL is used to query the data in the database, such as selecting, joining, filtering, sorting, grouping, or aggregating records.
- DCL is used to control the access and security of the database, such as granting, revoking, or denying permissions or roles to users or groups.
- Some examples of SQL queries from MySQL database are:

  - To create a table named `students` with four columns: `id` (integer, primary key, auto-increment), `name` (varchar, not null), `age` (integer, not null), and `grade` (char, not null):

    ```sql
    CREATE TABLE students (
      id INT PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(50) NOT NULL,
      age INT NOT NULL,
      grade CHAR(1) NOT NULL
    );
    ```

  - To insert a new record into the `students` table with the values: `id` = 1, `name` = 'Alice', `age` = 18, and `grade` = 'A':

    ```sql
    INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 18, 'A');
    ```

  - To update the `grade` of the record with `id` = 1 to 'B':

    ```sql
    UPDATE students SET grade = 'B' WHERE id = 1;
    ```

  - To delete the record with `id` = 1 from the `students` table:

    ```sql
    DELETE FROM students WHERE id = 1;
    ```

  - To select all the records from the `students` table:

    ```sql
    SELECT * FROM students;
    ```

  - To select only the `name` and `grade` of the records from the `students` table where `age` is greater than or equal to 20:

    ```sql
    SELECT name, grade FROM students WHERE age >= 20;
    ```

  - To select the `name` and `grade` of the records from the `students` table and sort them by `grade` in descending order:

    ```sql
    SELECT name, grade FROM students ORDER BY grade DESC;
    ```

  - To select the `name` and `grade` of the records from the `students` table and group them by `grade` and count the number of records in each group:

    ```sql
    SELECT grade, COUNT(*) AS count FROM students GROUP BY grade;
    ```

  - To grant the `SELECT` and `UPDATE` privileges on the `students` table to the user `bob`:

    ```sql
    GRANT SELECT, UPDATE ON students TO bob;
    ```

  - To revoke the `UPDATE` privilege on the `students` table from the user `bob`:

    ```sql
    REVOKE UPDATE ON students FROM bob;
    ```