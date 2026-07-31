### Views and Indexes in SQL

- A **view** is a named query that is stored in the database and can be used like a table. A view can simplify complex queries, hide sensitive data, or provide a consistent interface for different tables.
- An **index** is a data structure that improves the speed of data retrieval from a table. An index can be created on one or more columns of a table, and it allows the database to quickly find the rows that match a given condition.
- A **clustered index** determines the physical order of the data in the table. There can be only one clustered index per table. A clustered index is usually created on the primary key column of the table.
- A **nonclustered index** does not affect the physical order of the data, but creates a separate structure that points to the data rows. There can be multiple nonclustered indexes per table. A nonclustered index is useful for columns that are frequently used in queries, but not in the primary key.
- An **indexed view** is a view that has a clustered index created on it. An indexed view can improve the performance of queries that use the view, because the data is stored in a sorted and aggregated form. An indexed view also has statistics that help the query optimizer to choose the best execution plan. 
- To create an indexed view, the view must satisfy certain requirements, such as having a unique clustered index, not using non-deterministic functions, and having the same SET options as the session that queries the view.
- To use an indexed view, the query must reference the view by name, or use the NOEXPAND hint to prevent the view from being expanded into its base tables. The query optimizer may also use the indexed view automatically if it is beneficial for the query.
- An indexed view can have a positive or negative impact on the performance of insert, update, or delete operations on the base tables, depending on the complexity of the view and the frequency of the data changes. 

: Database Design - Views & indexes - California State University, Long Beach
: SQL Server Indexed Views: The Basics - Simple Talk
: Create Indexed Views - SQL Server | Microsoft Learn
: sql - How do indexes work on views? - Stack Overflow
: SQL INDEX - W3Schools