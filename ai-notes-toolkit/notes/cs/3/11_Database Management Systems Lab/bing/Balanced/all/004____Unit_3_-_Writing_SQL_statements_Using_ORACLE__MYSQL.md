# Unit 3 - Writing SQL statements Using ORACLE /MYSQL

SQL stands for Structured Query Language. It is a standard language for accessing and manipulating data in relational databases. SQL can be used to perform various tasks, such as creating tables, inserting records, updating data, deleting data, querying data, joining tables, and applying functions.

ORACLE and MYSQL are two popular relational database management systems (RDBMS) that support SQL. They have some differences in syntax, data types, and features, but they also share many commonalities. In this unit, we will learn how to write basic SQL statements using ORACLE or MYSQL.

## Creating Tables

To create a table in SQL, we use the CREATE TABLE statement. The syntax is:

```
CREATE TABLE table_name (
  column1 data_type constraints,
  column2 data_type constraints,
  ...
);
```

The table_name is the name of the table we want to create. The column names and data types define the structure of the table. The constraints are optional and specify rules for the data in each column, such as primary key, foreign key, not null, unique, etc.

For example, to create a table called customers with four columns: id, name, email, and phone, we can write:

```
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) UNIQUE,
  phone VARCHAR(15)
);
```

The data types and constraints may vary depending on the RDBMS. For example, ORACLE uses NUMBER instead of INT, and VARCHAR2 instead of VARCHAR. MYSQL supports AUTO_INCREMENT for generating sequential values for primary keys, while ORACLE uses SEQUENCE objects.

## Inserting Records

To insert a record into a table, we use the INSERT INTO statement. The syntax is:

```
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
```

The table_name is the name of the table we want to insert the record into. The column names and values specify the data for each column. If we omit the column names, we have to provide values for all columns in the same order as they are defined in the table.

For example, to insert a record into the customers table, we can write:

```
INSERT INTO customers (id, name, email, phone) VALUES (1, 'Alice', 'alice@example.com', '1234567890');
```

Or, we can write:

```
INSERT INTO customers VALUES (1, 'Alice', 'alice@example.com', '1234567890');
```

## Updating Data

To update data in a table, we use the UPDATE statement. The syntax is:

```
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

The table_name is the name of the table we want to update. The SET clause specifies the columns and values we want to change. The WHERE clause specifies the condition for selecting the records we want to update. If we omit the WHERE clause, all records in the table will be updated.

For example, to update the email of the customer with id 1, we can write:

```
UPDATE customers SET email = 'alice@gmail.com' WHERE id = 1;
```

## Deleting Data

To delete data from a table, we use the DELETE statement. The syntax is:

```
DELETE FROM table_name WHERE condition;
```

The table_name is the name of the table we want to delete data from. The WHERE clause specifies the condition for selecting the records we want to delete. If we omit the WHERE clause, all records in the table will be deleted.

For example, to delete the customer with id 1, we can write:

```
DELETE FROM customers WHERE id = 1;
```

## Querying Data

To query data from a table, we use the SELECT statement. The syntax is:

```
SELECT column1, column2, ... FROM table_name WHERE condition GROUP BY column1, column2, ... HAVING condition ORDER BY column1, column2, ... ASC/DESC;
```

The SELECT clause specifies the columns we want to retrieve from the table. We can use * to select all columns. The FROM clause specifies the table we want to query from. The WHERE clause specifies the condition for filtering the records. The GROUP BY clause specifies the columns we want to group the records by. The HAVING clause specifies the condition for filtering the groups. The ORDER BY clause specifies the columns we want to sort the records by. The ASC/DESC keywords specify the ascending or descending order of the sorting.

For example, to query the name and email of the customers who have a phone number, we can write:

``