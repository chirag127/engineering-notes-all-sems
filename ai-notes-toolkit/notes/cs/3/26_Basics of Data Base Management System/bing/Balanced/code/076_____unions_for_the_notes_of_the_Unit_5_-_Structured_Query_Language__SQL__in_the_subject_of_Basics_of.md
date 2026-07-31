### Unions

- A union is an SQL operator that combines the result sets of two or more SELECT queries into a single result set.
- A union removes any duplicate rows from the combined result set, unless the UNION ALL option is used, which preserves all rows.
- A union can be used to combine data from different tables or views that have the same or compatible column names and data types.
- A union can also be used to combine data from different databases or servers, as long as they support the same SQL dialect and have a common connection.
- The syntax of a union is:

```sql
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_1
UNION [ALL]
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_2
UNION [ALL]
...
UNION [ALL]
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_m;
```

- The number, order, and data type of the columns in each SELECT query must be the same or convertible.
- The column names in the result set are taken from the first SELECT query, unless aliases are used.
- The result set can be sorted by using the ORDER BY clause after the last SELECT query, but not within each individual query.
- The result set can be filtered by using the WHERE clause before the first SELECT query, but not after the UNION operator.
- The result set can be limited by using the LIMIT or TOP clause after the ORDER BY clause, but not within each individual query.
- The result set can be grouped by using the GROUP BY and HAVING clauses before the first SELECT query, but not after the UNION operator.
- The result set can be joined with other tables or views by using the JOIN clause before the first SELECT query, but not after the UNION operator.

- Some examples of using unions are:

  - To combine data from two tables that have the same columns:

  ```sql
  SELECT name, age, gender
  FROM students
  UNION
  SELECT name, age, gender
  FROM teachers;
  ```

  - To combine data from two tables that have different columns, but compatible data types:

  ```sql
  SELECT name, salary, NULL AS department
  FROM employees
  UNION
  SELECT name, NULL AS salary, department
  FROM managers;
  ```

  - To combine data from two tables that have different columns, and use aliases to rename them:

  ```sql
  SELECT name AS person_name, email AS contact_info
  FROM customers
  UNION
  SELECT company_name AS person_name, phone AS contact_info
  FROM suppliers;
  ```

  - To combine data from two tables and sort the result set by a column:

  ```sql
  SELECT name, price
  FROM products
  UNION
  SELECT name, price
  FROM services
  ORDER BY price DESC;
  ```

  - To combine data from two tables and limit the result set to 10 rows:

  ```sql
  SELECT name, price
  FROM products
  UNION
  SELECT name, price
  FROM services
  ORDER BY price DESC
  LIMIT 10;
  ```

  - To combine data from two tables and filter the result set by a condition:

  ```sql
  SELECT name, price
  FROM products
  WHERE price > 100
  UNION
  SELECT name, price
  FROM services
  WHERE price > 100;
  ```

  - To combine data from two tables and group the result set by a column:

  ```sql
  SELECT name, SUM(price) AS total_price
  FROM (
    SELECT name, price
    FROM products
    UNION
    SELECT name, price
    FROM services
  ) AS subquery
  GROUP BY name;
  ```

  - To combine data from two tables and join the result set with another table:

  ```sql
  SELECT subquery.name, subquery.price, categories.category
  FROM (
    SELECT name, price, category_id
    FROM products
    UNION
    SELECT name, price, category_id
    FROM services
  ) AS subquery
  JOIN categories
  ON subquery.category_id = categories.id;
  ```

  - To combine data from two databases or servers that have the same table structure:

  ```sql
  SELECT name, price
  FROM db1.products
  UNION
  SELECT name, price
  FROM db2.products;
  ```