### Basic Indexing Methods for Unit 5 - Applications in IDBS in the Subject of Intelligent Database System

1. **B+ Tree Indexing**: This is a tree-based indexing method that is commonly used in database systems. It allows for efficient searching, insertion, and deletion of data.

2. **Bitmap Indexing**: This indexing method uses bitmaps to represent the values of a column in a table. It is particularly useful for columns with low cardinality, where the number of distinct values is small.

3. **Clustered Indexing**: This method physically reorders the rows of a table to match the order of the index. This can improve the performance of queries that retrieve data in the order of the index.

4. **Hash Indexing**: This method uses a hash function to map the values of a column to a fixed number of buckets. It is useful for equality searches, where the goal is to find rows with a specific value in the indexed column.

5. **Non-Clustered Indexing**: This method creates an index that is separate from the physical storage of the table. It can improve the performance of queries that do not retrieve data in the order of the index.

These are some of the basic indexing methods used in intelligent database systems. Each method has its own advantages and disadvantages, and the choice of indexing method depends on the specific requirements of the application.