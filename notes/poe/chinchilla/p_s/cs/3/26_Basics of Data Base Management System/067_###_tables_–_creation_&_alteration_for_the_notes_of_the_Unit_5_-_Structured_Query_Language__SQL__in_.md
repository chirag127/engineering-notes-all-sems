### Tables – Creation & Alteration

In a database management system, a table is a collection of related data arranged in rows and columns. Tables are used to store and organize data and are a fundamental component of relational databases. In this section, we will discuss the creation and alteration of tables using SQL.

#### Creating a Table

To create a table in SQL, we use the CREATE TABLE statement. The syntax for creating a table is as follows:

```
CREATE TABLE table_name (
  column1 datatype,
  column2 datatype,
  ...
);
```

- The `CREATE TABLE` statement is used to create a new table.
- The `table_name` is the name of the table that we want to create.
- The `column1`, `column2`, etc., are the names of the columns in the table.
- The `datatype` is the type of data that each column will store.

For example, let's create a table named `customers` with columns for `id`, `name`, and `email`:

```
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100)
);
```

In the above example, we have created a table named `customers` with three columns - `id`, `name`, and `email`. The `id` column is set as the primary key, which means it will uniquely identify each row in the table.

#### Altering a Table

Sometimes, we may need to make changes to an existing table. This is where the ALTER TABLE statement comes in. The ALTER TABLE statement is used to add, modify, or delete columns in an existing table.

The syntax for altering a table is as follows:

```
ALTER TABLE table_name
  ADD column_name datatype;

ALTER TABLE table_name
  MODIFY column_name datatype;

ALTER TABLE table_name
  DROP column_name;
```

- The `ALTER TABLE` statement is used to modify an existing table.
- The `table_name` is the name of the table that we want to modify.
- The `column_name` is the name of the column that we want to add, modify, or delete.
- The `datatype` is the new data type for the column (if modifying) or the type of data for the new column (if adding).

For example, let's add a new column named `phone` to the `customers` table:

```
ALTER TABLE customers
  ADD phone VARCHAR(20);
```

In the above example, we have added a new column named `phone` to the `customers` table with a data type of `VARCHAR(20)`.

#### Conclusion

In conclusion, tables are a fundamental component of relational databases and are used to store and organize data. To create a table in SQL, we use the CREATE TABLE statement, and to make changes to an existing table, we use the ALTER TABLE statement. These statements are essential tools for managing data in a database management system.