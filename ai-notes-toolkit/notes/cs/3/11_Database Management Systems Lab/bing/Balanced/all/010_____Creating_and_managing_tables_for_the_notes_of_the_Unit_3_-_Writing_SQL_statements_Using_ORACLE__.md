# Creating and managing tables for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- A table is a collection of related data organized in rows and columns in a relational database.
- To create a table in SQL, use the `CREATE TABLE` command, followed by the name of the table and the definition of its columns and constraints.
- For example, to create a table called `students` with columns `id`, `name`, `age`, and `grade`, the SQL statement would be:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT CHECK (age > 0),
  grade CHAR(1) DEFAULT 'F'
);
```

- To modify an existing table, use the `ALTER TABLE` command, followed by the name of the table and the changes to be made.
- For example, to add a new column called `email` to the `students` table, the SQL statement would be:

```sql
ALTER TABLE students
ADD email VARCHAR(100) UNIQUE;
```

- To delete an existing table, use the `DROP TABLE` command, followed by the name of the table to be dropped.
- For example, to delete the `students` table, the SQL statement would be:

```sql
DROP TABLE students;
```

- To view the structure and contents of a table, use the `DESCRIBE` and `SELECT` commands, respectively.
- For example, to view the structure of the `students` table, the SQL statement would be:

```sql
DESCRIBE students;
```

- To view the contents of the `students` table, the SQL statement would be:

```sql
SELECT * FROM students;
```

- To insert, update, or delete data in a table, use the `INSERT`, `UPDATE`, or `DELETE` commands, respectively.
- For example, to insert a new row into the `students` table, the SQL statement would be:

```sql
INSERT INTO students (id, name, age, grade, email)
VALUES (1, 'Alice', 18, 'A', 'alice@example.com');
```

- To update an existing row in the `students` table, the SQL statement would be:

```sql
UPDATE students
SET grade = 'B', email = 'alice@new.com'
WHERE id = 1;
```

- To delete an existing row in the `students` table, the SQL statement would be:

```sql
DELETE FROM students
WHERE id = 1;
```

- To query data from a table, use the `SELECT` command, followed by the columns to be retrieved and the table to be queried.
- For example, to query the name and grade of all students from the `students` table, the SQL statement would be:

```sql
SELECT name, grade FROM students;
```

- To filter, sort, group, or join data from a table, use the `WHERE`, `ORDER BY`, `GROUP BY`, or `JOIN` clauses, respectively.
- For example, to query the name and grade of all students who have a grade higher than 'C' from the `students` table, sorted by name in ascending order, the SQL statement would be:

```sql
SELECT name, grade FROM students
WHERE grade > 'C'
ORDER BY name ASC;
```

- To create a copy of an existing table, use the `CREATE TABLE AS` command, followed by the name of the new table and the query to be used to populate it.
- For example, to create a new table called `top_students` with the same structure and data as the `students` table, the SQL statement would be:

```sql
CREATE TABLE top_students AS
SELECT * FROM students;
```

- To create a temporary table that exists only for the duration of a session, use the `CREATE TEMPORARY TABLE` command, followed by the name of the table and the definition of its columns and constraints.
- For example, to create a temporary table called `temp_students` with the same structure as the `students` table, the SQL statement would be:

```sql
CREATE TEMPORARY TABLE temp_students
LIKE students;
```