### Views and Indexes

- A **view** is a named query that defines a logical table based on the result of a SELECT statement.
- A view can be used to simplify queries, hide complex joins, restrict access to certain columns or rows, or provide a consistent interface to different tables.
- A view can be created, modified, or dropped using the SQL commands CREATE VIEW, ALTER VIEW, or DROP VIEW.
- A view can be queried, updated, inserted, or deleted from as if it were a base table, subject to some limitations.
- A view does not store any data physically, but only references the data in the underlying tables.
- A view can be materialized by creating an index on it, which stores the view data as a clustered index .
- An **index** is a data structure that allows faster access to rows in a table based on the values of one or more columns.
- An index can be created, modified, or dropped using the SQL commands CREATE INDEX, ALTER INDEX, or DROP INDEX.
- An index can improve the performance of queries that use the indexed columns in the WHERE, JOIN, ORDER BY, or GROUP BY clauses.
- An index can also enforce uniqueness or referential integrity constraints on the table data.
- An index can reduce the performance of insert, update, or delete operations on the table, as the index data has to be maintained as well.
- An index can be clustered or non-clustered, depending on whether it determines the physical order of the table data or not.