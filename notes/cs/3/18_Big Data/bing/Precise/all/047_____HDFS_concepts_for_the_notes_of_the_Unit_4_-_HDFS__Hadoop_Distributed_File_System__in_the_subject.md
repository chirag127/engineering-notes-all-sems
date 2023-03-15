# HDFS Concepts

Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It is a part of the Apache Hadoop framework and is used to store and manage large data sets.

Here are some key concepts of HDFS:

1. **Blocks:** HDFS stores files as blocks of a fixed size, typically 128 MB. Each block is stored on multiple DataNodes for fault tolerance.

2. **NameNode:** The NameNode is the master node that manages the file system namespace and regulates access to files. It maintains the file system tree and the metadata for all the files and directories in the tree.

3. **DataNode:** DataNodes are the worker nodes that store the data blocks. They are responsible for serving read and write requests from the clients and performing block creation, deletion, and replication upon instruction from the NameNode.

4. **Rack Awareness:** HDFS is designed to be rack-aware, meaning that it takes into account the physical location of the DataNodes when making decisions about data placement and replication. This helps to improve data reliability, availability, and network bandwidth utilization.

5. **Replication:** HDFS replicates each block on multiple DataNodes to ensure data availability and fault tolerance. The default replication factor is 3, meaning that each block is stored on 3 different DataNodes.

6. **High Availability:** HDFS supports high availability through the use of an active and a standby NameNode. In the event of a failure of the active NameNode, the standby NameNode takes over its duties to ensure continued availability of the file system.

These are some of the key concepts of HDFS. It is a robust and scalable distributed file system that is widely used in big data applications.