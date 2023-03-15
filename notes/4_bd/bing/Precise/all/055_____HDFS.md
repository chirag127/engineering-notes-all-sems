### HDFS

HDFS stands for Hadoop Distributed File System. It is a distributed file system designed to run on commodity hardware. It is a part of the Apache Hadoop ecosystem and is used to store and process large data sets.

- **Architecture:** HDFS follows a master/slave architecture. The master node is called the NameNode and the slave nodes are called DataNodes. The NameNode manages the file system namespace and regulates access to files by clients. The DataNodes store and retrieve data blocks when instructed by the NameNode.

- **Data Replication:** HDFS replicates data blocks across multiple DataNodes to ensure data availability and fault tolerance. The default replication factor is 3, meaning that each data block is stored on 3 different DataNodes.

- **Data Blocks:** HDFS stores files as a sequence of blocks. The default block size is 128 MB, but it can be configured by the user.

- **Rack Awareness:** HDFS is rack-aware, meaning that it takes into account the physical location of DataNodes when replicating data blocks. This helps to reduce network traffic and improve data locality.

- **Advantages:**
  - Scalability: HDFS can scale to store and process petabytes of data.
  - Fault Tolerance: HDFS replicates data blocks to ensure data availability in case of hardware failure.
  - Cost-Effective: HDFS is designed to run on commodity hardware, making it a cost-effective solution for storing and processing large data sets.

- **Disadvantages:**
  - Not suitable for small files: HDFS is not well-suited for storing a large number of small files, as each file is stored as a separate block, leading to inefficient use of storage space.
  - Not a POSIX file system: HDFS is not a fully POSIX-compliant file system, meaning that it does not support all the features and semantics of a traditional file system.

- **Mnemonics and Learning Tricks:**
  - Remember the acronym HDFS: Hadoop Distributed File System.
  - Remember the roles of the NameNode and DataNodes: NameNode manages the file system namespace, while DataNodes store and retrieve data blocks.
  - Remember the default replication factor and block size: 3 and 128 MB, respectively.
  - Remember that HDFS is rack-aware and takes into account the physical location of DataNodes when replicating data blocks.
