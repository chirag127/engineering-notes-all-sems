Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System. Here are some notes for you:

### Structured Query Language (SQL)

- SQL is a standard language for creating, manipulating, and querying relational databases.
- SQL consists of several commands, such as `CREATE`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and `DROP`, that can be used to perform different operations on database objects, such as tables, views, indexes, and constraints.
- SQL also supports various clauses, such as `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `JOIN`, and `UNION`, that can be used to filter, aggregate, sort, and combine data from one or more tables.
- SQL also supports various functions, such as `SUM`, `COUNT`, `AVG`, `MIN`, `MAX`, and `SUBSTRING`, that can be used to perform calculations and transformations on data values.
- SQL also supports various data types, such as `INTEGER`, `VARCHAR`, `DATE`, `TIME`, and `BOOLEAN`, that can be used to define the format and range of data values stored in database columns.
- SQL also supports various constraints, such as `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, and `CHECK`, that can be used to enforce the integrity and consistency of data in database tables.
- SQL also supports various keywords, such as `DISTINCT`, `ALL`, `AS`, `IN`, `BETWEEN`, and `LIKE`, that can be used to modify the behavior and output of SQL commands and clauses.

Here is an example of a SQL statement that creates a table called `students` with four columns: `id`, `name`, `age`, and `grade`:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INTEGER CHECK (age > 0),
  grade VARCHAR(2) CHECK (grade IN ('A', 'B', 'C', 'D', 'F'))
);
```

Here is an example of a SQL statement that inserts a new row into the `students` table with the values `1`, `Alice`, `20`, and `A`:

```sql
INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 20, 'A');
```

Here is an example of a SQL statement that selects all the columns and rows from the `students` table:

```sql
SELECT * FROM students;
```

Here is an example of a SQL statement that updates the `grade` column of the `students` table to `B` where the `id` column is `1`:

```sql
UPDATE students SET grade = 'B' WHERE id = 1;
```

Here is an example of a SQL statement that deletes the row from the `students` table where the `id` column is `1`:

```sql
DELETE FROM students WHERE id = 1;
```

Here is an example of a SQL statement that drops the `students` table from the database:

```sql
DROP TABLE students;
```