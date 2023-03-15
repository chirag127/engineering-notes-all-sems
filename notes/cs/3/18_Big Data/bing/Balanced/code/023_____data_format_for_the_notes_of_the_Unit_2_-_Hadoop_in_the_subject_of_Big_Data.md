### Data Format for the Notes of the Unit 2 - Hadoop in the Subject of Big Data

- Hadoop is a framework for storing and processing large datasets in a parallel and distributed manner .
- Hadoop has two main components: HDFS (Hadoop Distributed File System) and YARN (Yet Another Resource Negotiator) .
- HDFS is a distributed file system that stores data across multiple nodes in a cluster .
- HDFS has three components: NameNode, Secondary NameNode, and DataNode .
  - NameNode is the master node that keeps the metadata of the file system, such as the directory tree, the file locations, the file permissions, etc. .
  - Secondary NameNode is a backup node that keeps a copy of the NameNode's metadata on disk .
  - DataNode is the slave node that stores the actual data in the form of blocks .
- HDFS supports various data formats, such as text, binary, sequence, Avro, Parquet, etc. .
  - Text format is the simplest and most human-readable format, but it is not efficient for storage and processing .
  - Binary format is more compact and faster than text format, but it is not human-readable and requires a schema to interpret .
  - Sequence format is a binary format that stores key-value pairs in a sequence of records . It is suitable for storing intermediate data in MapReduce jobs .
  - Avro format is a binary format that stores data along with its schema in a JSON format . It is suitable for data exchange between different systems and languages .
  - Parquet format is a columnar format that stores data in columns rather than rows . It is suitable for analytical queries that access only a subset of columns .
- Hadoop supports various tools to import and export data between HDFS and other systems, such as Sqoop, Flume, Kafka, etc..
  - Sqoop is a tool that transfers data between HDFS and relational database management systems (RDBMS).
  - Flume is a tool that collects and transfers streaming data from various sources to HDFS.
  - Kafka is a tool that publishes and subscribes to streams of data from various sources and sinks.