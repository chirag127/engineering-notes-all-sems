Hello, I am Sydney, your AI assistant. I can help you with various SQL queries from MySQL database. Here is some content on the topic:

# CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL as its query language.
- A SQL query is a statement that specifies what data to retrieve, modify, insert, delete, or update from a database.
- There are different types of SQL queries, such as:
  - Data Definition Language (DDL) queries: These are used to define the structure and schema of the database, such as creating, altering, or dropping tables, views, indexes, etc.
  - Data Manipulation Language (DML) queries: These are used to manipulate the data in the database, such as inserting, updating, deleting, or selecting records from tables or views.
  - Data Control Language (DCL) queries: These are used to control the access and permissions of the database, such as granting or revoking privileges, roles, or users.
  - Transaction Control Language (TCL) queries: These are used to manage the transactions in the database, such as committing, rolling back, or saving changes.
  - Data Query Language (DQL) queries: These are used to query the data in the database, such as selecting, joining, filtering, sorting, grouping, or aggregating data from tables or views.
- Some examples of SQL queries from MySQL database are:

  - Creating a table named `students` with four columns: `id`, `name`, `age`, and `grade`:

    ```sql
    CREATE TABLE students (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      age INT,
      grade CHAR(1)
    );
    ```

  - Inserting three records into the `students` table:

    ```sql
    INSERT INTO students (id, name, age, grade) VALUES
    (1, 'Alice', 18, 'A'),
    (2, 'Bob', 19, 'B'),
    (3, 'Charlie', 20, 'C');
    ```

  - Updating the `grade` of the student with `id` 2 to 'A':

    ```sql
    UPDATE students
    SET grade = 'A'
    WHERE id = 2;
    ```

  - Deleting the record of the student with `id` 3 from the `students` table:

    ```sql
    DELETE FROM students
    WHERE id = 3;
    ```

  - Selecting all the records from the `students` table:

    ```sql
    SELECT * FROM students;
    ```

  - Selecting the `name` and `grade` of the students who are older than 18:

    ```sql
    SELECT name, grade FROM students
    WHERE age > 18;
    ```

  - Selecting the `name` and `grade` of the students who have grade 'A' or 'B', sorted by `name` in ascending order:

    ```sql
    SELECT name, grade FROM students
    WHERE grade IN ('A', 'B')
    ORDER BY name ASC;
    ```

  - Selecting the `name` and `grade` of the students, grouped by `grade` and showing the count of each group:

    ```sql
    SELECT grade, COUNT(*) AS count FROM students
    GROUP BY grade;
    ```

  - Selecting the `name` and `grade` of the students who have the highest `grade` in the table:

    ```sql
    SELECT name, grade FROM students
    WHERE grade = (SELECT MAX(grade) FROM students);
    ```