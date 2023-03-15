### Views and Indexes

#### Views
- A view is a virtual table based on the result-set of an SQL statement.
- A view contains rows and columns, just like a real table.
- The fields in a view are fields from one or more real tables in the database.
- You can add SQL functions, WHERE, and JOIN statements to a view and present the data as if the data were coming from one single table.

#### Indexes
- An index is a performance-tuning method of allowing faster retrieval of records.
- An index creates an entry for each value that appears in the indexed columns.
- By default, the CREATE INDEX statement creates a B-tree index.
- Indexes can be unique or non-unique.
- Unique indexes guarantee that no two rows of a table have duplicate values in the key column (or columns).
- Non-unique indexes do not impose this restriction on the column values.
