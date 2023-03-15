# SQL Operators and Their Procedure

SQL operators are symbols or keywords that are used to perform operations on values or expressions in SQL statements. They can be used to specify conditions, filter results, compare values, perform calculations, concatenate strings, and more. SQL operators can be classified into six types:

- Arithmetic operators: These operators are used to perform mathematical operations on numerical data, such as addition, subtraction, multiplication, division, modulus, and exponentiation. For example:

```sql
SELECT 10 + 5; -- returns 15
SELECT 10 - 5; -- returns 5
SELECT 10 * 5; -- returns 50
SELECT 10 / 5; -- returns 2
SELECT 10 % 5; -- returns 0
SELECT 10 ^ 2; -- returns 100
```

- Comparison operators: These operators are used to compare two values or expressions and return a boolean value (true or false). They can be used with the WHERE, HAVING, ON, and CASE clauses. For example:

```sql
SELECT * FROM customers WHERE age > 30; -- returns customers older than 30
SELECT * FROM products WHERE price = 100; -- returns products with price equal to 100
SELECT * FROM orders WHERE order_date BETWEEN '2020-01-01' AND '2020-12-31'; -- returns orders placed in 2020
SELECT * FROM employees WHERE name LIKE 'A%'; -- returns employees whose name starts with A
SELECT * FROM students WHERE grade IN ('A', 'B', 'C'); -- returns students with grade A, B, or C
```

- Logical operators: These operators are used to combine two or more conditions and return a boolean value. They can be used with the WHERE, HAVING, ON, and CASE clauses. For example:

```sql
SELECT * FROM customers WHERE country = 'USA' AND state = 'CA'; -- returns customers from California, USA
SELECT * FROM products WHERE category = 'Books' OR price < 50; -- returns products that are books or have price less than 50
SELECT * FROM orders WHERE NOT status = 'Cancelled'; -- returns orders that are not cancelled
SELECT * FROM employees WHERE salary > 5000 AND (department = 'Sales' OR department = 'Marketing'); -- returns employees with salary greater than 5000 and belong to either sales or marketing department
```

- Bitwise operators: These operators are used to perform bitwise operations on binary data, such as AND, OR, XOR, NOT, and SHIFT. They can be used with the WHERE, HAVING, ON, and CASE clauses. For example:

```sql
SELECT 10 & 5; -- returns 0 (bitwise AND)
SELECT 10 | 5; -- returns 15 (bitwise OR)
SELECT 10 ^ 5; -- returns 15 (bitwise XOR)
SELECT ~10; -- returns -11 (bitwise NOT)
SELECT 10 << 2; -- returns 40 (bitwise left shift)
SELECT 10 >> 2; -- returns 2 (bitwise right shift)
```

- String operators: These operators are used to manipulate string data, such as concatenation, extraction, conversion, and trimming. They can be used with the SELECT, WHERE, HAVING, ON, and CASE clauses. For example:

```sql
SELECT 'Hello' + ' ' + 'World'; -- returns 'Hello World' (string concatenation)
SELECT SUBSTRING('Hello World', 1, 5); -- returns 'Hello' (string extraction)
SELECT UPPER('Hello World'); -- returns 'HELLO WORLD' (string conversion)
SELECT TRIM(' Hello World '); -- returns 'Hello World' (string trimming)
```

- Set operators: These operators are used to combine the results of two or more SELECT statements and return a single result set. They can be used with the UNION, INTERSECT, EXCEPT, and MINUS keywords. For example:

```sql
SELECT name FROM customers
UNION
SELECT name FROM employees; -- returns the names of both customers and employees, without duplicates

SELECT name FROM customers
INTERSECT
SELECT name FROM employees; -- returns the names of both customers and employees, with duplicates

SELECT name FROM customers
EXCEPT
SELECT name FROM employees; -- returns the names of customers who are not employees

SELECT name FROM customers
MINUS
SELECT name FROM employees; -- returns the same as EXCEPT
```