# Unit 6 - PL/SQL in the subject of Basics of Data Base Management System

### Indices

- An index is a database object that improves the performance of data retrieval.
- It does this by reducing the number of disk accesses required when a query is executed.
- An index is created on one or more columns of a table.
- When a query is executed that involves a search on the indexed column(s), the database uses the index to find the rows that match the search condition.
- This can be much faster than scanning the entire table to find the matching rows.
- Indices can be created explicitly by the user or automatically by the database.
- The decision to create an index should be based on the trade-off between faster query performance and slower data modification performance.
- When data is inserted, updated, or deleted in a table, the index must also be updated, which can slow down these operations.
- Therefore, indices should be created judiciously, taking into account the frequency of data modification and the performance requirements of queries.