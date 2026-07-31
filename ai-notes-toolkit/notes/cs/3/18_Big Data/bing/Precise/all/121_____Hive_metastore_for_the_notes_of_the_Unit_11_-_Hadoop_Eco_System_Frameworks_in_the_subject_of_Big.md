### Hive Metastore

- Hive Metastore (HMS) is a service that stores metadata related to Apache Hive and other services, in a backend RDBMS, such as MySQL or PostgreSQL  .
- Impala, Spark, Hive, and other services share the metastore  .
- The connections to and from HMS include HiveServer, Ranger, and the NameNode that represents HDFS  .
- HMS is a central repository of metadata for Hive tables and partitions in a relational database, and provides clients (including Hive, Impala and Spark) access to this information using the metastore service API .
- HMS provides a central repository of metadata that can easily be analyzed to make informed, data-driven decisions, and therefore it is a critical component of many data lake architectures .
- Hive is built on top of Apache Hadoop and supports storage on S3, adls, gs etc though hdfs .
- Hive Metastore was developed as a part of Apache Hive, “a distributed, fault-tolerant data warehouse system that enables analytics at a massive scale” .
- Hive achieves this goal by being the storage point for all the meta-information about your data storages .