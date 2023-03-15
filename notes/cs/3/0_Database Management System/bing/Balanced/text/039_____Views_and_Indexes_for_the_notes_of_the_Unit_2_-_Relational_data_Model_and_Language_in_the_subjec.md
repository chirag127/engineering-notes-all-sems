### Views and Indexes

- A **view** is a named query that defines a logical table based on the result of a SELECT statement.
- A view can be used to simplify complex queries, hide sensitive data, or provide a consistent interface to different tables.
- A view can be created, modified, or dropped using the CREATE VIEW, ALTER VIEW, or DROP VIEW statements.
- A view can be queried, updated, inserted, or deleted from as if it were a base table, subject to some restrictions.
- A view does not store any data physically, but only references the data in the underlying tables.
- An **index** is a data structure that improves the speed of data retrieval operations on a table.
- An index can be created on one or more columns of a table, providing a sorted look-up for the rows.
- An index can be created, modified, or dropped using the CREATE INDEX, ALTER INDEX, or DROP INDEX statements.
- An index can reduce the number of disk accesses required to find a row or a range of rows, thus improving query performance.
- An index can also enforce uniqueness constraints on a table, preventing duplicate values in the indexed columns.
- An index requires additional disk space and maintenance overhead, and can slow down data modification operations on a table.
- An **indexed view** is a special type of view that has a unique clustered index on it, and stores the view data physically as a table .
- An indexed view can improve the performance of queries that join and aggregate data from multiple tables .
- An indexed view has some limitations and requirements, such as the same owner as the referenced tables, the SCHEMABINDING option, and the compatibility level of the database .
- An indexed view can be created, modified, or dropped using the same statements as a regular view, but with the addition of the WITH clause to specify the index options .
- An indexed view can be used explicitly by referencing its name in a query, or implicitly by the query optimizer if the query matches the view definition .