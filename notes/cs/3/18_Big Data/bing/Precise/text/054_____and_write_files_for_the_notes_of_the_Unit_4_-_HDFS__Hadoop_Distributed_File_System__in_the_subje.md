### Unit 4 - HDFS (Hadoop Distributed File System)

Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It is a part of the Apache Hadoop project and is used to store and manage large data sets.

1. **Architecture:** HDFS has a master/slave architecture. The master node, called the NameNode, manages the file system namespace and regulates access to files by clients. The slave nodes, called DataNodes, store the data blocks of the files and perform block operations as instructed by the NameNode.

2. **Data Replication:** HDFS replicates data blocks for fault tolerance. The default replication factor is 3, meaning that each data block is stored on 3 different DataNodes. The replication factor can be configured by the user.

3. **Data Blocks:** HDFS stores files as a sequence of blocks. The default block size is 128 MB, but it can be configured by the user. Each block is stored on multiple DataNodes for fault tolerance.

4. **Data Integrity:** HDFS uses checksums to ensure data integrity. When a client writes data to HDFS, it computes a checksum for each block and sends it to the DataNode along with the data. The DataNode verifies the checksum before storing the data. When a client reads data from HDFS, it verifies the checksum to ensure that the data has not been corrupted.

5. **High Availability:** HDFS supports high availability through the use of redundant NameNodes. In this configuration, there are two NameNodes: an active NameNode and a standby NameNode. The active NameNode is responsible for all file system operations, while the standby NameNode maintains an up-to-date copy of the file system metadata. In the event of a failure of the active NameNode, the standby NameNode can take over its responsibilities.

6. **Federation:** HDFS supports federation, which allows multiple independent namespaces to coexist within a single HDFS cluster. Each namespace is managed by a separate NameNode, and the DataNodes can store data blocks for multiple namespaces.

7. **Accessing HDFS:** HDFS can be accessed through a variety of methods, including the Hadoop command line, the Hadoop API, and the Hadoop web user interface. Additionally, HDFS can be accessed through other tools and frameworks that support the Hadoop ecosystem, such as Apache Hive and Apache Pig.
