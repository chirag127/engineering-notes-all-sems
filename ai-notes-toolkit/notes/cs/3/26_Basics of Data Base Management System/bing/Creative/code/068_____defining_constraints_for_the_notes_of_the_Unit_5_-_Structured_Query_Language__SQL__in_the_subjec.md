Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of defining constraints for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System.

```markdown
# Defining Constraints

- Constraints are rules that restrict the values or formats of the data in a table.
- Constraints can be defined at the column level or the table level.
- Constraints can be specified when creating a table using the CREATE TABLE statement, or after creating a table using the ALTER TABLE statement.
- Constraints can be enforced by the database system (declarative constraints) or by the application program (procedural constraints).
- Constraints can be used to ensure data integrity, data consistency, and data quality.

## Types of Constraints

- There are different types of constraints in SQL, such as:

  - NOT NULL: This constraint ensures that a column cannot have a NULL value.
  - UNIQUE: This constraint ensures that a column or a combination of columns has a unique value for each row in a table.
  - PRIMARY KEY: This constraint identifies a column or a combination of columns as the primary key of a table, which uniquely identifies each row in a table. A primary key also implies NOT NULL and UNIQUE constraints.
  - FOREIGN KEY: This constraint establishes a relationship between a column or a combination of columns in one table and the primary key of another table, which is called the referenced table. A foreign key ensures that the values in the referencing column(s) match the values in the referenced column(s).
  - CHECK: This constraint allows specifying a condition that the values in a column or a row must satisfy.
  - DEFAULT: This constraint allows specifying a default value for a column when no value is provided for that column in an INSERT or UPDATE statement.

## Syntax of Constraints

- The general syntax of defining constraints in SQL is:

  ```sql
  CREATE TABLE table_name (
    column1 datatype [CONSTRAINT constraint_name] constraint_type [constraint_parameters],
    column2 datatype [CONSTRAINT constraint_name] constraint_type [constraint_parameters],
    ...
    [CONSTRAINT constraint_name] constraint_type (column1, column2, ...) [constraint_parameters]
  );
  ```

  - The CONSTRAINT keyword is optional, but it is recommended to use it to give a meaningful name to the constraint.
  - The constraint_type can be one of the types mentioned above, such as NOT NULL, UNIQUE, etc.
  - The constraint_parameters are optional and depend on the type of the constraint, such as the name of the referenced table and column(s) for a foreign key constraint, or the condition for a check constraint.
  - The column-level constraints are defined after the datatype of the column, and they apply only to that column.
  - The table-level constraints are defined after all the columns, and they can apply to one or more columns in the table.

## Examples of Constraints

- Here are some examples of defining constraints in SQL:

  - Creating a table with a primary key constraint on the id column, a not null constraint on the name column, and a unique constraint on the email column:

    ```sql
    CREATE TABLE student (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      email VARCHAR(50) UNIQUE
    );
    ```

  - Creating a table with a foreign key constraint on the course_id column, which references the id column of the course table, and a check constraint on the grade column, which ensures that the grade is between 0 and 100:

    ```sql
    CREATE TABLE enrollment (
      student_id INT,
      course_id INT,
      grade INT,
      CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES course (id),
      CONSTRAINT ck_grade CHECK (grade BETWEEN 0 AND 100)
    );
    ```

  - Creating a table with a default constraint on the status column, which assigns the value 'active' to the status column if no value is provided:

    ```sql
    CREATE TABLE employee (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      salary DECIMAL(10,2),
      status VARCHAR(10) DEFAULT 'active'
    );
    ```
```