### Unions

In SQL, a union is a way to combine the results of two or more SELECT statements into a single result set. Here are some important points to keep in mind when working with unions:

- The SELECT statements that are being combined must have the same number of columns and the columns must have compatible data types.

- The result set of a union will only include distinct values. If you want to include all values (including duplicates), you can use the UNION ALL operator instead.

- The columns in the result set of a union will be in the order they appear in the first SELECT statement.

- You can use the ORDER BY clause to order the result set of a union.

- If you need to combine more than two SELECT statements, you can use multiple union operators.

Here's an example of a union:

```
SELECT first_name, last_name, email
FROM customers
WHERE state = 'CA'
UNION
SELECT first_name, last_name, email
FROM customers
WHERE state = 'NY'
ORDER BY last_name;
```

This query combines the results of two SELECT statements to create a result set that includes the first name, last name, and email address of all customers in California or New York, ordered by last name.

In summary, unions are a useful tool for combining the results of multiple SELECT statements into a single result set. Keep in mind the points mentioned above and use them appropriately to get the desired results.