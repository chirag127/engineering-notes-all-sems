Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes for the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data.

```markdown
# Unit 4 - HDFS (Hadoop Distributed File System)

## Introduction

- HDFS is a distributed file system that provides scalable, reliable, and fault-tolerant storage for large-scale data processing applications.
- HDFS is designed to run on clusters of commodity hardware and to handle failures gracefully.
- HDFS follows a master-slave architecture, where a single NameNode manages the namespace and metadata of the file system, and multiple DataNodes store the actual data blocks.
- HDFS supports a write-once-read-many model, where files are split into fixed-size blocks (typically 128 MB) and replicated across DataNodes for fault tolerance and parallel access.
- HDFS provides a Java-based API for clients to interact with the file system, as well as a web-based interface and a command-line interface.

## Features and Benefits of HDFS

- Scalability: HDFS can scale to store and process petabytes of data across thousands of nodes.
- Reliability: HDFS can tolerate node failures and network partitions by replicating data blocks across multiple DataNodes. It also performs checksums and self-healing to detect and correct data corruption.
- Performance: HDFS can leverage the locality of data by placing data blocks close to the computation nodes, reducing network traffic and improving throughput. It also supports parallel processing of data by multiple clients and applications.
- Cost-effectiveness: HDFS can run on commodity hardware, lowering the capital and operational costs of storage and processing.
- Compatibility: HDFS can integrate with various data sources and formats, such as structured, semi-structured, and unstructured data. It can also support various data processing frameworks, such as MapReduce, Spark, Hive, Pig, etc.

## Components and Architecture of HDFS

- NameNode: The NameNode is the master node that maintains the namespace and metadata of the file system, such as file names, permissions, locations, etc. It also manages the block allocation and replication across DataNodes. The NameNode is a single point of failure and a performance bottleneck, so it is usually configured with high availability and backup mechanisms.
- DataNode: The DataNode is the slave node that stores the data blocks of the files in the local disks. It also performs read and write operations on the blocks as instructed by the NameNode or the clients. It also periodically sends heartbeat and block report messages to the NameNode to report its status and block inventory.
- Secondary NameNode: The Secondary NameNode is an optional node that helps the NameNode by performing periodic checkpoints of the file system metadata. It merges the edits log (a record of changes made to the file system) with the fsimage (a snapshot of the file system) and creates a new fsimage. This reduces the recovery time of the NameNode in case of a failure.
- Client: The Client is the node that accesses the file system through the HDFS API. It interacts with the NameNode to obtain the metadata and locations of the data blocks, and then directly communicates with the DataNodes to read or write the data blocks. It also performs some tasks on behalf of the NameNode, such as block replication and checksum verification.
```