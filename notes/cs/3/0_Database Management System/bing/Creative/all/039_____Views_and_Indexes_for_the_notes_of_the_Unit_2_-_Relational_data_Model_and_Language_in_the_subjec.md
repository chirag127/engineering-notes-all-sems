# Views and Indexes for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

## Views
- A view is a logical representation of a table or a query that is stored in the database.
- A view can be created from one or more tables or other views, by using a SELECT statement.
- A view can be used to simplify queries, restrict access to data, or provide a consistent interface to data.
- A view does not store any data physically, but only references the data in the underlying tables or views.
- A view can be created, modified, or dropped using the SQL commands CREATE VIEW, ALTER VIEW, or DROP VIEW.
- A view can have the same name as a table, as long as they are in different schemas.
- A view can be queried, updated, inserted, or deleted from, as long as it meets certain conditions.
- A view can be joined with other tables or views, as long as the join conditions are valid.

## Indexes
- An index is a data structure that improves the speed of data retrieval from a table or a view.
- An index can be created on one or more columns of a table or a view, by using a CREATE INDEX statement.
- An index can be used to speed up queries that involve filtering, sorting, grouping, or joining on the indexed columns.
- An index can also enforce uniqueness or referential integrity constraints on the indexed columns.
- An index stores a copy of the indexed columns and a pointer to the corresponding rows in the table or the view.
- An index can be clustered or nonclustered, depending on how the data is physically stored.
- A clustered index determines the order of the rows in the table or the view, and can only be one per table or view.
- A nonclustered index does not affect the order of the rows in the table or the view, and can be multiple per table or view.
- An index can be created, modified, or dropped using the SQL commands CREATE INDEX, ALTER INDEX, or DROP INDEX.
- An index can be disabled, rebuilt, or reorganized using the SQL commands DISABLE INDEX, REBUILD INDEX, or REORGANIZE INDEX.

## Indexed Views
- An indexed view is a view that has a unique clustered index created on it .
- An indexed view is also called a materialized view, because it stores the result of the view definition in a physical table .
- An indexed view can improve the performance of queries that involve aggregations, joins, or complex calculations on the view columns .
- An indexed view can also reduce the storage space and maintenance cost of the underlying tables or views, by eliminating the need for redundant data .
- An indexed view has some limitations and requirements, such as the view definition must be deterministic, schema-bound, and not reference any non-deterministic functions or expressions .
- An indexed view can be created, modified, or dropped using the SQL commands CREATE VIEW, ALTER VIEW, or DROP VIEW, with the WITH SCHEMABINDING and WITH (CLUSTERED) options .
- An indexed view can be queried, updated, inserted, or deleted from, as long as it meets the same conditions as a regular view .
- An indexed view can be joined with other tables or views, as long as the join conditions are valid .