 Here is the content in markdown format for the topic ### views and indexes for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System:

### Views

- A view is a virtual table based on the result of an SQL statement.
- A view contains rows and columns, just like a real table. But the rows are not explicitly stored, only the SQL statement that defines the view is stored.
- The view is generated using the SQL statement each time it is referenced in a query.
- Views are used to:
  - Simplify SQL statements.
  - Restrict access to data (by filtering rows or columns).
  - Present data in different formats.
  - Hide the complexity of table structures.
- The SQL statement that defines the view can include joins, aggregations, and other operations.
- Views can be updated, deleted, and inserted into just like real tables (unless the view definition contains aggregations or complex joins etc.).

Advantages:
- Provide an additional level of table security, since users can be given access to a view, rather than the underlying base tables.
- Simplify SQL statements for users.
- Present data in a different format/arrangement than that of the base tables.

Disadvantages:
- Views require processing time to generate, and take up storage space.
- If a view is based on multiple tables, executing an update query on the view may be complex.

ASCII Diagram:

View (virtual table)
|
v
SQL Statement
|
v
Base Table(s)

### Indexes

- An index is a database structure that improves the speed of data retrieval operations on a table at the cost of additional writes and storage space to maintain the index data structure.
- Indexes are used to quickly locate data without having to search every row in a database table every time a database table is accessed.
- Types of indexes:
  - Unique indexes: Prevents duplicate values in a column.
  - Clustered indexes: Sorted data, only one per table.
  - Nonclustered indexes: Pointers to data in a table, several per table.
- Advantages: Data retrieval is faster.
- Disadvantages: Additional storage space required and decreased performance of data modification statements (insert, update, delete).