# Views and Indexes

## Views

- A view is a named query that defines a logical table based on the result of a SELECT statement.
- A view can be used to simplify complex queries, hide sensitive data, or provide a consistent interface to different tables.
- A view does not store any data physically, but only references the data in the underlying tables.
- A view can be created, modified, or dropped using the CREATE VIEW, ALTER VIEW, or DROP VIEW statements.
- A view can be queried, updated, inserted, or deleted as if it were a table, as long as it meets certain conditions.
- A view can be indexed to improve the performance of queries that use the view .

## Indexes

- An index is a data structure that organizes the data in a table based on one or more columns.
- An index can speed up the retrieval of data from a table by reducing the number of disk accesses.
- An index can also enforce uniqueness, referential integrity, or sorting order on the indexed columns.
- An index can be created, modified, or dropped using the CREATE INDEX, ALTER INDEX, or DROP INDEX statements.
- An index can be clustered or nonclustered, depending on how the data is physically stored in relation to the index.
- An index can have positive or negative effects on the performance of queries, depending on the query type, the data distribution, and the workload.