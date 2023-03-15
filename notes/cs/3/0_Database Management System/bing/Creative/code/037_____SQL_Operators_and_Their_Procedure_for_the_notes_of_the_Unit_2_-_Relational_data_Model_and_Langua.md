### SQL Operators and Their Procedure

SQL operators are symbols or keywords that are used to perform operations on data items or operands in SQL statements. They can be used to specify conditions, filter results, compare values, perform calculations, or manipulate strings. SQL operators can be classified into six types:

- Arithmetic operators: These operators are used for mathematical operations on numerical data, such as addition, subtraction, multiplication, division, modulo, and exponentiation. They follow the standard order of operations and can be used with parentheses to change the precedence. For example:

```sql
-- Calculate the total price of an order
SELECT quantity * price AS total FROM orders;

-- Calculate the average salary of employees
SELECT AVG(salary) FROM employees;

-- Calculate the remainder of dividing 7 by 3
SELECT 7 % 3;
```

- Comparison operators: These operators are used to compare two values and return a boolean result (TRUE, FALSE, or NULL). They can be used with numeric, string, or date data types. Some common comparison operators are: = (equal), <> (not equal), > (greater than), < (less than), >= (greater than or equal), <= (less than or equal), BETWEEN (within a range), LIKE (matches a pattern), and IN (belongs to a set). For example:

```sql
-- Find the employees who have a salary greater than 5000
SELECT name, salary FROM employees WHERE salary > 5000;

-- Find the products whose name starts with 'A'
SELECT name, price FROM products WHERE name LIKE 'A%';

-- Find the orders that were placed on 2020-01-01
SELECT order_id, customer_id, date FROM orders WHERE date = '2020-01-01';
```

- Logical operators: These operators are used to combine multiple conditions and return a boolean result. They can be used with the WHERE, HAVING, or ON clauses. Some common logical operators are: AND (both conditions must be true), OR (either condition must be true), NOT (negates the condition), and EXISTS (checks if a subquery returns any rows). For example:

```sql
-- Find the customers who live in New York or Los Angeles
SELECT name, city FROM customers WHERE city = 'New York' OR city = 'Los Angeles';

-- Find the products that have a price between 10 and 20 and are not out of stock
SELECT name, price, stock FROM products WHERE price BETWEEN 10 AND 20 AND stock <> 0;

-- Find the orders that have at least one item with a quantity greater than 10
SELECT order_id, date FROM orders WHERE EXISTS (SELECT * FROM order_items WHERE order_id = orders.order_id AND quantity > 10);
```

- Bitwise operators: These operators are used to perform bit-level operations on binary data, such as AND, OR, XOR, NOT, SHIFT, and ROTATE. They can be used to manipulate flags, masks, or encryption keys. For example:

```sql
-- Find the employees who have the manager flag set to 1
SELECT name, flags FROM employees WHERE flags & 1 = 1;

-- Find the products whose price is a power of 2
SELECT name, price FROM products WHERE price & (price - 1) = 0;

-- Find the orders whose order_id is an odd number
SELECT order_id, date FROM orders WHERE order_id & 1 = 1;
```

- String operators: These operators are used to perform operations on string data, such as concatenation, extraction, replacement, conversion, or trimming. They can be used to manipulate text, format output, or generate dynamic queries. For example:

```sql
-- Concatenate the first name and last name of customers
SELECT first_name || ' ' || last_name AS full_name FROM customers;

-- Extract the year from the date column
SELECT EXTRACT(YEAR FROM date) AS year FROM orders;

-- Replace the 'a' character with 'e' in the product names
SELECT REPLACE(name, 'a', 'e') AS new_name FROM products;
```

- Set operators: These operators are used to combine the results of two or more queries into a single result set. They can be used to perform operations such as union, intersection, difference, or symmetric difference. They follow the rules of set theory and require that the queries have the same number and type of columns. Some common set operators are: UNION (returns all distinct rows from both queries), UNION ALL (returns all rows from both queries, including duplicates), INTERSECT (returns only the common rows