### Tables – Creation & Alteration

In the Structured Query Language (SQL), tables are used to store data. In this section, we will discuss the creation and alteration of tables in SQL.

#### Creating Tables

To create a table in SQL, we use the `CREATE TABLE` statement. The syntax for creating a table is as follows:

```sql
CREATE TABLE table_name (
   column1 datatype,
   column2 datatype,
   column3 datatype,
   .....
);
```

Here, `table_name` is the name of the table that we want to create. The columns of the table are defined inside the parentheses. Each column is defined by its name and data type.

For example, to create a table called `employees` with columns `id`, `name`, `age`, and `salary`, we can use the following SQL statement:

```sql
CREATE TABLE employees (
   id INT PRIMARY KEY,
   name VARCHAR(255),
   age INT,
   salary DECIMAL(10, 2)
);
```

#### Altering Tables

We can modify the structure of a table by using the `ALTER TABLE` statement. The syntax for altering a table is as follows:

```sql
ALTER TABLE table_name
   action;
```

Here, `table_name` is the name of the table that we want to alter. The `action` parameter specifies the modification that we want to make.

Some common actions that can be performed using the `ALTER TABLE` statement are:

- Adding a new column to a table:

```sql
ALTER TABLE table_name
   ADD column_name datatype;
```

- Modifying the data type of a column:

```sql
ALTER TABLE table_name
   ALTER COLUMN column_name datatype;
```

- Dropping a column from a table:

```sql
ALTER TABLE table_name
   DROP COLUMN column_name;
```

- Renaming a table:

```sql
ALTER TABLE table_name
   RENAME TO new_table_name;
```

These are some basic operations that can be performed using the `ALTER TABLE` statement. It is important to note that some of these operations may cause the data in the table to be lost, so it is recommended to take a backup of the table before making any modifications.

In conclusion, tables are an essential part of any database, and knowing how to create and modify them is crucial for using SQL effectively. With the `CREATE TABLE` and `ALTER TABLE` statements, we can easily create and modify tables in SQL.