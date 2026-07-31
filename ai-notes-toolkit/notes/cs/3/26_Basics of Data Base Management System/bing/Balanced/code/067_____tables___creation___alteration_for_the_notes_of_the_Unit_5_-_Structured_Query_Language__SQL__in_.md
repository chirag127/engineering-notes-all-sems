### Tables – Creation & Alteration

- A table is a collection of data organized in rows and columns in a relational database.
- To create a table in SQL, use the `CREATE TABLE` statement, followed by the table name and the column definitions.
- For example, to create a table called `Students` with four columns: `id`, `name`, `age`, and `grade`, the syntax would be:

```sql
CREATE TABLE Students (
  id int,
  name varchar(50),
  age int,
  grade char(1)
);
```

- To add data to a table, use the `INSERT INTO` statement, followed by the table name, the column names, and the values to insert.
- For example, to insert a row into the `Students` table, the syntax would be:

```sql
INSERT INTO Students (id, name, age, grade) VALUES (1, 'Alice', 18, 'A');
```

- To modify the structure of a table, use the `ALTER TABLE` statement, followed by the table name and the changes to make.
- For example, to add a new column called `email` to the `Students` table, the syntax would be:

```sql
ALTER TABLE Students ADD email varchar(50);
```

- To delete a table, use the `DROP TABLE` statement, followed by the table name.
- For example, to delete the `Students` table, the syntax would be:

```sql
DROP TABLE Students;
```

- To delete all the data from a table, but keep the table structure, use the `TRUNCATE TABLE` statement, followed by the table name.
- For example, to delete all the data from the `Students` table, the syntax would be:

```sql
TRUNCATE TABLE Students;
```

- To create a copy of an existing table, use the `CREATE TABLE AS` statement, followed by the new table name and a `SELECT` query that specifies the columns and data to copy.
- For example, to create a new table called `Graduates` that is a copy of the `Students` table with only the students who have grade 'A', the syntax would be:

```sql
CREATE TABLE Graduates AS
SELECT id, name, age, grade
FROM Students
WHERE grade = 'A';
```

- To rename a table, use the `ALTER TABLE` statement, followed by the old table name, the `RENAME TO` keyword, and the new table name.
- For example, to rename the `Graduates` table to `Alumni`, the syntax would be:

```sql
ALTER TABLE Graduates RENAME TO Alumni;
```

- To change the data type or size of a column, use the `ALTER TABLE` statement, followed by the table name, the `ALTER COLUMN` keyword, the column name, and the new data type or size.
- For example, to change the data type of the `age` column in the `Students` table from `int` to `smallint`, the syntax would be:

```sql
ALTER TABLE Students ALTER COLUMN age smallint;
```

- To add a constraint to a table or a column, use the `ALTER TABLE` statement, followed by the table name, the `ADD` keyword, and the constraint definition.
- For example, to add a primary key constraint to the `id` column in the `Students` table, the syntax would be:

```sql
ALTER TABLE Students ADD PRIMARY KEY (id);
```

- To remove a constraint from a table or a column, use the `ALTER TABLE` statement, followed by the table name, the `DROP` keyword, and the constraint name.
- For example, to remove the primary key constraint from the `id` column in the `Students` table, the syntax would be:

```sql
ALTER TABLE Students DROP PRIMARY KEY;
```

- To view the structure and data of a table, use the `DESCRIBE` or `DESC` statement, followed by the table name, or the `SELECT` statement, followed by the columns and the table name.
- For example, to view the structure of the `Students` table, the syntax would be:

```sql
DESCRIBE Students;
```

- To view the data of the `Students` table, the syntax would be:

```sql
SELECT * FROM Students;
```