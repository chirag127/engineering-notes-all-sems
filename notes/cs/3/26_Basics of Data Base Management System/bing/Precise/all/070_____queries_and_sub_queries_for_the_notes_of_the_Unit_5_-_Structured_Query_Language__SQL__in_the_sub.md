# Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

### Queries and Subqueries

- A query is a request for data or information from a database table or combination of tables.
- A query can be used to retrieve, insert, update, or delete data from a database.
- A subquery is a query that is nested inside a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery.
- A subquery can be used to return data that will be used in the main query as a condition to further restrict the data that is retrieved.
- Subqueries can be used with the SELECT, INSERT, UPDATE, and DELETE statements along with the operators like =, <, >, >=, <=, IN, BETWEEN, etc.
- There are two types of subqueries: correlated and non-correlated.
- A correlated subquery is a subquery that depends on the outer query for its values. This means that the subquery is executed repeatedly, once for each row that might be selected by the outer query.
- A non-correlated subquery is a subquery that can be run independently of the outer query and returns its result.