# Tables – Creation & Alteration

- A table is a collection of related data organized in rows and columns in a database.
- To create a table in SQL, use the `CREATE TABLE` statement, followed by the name of the table and the definition of its columns and constraints.
- For example, to create a table called `Students` with four columns: `id`, `name`, `age`, and `grade`, the syntax would be:

```sql
CREATE TABLE Students (
  id int,
  name varchar(50),
  age int,
  grade char(1)
);
```

- To modify the structure of an existing table, use the `ALTER TABLE` statement, followed by the name of the table and the changes to be made.
- The `ALTER TABLE` statement can be used to add, delete, or modify columns, as well as to add or delete constraints in a table.
- For example, to add a new column called `email` to the `Students` table, the syntax would be:

```sql
ALTER TABLE Students
ADD email varchar(50);
```

- To delete a column from a table, use the `DROP COLUMN` clause with the `ALTER TABLE` statement. For example, to delete the `grade` column from the `Students` table, the syntax would be:

```sql
ALTER TABLE Students
DROP COLUMN grade;
```

- To change the data type or size of a column, use the `ALTER COLUMN` clause with the `ALTER TABLE` statement. For example, to change the data type of the `age` column from `int` to `smallint`, the syntax would be:

```sql
ALTER TABLE Students
ALTER COLUMN age smallint;
```

- To add a constraint to a table, use the `ADD CONSTRAINT` clause with the `ALTER TABLE` statement. A constraint is a rule that restricts the values that can be stored in a column or a combination of columns. Some common types of constraints are: `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, and `CHECK`.
- For example, to add a primary key constraint to the `id` column of the `Students` table, the syntax would be:

```sql
ALTER TABLE Students
ADD CONSTRAINT pk_students PRIMARY KEY (id);
```

- To delete a constraint from a table, use the `DROP CONSTRAINT` clause with the `ALTER TABLE` statement. For example, to delete the primary key constraint from the `Students` table, the syntax would be:

```sql
ALTER TABLE Students
DROP CONSTRAINT pk_students;
```

- To create a copy of an existing table, use the `CREATE TABLE AS` statement, followed by the name of the new table and a query that selects the data from the existing table.
- For example, to create a new table called `Students_backup` that is a copy of the `Students` table, the syntax would be:

```sql
CREATE TABLE Students_backup AS
SELECT * FROM Students;
```

- To delete a table from a database, use the `DROP TABLE` statement, followed by the name of the table to be deleted.
- For example, to delete the `Students_backup` table, the syntax would be:

```sql
DROP TABLE Students_backup;
```

- To delete all the data from a table, but keep the table structure, use the `TRUNCATE TABLE` statement, followed by the name of the table to be emptied.
- For example, to delete all the data from the `Students` table, the syntax would be:

```sql
TRUNCATE TABLE Students;
```

- Note: The `TRUNCATE TABLE` statement is faster and more efficient than the `DELETE` statement, but it cannot be rolled back.