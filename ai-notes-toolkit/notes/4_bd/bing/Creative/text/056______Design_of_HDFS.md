#### Design of HDFS

HDFS stands for Hadoop Distributed File System. It is a file system that is designed to store very large files across multiple machines in a cluster. HDFS has the following characteristics and features:

- HDFS is based on the Google File System (GFS) .
- HDFS was originally built as infrastructure for the Apache Nutch web search engine project .
- HDFS is a member of the Hadoop Ecosystem, which includes other components such as MapReduce, YARN, Hive, Pig, HBase, etc.
- HDFS is highly fault-tolerant and can handle hardware failures, network partitions, and data corruption .
- HDFS is optimized for streaming data access patterns, where files are read and written in large sequential blocks .
- HDFS relaxes some POSIX requirements to enable high throughput and scalability .
- HDFS supports replication of data blocks across multiple nodes to ensure data availability and durability .
- HDFS has a master-slave architecture, where a single NameNode manages the namespace and metadata of the file system, and multiple DataNodes store and serve the data blocks .
- HDFS provides a Java API and a command-line interface for clients to interact with the file system .
- HDFS also provides a web interface and a REST API for monitoring and administration .

: https://www.databricks.com/glossary/hadoop-distributed-file-system-hdfs
: https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html