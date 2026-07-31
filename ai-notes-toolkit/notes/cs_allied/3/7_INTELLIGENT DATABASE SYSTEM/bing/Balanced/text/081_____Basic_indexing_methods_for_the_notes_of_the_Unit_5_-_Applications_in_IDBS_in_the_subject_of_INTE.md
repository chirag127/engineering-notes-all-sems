### Basic indexing methods for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Indexing is a technique to optimize the performance of a database by reducing the number of disk accesses required to process a query.
- Indexing creates a data structure that allows faster and easier access to the data in a database table.
- Indexing is based on the indexing attributes, which are the columns or fields used to search, sort, or join the data.
- There are two main types of indexing methods: primary indexing and secondary indexing.
- Primary indexing is defined on an ordered data file, where the data file is sorted on a key field, which is usually the primary key of the table.
- Primary indexing has two subtypes: dense indexing and sparse indexing.
- Dense indexing creates an index record for every search key value in the database, and each index record contains the search key value and a pointer to the actual record in the data file.
- Sparse indexing creates an index record only for some of the search key values, and each index record contains the search key value and a pointer to the first data block that contains that value.
- Secondary indexing is defined on a field that is not the primary key of the table, and it can be either a candidate key or a non-key field.
- Secondary indexing creates an index file that contains the values of the secondary key and pointers to the records that have that value.
- Secondary indexing can be used to support queries that do not involve the primary key, or to create multiple access paths to the data.
- There are other types of indexing methods, such as clustering indexing, multilevel indexing, hash-based indexing, bitmap indexing, etc., that are designed for specific purposes or data types.
- Indexing in intelligent database systems can also involve techniques such as semantic indexing, content-based indexing, or similarity-based indexing, that use the meaning, content, or similarity of the data to create indexes.