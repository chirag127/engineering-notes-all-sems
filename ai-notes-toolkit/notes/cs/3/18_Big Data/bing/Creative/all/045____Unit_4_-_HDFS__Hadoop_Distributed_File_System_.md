## Unit 4 - HDFS (Hadoop Distributed File System)

- HDFS is a distributed file system that handles large data sets running on commodity hardware.
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN.
- HDFS is designed to be highly fault-tolerant, scalable, and efficient.
- HDFS employs a NameNode and DataNode architecture to implement a distributed file system.
- The NameNode is the master node that manages the file system namespace and regulates access to files by clients.
- The DataNodes are the worker nodes that store the actual data in blocks and perform read and write operations on the blocks as instructed by the NameNode.
- HDFS supports a traditional hierarchical file organization, where a user or an application can create directories and store files inside them.
- HDFS provides a command-line interface and a Java API for interacting with the file system.
- HDFS also supports a web-based browser for accessing the file system.
- HDFS follows a write-once-read-many model, where a file once created, written, and closed cannot be modified.
- HDFS is suitable for applications that have large data sets, sequential access patterns, and high throughput requirements.
- HDFS is not suitable for applications that require low latency, random access, or multiple writers.