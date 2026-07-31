### Tables – Creation & Alteration

- A table is a collection of data organized in rows and columns in a relational database.
- To create a table in SQL, use the `CREATE TABLE` command, followed by the name of the table and the definition of its columns and constraints.
- For example, the following SQL statement creates a table called `Students` with four columns: `id`, `name`, `grade`, and `email`.

```sql
CREATE TABLE Students (
  id int PRIMARY KEY,
  name varchar(50) NOT NULL,
  grade char(1) CHECK (grade IN ('A', 'B', 'C', 'D', 'F')),
  email varchar(50) UNIQUE
);
```

- The `PRIMARY KEY` constraint defines a column that uniquely identifies each row in the table.
- The `NOT NULL` constraint ensures that a column cannot have a null value.
- The `CHECK` constraint validates that a column value satisfies a logical condition.
- The `UNIQUE` constraint ensures that a column value is not repeated in the table.
- To modify the structure of an existing table, use the `ALTER TABLE` command, followed by the name of the table and the changes to be made.
- For example, the following SQL statement adds a new column called `phone` to the `Students` table.

```sql
ALTER TABLE Students
ADD phone varchar(10);
```

- To delete a column from a table, use the `DROP COLUMN` clause with the `ALTER TABLE` command.
- For example, the following SQL statement deletes the `email` column from the `Students` table.

```sql
ALTER TABLE Students
DROP COLUMN email;
```

- To rename a table or a column, use the `RENAME` clause with the `ALTER TABLE` command.
- For example, the following SQL statement renames the `Students` table to `Learners`.

```sql
ALTER TABLE Students
RENAME TO Learners;
```

- To delete a table from the database, use the `DROP TABLE` command, followed by the name of the table.
- For example, the following SQL statement deletes the `Learners` table from the database.

```sql
DROP TABLE Learners;
```

- To create a copy of an existing table, use the `CREATE TABLE AS` command, followed by the name of the new table and a query that selects the data from the existing table.
- For example, the following SQL statement creates a new table called `Grades` that contains the `id`, `name`, and `grade` columns from the `Students` table.

```sql
CREATE TABLE Grades AS
SELECT id, name, grade
FROM Students;
```