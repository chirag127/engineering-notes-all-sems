#### Hive metastore

- Hive metastore (HMS) is a service that stores metadata related to Apache Hive and other services, such as Impala, Spark, and Ranger, in a backend relational database, such as MySQL or PostgreSQL  .
- HMS provides a central repository of metadata that can easily be analyzed to make informed, data-driven decisions, and therefore it is a critical component of many data lake architectures.
- HMS provides clients access to this information using the metastore service API, which is based on Apache Thrift .
- HMS supports various storage formats, such as ORC, Parquet, Avro, and JSON, and various storage systems, such as HDFS, S3, ADLS, and GCS.
- HMS supports various features, such as ACID transactions, data compaction, replication, security, observability, and low latency analytical processing (LLAP).
- HMS uses Apache Calcite's cost-based query optimizer (CBO) and query execution framework to optimize SQL queries.
- HMS can operate in active/active mode, where multiple HMS instances use the same backend database and provide high availability.