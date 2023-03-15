## Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that handles large data sets running on commodity hardware. It is one of the major components of Apache Hadoop, the others being MapReduce and YARN.

### HDFS Architecture

HDFS has a master-slave architecture that consists of the following components:

- **NameNode**: The master node that manages the file system namespace and regulates access to files by clients. It also maintains the metadata of the file system, such as the file hierarchy, the locations of blocks, the replication factor, etc. There is only one active NameNode in a cluster, and it is a single point of failure.
- **DataNode**: The slave nodes that store and serve the data blocks of files. They also perform block operations such as creation, deletion, replication, etc. as instructed by the NameNode. There can be multiple DataNodes in a cluster, and each DataNode can store multiple blocks of different files.
- **Secondary NameNode**: An optional node that periodically merges the namespace image and the edit log of the NameNode to prevent the edit log from becoming too large. It also acts as a backup for the NameNode in case of failure. It is not a standby NameNode, and it does not serve client requests.
- **Client**: The node that accesses the file system and performs read and write operations. It interacts with the NameNode to get the metadata of the file system and the locations of the blocks, and then directly communicates with the DataNodes to transfer the data.

The following diagram illustrates the HDFS architecture:

![HDFS Architecture](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/images/hdfsarchitecture.png)

### HDFS Features

HDFS has the following features that make it suitable for storing and processing large-scale data:

- **Fault-tolerance**: HDFS can tolerate failures of nodes by replicating the data blocks across multiple DataNodes. The default replication factor is 3, which means each block is stored on three different DataNodes. The NameNode can detect the failure of a DataNode and initiate the replication of the missing blocks to maintain the desired replication factor. The Secondary NameNode can also help in recovering the NameNode in case of failure.
- **Scalability**: HDFS can scale to thousands of nodes and petabytes of data by adding more DataNodes to the cluster. The NameNode can handle millions of files and blocks by using efficient data structures and algorithms. The DataNodes can store multiple blocks of different files, and the blocks can be of different sizes depending on the configuration.
- **High-throughput**: HDFS can provide high-throughput access to data by using a streaming data access model. The data blocks are stored in a contiguous manner on the local disks of the DataNodes, and the clients can read and write the data in a sequential fashion. The network bandwidth is optimized by transferring the data directly between the clients and the DataNodes, without involving the NameNode.
- **Compatibility**: HDFS can run on various types of hardware and operating systems, as it is implemented in Java. It can also support different types of data formats, such as structured, semi-structured, or unstructured. It can also integrate with various data processing frameworks, such as MapReduce, Spark, Hive, etc.