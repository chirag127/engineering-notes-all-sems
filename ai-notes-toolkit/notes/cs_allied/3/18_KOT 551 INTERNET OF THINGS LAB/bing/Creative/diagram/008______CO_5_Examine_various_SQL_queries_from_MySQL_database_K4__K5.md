#### CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- MySQL is a relational database management system (RDBMS) that supports different back ends, several different client programs and libraries, administrative tools, and a wide range of application-programming interfaces (APIs).
- MySQL is the world’s most popular open source database, and it powers many of the most accessed applications, such as Facebook, Twitter, Netflix, Uber, Airbnb, Shopify, and Booking.com.
- SQL queries are statements that are used to perform operations on data, such as selecting, inserting, updating, deleting, creating, altering, and dropping tables, views, indexes, and other database objects.
- SQL queries can be executed from MySQL command-line client, MySQL Workbench, or any other application that can connect to MySQL database server.
- SQL queries follow a specific syntax and structure, which consists of keywords, clauses, expressions, operators, functions, and parameters.
- SQL queries can be categorized into two types: data definition language (DDL) and data manipulation language (DML).
- DDL queries are used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, and other database objects.
- DML queries are used to manipulate the data in the database, such as selecting, inserting, updating, and deleting records from tables and views.
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

  - To insert a record into the `students` table with values: `1`, `Alice`, `18`, and `A`:

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

  - To select only the records from the `students` table where the `age` is greater than or equal to `20`:

    ```sql
    SELECT * FROM students WHERE age >= 20;
    ```

  - To update the `grade` column of the record with `id` equal to `1` in the `students` table to `B`:

    ```sql
    UPDATE students SET grade = 'B' WHERE id = 1;
    ```

  - To delete the record with `id` equal to `1` from the `students` table:

    ```sql
    DELETE FROM students WHERE id = 1;
    ```

  - To drop the `students` table from the database:

    ```sql
    DROP TABLE students;
    ```

- To learn more about SQL queries from MySQL database, you can refer to the official documentation or the online tutorials.