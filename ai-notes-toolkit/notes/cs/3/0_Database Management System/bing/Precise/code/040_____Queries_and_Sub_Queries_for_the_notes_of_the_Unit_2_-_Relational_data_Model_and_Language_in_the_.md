### Queries and Sub Queries

A query is a request for data or information from a database table or combination of tables. This data may be generated as results returned by Structured Query Language (SQL) or as pictorials, graphs or complex results, e.g., trend analyses from data-mining tools.

A subquery is a query that is nested inside a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can be used anywhere an expression is allowed.

#### Key points to remember:
- A query can retrieve data from specified columns or all columns in a table.
- A query can also retrieve data from multiple tables.
- A subquery is used to return data that will be used in the main query as a condition to further restrict the data that is retrieved.
- Subqueries can be used with the SELECT, INSERT, UPDATE, and DELETE statements along with the operators like =, <, >, >=, <=, IN, BETWEEN, etc.
- There are two types of subquery – Correlated and Non-Correlated.
- A correlated subquery cannot be considered as an independent query, but it can refer the column in a table listed in the FROM the list of the main query.
- A Non-Correlated subquery is an independent query where the output of subquery is substituted in the main query.
