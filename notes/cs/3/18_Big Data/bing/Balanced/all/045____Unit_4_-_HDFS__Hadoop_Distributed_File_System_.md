# Unit 4 - HDFS (Hadoop Distributed File System)

- HDFS is a distributed file system that handles large data sets running on commodity hardware.
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN .
- HDFS is designed to be highly fault-tolerant, scalable, and efficient .
- HDFS employs a NameNode and DataNode architecture to implement a distributed file system.
  - NameNode is the master node that manages the file system namespace and regulates access to files by clients.
  - DataNode is the slave node that stores the actual data in blocks and performs read and write operations as instructed by the NameNode.
- HDFS splits files into large blocks (typically 128 MB or 256 MB) and distributes them across nodes in a cluster .
- HDFS replicates each block across multiple nodes (default replication factor is 3) to ensure reliability and availability .
- HDFS supports a write-once-read-many access model for files.
- HDFS provides a command-line interface and a Java API for interacting with the file system.
- HDFS supports several file formats, such as text, CSV, JSON, XML, Parquet, ORC, Avro, etc.