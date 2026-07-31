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
- An index is a data structure that improves the speed of data retrieval operations on a database table. It works by maintaining a separate data structure that stores the values for one or more columns in the table, along with a pointer to the location of each value on disk.
- Indexes can be created explicitly or automatically by the database management system, depending on the database management system in use and the options specified when creating the index.
- Indexes can be unique or non-unique. A unique index ensures that no two rows of a table have the same values in the indexed columns. A non-unique index allows multiple rows to have the same values in the indexed columns.
- Indexes can be created on computed columns, which are columns that are derived from other columns in the same table or from columns in other tables.
- Indexes can improve the performance of data retrieval operations, but they can also slow down data modification operations, such as inserts, updates, and deletes, because the database must update the index every time data is modified. Therefore, it is important to use indexes judiciously and to monitor their performance over time.