### Tables – Creation & Alteration

Tables are the fundamental objects in a relational database management system. They are used to store and organize data in a structured manner. In SQL, tables can be created and altered using the `CREATE TABLE` and `ALTER TABLE` statements respectively.

#### Creating Tables

To create a table in SQL, the `CREATE TABLE` statement is used. The basic syntax for creating a table is as follows:

```SQL
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

Here, `table_name` is the name of the table being created, `column1`, `column2`, etc. are the names of the columns in the table, and `datatype` specifies the data type of each column.

For example, to create a table named `students` with columns `id`, `name`, and `age`, the following SQL statement can be used:

```SQL
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);
```

This creates a table named `students` with three columns: `id` of type `INTEGER`, `name` of type `TEXT`, and `age` of type `INTEGER`. The `PRIMARY KEY` constraint is used to specify that the `id` column is the primary key of the table, and the `NOT NULL` constraint is used to specify that the `name` column cannot contain null values.

#### Altering Tables

Once a table has been created, its structure can be modified using the `ALTER TABLE` statement. This statement can be used to add, modify, or delete columns in a table, as well as to add or drop constraints.

The basic syntax for adding a column to a table is as follows:

```SQL
ALTER TABLE table_name
ADD column_name datatype;
```

Here, `table_name` is the name of the table being altered, `column_name` is the name of the column being added, and `datatype` specifies the data type of the new column.

For example, to add a new column named `email` to the `students` table, the following SQL statement can be used:

```SQL
ALTER TABLE students
ADD email TEXT;
```

This adds a new column named `email` of type `TEXT` to the `students` table.

To modify an existing column, the `ALTER COLUMN` clause is used. The basic syntax for modifying a column is as follows:

```SQL
ALTER TABLE table_name
ALTER COLUMN column_name datatype;
```

Here, `table_name` is the name of the table being altered, `column_name` is the name of the column being modified, and `datatype` specifies the new data type of the column.

For example, to change the data type of the `age` column in the `students` table to `REAL`, the following SQL statement can be used:

```SQL
ALTER TABLE students
ALTER COLUMN age REAL;
```

This changes the data type of the `age` column in the `students` table to `REAL`.

To delete a column from a table, the `DROP COLUMN` clause is used. The basic syntax for deleting a column is as follows:

```SQL
ALTER TABLE table_name
DROP COLUMN column_name;
```

Here, `table_name` is the name of the table being altered, and `column_name` is the name of the column being deleted.

For example, to delete the `email` column from the `students` table, the following SQL statement can be used:

```SQL
ALTER TABLE students
DROP COLUMN email;
```

This deletes the `email` column from the `students` table.

In addition to adding, modifying, and deleting columns, the `ALTER TABLE` statement can also be used to add or drop constraints on a table. The syntax for adding or dropping constraints is specific to the type of constraint being added or dropped.