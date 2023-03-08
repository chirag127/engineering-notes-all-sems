 Here is the content in markdown format for the topic ### Hive and HBase for the notes of the Unit 11 - Hadoop Eco System Frameworks in the subject of Big Data:

### Hive

- Hive is a data warehouse infrastructure built on top of Hadoop for providing data summarization, query, and analysis.
- It converts SQL-like queries into MapReduce jobs which are executed on Hadoop.
- Hive queries are converted into multiple MapReduce jobs based on the tasks.
- Hive supports partitioning of tables and the use of indexes for faster query processing.
- Data in Hive is stored in HDFS as flat files in a Hive warehouse directory.
- Hive is suitable for data warehouse applications where data is batch processed and queries are predefined and static.
- Some disadvantages of Hive are:
-- Hive queries are compiled into MapReduce jobs, so they have higher latency.
-- Hive cannot be used for real-time queries.
-- Hive does not support transactions.

### HBase

- HBase is a distributed, scalable, big data store built on Hadoop for random read/write access of large datasets.
- Data in HBase is stored in tables which contain rows and columns like a traditional database.
- However, data is stored as key-value pairs in a sparse, distributed, and persistent multidimensional sorted map.
- HBase scales horizontally by distributing regions of tables to nodes in the cluster.
- HBase is suitable for real-time access of large datasets with dynamic schemas.
- Some advantages of HBase are:
-- High throughput and scalability.
-- Strong consistency and atomicity of rows.
-- Flexible schemas (columns can be added on the fly).
-- Integration with MapReduce.
- Some disadvantages are:
-- Complex architecture and configuration.
-- Lack of SQL interface (uses Java API).
-- Not suitable for complex joins and transactions.

[Diagrams and examples can be added here]