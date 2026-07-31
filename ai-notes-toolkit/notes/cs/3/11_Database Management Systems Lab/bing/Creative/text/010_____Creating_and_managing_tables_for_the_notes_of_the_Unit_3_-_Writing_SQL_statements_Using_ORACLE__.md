Hello, I am Sydney, your AI assistant. I can help you with your topic of creating and managing tables for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab. Here is some content that you can use for your notes:

### Creating and managing tables

- A table is a collection of related data organized in rows and columns.
- To create a table, you need to specify its name, columns, data types, and constraints.
- The syntax for creating a table in SQL is:

```sql
CREATE TABLE table_name (
  column1 data_type constraints,
  column2 data_type constraints,
  ...
);
```

- For example, to create a table called `students` with columns `id`, `name`, `age`, and `grade`, you can write:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT CHECK (age > 0),
  grade CHAR(1) DEFAULT 'F'
);
```

- To insert data into a table, you can use the `INSERT` statement.
- The syntax for inserting data into a table is:

```sql
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
```

- For example, to insert a row into the `students` table, you can write:

```sql
INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 19, 'A');
```

- To view the data in a table, you can use the `SELECT` statement.
- The syntax for selecting data from a table is:

```sql
SELECT column1, column2, ... FROM table_name WHERE condition;
```

- For example, to select all the rows from the `students` table, you can write:

```sql
SELECT * FROM students;
```

- To update the data in a table, you can use the `UPDATE` statement.
- The syntax for updating data in a table is:

```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

- For example, to change the grade of Alice to 'B', you can write:

```sql
UPDATE students SET grade = 'B' WHERE name = 'Alice';
```

- To delete the data from a table, you can use the `DELETE` statement.
- The syntax for deleting data from a table is:

```sql
DELETE FROM table_name WHERE condition;
```

- For example, to delete the row of Alice from the `students` table, you can write:

```sql
DELETE FROM students WHERE name = 'Alice';
```

- To delete the entire table, you can use the `DROP` statement.
- The syntax for dropping a table is:

```sql
DROP TABLE table_name;
```

- For example, to drop the `students` table, you can write:

```sql
DROP TABLE students;
```

- To modify the structure of a table, you can use the `ALTER` statement.
- The syntax for altering a table is:

```sql
ALTER TABLE table_name action;
```

- The action can be one of the following:

  - `ADD column_name data_type constraints` to add a new column to the table.
  - `DROP column_name` to delete a column from the table.
  - `RENAME TO new_table_name` to change the name of the table.
  - `MODIFY column_name data_type constraints` to change the data type or constraints of a column.

- For example, to add a new column called `email` to the `students` table, you can write:

```sql
ALTER TABLE students ADD email VARCHAR(50);
```

- To rename the `students` table to `learners`, you can write:

```sql
ALTER TABLE students RENAME TO learners;
```

- To modify the data type of the `age` column to `SMALLINT`, you can write:

```sql
ALTER TABLE learners MODIFY age SMALLINT;
```

- To drop the `email` column from the `learners` table, you can write:

```sql
ALTER TABLE learners DROP email;
```

- These are some of the basic operations that you can perform on tables using SQL statements. You can also use other clauses and functions to manipulate the data in more complex ways. For more details, you can refer to the official documentation of ORACLE or MYSQL.