# Joins

Joins are used to combine data from two or more tables based on a common column. Joins allow us to query data from multiple sources as if they were a single table.

There are different types of joins in SQL, each with a different way of handling non-matching rows. The most common types of joins are:

- **Inner join**: returns only the rows that match in both tables.
- **Left outer join**: returns all the rows from the left table, and the matching rows from the right table. If there is no match, the right side will be NULL.
- **Right outer join**: returns all the rows from the right table, and the matching rows from the left table. If there is no match, the left side will be NULL.
- **Full outer join**: returns all the rows from both tables, and matches them if possible. If there is no match, both sides will be NULL.
- **Cross join**: returns the Cartesian product of both tables, meaning every possible combination of rows.

The syntax for joining two tables is:

```sql
SELECT column_list
FROM table1
JOIN table2
ON join_condition;
```

The join condition specifies how the tables are related, usually by comparing a column from each table. The join condition can also use other operators, such as `=`, `<>`, `<`, `>`, etc.

Here is an example of an inner join between two tables, Customers and Orders, based on the CustomerID column:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

This query will return the customer ID, first name, and order amount for each order placed by a customer. If a customer has not placed any order, or if an order has no customer, they will not be included in the result.

Here is an example of a left outer join between the same tables:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
LEFT JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

This query will return the same columns as the previous one, but it will also include the customers who have not placed any order. In that case, the order amount will be NULL.

Here is an example of a right outer join between the same tables:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
RIGHT JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

This query will return the same columns as the previous ones, but it will also include the orders that have no customer. In that case, the customer ID and first name will be NULL.

Here is an example of a full outer join between the same tables:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
FULL JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

This query will return the same columns as the previous ones, but it will also include all the rows from both tables, regardless of whether they have a match or not. If there is no match, both sides will be NULL.

Here is an example of a cross join between the same tables:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
CROSS JOIN Orders;
```

This query will return the same columns as the previous ones, but it will also include every possible combination of rows from both tables. For example, if there are 10 customers and 5 orders, the result will have 50 rows. This type of join is rarely useful, unless you want to generate some test data.

Sources:

: Joins (SQL Server) - SQL Server | Microsoft Learn
: SQL JOIN (With Examples) - Programiz
: SQL Joins - W3Schools
: SQL JOIN - W3Schools