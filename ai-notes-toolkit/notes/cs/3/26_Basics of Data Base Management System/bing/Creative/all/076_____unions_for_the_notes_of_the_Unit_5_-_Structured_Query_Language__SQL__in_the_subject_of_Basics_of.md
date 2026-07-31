# Unions in SQL

- UNION is an SQL operator that combines the result of two or more SELECT queries and provides a single set in the output  .
- The UNION operator removes any duplicates present in the results being combined .
- Every SELECT statement within UNION must have the same number of columns, the same data types, and the same order .
- The syntax of UNION in SQL is:

```sql
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_1
UNION
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_2
UNION
...
UNION
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_m;
```

- A UNION operation is different from a JOIN operation: A UNION concatenates result sets from two queries, but a UNION does not create individual rows from columns gathered from two tables. A JOIN compares columns from two tables, to create result rows composed of columns from two tables.
- An example of UNION in SQL is:

```sql
-- Create two tables with some data
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  city VARCHAR(50)
);

CREATE TABLE suppliers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice', 'New York'),
(2, 'Bob', 'Los Angeles'),
(3, 'Charlie', 'Chicago');

INSERT INTO suppliers VALUES
(4, 'David', 'New York'),
(5, 'Eve', 'Los Angeles'),
(6, 'Frank', 'Boston');

-- Use UNION to get the names and cities of both customers and suppliers
SELECT name, city FROM customers
UNION
SELECT name, city FROM suppliers
ORDER BY name;

-- The output is:

name    | city
-----------------
Alice   | New York
Bob     | Los Angeles
Charlie | Chicago
David   | New York
Eve     | Los Angeles
Frank   | Boston
```

- Note that the output does not have any duplicates, even though both tables have entries with the same city. If you want to keep the duplicates, you can use UNION ALL instead of UNION  .