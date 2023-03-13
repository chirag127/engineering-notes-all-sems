#### Advanced Indexing in HBase

HBase is a distributed NoSQL database that can handle large amounts of structured and semi-structured data. HBase is built on top of the Hadoop Distributed File System (HDFS) and provides real-time read/write access to data. Advanced indexing is one of the key features of HBase that allows efficient data retrieval.

Here are some important advanced indexing techniques used in HBase:

1. Bloom Filters: Bloom Filters are probabilistic data structures that allow us to check if an element is present in a set or not. Bloom Filters are used in HBase to reduce disk I/O by avoiding unnecessary disk reads. Bloom Filters are used to check if a particular row or column family is present in a region or not. Bloom Filters are implemented at the store file level in HBase and can be enabled or disabled for each store file.

2. In-Memory Indexing: In-Memory Indexing is a technique used in HBase to speed up data retrieval. In-Memory Indexing involves keeping the most frequently accessed data in memory. In-Memory Indexing is useful for read-heavy workloads where the same data is accessed repeatedly.

3. Secondary Indexing: Secondary Indexing is a technique used in HBase to allow efficient data retrieval based on non-primary key columns. Secondary Indexing involves creating an index on a non-primary key column. The index contains a mapping of the column values to the rows that contain those values. Secondary Indexing is useful for queries that involve the non-primary key columns.

4. Composite Indexing: Composite Indexing is a technique used in HBase to create an index on multiple columns. Composite Indexing involves creating an index on a combination of two or more columns. The index contains a mapping of the column values to the rows that contain those values. Composite Indexing is useful for queries that involve multiple columns.

5. Prefix Trie Indexing: Prefix Trie Indexing is a technique used in HBase to allow efficient data retrieval based on prefix search queries. Prefix Trie Indexing involves creating an index on a column that contains string values. The index contains a mapping of the prefixes of the string values to the rows that contain those values. Prefix Trie Indexing is useful for queries that involve prefix search on string values.

Mnemonics and Tricks:

1. Bloom Filters can be remembered as a flower that helps in reducing disk I/O.

2. In-Memory Indexing can be remembered as keeping the frequently accessed data in memory.

3. Secondary Indexing can be remembered as creating an index on non-primary key columns.

4. Composite Indexing can be remembered as creating an index on multiple columns.

5. Prefix Trie Indexing can be remembered as creating an index on string values based on the prefixes.

Advanced indexing is a powerful feature of HBase that allows efficient data retrieval. By using advanced indexing techniques, we can reduce disk I/O, speed up data retrieval, and allow efficient data retrieval based on non-primary key columns.