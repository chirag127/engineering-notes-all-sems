### Unions

- UNION is an SQL operator that combines the result sets of two or more SELECT queries into a single result set  .
- UNION removes any duplicate rows from the combined result set .
- Every SELECT statement within UNION must have the same number of columns, the same data types, and the same order of columns .
- The syntax of UNION in SQL is:

```sql
SELECT column_name_1, column_name_2, ..., column_name_n FROM table_name_1
UNION
SELECT column_name_1, column_name_2, ..., column_name_n FROM table_name_2
UNION
...
UNION
SELECT column_name_1, column_name_2, ..., column_name_n FROM table_name_m;
```

- UNION is different from JOIN, which compares columns from two tables and creates result rows composed of columns from both tables.
- UNION can be used to combine data from different tables that have similar structure or meaning.
- For example, if there are two tables named `customers` and `suppliers` that have the same columns `id`, `name`, and `city`, the following query will return all the customers and suppliers from New York:

```sql
SELECT id, name, city FROM customers
WHERE city = 'New York'
UNION
SELECT id, name, city FROM suppliers
WHERE city = 'New York';
```

- If the order of the columns is different in the two tables, the query will fail. For example, the following query will cause an error:

```sql
SELECT id, name, city FROM customers
UNION
SELECT city, name, id FROM suppliers;
```

- To preserve the duplicates in the combined result set, the UNION ALL operator can be used instead of UNION . For example, the following query will return all the customers and suppliers from New York, including the duplicates:

```sql
SELECT id, name, city FROM customers
WHERE city = 'New York'
UNION ALL
SELECT id, name, city FROM suppliers
WHERE city = 'New York';
```

- UNION can also be used with other clauses, such as ORDER BY, GROUP BY, and HAVING . For example, the following query will return the names and cities of all the customers and suppliers, sorted by name:

```sql
SELECT name, city FROM customers
UNION
SELECT name, city FROM suppliers
ORDER BY name;
```

- UNION can also be nested within other queries, such as subqueries, derived tables, and common table expressions. For example, the following query will return the total number of customers and suppliers from New York:

```sql
SELECT COUNT(*) FROM
(
  SELECT id FROM customers
  WHERE city = 'New York'
  UNION
  SELECT id FROM suppliers
  WHERE city = 'New York'
) AS t;
```