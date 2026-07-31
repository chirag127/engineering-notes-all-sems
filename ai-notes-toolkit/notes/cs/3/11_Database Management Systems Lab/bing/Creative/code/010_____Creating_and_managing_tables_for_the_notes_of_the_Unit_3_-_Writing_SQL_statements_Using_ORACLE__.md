### Creating and managing tables for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- A table is a collection of related data organized in rows and columns in a database.
- To create a table in SQL, use the `CREATE TABLE` command, followed by the name of the table and the definitions of the columns.
- For example, to create a table called `students` with columns `id`, `name`, `age`, and `grade`, the SQL statement would be:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT CHECK (age > 0),
  grade CHAR(1) DEFAULT 'F'
);
```

- The column definitions specify the data type, constraints, and default values of each column.
- To view the structure of a table, use the `DESCRIBE` command, followed by the name of the table.
- For example, to view the structure of the `students` table, the SQL statement would be:

```sql
DESCRIBE students;
```

- To modify the structure of a table, use the `ALTER TABLE` command, followed by the name of the table and the changes to be made.
- For example, to add a new column called `email` to the `students` table, the SQL statement would be:

```sql
ALTER TABLE students
ADD email VARCHAR(100) UNIQUE;
```

- To delete a column from a table, use the `DROP COLUMN` clause with the `ALTER TABLE` command.
- For example, to delete the `grade` column from the `students` table, the SQL statement would be:

```sql
ALTER TABLE students
DROP COLUMN grade;
```

- To rename a table or a column, use the `RENAME` clause with the `ALTER TABLE` command.
- For example, to rename the `students` table to `learners`, the SQL statement would be:

```sql
ALTER TABLE students
RENAME TO learners;
```

- To delete a table from the database, use the `DROP TABLE` command, followed by the name of the table.
- For example, to delete the `learners` table, the SQL statement would be:

```sql
DROP TABLE learners;
```

- To create a copy of an existing table, use the `CREATE TABLE AS` command, followed by the name of the new table and the query to select the data from the existing table.
- For example, to create a copy of the `students` table called `backup`, the SQL statement would be:

```sql
CREATE TABLE backup AS
SELECT * FROM students;
```

- To create a table with only specific columns from another table, use the `CREATE TABLE AS` command with the column names in the query.
- For example, to create a table called `names` with only the `id` and `name` columns from the `students` table, the SQL statement would be:

```sql
CREATE TABLE names AS
SELECT id, name FROM students;
```

- To create an empty table with the same structure as another table, use the `CREATE TABLE AS` command with the `WHERE` clause that evaluates to false.
- For example, to create an empty table called `empty` with the same structure as the `students` table, the SQL statement would be:

```sql
CREATE TABLE empty AS
SELECT * FROM students
WHERE 1 = 0;
```

- To view the data in a table, use the `SELECT` command, followed by the column names or `*` for all columns, and the name of the table.
- For example, to view all the data in the `students` table, the SQL statement would be:

```sql
SELECT * FROM students;
```

- To insert data into a table, use the `INSERT INTO` command, followed by the name of the table, the column names (optional), and the values to be inserted.
- For example, to insert a new row into the `students` table, the SQL statement would be:

```sql
INSERT INTO students (id, name, age, grade)
VALUES (1, 'Alice', 18, 'A');
```

- To update data in a table, use the `UPDATE` command, followed by the name of the table, the `SET` clause with the new values, and the `WHERE` clause to specify the rows to be updated.
- For example, to change the grade of Alice to 'B' in the `students