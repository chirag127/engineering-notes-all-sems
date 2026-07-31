### Views and Indexes

- A **view** is a named query that defines a logical table based on the result of a SELECT statement. 
- A view can be used to simplify queries, hide complex joins, restrict access to certain columns or rows, or provide a consistent interface to different tables. 
- A view can be created, modified, or dropped using the CREATE VIEW, ALTER VIEW, or DROP VIEW statements. 
- A view can be queried, updated, inserted into, or deleted from, as if it were a base table. However, some restrictions apply depending on the view definition and the underlying tables. 
- A **index** is a data structure that improves the speed of data retrieval operations on a table. 
- An index can be created on one or more columns of a table, and it provides a sorted lookup for the values in those columns. 
- An index can be created, modified, or dropped using the CREATE INDEX, ALTER INDEX, or DROP INDEX statements. 
- An index can reduce the number of disk accesses required to find a row or a set of rows that match a search condition. However, an index also increases the space and time required to insert, update, or delete rows in the table. 
- An **indexed view** is a special type of view that has a unique clustered index on it, and stores the result of the view definition as a physical table.  
- An indexed view can improve the performance of queries that join or aggregate large tables, by pre-computing the join or aggregation and storing it in the index.  
- An indexed view can be created by using the CREATE VIEW statement with the WITH SCHEMABINDING option, and then creating a unique clustered index on the view. 
- An indexed view has some limitations and requirements, such as the view and the underlying tables must have the same owner, the view definition must follow certain rules, and the SET options for the connection must be set correctly.