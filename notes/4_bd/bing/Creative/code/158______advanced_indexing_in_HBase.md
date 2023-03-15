#### Advanced Indexing in HBase

- HBase is a column-oriented NoSQL database that runs on top of Hadoop and is modelled after Google's BigTable.
- HBase has only one primary index that is lexicographically sorted on the row key. This means that access to records by any other attribute requires scanning over potentially all the rows in the table, which is inefficient and costly.
- Secondary indexing is a technique to create additional indexes on other attributes of the table, such as column family, column qualifier, or value. Secondary indexes can improve the performance of queries that filter or join on these attributes.
- However, secondary indexing in HBase is not a built-in feature and requires additional design and implementation considerations. Some of the challenges are:
  - How to maintain consistency between the primary table and the secondary indexes, especially in the face of concurrent updates, failures, and compactions  ?
  - How to balance the trade-off between write throughput and query latency, as more indexes mean more writes and compactions, but also faster queries  ?
  - How to distribute and partition the secondary indexes across the cluster, and how to co-locate them with the primary table for optimal performance  ?
- There are different approaches to implement secondary indexing in HBase, such as:
  - Using coprocessors, which are user-defined code that run on the server side and can intercept read and write operations on the table . Coprocessors can be used to create and update secondary indexes automatically, but they also introduce additional complexity and overhead .
  - Using external frameworks, such as Apache Phoenix, Lily HBase Indexer, or Pinterest HBase Indexer, which provide scalable and near-real time indexing solutions on top of HBase  . These frameworks use different strategies to handle the challenges of secondary indexing, such as using HBase replication, HBase snapshots, or HBase WAL to capture the updates on the primary table and apply them to the secondary indexes  .
  - Using manual indexing, which involves creating and updating secondary indexes by the application logic or by periodic batch jobs . Manual indexing gives more control and flexibility to the user, but also requires more effort and coordination .
- Secondary indexing in HBase is a trade-off between performance, complexity, and consistency, and there is no one-size-fits-all solution. The user needs to evaluate the requirements and characteristics of their data and queries, and choose the most suitable approach for their use case   .