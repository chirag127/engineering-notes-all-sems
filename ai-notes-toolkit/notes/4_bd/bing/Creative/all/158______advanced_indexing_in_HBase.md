#### Advanced Indexing in HBase

- HBase is a column-oriented NoSQL database that runs on top of Hadoop Distributed File System (HDFS).
- HBase supports rowkey (primary key) indexing, which allows sorting rows based on the binary order of rowkeys. 
- Rowkey indexing enables efficient access to records by the primary row key, but not by other attributes or columns. 
- Secondary indexing is a technique to create additional indexes on other columns or attributes, which can improve the performance of queries that filter or join by those columns. 
- Secondary indexing in HBase is not built-in, but can be implemented using different approaches, such as:
  - Creating and maintaining a separate table as the index, which maps the secondary column values to the primary row keys. This requires manual or periodic updates to keep the index consistent with the main table. 
  - Using coprocessors, which are user-defined code that run on the HBase server side, to intercept and handle the data manipulation operations on the main table and update the index table accordingly. This can achieve near-real-time indexing, but requires custom coding and deployment. 
  - Using external tools or frameworks, such as Apache Phoenix, Lily HBase Indexer, or Pinterest HBase Indexer, which provide scalable and automated solutions for secondary indexing on HBase. These tools leverage different technologies, such as SQL, Solr, or Kafka, to create and query the secondary indexes.   
- Secondary indexing in HBase can improve the query performance, but also introduces additional complexity and overhead. Therefore, it should be used with careful design and evaluation.