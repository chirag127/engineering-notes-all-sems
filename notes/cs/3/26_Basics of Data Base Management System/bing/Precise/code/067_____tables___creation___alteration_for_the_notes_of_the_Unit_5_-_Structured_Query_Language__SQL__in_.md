### Tables – Creation & Alteration

Tables are the fundamental objects in a relational database management system. They are used to store and organize data in a structured manner. In SQL, tables can be created and altered using the `CREATE TABLE` and `ALTER TABLE` statements respectively.

#### Creating Tables

The `CREATE TABLE` statement is used to create a new table in a database. The basic syntax for creating a table is as follows:

```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

Here, `table_name` is the name of the table and `column1`, `column2`, etc. are the names of the columns in the table. The `datatype` specifies the type of data that can be stored in the column.

For example, to create a table named `students` with columns `id`, `name`, and `age`, the following `CREATE TABLE` statement can be used:

```
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);
```

#### Altering Tables

The `ALTER TABLE` statement is used to add, modify, or delete columns in an existing table. It can also be used to add or drop constraints on a table.

The basic syntax for adding a column to a table is as follows:

```
ALTER TABLE table_name
ADD COLUMN column_name datatype;
```

Here, `table_name` is the name of the table, `column_name` is the name of the new column, and `datatype` specifies the type of data that can be stored in the column.

For example, to add a new column `email` to the `students` table, the following `ALTER TABLE` statement can be used:

```
ALTER TABLE students
ADD COLUMN email TEXT;
```

To modify a column in a table, the `ALTER TABLE` statement can be used with the `MODIFY COLUMN` clause. The basic syntax for modifying a column is as follows:

```
ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
```

Here, `table_name` is the name of the table, `column_name` is the name of the column to be modified, and `datatype` specifies the new data type for the column.

To delete a column from a table, the `ALTER TABLE` statement can be used with the `DROP COLUMN` clause. The basic syntax for deleting a column is as follows:

```
ALTER TABLE table_name
DROP COLUMN column_name;
```

Here, `table_name` is the name of the table and `column_name` is the name of the column to be deleted.

In summary, tables are the fundamental objects in a relational database management system and can be created and altered using the `CREATE TABLE` and `ALTER TABLE` statements in SQL. These statements allow for the addition, modification, and deletion of columns in a table, as well as the addition and removal of constraints on a table.