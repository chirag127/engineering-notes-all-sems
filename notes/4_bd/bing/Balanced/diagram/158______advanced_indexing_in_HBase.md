#### Advanced Indexing in HBase

- HBase is a column-oriented NoSQL database that runs on top of Hadoop Distributed File System (HDFS) and is modelled after Google's Big Table.
- HBase has only one primary index that is lexicographically sorted on the row key. Accessing records by any other criteria requires scanning over potentially all the rows in the table, which is inefficient and slow.
- Secondary indexing is a technique to create additional indexes on other columns or attributes of the data, which can improve the query performance and reduce the scan overhead.
- There are different approaches to implement secondary indexing in HBase, such as:
  - Using a separate table as an index and manually updating it whenever the main table changes. This requires extra storage and maintenance, and may cause inconsistency or stale data.
  - Using coprocessors, which are user-defined code that run on the server side and can intercept the read and write operations on the main table. Coprocessors can create and maintain secondary indexes on the fly, but they may introduce additional complexity and overhead.
  - Using external frameworks or tools, such as Apache Phoenix, Lily HBase Indexer, or Elasticsearch, which provide built-in or near-real-time secondary indexing capabilities on top of HBase. These solutions may offer more features and flexibility, but they may also depend on additional components or configurations .
- The choice of secondary indexing strategy depends on the use case, the data model, the query pattern, and the trade-offs between performance, consistency, and complexity.