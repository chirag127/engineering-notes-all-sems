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
- To alter a table in SQL, use the `ALTER TABLE` command, followed by the name of the table and the changes to be made.
- For example, the following SQL statement adds a new column called `phone` to the `Students` table.

```sql
ALTER TABLE Students
ADD phone varchar(10);
```

- The `ADD` clause adds a new column or constraint to the table.
- To modify an existing column or constraint, use the `MODIFY` or `ALTER` clause.
- For example, the following SQL statement changes the data type of the `phone` column to `char(10)`.

```sql
ALTER TABLE Students
MODIFY phone char(10);
```

- To delete an existing column or constraint, use the `DROP` clause.
- For example, the following SQL statement removes the `email` column from the `Students` table.

```sql
ALTER TABLE Students
DROP COLUMN email;
```

- To rename a table or a column, use the `RENAME` clause.
- For example, the following SQL statement renames the `Students` table to `Learners`.

```sql
ALTER TABLE Students
RENAME TO Learners;
```

- To delete a table from the database, use the `DROP TABLE` command, followed by the name of the table.
- For example, the following SQL statement deletes the `Learners` table.

```sql
DROP TABLE Learners;
```

- To create a copy of an existing table, use the `CREATE TABLE AS` command, followed by the name of the new table and a query that selects the data from the existing table.
- For example, the following SQL statement creates a new table called `Graduates` that contains the data from the `Students` table where the `grade` is `A`.

```sql
CREATE TABLE Graduates AS
SELECT * FROM Students
WHERE grade = 'A';
```

- To truncate a table, use the `TRUNCATE TABLE` command, followed by the name of the table.
- This command deletes all the data from the table, but preserves its structure and constraints.
- For example, the following SQL statement truncates the `Graduates` table.

```sql
TRUNCATE TABLE Graduates;
```

- To view the structure and constraints of a table, use the `DESCRIBE` or `DESC` command, followed by the name of the table.
- For example, the following SQL statement describes the `Students` table.

```sql
DESCRIBE Students;
```

- This command returns the following output:

| Field | Type        | Null | Key  | Default | Extra |
| ----- | ----------- | ---- | ---- | ------- | ----- |
| id    | int         | NO   | PRI  | NULL    |       |
| name  | varchar(50) | NO   |      | NULL    |       |
| grade | char(1)     | YES  |      | NULL    |       |
| email | varchar(50) | YES  | UNI  | NULL    |       |
| phone | char(10)    | YES  |      | NULL    |       |

- To view the data in a table, use the `SELECT` command, followed by the columns and the table name.
- For example, the following SQL statement selects all the columns and rows from the `Students` table.

```sql
SELECT * FROM Students;
```

- This command returns the following output:

| id | name       | grade