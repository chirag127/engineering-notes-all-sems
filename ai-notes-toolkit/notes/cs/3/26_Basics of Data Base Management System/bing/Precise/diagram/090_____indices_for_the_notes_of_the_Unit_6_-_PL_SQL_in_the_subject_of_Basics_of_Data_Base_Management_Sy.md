### Unit 6 - PL/SQL: Indices

1. An index is a database object that improves the performance of data retrieval.
2. Indices are created on one or more columns of a table.
3. When a query is executed, the database searches the index for the values specified in the WHERE clause, rather than scanning the entire table.
4. This can significantly reduce the time it takes to retrieve data.
5. Indices can be created explicitly using the CREATE INDEX statement or implicitly when a UNIQUE, PRIMARY KEY, or FOREIGN KEY constraint is defined on a table.
6. The database automatically maintains the index as data is inserted, updated, or deleted in the indexed columns.
7. Indices can be created in ascending or descending order, and can be either unique or non-unique.
8. The decision to create an index should be based on the query performance and the frequency of data modification.
9. Creating too many indices can slow down data modification operations, as the database must update the indices as well as the table data.
10. It is important to monitor the performance of indices and rebuild or drop them if necessary.
