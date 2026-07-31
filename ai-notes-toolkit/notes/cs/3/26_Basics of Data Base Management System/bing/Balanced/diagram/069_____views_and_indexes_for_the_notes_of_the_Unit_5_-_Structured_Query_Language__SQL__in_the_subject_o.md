### Views and Indexes in SQL

#### Views

- A view is a named query that is stored in the database and can be used like a table.
- A view can be created from one or more tables or other views, and can have a subset of columns and rows from the source tables.
- A view can be used to simplify complex queries, hide sensitive data, or provide a consistent interface to changing data structures.
- A view can be created using the CREATE VIEW statement, followed by the view name and the SELECT query that defines the view.
- A view can be queried, updated, inserted, or deleted from, as long as it follows certain rules, such as not having aggregate functions, DISTINCT, or GROUP BY clauses.
- A view can be dropped using the DROP VIEW statement, followed by the view name.

#### Indexes

- An index is a data structure that improves the speed of data retrieval from a table or a view.
- An index can be created on one or more columns of a table or a view, and can be used by the query optimizer to find the best execution plan for a query.
- An index can be created using the CREATE INDEX statement, followed by the index name, the table or view name, and the list of columns to be indexed.
- An index can be clustered or nonclustered, depending on how the data is physically stored in the database. A clustered index determines the order of the rows in the table or view, while a nonclustered index does not.
- An index can be unique or nonunique, depending on whether it allows duplicate values in the indexed columns or not. A unique index can also be used to enforce a primary key or a unique constraint on a table or view.
- An index can be dropped using the DROP INDEX statement, followed by the index name and the table or view name.