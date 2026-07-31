### Queries and Sub Queries

A query is a request for data or information from a database table or combination of tables. This data may be generated as results returned by Structured Query Language (SQL) or as pictorials, graphs or complex results, e.g., trend analyses from data-mining tools.

One of the most powerful features of a relational database is its ability to deliver answers to complex questions or queries. A query can be a simple request for all the data in a table or a complex request for data that meets multiple criteria.

A subquery is a query that is nested inside a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can be used anywhere an expression is allowed. In a subquery, you use a SELECT statement to provide a set of one or more specific values to evaluate in the WHERE or HAVING clause expression of the outer query.

Subqueries can be used to return either a scalar (single) value or a row set; although, scalar subqueries are more commonly used. A subquery is usually added within the WHERE Clause of another SQL SELECT statement.

Here are some key points to remember about subqueries:
- A subquery must be enclosed in parentheses.
- A subquery must be put in the right hand of the comparison operator, and
- Subquery cannot manipulate its result set, meaning ORDER BY clause cannot be added into a subquery.