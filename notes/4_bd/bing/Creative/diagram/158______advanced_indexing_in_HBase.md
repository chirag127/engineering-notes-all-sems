#### Advanced Indexing in HBase

- HBase is a column-oriented NoSQL database that runs on top of Hadoop Distributed File System (HDFS) and is modelled after Google's BigTable.
- HBase has only one primary index that is lexicographically sorted on the row key. Accessing records by any other criteria requires scanning over potentially all the rows in the table to test them against a filter.
- Secondary indexing is a technique to create additional indexes on other columns or attributes of the data, to improve the query performance and avoid full table scans.
- HBase does not provide native support for secondary indexing, but there are several approaches to implement it, such as:
  - Using an additional table to store the secondary index and manually update it whenever the main table changes. This requires extra storage and maintenance, and may cause inconsistency if the updates are not atomic.
  - Using coprocessors, which are user-defined code that run on the HBase server side and can intercept read and write operations. Coprocessors can be used to create and maintain secondary indexes automatically, but they may introduce additional overhead and complexity.
  - Using external frameworks or tools that integrate with HBase and provide secondary indexing capabilities, such as Apache Phoenix, Lily HBase Indexer, or Elasticsearch. These solutions may vary in their features, performance, scalability, and reliability .
- The choice of secondary indexing approach depends on the use case, the data model, the query patterns, and the trade-offs between speed, space, and consistency.