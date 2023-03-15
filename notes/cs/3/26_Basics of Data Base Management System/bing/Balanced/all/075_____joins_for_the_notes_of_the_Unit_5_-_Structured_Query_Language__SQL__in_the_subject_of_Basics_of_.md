# Joins

- A join is a way of combining data from two or more tables based on a common column or condition.
- A join condition specifies how the tables are related, usually by matching values in one or more columns.
- A join can be classified into different types, such as inner join, outer join, cross join, self join, etc.
- A join can improve the performance and efficiency of queries by reducing the amount of data that needs to be scanned and processed.
- A join can also enhance the readability and maintainability of queries by avoiding subqueries and duplication of code.

## Inner Join

- An inner join returns only the rows that match the join condition in both tables.
- An inner join can be written using the keyword JOIN or the operator =.
- An inner join can be used to retrieve data from multiple tables that have a one-to-one, one-to-many, or many-to-many relationship.
- An inner join can be written as:

```sql
SELECT column_list
FROM table1
JOIN table2
ON table1.column = table2.column;
```

- Or as:

```sql
SELECT column_list
FROM table1, table2
WHERE table1.column = table2.column;
```

- For example, to join the Customers and Orders tables based on the CustomerID column, we can write:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

- This query will return the customer ID, first name, and order amount for all customers who have placed at least one order.

## Outer Join

- An outer join returns all the rows that match the join condition in either table, and also the rows that do not match in one or both tables.
- An outer join can be written using the keywords LEFT JOIN, RIGHT JOIN, or FULL JOIN.
- An outer join can be used to retrieve data from multiple tables that have a one-to-one, one-to-many, or many-to-many relationship, and also to find the missing or unmatched data in either table.
- An outer join can be written as:

```sql
SELECT column_list
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

- Or as:

```sql
SELECT column_list
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

- Or as:

```sql
SELECT column_list
FROM table1
FULL JOIN table2
ON table1.column = table2.column;
```

- For example, to join the Customers and Orders tables based on the CustomerID column, and also to find the customers who have not placed any order, we can write:

```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
LEFT JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

- This query will return the customer ID, first name, and order amount for all customers, and NULL for the order amount for the customers who have not placed any order.

## Cross Join

- A cross join returns the Cartesian product of the rows from the joined tables, i.e., every possible combination of rows from both tables.
- A cross join can be written using the keyword CROSS JOIN or the operator *.
- A cross join can be used to generate test data or to combine data from different sources that have no common column or condition.
- A cross join can be written as:

```sql
SELECT column_list
FROM table1
CROSS JOIN table2;
```

- Or as:

```sql
SELECT column_list
FROM table1, table2;
```

- For example, to join the Customers and Products tables based on no condition, we can write:

```sql
SELECT Customers.customer_id, Customers.first_name, Products.product_id, Products.product_name
FROM Customers
CROSS JOIN Products;
```

- This query will return the customer ID, first name, product ID, and product name for every possible combination of customers and products.

## Self Join

- A self join is a way of joining a table to itself, i.e., using the same table as both the left and right tables in the join.
- A self join can be written using any type of join, such as inner join, outer join, cross join, etc.
- A self join can be used to compare or find the relationship between the rows within the same table.
- A self join can be written as:

```sql
SELECT column_list
FROM table1 AS alias1
JOIN table1 AS alias2
ON alias1.column