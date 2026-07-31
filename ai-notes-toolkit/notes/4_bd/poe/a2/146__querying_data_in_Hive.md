 Here is the formal content in Markdown format on the topic of querying data in Hive:

#### Querying data in Hive

1. HiveQL: HiveQL is a query language similar to SQL which is used to query the data stored in Hive. It is translated into a series of MapReduce jobs which are executed on the cluster to return the result.

2. Hive Tables: Data in Hive is stored in tables. There are two types of tables - managed tables (data is deleted when table is dropped) and external tables (data is retained even after table is dropped). Tables can be created, altered or dropped using CREATE, ALTER and DROP statements respectively.

3. Loading data: Data can be loaded into Hive tables from files in HDFS, local filesystem or other tables using LOAD statement. The input data can be in text, CSV, Parquet, ORC, Avro, RCFile formats etc. Storage formats can be specified while creating tables or modified later using ALTER TABLE statement.

4. Running Queries: Queries on tables can be written in HiveQL and executed using CLI or Beeline (shell). The results are retrieved in tabular form or can be stored in output tables/HDFS files. Complex queries can be written with joins, aggregations, subqueries etc.

5. Performance Tuning: There are various parameters and configurations available to tune the performance of Hive queries. Some of these include:

- Optimal file formats (ORC, Parquet)
- Bucketing and partitioning of tables
- Dynamic partitioning
- Joins (using buckets/sorts)
- Map join
- Vectorization
- Compression
- Execution engines (MR, Tez)
- Caching/prewarming

The above points summarize the key steps involved in querying data stored in Hive. Let me know if you would like me to elaborate on any of the points.