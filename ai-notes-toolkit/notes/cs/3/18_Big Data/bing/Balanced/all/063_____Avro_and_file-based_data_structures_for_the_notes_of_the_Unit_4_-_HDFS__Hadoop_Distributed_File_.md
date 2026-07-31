# Avro and file-based data structures for HDFS

- HDFS (Hadoop Distributed File System) is a distributed file system that stores large amounts of data across multiple nodes in a cluster.
- HDFS supports different types of file formats, such as text, sequence, Avro, and Parquet, that have different characteristics and use cases.
- Avro is a data serialization framework that allows data to be represented in a compact binary format, which reduces the storage space and network bandwidth required for data transfer.
- Avro also provides a schema for the data, which defines the structure and data types of the fields. The schema can be stored separately from the data, or embedded within the data file.
- Avro files can be created and processed by various Hadoop components, such as Sqoop, Hive, Impala, Spark, and Flume.
- Sqoop is a tool that can import and export data between HDFS and relational databases. Sqoop can import data to HDFS in Avro format, or export data from HDFS in Avro format to relational databases.
- Hive and Impala are query engines that can create and query tables in HDFS using SQL-like syntax. Hive and Impala can create tables using Avro files as the underlying storage format, or query existing Avro files in HDFS.
- Spark is a distributed computing framework that can perform various transformations and actions on data in HDFS. Spark can read and write Avro files using the spark-avro library, or using the built-in support for Avro in Spark 3.0 and later.
- Flume is a tool that can collect and stream data from various sources to HDFS. Flume can convert JSON data to Avro format and store it in HDFS, or read Avro data from HDFS and send it to other destinations.