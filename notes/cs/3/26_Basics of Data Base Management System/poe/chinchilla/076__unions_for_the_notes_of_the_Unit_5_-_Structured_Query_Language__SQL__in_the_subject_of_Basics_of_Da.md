### Unions

Unions are used to combine the results of two or more SELECT statements into a single result set. The result set returned by a union contains all the rows that are returned by the individual SELECT statements.

#### Syntax

The basic syntax for a union is as follows:

```sql
SELECT column1, column2, ... FROM table1
UNION
SELECT column1, column2, ... FROM table2;
```

#### Rules for Using Unions

When using unions, there are a few rules that must be followed:

- The number and order of the columns in all SELECT statements must be the same.
- The data types of the corresponding columns in all SELECT statements must be compatible.
- The column names of the result set are taken from the first SELECT statement.

#### Example

Let's say we have two tables, `customers` and `orders`, with the following data:

`customers` table:

| id | name   | city      |
|----|--------|-----------|
| 1  | Alice  | New York  |
| 2  | Bob    | Los Angeles |
| 3  | Carol  | Chicago   |

`orders` table:

| id | customer_id | amount |
|----|-------------|--------|
| 1  | 1           | 100    |
| 2  | 2           | 200    |
| 3  | 3           | 300    |

We can use a union to combine the results of two SELECT statements that retrieve data from these tables:

```sql
SELECT name, city FROM customers
UNION
SELECT customer_id, amount FROM orders;
```

This will return the following result set:

| name   | city        |
|--------|-------------|
| Alice  | New York    |
| Bob    | Los Angeles |
| Carol  | Chicago     |
| 1      | 100         |
| 2      | 200         |
| 3      | 300         |

#### Union All

In addition to the union operator, there is also a union all operator. The difference between the two is that the union operator removes duplicate rows from the result set, while the union all operator retains them.

```sql
SELECT name, city FROM customers
UNION ALL
SELECT customer_id, amount FROM orders;
```

This will return the following result set:

| name   | city        |
|--------|-------------|
| Alice  | New York    |
| Bob    | Los Angeles |
| Carol  | Chicago     |
| 1      | 100         |
| 2      | 200         |
| 3      | 300         |
| 2      | 200         |
| 3      | 300         |