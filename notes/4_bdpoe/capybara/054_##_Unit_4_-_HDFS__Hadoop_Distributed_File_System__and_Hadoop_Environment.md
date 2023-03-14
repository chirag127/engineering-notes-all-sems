## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

Hadoop is an open-source framework that allows for the distributed processing of large datasets across clusters of computers. Hadoop Distributed File System (HDFS) is a key component of the Hadoop ecosystem. In this unit, we will learn about HDFS and the Hadoop environment.

### HDFS

HDFS is a distributed file system that is designed to run on commodity hardware. It is highly fault-tolerant and can handle large datasets by dividing them into smaller blocks and distributing them across multiple nodes in a cluster. Here are some important concepts related to HDFS:

- **NameNode**: It is the central node in an HDFS cluster that manages the metadata of the files and directories stored in HDFS. It maintains the namespace, access control, and file system hierarchy.

- **DataNode**: It is the node in an HDFS cluster that stores the actual data. It receives instructions from the NameNode on how to store and retrieve data.

- **Block**: HDFS divides the data into smaller blocks of a fixed size (default is 128 MB). Each block is stored in multiple DataNodes for redundancy and fault tolerance.

- **Replication**: HDFS replicates each block multiple times (default is three) across different DataNodes to ensure data availability in case of node failures.

- **Read and Write Operations**: HDFS provides APIs for reading and writing data to/from the file system. These APIs are similar to those provided by the traditional file systems.

### Hadoop Environment

The Hadoop environment consists of several components that work together to process large datasets. Here are some important components of the Hadoop environment:

- **Hadoop Common**: It is a set of common libraries and utilities used by other Hadoop modules.

- **Hadoop Distributed File System (HDFS)**: It is a distributed file system that stores large datasets.

- **Hadoop YARN**: It is a framework for job scheduling and cluster resource management.

- **Hadoop MapReduce**: It is a programming model for processing large datasets in parallel across a Hadoop cluster.

- **Hadoop Ecosystem**: It is a collection of open-source projects that integrate with Hadoop to provide additional functionalities such as data ingestion, processing, and storage.

### Mnemonics and Learning Tricks

- To remember the key components of the Hadoop environment, you can use the acronym "CHYME". It stands for "Common, HDFS, YARN, MapReduce, and Ecosystem".
- To remember the key concepts related to HDFS, you can use the acronym "NDRRW". It stands for "NameNode, DataNode, Replication, Read Operations, and Write Operations".