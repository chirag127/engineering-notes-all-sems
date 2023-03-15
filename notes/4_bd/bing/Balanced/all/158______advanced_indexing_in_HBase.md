# Advanced Indexing in HBase

- HBase is a column-oriented NoSQL database management system that runs on top of the Hadoop Distributed File System (HDFS). It is modelled after Google’s Big Table and written in Java.
- In HBase, there are no indexes. The rowkey, column family, column qualifier are all stored in sort order based on the java comparable method for byte arrays.
- Access to records in any way other than through the primary row key requires scanning over potentially all the rows in the table to test them against your filter. This can be inefficient and slow for large tables.
- Secondary indexing is a technique to create and maintain additional indexes on the table data based on some non-rowkey columns. This can improve the performance of queries that filter or sort by those columns.
- There are different approaches to implement secondary indexing in HBase, such as:
  - Using an additional table to act as the index and update it manually or periodically. This can be simple but requires extra storage and consistency management.
  - Using coprocessors to intercept the data mutations and update the index automatically. This can be efficient but requires custom code and complex logic.
  - Using external frameworks or tools such as Apache Phoenix, Lily HBase Indexer, or Elasticsearch to provide secondary indexing functionality on top of HBase . This can be convenient but introduces additional dependencies and overheads.
- Secondary indexing in HBase is not a trivial task and requires careful design and trade-offs. There are many factors to consider, such as:
  - The cardinality and distribution of the indexed columns. High cardinality and skewed distribution can lead to hotspots and imbalance in the index table.
  - The query patterns and access frequency. Frequent and complex queries can benefit from secondary indexing, but also incur more update costs and consistency challenges.
  - The consistency and durability requirements. Secondary indexes can be out of sync with the main table due to failures or delays. This can affect the correctness and freshness of the query results.
- Secondary indexing in HBase is an active research and development topic. There are ongoing efforts to improve the existing solutions and propose new ones. For example, HBASE-9203 is a Jira entry that exists specifically to address the ideas behind secondary indexing.