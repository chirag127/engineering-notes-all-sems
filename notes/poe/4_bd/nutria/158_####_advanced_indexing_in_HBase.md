
# Advanced Indexing in HBase

* HBase supports two types of indexing: **secondary indexing** and **coprocessor-based indexing**. 
* **Secondary indexing** is a type of indexing that stores a separate table containing a mapping from row keys to column values. It is useful for quickly retrieving data based on a particular value of a column.
* **Coprocessor-based indexing** is a type of indexing that uses a coprocessor to build an index on the fly. It is useful for quickly retrieving data based on a particular value of a column without the need for a separate table.
* Secondary indexing is more efficient than coprocessor-based indexing, but it requires more storage space.
* To use secondary indexing, you must first create a table with the columns that you want to index.
* To use coprocessor-based indexing, you must first create a coprocessor and configure it to build an index on the fly.
* Secondary indexing is useful for quickly retrieving data based on a particular value of a column. It is also useful for reducing the amount of data that needs to be scanned when performing a query.
* Coprocessor-based indexing is useful for quickly retrieving data based on a particular value of a column without the need for a separate table. It is also useful for reducing the amount of data that needs to be scanned when performing a query.
* Both types of indexing have advantages and disadvantages. Secondary indexing requires more storage space, but is more efficient. Coprocessor-based indexing requires less storage space, but is less efficient.
* To improve the efficiency of indexing, it is important to create an index on the columns that are most frequently used in queries. 
* It is also important to keep the index up to date by regularly updating the index when data is added or modified.