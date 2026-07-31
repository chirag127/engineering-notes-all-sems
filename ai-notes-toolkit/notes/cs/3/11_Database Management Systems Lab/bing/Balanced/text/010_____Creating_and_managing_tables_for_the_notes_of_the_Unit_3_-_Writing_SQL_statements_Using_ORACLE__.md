### Creating and managing tables for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- A table is a collection of related data organized in rows and columns in a database.
- To create a table in Oracle SQL, you use the `CREATE TABLE` statement, followed by the table name and the column definitions.
- The basic syntax of the `CREATE TABLE` statement is:

```sql
CREATE TABLE schema_name.table_name (
  column_1 data_type column_constraint,
  column_2 data_type column_constraint,
  ...
  table_constraint
);
```

- The `schema_name` is optional and specifies the schema where the table belongs. If omitted, the table is created in the current schema.
- The `table_name` is the name of the table that you want to create. It must be unique within the schema.
- The `column_1`, `column_2`, etc. are the names of the columns in the table. Each column must have a data type and an optional column constraint.
- The `data_type` specifies the type and size of the data that can be stored in the column. Oracle SQL supports many data types, such as `NUMBER`, `VARCHAR2`, `DATE`, `TIMESTAMP`, `CLOB`, etc.
- The `column_constraint` specifies the rules that the data in the column must follow. Some common column constraints are `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, etc.
- The `table_constraint` specifies the rules that the data in the table must follow. Some common table constraints are `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, etc.

- For example, to create a table named `employees` with four columns: `id`, `name`, `salary`, and `department_id`, you can use the following statement:

```sql
CREATE TABLE employees (
  id NUMBER PRIMARY KEY,
  name VARCHAR2(50) NOT NULL,
  salary NUMBER CHECK (salary > 0),
  department_id NUMBER REFERENCES departments(id)
);
```

- This statement creates a table named `employees` in the current schema with the following characteristics:
  - The `id` column is of type `NUMBER` and is the primary key of the table. This means that the values in this column must be unique and not null.
  - The `name` column is of type `VARCHAR2(50)` and is not null. This means that the values in this column can store up to 50 characters and cannot be empty.
  - The `salary` column is of type `NUMBER` and has a check constraint. This means that the values in this column must be greater than zero.
  - The `department_id` column is of type `NUMBER` and references the `id` column of the `departments` table. This means that the values in this column must exist in the `departments` table and create a foreign key relationship between the two tables.

- To manage tables in Oracle SQL, you can use various commands, such as `ALTER TABLE`, `DROP TABLE`, `RENAME TABLE`, `TRUNCATE TABLE`, etc.
- The `ALTER TABLE` command allows you to modify the structure or properties of an existing table. For example, you can add, drop, or modify columns, add or drop constraints, enable or disable triggers, etc.
- The `DROP TABLE` command allows you to delete an existing table and its data from the database. For example, you can use the following statement to delete the `employees` table:

```sql
DROP TABLE employees;
```

- The `RENAME TABLE` command allows you to change the name of an existing table. For example, you can use the following statement to rename the `employees` table to `staff`:

```sql
RENAME TABLE employees TO staff;
```

- The `TRUNCATE TABLE` command allows you to delete all the data from an existing table without deleting the table itself. For example, you can use the following statement to delete all the data from the `employees` table:

```sql
TRUNCATE TABLE employees;
```

- These are some of the basic commands for creating and managing tables in Oracle SQL. For more details and examples, you can refer to the official Oracle documentation    or online tutorials.