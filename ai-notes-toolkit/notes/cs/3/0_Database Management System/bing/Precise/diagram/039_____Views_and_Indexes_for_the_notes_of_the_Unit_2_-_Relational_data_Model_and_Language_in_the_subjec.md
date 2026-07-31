### Views and Indexes

#### Views
- A view is a virtual table based on the result-set of an SQL statement.
- A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.
- You can add SQL functions, WHERE, and JOIN statements to a view and present the data as if the data were coming from one single table.
- Views can provide advantages over tables:
  - Views can represent a subset of the data contained in a table.
  - Views can join and simplify multiple tables into a single virtual table.
  - Views can act as aggregated tables, where the database engine aggregates data (sum, average, etc.) and presents the calculated results as part of the data.
  - Views can hide the complexity of data. For example, a view could appear as Sales2000 or Sales2001, transparently partitioning the actual underlying table.
  - Views take very little space to store; the database contains only the definition of a view, not a copy of all the data that it presents.

#### Indexes
- An index is an object in a database that improves the speed of data retrieval operations on a database table.
- By creating an index on one or more columns of a table, you can make it faster for the database engine to search for rows in the table that match certain criteria.
- Indexes can be created using one or more columns of a database table, providing the basis for both rapid random lookups and efficient access of ordered records.
- An index helps speed up SELECT queries and WHERE clauses, but it slows down data input, with UPDATE and INSERT statements. Indexes can be created or dropped with no effect on the data.
- Creating an index involves the database engine creating a new, separate data structure that contains a sorted list of the indexed column values, along with a pointer to the location of each value on the disk where the table row data is stored.
- The database engine uses the index to find the rows in the table that match the search criteria specified in a query, instead of scanning the entire table to find the matching rows.