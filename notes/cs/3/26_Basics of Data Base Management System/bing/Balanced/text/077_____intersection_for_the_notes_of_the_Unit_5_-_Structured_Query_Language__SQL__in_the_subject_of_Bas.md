### Intersection

- The intersection operation in SQL is used to combine two queries and return only the records that are common to both the queries.
- The syntax of the intersection operation is:

```sql
SELECT column_list
FROM table1
INTERSECT
SELECT column_list
FROM table2;
```

- The column_list in both the queries must have the same number and order of columns, and the data types must be compatible.
- The intersection operation eliminates any duplicate rows from the result set.
- The intersection operation can be used to find the common values in two or more tables. For example, to find the customers who have ordered both books and DVDs from an online store, we can use the following query:

```sql
SELECT customer_id
FROM orders
WHERE product_type = 'book'
INTERSECT
SELECT customer_id
FROM orders
WHERE product_type = 'DVD';
```

- The intersection operation can also be combined with other set operations, such as union and except, using parentheses to specify the order of execution. For example, to find the customers who have ordered books or DVDs, but not both, we can use the following query:

```sql
(SELECT customer_id
FROM orders
WHERE product_type = 'book'
UNION
SELECT customer_id
FROM orders
WHERE product_type = 'DVD')
EXCEPT
(SELECT customer_id
FROM orders
WHERE product_type = 'book'
INTERSECT
SELECT customer_id
FROM orders
WHERE product_type = 'DVD');
```