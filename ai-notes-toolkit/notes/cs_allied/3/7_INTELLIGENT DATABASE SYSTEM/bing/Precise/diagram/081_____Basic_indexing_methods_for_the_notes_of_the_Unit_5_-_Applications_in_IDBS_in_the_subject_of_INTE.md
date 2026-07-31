### Basic Indexing Methods for Unit 5 - Applications in IDBS in the Subject of Intelligent Database System

1. **B+ Tree Indexing**: This is a tree-based indexing method that is commonly used in database systems. It is an extension of the B-tree, where all data is stored in the leaf nodes and the internal nodes only contain index values.

2. **Bitmap Indexing**: This is a type of indexing that uses bitmaps to represent the relationship between the indexed column and the rows in the table. It is particularly useful for columns with low cardinality, where the number of distinct values is small compared to the number of rows.

3. **Clustered Indexing**: This is a type of indexing where the physical order of the rows in the table is the same as the logical order of the index. This can improve the performance of range queries, as the data is stored contiguously on disk.

4. **Hash Indexing**: This is a type of indexing that uses a hash function to map the values of the indexed column to a fixed number of buckets. It is particularly useful for equality queries, where the goal is to find all rows with a specific value in the indexed column.

5. **ISAM Indexing**: This stands for Indexed Sequential Access Method. It is a type of indexing that uses a combination of a sequential file and an index to improve the performance of data retrieval. It is particularly useful for applications where the data is mostly read and not frequently updated.

These are some of the basic indexing methods used in Intelligent Database Systems. Each method has its own advantages and disadvantages, and the choice of indexing method depends on the specific requirements of the application.