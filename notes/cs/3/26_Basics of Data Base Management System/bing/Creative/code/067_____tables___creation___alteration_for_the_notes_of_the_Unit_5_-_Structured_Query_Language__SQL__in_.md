Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System. Here is the content for the topic of tables – creation & alteration:

### Tables – creation & alteration

- A table is a collection of data organized in rows and columns in a relational database.
- A table has a name, a set of columns, and a set of rows. Each column has a name, a data type, and optionally some constraints. Each row has a value for each column.
- To create a table in SQL, we use the `CREATE TABLE` statement. The syntax is:

```sql
CREATE TABLE table_name (
  column1 data_type constraints,
  column2 data_type constraints,
  ...
);
```

- For example, to create a table called `students` with four columns: `id`, `name`, `age`, and `grade`, we can write:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT CHECK (age > 0),
  grade CHAR(1) DEFAULT 'F'
);
```

- The `PRIMARY KEY` constraint specifies that the `id` column is the unique identifier for each row. The `NOT NULL` constraint specifies that the `name` column cannot have null values. The `CHECK` constraint specifies that the `age` column must have positive values. The `DEFAULT` constraint specifies that the `grade` column will have the value 'F' if not specified otherwise.
- To alter a table in SQL, we use the `ALTER TABLE` statement. The syntax is:

```sql
ALTER TABLE table_name
  action;
```

- The action can be one of the following:

  - `ADD column_name data_type constraints` to add a new column to the table.
  - `DROP COLUMN column_name` to delete a column from the table.
  - `RENAME COLUMN old_name TO new_name` to rename a column in the table.
  - `MODIFY column_name data_type constraints` to change the data type or constraints of a column in the table.

- For example, to add a new column called `email` to the `students` table, we can write:

```sql
ALTER TABLE students
  ADD email VARCHAR(100) UNIQUE;
```

- The `UNIQUE` constraint specifies that the `email` column must have unique values for each row.