# Views and Indexes in SQL

## Views

- A view is a virtual table that contains data from one or more tables based on a SELECT query.
- A view does not store any data physically, but only shows the result of the query when it is referenced.
- A view can be used to simplify complex queries, hide sensitive data, or provide a consistent interface for different users.
- A view can be created using the CREATE VIEW statement, and can be modified using the ALTER VIEW statement.
- A view can be dropped using the DROP VIEW statement, or renamed using the SP_RENAME stored procedure.
- A view can be queried, updated, inserted, or deleted from, as long as it follows certain rules.
- Some of the rules for modifying data through a view are:
  - The view must include the primary key of the underlying table.
  - The view must not contain any aggregate functions, DISTINCT, GROUP BY, HAVING, or SET operators.
  - The view must not contain any subqueries, joins, or derived tables.
  - The view must not contain any computed columns or non-deterministic functions.
  - The view must not contain any TOP or ORDER BY clauses.

## Indexes

- An index is a data structure that improves the speed of data retrieval from a table or a view.
- An index is created on one or more columns of a table or a view, and stores the values of those columns in a sorted order.
- An index can be used by the query optimizer to find the rows that match a search condition more efficiently, without scanning the entire table or view.
- An index can be created using the CREATE INDEX statement, and can be modified using the ALTER INDEX statement.
- An index can be dropped using the DROP INDEX statement, or disabled using the DISABLE INDEX statement.
- An index can be clustered or non-clustered, depending on how the data is physically stored.
- A clustered index determines the order of the data in the table or view, and can only be one per table or view.
- A non-clustered index does not affect the order of the data in the table or view, and can be multiple per table or view.
- A non-clustered index can also include additional columns that are not part of the index key, to avoid accessing the table or view for those columns.
- An indexed view is a view that has a unique clustered index on it, and is stored in the database like a table  .
- An indexed view can improve the performance of queries that join or aggregate data from multiple tables or views  .
- An indexed view has some limitations and requirements, such as:
  - The view must be created with the SCHEMABINDING option, which means it cannot reference any objects outside the current database or schema.
  - The view must not reference any tables or views that use temporary tables, table variables, or table-valued parameters.
  - The view must not reference any user-defined functions, or any system functions that are not deterministic or precise.
  - The view must not contain any outer or self joins, or any APPLY operators.
  - The view must not contain any UNION, INTERSECT, or EXCEPT operators, or any subqueries or derived tables.
  - The view must not contain any DISTINCT, TOP, or ORDER BY clauses, or any aggregate functions that are not COUNT_BIG.
  - The view must not contain any full-text predicates, or any expressions that involve collation changes or implicit conversions.
  - The view must not contain any modifications of data, such as INSERT, UPDATE, DELETE, or MERGE statements.
  - The view must not reference any views that are not indexed themselves.
  - The view must be referenced by the query optimizer using the NOEXPAND hint, or the database compatibility level must be 90 or higher.