 Here is the content in markdown format for Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment:

## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

- HDFS (Hadoop Distributed File System) is the primary storage system used by Hadoop applications. It is designed to store very large data sets reliably, and to stream those data sets at high bandwidth to user applications.
- HDFS has a master-slave architecture. The NameNode is the master server that manages the file system namespace and regulates access to files by clients. DataNodes are slave nodes that store the blocks and serve read/write requests from clients.
- HDFS provides high throughput access to application data and is suitable for applications that have large data sets. HDFS is designed to be deployed on low-cost hardware, and to provide extremely high aggregate bandwidth across the cluster.
- Some key characteristics & features of HDFS:
	- HDFS is designed for portability across various hardware platforms and operating systems.
	- HDFS is fault-tolerant, designed to be deployed on low-cost hardware.
	- HDFS is highly configurable and scales to handle very large data sets and high throughput access.
	- HDFS provides high throughput access to application data and is suitable for applications that have large data sets.
	- HDFS follows a master-slave architecture and has a NameNode and DataNodes.
	- HDFS uses racks & replicas for efficient storage.
	- HDFS has a file system namespace with files organized in a tree-like structure.
- Some advantages of using HDFS are:
	- Streaming access of data at high throughput rates.
	- Simple coherency model & high availability.
	- Scales to store very large data sets.
	- Fault tolerance due to replication of data blocks across clusters.
	- Streaming access of data makes it suitable for distributed processing of large data sets.
- Some disadvantages of using HDFS are:
	- Not suitable for low latency data access.
	- Limited number of files in a directory.
	- Suitable for large files, not suitable for a large number of small files.
	- Single client can't read & write simultaneously.