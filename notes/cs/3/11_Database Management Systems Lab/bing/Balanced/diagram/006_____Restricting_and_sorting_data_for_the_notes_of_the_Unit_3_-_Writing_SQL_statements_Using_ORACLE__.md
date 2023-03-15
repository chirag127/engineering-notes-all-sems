Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of restricting and sorting data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab.

### Restricting and sorting data

- Restricting data means limiting the rows that are retrieved by a query based on some conditions.
- Sorting data means arranging the rows that are retrieved by a query in a specific order.
- Both restricting and sorting data can be done by using clauses in the SQL SELECT statement.

#### Restricting data

- The WHERE clause is used to restrict data by specifying one or more conditions that the rows must satisfy to be selected.
- The conditions can be based on the values of the columns, expressions, or functions.
- The conditions can be combined using logical operators such as AND, OR, NOT, IN, BETWEEN, LIKE, etc.
- The conditions can also use comparison operators such as =, <, >, <=, >=, <>, !=, etc.
- The conditions can be grouped using parentheses to change the order of evaluation.
- Example: SELECT first_name, last_name, salary FROM employees WHERE salary > 10000 AND department_id = 10;

#### Sorting data

- The ORDER BY clause is used to sort data by specifying one or more columns or expressions that determine the order of the rows.
- The columns or expressions can be given aliases using the AS keyword.
- The order can be ascending (ASC) or descending (DESC). The default order is ascending.
- The order can also specify how to handle null values using the NULLS FIRST or NULLS LAST option.
- The columns or expressions can be referred by their position in the SELECT list using numeric values.
- Example: SELECT first_name, last_name, salary FROM employees ORDER BY salary DESC, last_name ASC NULLS LAST;

#### Limiting the rows that are retrieved by a query

- Different database systems have different ways of limiting the rows that are retrieved by a query.
- In Oracle, the ROWNUM pseudocolumn can be used to assign a sequential number to each row in the result set. The ROWNUM can be used in the WHERE clause to limit the rows. However, the ROWNUM is assigned before the ORDER BY clause, so the order may not be as expected. To avoid this, a subquery can be used to first order the rows and then apply the ROWNUM filter.
- Example: SELECT * FROM (SELECT first_name, last_name, salary FROM employees ORDER BY salary DESC) WHERE ROWNUM <= 5;
- In MySQL, the LIMIT clause can be used to limit the rows by specifying the number of rows to return or the range of rows to return. The LIMIT clause is applied after the ORDER BY clause, so the order is preserved.
- Example: SELECT first_name, last_name, salary FROM employees ORDER BY salary DESC LIMIT 5;