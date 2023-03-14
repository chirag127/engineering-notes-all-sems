## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

- HDFS is a distributed file system that stores large amounts of data across multiple nodes in a cluster.
- HDFS provides high availability, fault tolerance, scalability, and reliability for data storage and processing.
- HDFS follows a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as DataNodes (slaves).
- The NameNode manages the metadata of the file system, such as the file names, directories, permissions, and locations of the data blocks.
- The DataNodes store the actual data blocks of the files in HDFS. Each data block is replicated across multiple DataNodes for fault tolerance.
- The default size of a data block in HDFS is 128 MB, which can be configured according to the needs of the application.
- HDFS supports a write-once-read-many model, where a file can be written only once by a single writer, and then read by multiple readers.
- HDFS provides a command-line interface and a web interface for interacting with the file system.
- HDFS also provides a Java API for application developers to access the file system programmatically.

- Hadoop Environment is the set of software components and configurations that are required to run Hadoop applications on a cluster.
- Hadoop Environment consists of the following components:
  - Hadoop Common: The common utilities and libraries that are used by other Hadoop modules.
  - Hadoop Distributed File System (HDFS): The distributed file system that stores the data for Hadoop applications.
  - Hadoop YARN: The resource management and scheduling framework that allocates the resources and executes the tasks on the cluster.
  - Hadoop MapReduce: The programming model and execution engine that processes the data in parallel using map and reduce functions.
  - Hadoop Ecosystem: The collection of tools and frameworks that extend the functionality of Hadoop, such as Hive, Pig, Spark, HBase, etc.