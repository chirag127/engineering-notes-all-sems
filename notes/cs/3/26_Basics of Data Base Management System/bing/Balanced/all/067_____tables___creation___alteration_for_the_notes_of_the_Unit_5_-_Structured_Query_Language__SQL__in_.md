# Tables – Creation & Alteration

- A table is a collection of data organized in rows and columns in a relational database.
- To create a table in SQL, we use the **CREATE TABLE** statement, followed by the name of the table and the definition of the columns and their data types   .
- For example, the following SQL statement creates a table called **Customers** with four columns: **id**, **name**, **address**, and **phone**.

```sql
CREATE TABLE Customers (
  id int,
  name varchar(50),
  address text,
  phone varchar(10)
);
```

- To add data to a table, we use the **INSERT INTO** statement, followed by the name of the table, the columns to insert, and the values to insert .
- For example, the following SQL statement inserts a row into the **Customers** table with the values 1, 'Alice', '123 Main Street', and '555-1111'.

```sql
INSERT INTO Customers (id, name, address, phone)
VALUES (1, 'Alice', '123 Main Street', '555-1111');
```

- To modify the structure of a table, we use the **ALTER TABLE** statement, followed by the name of the table and the changes to apply   .
- For example, the following SQL statement adds a new column called **email** to the **Customers** table.

```sql
ALTER TABLE Customers
ADD email varchar(50);
```

- To delete a table, we use the **DROP TABLE** statement, followed by the name of the table .
- For example, the following SQL statement deletes the **Customers** table.

```sql
DROP TABLE Customers;
```

- To delete all the data from a table, but keep the table structure, we use the **TRUNCATE TABLE** statement, followed by the name of the table.
- For example, the following SQL statement deletes all the rows from the **Customers** table, but keeps the columns.

```sql
TRUNCATE TABLE Customers;
```

- To create a copy of an existing table, we use the **CREATE TABLE AS** statement, followed by the name of the new table and a query to select the data from the existing table.
- For example, the following SQL statement creates a new table called **TestTable** that is a copy of the **Customers** table.

```sql
CREATE TABLE TestTable AS
SELECT * FROM Customers;
```