### Tables – Creation & Alteration

Tables are the fundamental building blocks of a database. They store and organize data in rows and columns. Here are the key points to know about creating and altering tables in SQL:

#### Creating Tables

To create a table, you use the `CREATE TABLE` statement followed by the table name and a list of columns and their data types. Here's an example:

```sql
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20)
);
```

In this example, we're creating a table called `customers` with four columns: `id`, `name`, `email`, and `phone`. The `id` column is the primary key, which means it uniquely identifies each row in the table. The other columns are of type `VARCHAR`, which stores variable-length character strings. The number in parentheses specifies the maximum length of the string.

#### Altering Tables

Sometimes you need to modify an existing table. Here are some common alterations you might make:

- Add a new column to a table using the `ALTER TABLE` statement:

```sql
ALTER TABLE customers
ADD address VARCHAR(200);
```

- Rename a column using the `ALTER TABLE` statement:

```sql
ALTER TABLE customers
RENAME COLUMN phone TO phone_number;
```

- Change the data type of a column using the `ALTER TABLE` statement:

```sql
ALTER TABLE customers
ALTER COLUMN email SET DATA TYPE TEXT;
```

- Delete a column from a table using the `ALTER TABLE` statement:

```sql
ALTER TABLE customers
DROP COLUMN address;
```

- Add a constraint to a table using the `ALTER TABLE` statement:

```sql
ALTER TABLE customers
ADD CONSTRAINT unique_email UNIQUE (email);
```

In this example, we're adding a unique constraint to the `email` column, which ensures that no two rows can have the same email address.

#### Conclusion

Creating and altering tables is a fundamental skill in SQL. By understanding how to use the `CREATE TABLE` and `ALTER TABLE` statements, you can design and modify databases to meet your needs.