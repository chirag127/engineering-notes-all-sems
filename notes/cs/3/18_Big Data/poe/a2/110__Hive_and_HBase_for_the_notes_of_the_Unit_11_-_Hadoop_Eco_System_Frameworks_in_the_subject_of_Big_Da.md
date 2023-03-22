 Here is the formal notes on Hive and HBase for the Unit 11 - Hadoop Eco System Frameworks in markdown format:

### Hive

1. Hive is a data warehouse infrastructure built on top of Hadoop for providing data summarization, query, and analysis.
2. It converts SQL queries into MapReduce jobs which are executed on Hadoop cluster.
3. Hive provides a mechanism to project structure onto this data and query the data using a SQL-like language called HiveQL.
4. HiveQL is translated into a series of MapReduce jobs to perform the query.
5. Hive allows easy data extracting, transforming and loading (ETL).
6. It has a Metastore that stores metadata about the data, including schema and partition information.
7. Hive is most appropriate for queries that can be expressed in terms of map and reduce tasks.
8. Limitations - Not good for low latency queries, Cannot perform transactions, Not appropriate for recursive queries.

### HBase

1. HBase is a scalable, distributed, versioned, non-relational database.
2. It is built on Hadoop and provides random read/write access to the data.
3. Data in HBase is organized into tables with rows and columns like a table in traditional database.
4. However, the data is stored in HDFS and accessed using the Hadoop APIs.
5. HBase provides strong consistency and high throughput for both reads and writes.
6. HBase scales to billions of rows and millions of columns.
7. It uses a master-slave architecture with one master server and multiple region servers.
8. HBase is appropriate for random 'get/put' access to big datasets.
9. Use cases include - real-time access to Big Data, frequently updating random access patterns, sparse data sets.