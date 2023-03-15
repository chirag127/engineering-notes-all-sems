## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

- HDFS is a distributed file system that handles large data sets running on commodity hardware.
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN.
- HDFS provides high-performance access to data across highly scalable Hadoop clusters.
- HDFS employs a NameNode and DataNode architecture to implement a distributed file system.
- The NameNode is the master node that manages the file system namespace and regulates access to files by clients.
- The DataNodes are the slave nodes that store the actual data in blocks and perform read and write operations as instructed by the NameNode.
- HDFS is designed to be fault-tolerant, reliable, and efficient.
- HDFS supports a large number of concurrent clients, a large number of files, and a large file size.
- HDFS follows a write-once-read-many model, where files are appended to but not modified.
- HDFS provides a command-line interface and a Java API for interacting with the file system.
- HDFS also supports a web-based browser for viewing the file system status and contents.
- Hadoop Environment is the set of software and hardware components that are required to run Hadoop applications.
- Hadoop Environment includes the Hadoop core components (HDFS, MapReduce, and YARN), the Hadoop ecosystem components (such as Hive, Pig, Spark, etc.), and the underlying infrastructure (such as network, storage, memory, CPU, etc.).
- Hadoop Environment can be deployed on a single node, a cluster of nodes, or a cloud platform.
- Hadoop Environment requires proper configuration, tuning, and monitoring to ensure optimal performance and availability.