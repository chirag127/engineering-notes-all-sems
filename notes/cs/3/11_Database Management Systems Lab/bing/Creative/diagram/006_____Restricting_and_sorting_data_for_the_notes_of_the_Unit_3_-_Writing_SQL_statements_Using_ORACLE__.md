Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of restricting and sorting data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab.

### Restricting and sorting data

- Restricting data means limiting the rows that are retrieved by a query based on some conditions.
- Sorting data means arranging the rows that are retrieved by a query in a specific order.
- Both restricting and sorting data can be done by using clauses in the SQL statement.

#### Restricting data

- The WHERE clause is used to restrict data by specifying one or more conditions that the rows must satisfy to be selected.
- The conditions can be based on arithmetic, logical, or comparison operators, such as =, <, >, <=, >=, <>, !=, AND, OR, NOT, BETWEEN, IN, LIKE, IS NULL, etc.
- The conditions can also involve expressions, functions, or subqueries that return a single value or a set of values.
- The WHERE clause is placed after the FROM clause and before the ORDER BY clause in the SQL statement.
- Example: SELECT first_name, last_name, salary FROM employees WHERE salary > 10000;

#### Sorting data

- The ORDER BY clause is used to sort data by specifying one or more columns or expressions that determine the order of the rows.
- The columns or expressions can be followed by ASC (ascending) or DESC (descending) keywords to indicate the sort direction. The default is ASC if not specified.
- The columns or expressions can also be assigned numbers to indicate the order of precedence. The lowest number is sorted first.
- The ORDER BY clause is placed at the end of the SQL statement.
- Example: SELECT first_name, last_name, salary FROM employees ORDER BY salary DESC, last_name ASC;

#### Restricting and sorting data in Oracle

- Oracle supports the ROWNUM pseudocolumn that assigns a sequential number to each row retrieved by a query.
- The ROWNUM can be used in the WHERE clause to limit the number of rows returned by a query, such as ROWNUM <= 10.
- The ROWNUM can also be used in the ORDER BY clause to sort the rows by their sequence number, such as ORDER BY ROWNUM.
- However, the ROWNUM is assigned before the ORDER BY clause is executed, so it cannot be used to limit the rows after sorting them by another column or expression.
- To limit the rows after sorting them, a subquery can be used, such as SELECT * FROM (SELECT * FROM employees ORDER BY salary DESC) WHERE ROWNUM <= 10;
- Alternatively, Oracle 12c and later versions support the FETCH FIRST clause that can be used to limit the rows after sorting them, such as SELECT * FROM employees ORDER BY salary DESC FETCH FIRST 10 ROWS ONLY;

#### Restricting and sorting data in MySQL

- MySQL supports the LIMIT clause that can be used to limit the number of rows returned by a query, such as LIMIT 10.
- The LIMIT clause can also specify an offset to skip a certain number of rows before returning the rest, such as LIMIT 5, 10 (skip the first 5 rows and return the next 10 rows).
- The LIMIT clause is placed after the ORDER BY clause in the SQL statement.
- Example: SELECT first_name, last_name, salary FROM employees ORDER BY salary DESC LIMIT 10;