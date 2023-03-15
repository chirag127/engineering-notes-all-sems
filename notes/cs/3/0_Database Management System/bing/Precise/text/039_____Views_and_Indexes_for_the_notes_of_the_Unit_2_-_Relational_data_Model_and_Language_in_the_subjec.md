### Views and Indexes

#### Views
- A view is a virtual table based on the result-set of an SQL statement.
- A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.
- You can add SQL functions, WHERE, and JOIN statements to a view and present the data as if the data were coming from one single table.
- Views can be used to provide a specific perspective on the data in the underlying tables.
- Views can be used to restrict access to specific columns or rows in the underlying tables.

#### Indexes
- An index is a database object that improves the speed of data retrieval operations on a database table.
- Indexes can be created using one or more columns of a database table, providing the basis for both rapid random lookups and efficient access of ordered records.
- An index helps speed up SELECT queries and WHERE clauses, but it slows down data input, with UPDATE and INSERT statements.
- Indexes can be unique or non-unique. Unique indexes ensure that no two rows of a table have duplicate values in the indexed column(s).
- Indexes can be created explicitly or automatically by the database management system, depending on the database design and application requirements.