# DDL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- DDL stands for Data Definition Language, which is a subset of SQL commands that are used to create, modify, and delete database objects such as tables, views, indexes, schemas, etc.
- DDL commands do not affect the data stored in the database, but only the structure or schema of the database.
- Some of the common DDL commands are:

  - CREATE: This command is used to create a new database object, such as a table, view, index, etc. For example, the following statement creates a table named `students` with four columns: `id`, `name`, `age`, and `grade`.

    ```sql
    CREATE TABLE students (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      age INT CHECK (age > 0),
      grade CHAR(1) CHECK (grade IN ('A', 'B', 'C', 'D', 'F'))
    );
    ```

  - ALTER: This command is used to modify an existing database object, such as adding, dropping, or renaming columns, changing data types, adding or removing constraints, etc. For example, the following statement adds a new column named `email` to the `students` table.

    ```sql
    ALTER TABLE students
    ADD email VARCHAR(100) UNIQUE;
    ```

  - DROP: This command is used to delete an existing database object, such as a table, view, index, etc. For example, the following statement drops the `students` table from the database.

    ```sql
    DROP TABLE students;
    ```

  - RENAME: This command is used to change the name of an existing database object, such as a table, view, index, etc. For example, the following statement renames the `students` table to `learners`.

    ```sql
    RENAME TABLE students TO learners;
    ```

  - TRUNCATE: This command is used to delete all the data from a table, but not the table itself. It is faster than using the `DELETE` command, which is a DML command. For example, the following statement deletes all the data from the `students` table.

    ```sql
    TRUNCATE TABLE students;
    ```

- DDL commands are normally executed by database administrators or developers, who have the necessary permissions to create or modify the database schema. They are not used by general users, who access the database through applications or queries.