# Views and Indexes in SQL

## Views

- A view is a named query that is stored in the database and can be used to access or manipulate data from one or more tables.
- A view does not contain any data or exist in physical storage, but it acts like a virtual table that can be queried or updated.
- A view can be used to:
  - Limit a user's access to specific rows and columns of a table.
  - Manipulate data from multiple tables as if all the data were contained in a single table.
  - Simplify complex queries and hide their details.
  - Provide a consistent interface to the underlying data, even if the data structure changes.
- A view can be created using the CREATE VIEW statement, followed by the name of the view and the SELECT query that defines the view.
- A view can be queried or updated using the same syntax as a table, as long as the view is updatable.
- A view can be dropped using the DROP VIEW statement, followed by the name of the view.

## Indexes

- An index is a data structure that improves the speed of data retrieval operations on a table by creating a pointer to the data in a specific column or a set of columns.
- An index can be used to:
  - Reduce the amount of data that needs to be scanned by the query optimizer.
  - Sort and group data more efficiently.
  - Enforce uniqueness and referential integrity constraints on the table.
- An index can be created using the CREATE INDEX statement, followed by the name of the index, the name of the table, and the name of the column or columns to be indexed.
- An index can be dropped using the DROP INDEX statement, followed by the name of the index and the name of the table.

## Indexed Views

- An indexed view is a view that has a unique clustered index on it, which physically stores the view data in the database and makes the view act like a table.
- An indexed view can be used to:
  - Improve the performance of queries that join and aggregate data from multiple tables.
  - Write fewer pages to disk than the underlying tables, meaning fewer pages queries need to read fewer pages to return results.
  - Create statistics for the view that optimize cardinality estimations.
- An indexed view can be created using the CREATE VIEW statement with the WITH SCHEMABINDING option, followed by the name of the view and the SELECT query that defines the view, and then using the CREATE UNIQUE CLUSTERED INDEX statement, followed by the name of the index and the name of the view.
- An indexed view can be dropped using the DROP VIEW statement, followed by the name of the view, or using the DROP INDEX statement, followed by the name of the index and the name of the view.
- An indexed view has some limitations and requirements, such as:
  - The view must be schema-bound to the base tables, meaning the view definition cannot be changed and the base tables cannot be modified in a way that affects the view.
  - The view must not contain any non-deterministic expressions, such as GETDATE(), NEWID(), or RAND().
  - The view must not contain any outer or self joins, subqueries, or derived tables.
  - The view must contain a COUNT_BIG(*) expression in the SELECT list.
  - The view must be referenced by the query optimizer to produce the query plan, which depends on the SET options of the session.
  - Any insert, update, or delete operation performed on any table that participates in the indexed view must also update the indexed view, which may incur some overhead .

: Database Design - Views & indexes - California State University, Long Beach
: SQL Server Indexed Views: The Basics - Simple Talk
: Create Indexed Views - SQL Server | Microsoft Learn
: sql - How do indexes work on views? - Stack Overflow
: Tables, Views and Indexes in SQL - theintactone