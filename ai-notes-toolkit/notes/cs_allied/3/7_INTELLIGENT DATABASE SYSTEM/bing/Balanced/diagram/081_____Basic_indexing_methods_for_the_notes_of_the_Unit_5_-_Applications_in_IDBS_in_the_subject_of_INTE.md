### Basic indexing methods for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Indexing is a way to optimize the performance of a database by minimizing the number of disk accesses required when a query is processed.
- Indexing is a data structure technique which is used to quickly locate and access the data in a database.
- Indexes are created using a few database columns.
- Indexing in Database is defined based on its indexing attributes.
- Two main types of indexing methods are:
  - Primary Indexing
  - Secondary Indexing
- Primary Indexing
  - Primary Index is an ordered file which is fixed length size with two fields.
  - The first field is the same as the primary key and the second field is a pointer to that specific data block.
  - Primary Indexing is also further divided into two types:
    - Dense Index
    - Sparse Index
  - Dense Index
    - In a dense index, a record is created for every search key value in the database.
    - The index records are stored in a separate file and sorted by the search key value.
    - The dense index is faster to search but requires more space and maintenance.
  - Sparse Index
    - In a sparse index, a record is created for only some of the search key values in the database.
    - The index records are stored in a separate file and sorted by the search key value.
    - The sparse index is slower to search but requires less space and maintenance.
- Secondary Indexing
  - Secondary Index is an ordered file which is variable length size with two fields.
  - The first field is a non-key field and the second field is a pointer to the data block or a list of pointers to all the data blocks that contain that value.
  - Secondary Index is used to speed up the queries that involve non-key attributes.
  - Secondary Index can be dense or sparse depending on whether it contains a record for every value or some values of the non-key attribute.
- A diagram to illustrate the basic indexing methods is shown below:

![Basic Indexing Methods](https://media.geeksforgeeks.org/wp-content/uploads/20191112172902/Indexing-in-DBMS-Set-1-1.png)