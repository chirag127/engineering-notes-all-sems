#### Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications.
- HDFS is a distributed file system that provides high-throughput access to large data sets across scalable Hadoop clusters   .
- HDFS employs a NameNode and DataNode architecture to implement the file system .
  - NameNode is the master node that manages the file system namespace and regulates access to files by clients.
  - DataNode is the slave node that stores the actual data in the form of blocks.
- HDFS splits files into large blocks (typically 64 MB or 128 MB) and distributes them across nodes in a cluster  .
- HDFS also transfers packaged code into nodes to process the data in parallel using MapReduce, a programming model for large-scale data processing .
- HDFS is designed to handle hardware failures, data replication, load balancing, and data locality .
- HDFS has a web-based user interface that allows users to browse the file system, view file contents, and perform administrative tasks.