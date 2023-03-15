# Intersection

- The **INTERSECT** operator in SQL is used to combine two **SELECT** statements and return only the rows that are common in both the statements.
- The **INTERSECT** operator acts as a mathematical intersection, meaning it returns the elements that belong to both sets.
- The syntax of the **INTERSECT** operator is as follows:

```sql
SELECT column_list
FROM table1
INTERSECT
SELECT column_list
FROM table2;
```

- The column_list in both the **SELECT** statements must have the same number and order of columns, and the data types must be compatible.
- The **INTERSECT** operator eliminates duplicate rows from the result set, unless the **ALL** option is specified.
- The **INTERSECT** operator can be combined with other set operators, such as **UNION** and **EXCEPT**, using parentheses to specify the order of operations.
- The **INTERSECT** operator can be used to find common values in different tables, such as customers who ordered products from different categories, or employees who work in different departments.
- Some examples of using the **INTERSECT** operator are:

```sql
-- Find the customers who ordered both books and movies
SELECT customer_id
FROM orders
WHERE category = 'Books'
INTERSECT
SELECT customer_id
FROM orders
WHERE category = 'Movies';

-- Find the employees who work in both sales and marketing departments
SELECT employee_id
FROM employees
WHERE department = 'Sales'
INTERSECT
SELECT employee_id
FROM employees
WHERE department = 'Marketing';

-- Find the products that are sold in both USA and Canada
SELECT product_id
FROM sales
WHERE country = 'USA'
INTERSECT
SELECT product_id
FROM sales
WHERE country = 'Canada';
```