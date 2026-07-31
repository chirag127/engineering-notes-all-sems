 Here are the notes for the topic 'Queries and Subqueries' for Unit 5 - Structured Query Language (SQL) in the subject Basics of Data Base Management System:

### Queries

- A query is a question asked to the database to retrieve data.
- The query is written in SQL and executed by the DBMS.
- The result of the query is a dataset that answers the question.

Types of Queries:

- Select Query - Retrieves data from the database. Used for retrieval of data.
- Update Query - Updates existing data in the database.
- Delete Query - Deletes existing data from the database.
- Insert Query - Inserts new data into the database.
- Create/Alter/Drop Query - Used to create, modify or remove database objects like tables, indexes, views, etc.

Query Clauses:

- SELECT - Retrieves data from the database
- FROM - Specifies the table to query
- WHERE - Specifies a condition for filtering records
- GROUP BY - Groups records based on a column
- HAVING - Filters groups based on a condition
- ORDER BY - Sorts the result set in ascending or descending order

### Subqueries

- A subquery is a query within another query.
- The inner subquery is executed first and then its result is used by the outer query.
- Subqueries are used to retrieve relational information and perform calculations.
- Subqueries can be nested to multiple levels.

Types of Subqueries:

- Correlated - Uses values from the outer query.
- Non-Correlated - Independent of the outer query.

Uses of Subqueries:

- Retrieve relational data
- Provide values for filtering and ordering
- Provide values to be used in calculations
- Simplify complex queries
- Replace views and derived tables