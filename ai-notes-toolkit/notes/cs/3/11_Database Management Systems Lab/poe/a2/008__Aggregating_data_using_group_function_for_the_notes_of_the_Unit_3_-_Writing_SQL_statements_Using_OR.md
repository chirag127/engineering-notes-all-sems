 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Aggregating data using group function for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab.

1. aggregrate functions:
- count(): Returns the number of rows that matches a specified criteria.
- sum(): Returns the sum of a numeric column.
- avg(): Returns the average of a numeric column.
- min(): Returns the minimum value of a column.
- max(): Returns the maximum value of a column.

2. GROUP BY clause:
- The GROUP BY clause groups rows that have the same values into summary rows.
- The GROUP BY clause is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.

3. HAVING clause:
- The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.
- The HAVING clause allows you to filter record sets based on aggregate function conditions.

4. Examples:

COUNT():
SELECT COUNT(customer_id) FROM customers;

SUM():
SELECT SUM(price) FROM products;

AVG():
SELECT AVG(price) FROM products;

MIN() and MAX():
SELECT MIN(price) AS lowest_price, MAX(price) AS highest_price FROM products;

GROUP BY:
SELECT category_id, COUNT(product_id)
FROM products
GROUP BY category_id;

HAVING:
SELECT category_id, COUNT(product_id)
FROM products
GROUP BY category_id
HAVING COUNT(product_id) > 10;