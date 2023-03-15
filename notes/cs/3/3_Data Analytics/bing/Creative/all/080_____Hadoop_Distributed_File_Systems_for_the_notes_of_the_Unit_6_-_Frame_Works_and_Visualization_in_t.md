# Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications.
- HDFS is a distributed file system that provides high-throughput access to data across highly scalable Hadoop clusters  .
- HDFS splits files into large blocks and distributes them across nodes in a cluster. It then transfers packaged code into nodes to process the data in parallel using MapReduce programming model.
- HDFS is designed to handle large data sets running on commodity hardware, and to tolerate hardware failures.
- HDFS has a master-slave architecture, where one node (the NameNode) manages the file system namespace and regulates access to files by clients, and the other nodes (the DataNodes) store the actual data in blocks.
- HDFS provides a command-line interface and a Java API for users to interact with the file system.
- HDFS supports data replication, fault tolerance, data locality, scalability, and security features.