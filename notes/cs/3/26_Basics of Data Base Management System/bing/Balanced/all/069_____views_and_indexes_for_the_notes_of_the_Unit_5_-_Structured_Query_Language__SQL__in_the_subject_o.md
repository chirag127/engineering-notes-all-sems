# Views and Indexes in SQL

## Views

- A view is a named query that is stored in the database and can be used like a table.
- A view can be created from one or more tables or other views, and can have a subset of columns and rows from the source tables.
- A view can be used to simplify complex queries, hide sensitive data, or provide a consistent interface to changing data structures.
- A view can be created using the CREATE VIEW statement, followed by the view name and the SELECT query that defines the view.
- A view can be queried, updated, inserted into, or deleted from, as long as it meets certain conditions, such as not having aggregate functions, DISTINCT, or GROUP BY clauses.
- A view can be dropped using the DROP VIEW statement, followed by the view name.

## Indexes

- An index is a data structure that improves the speed of data retrieval from a table or a view.
- An index can be created on one or more columns of a table or a view, and can be used to quickly locate rows that match a search condition.
- An index can be created using the CREATE INDEX statement, followed by the index name, the table or view name, and the list of columns to be indexed.
- An index can be clustered or non-clustered, depending on whether it physically sorts the data rows or not.
- An index can be unique or non-unique, depending on whether it allows duplicate values or not.
- An index can be dropped using the DROP INDEX statement, followed by the index name and the table or view name.