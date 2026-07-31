### Views and Indexes

- A **view** is a named query that defines a logical table based on the result of a SELECT statement.
- A view can be used to simplify queries, hide complex joins, restrict access to certain columns or rows, or provide a consistent interface to data that may change over time.
- A view can be created using the CREATE VIEW statement, and can be queried, updated, inserted, or deleted from as if it were a base table.
- A view does not store any data physically, but only references the data in the underlying tables.
- A view can be dropped using the DROP VIEW statement, which does not affect the data in the underlying tables.

- An **index** is a data structure that improves the speed of data retrieval operations on a table by creating a pointer to the location of the data.
- An index can be created on one or more columns of a table, and can be used to quickly find the rows that match a search condition.
- An index can be created using the CREATE INDEX statement, and can be dropped using the DROP INDEX statement.
- An index can also be created on a view, which is called an **indexed view** .
- An indexed view is a view that has been materialized, meaning that the view definition has been computed and the resulting data stored just like a table.
- An indexed view can improve the performance of some types of queries, especially those that involve aggregations, joins, or subqueries.
- An indexed view can be created by creating a unique clustered index on the view using the CREATE UNIQUE CLUSTERED INDEX statement .
- An indexed view has some restrictions, such as the view and the underlying tables must have the same owner, the view must have a schema binding option, and the view must not contain certain elements such as outer joins, subqueries, or non-deterministic functions .