 Here is the content in markdown format on the topic #### advanced indexing in HBase:

#### Advanced Indexing in HBase

HBase provides advanced indexing capabilities to speed up queries and enable efficient database access patterns. Some of the key advanced indexing techniques in HBase are:

- Bloom Filters: Bloom filters are space-efficient probabilistic data structures used to test if an element is a member of a set. In HBase, bloom filters are used to check if a row exists in a table or not, thereby improving read performance. They give fast negative responses at the cost of possible false positives.
- Block Cache: The block cache is a memory cache used to store HFile blocks in memory to speed up data access. It reduces the number of disk I/O operations thereby improving read performance. The most frequently accessed blocks are stored in the block cache.
- Compression: HBase provides compression algorithms like Gzip, LZO, Snappy, etc. to reduce the size of stored data. This decreases I/O costs and increases the effective memory size of the block cache.
- Column Families: HBase organizes data into tables which contain column families. Placing columns with similar access patterns in the same column family improves performance as the data is stored together on disk. This is a form of logical indexing in HBase.
- Secondary Indexes: HBase provides secondary indexing through coprocessors to index row keys or values of specific columns. This enables efficient key-value lookups, range scans, etc. on indexed columns leading to faster queries with low latency.

Some Mnemonics and Tips:
- B: Think of Bloom filter as checking if row is There (T) or not There (NT). It gives fast NT responses.
- Block cache: Hot data in memory, cold data on disk.
- 3Cs: Compression, Column families, Coprocessors (secondary indexes)
- Diagrams and examples can help in understanding the concepts.

The above techniques can significantly boost read and write performance in HBase and enable efficient access patterns crucial for fast querying and analysis of huge datasets.