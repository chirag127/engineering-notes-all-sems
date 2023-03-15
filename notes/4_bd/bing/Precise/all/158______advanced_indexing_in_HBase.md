#### Advanced Indexing in HBase

- HBase is a column-oriented NoSQL database management system that runs on top of the Hadoop Distributed File System (HDFS). It is modeled after Google’s Big Table and written in Java.
- In HBase, there are no indexes. The rowkey, column family, column qualifier are all stored in sort order based on the java comparable method for byte arrays.
- Access to records in any way other than through the primary row requires scanning over potentially all the rows in the table to test them against your filter.
- Secondary indexing is a way to improve the performance of HBase by creating an additional table to act as the index and update manually.
- Lily HBase Indexer service embeds the NG-Data Indexer to provide a Near-Real-Time (NRT) resilient automated configuration-driven mechanism to trigger Morphline (Kite SDK) parsers over an HBase table.
