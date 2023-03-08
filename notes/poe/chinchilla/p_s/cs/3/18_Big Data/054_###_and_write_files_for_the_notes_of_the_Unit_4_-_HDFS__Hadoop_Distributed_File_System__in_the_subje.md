### Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that is designed to run on commodity hardware. It is the primary storage system used by Hadoop applications. In this unit, we will discuss the architecture of HDFS, its components, and their functionalities.

#### Architecture of HDFS

The architecture of HDFS consists of two main components: NameNode and DataNode. 

1. NameNode: It is the master node that stores the metadata of the file system, including the location of file blocks, permissions, and other attributes. NameNode manages the file system namespace and regulates access to files by clients. The NameNode is a single point of failure for the HDFS cluster.

2. DataNode: It is the slave node that stores the actual data blocks of files. DataNodes communicate with the NameNode to report the status of the blocks they store and to receive instructions for replication and deletion of blocks.

#### Components of HDFS

1. NameNode: It is the master node that manages the file system namespace and regulates access to files by clients.

2. DataNode: It is the slave node that stores the actual data blocks of files.

3. Secondary NameNode: It is a helper node that periodically merges the edits log with the fsimage file to create a new checkpoint, which can be used to restore the file system state in case of NameNode failure.

4. Client: It is an application that interacts with HDFS to read, write, and manage files.

#### Functionalities of HDFS Components

1. NameNode: It manages the file system namespace, allocates blocks to files, and maintains metadata about files and directories. It also performs block replication and deletion.

2. DataNode: It stores the actual data blocks of files and communicates with the NameNode to report the status of the blocks it stores.

3. Secondary NameNode: It helps to create a new checkpoint of the file system state.

4. Client: It interacts with HDFS to read, write, and manage files.

#### Advantages of HDFS

1. Scalability: HDFS can scale horizontally by adding more DataNodes to the cluster.

2. Fault-tolerant: HDFS replicates data blocks across multiple DataNodes to ensure high availability and fault tolerance.

3. Cost-effective: HDFS uses commodity hardware, which is less expensive than enterprise-grade storage systems.

4. High throughput: HDFS is optimized for streaming data access, which enables high throughput for large data sets.

#### Disadvantages of HDFS

1. Low latency: HDFS is not optimized for low-latency access, which makes it unsuitable for real-time data processing.

2. Single point of failure: The NameNode is a single point of failure for the HDFS cluster, which can cause downtime and data loss.

#### Examples of HDFS Applications

1. Data warehousing: HDFS is used as a storage system for data warehousing applications, which require high capacity and fault tolerance.

2. Big data analytics: HDFS is used as a storage system for big data analytics applications, which require the processing of large volumes of data.

3. Log processing: HDFS is used as a storage system for log processing applications, which require the processing of large volumes of log data.

#### Conclusion

HDFS is a scalable, fault-tolerant, and cost-effective distributed file system that is optimized for large data sets. It is widely used in big data applications for storage and processing of data. Understanding the architecture and components of HDFS is essential for building and managing Hadoop clusters.