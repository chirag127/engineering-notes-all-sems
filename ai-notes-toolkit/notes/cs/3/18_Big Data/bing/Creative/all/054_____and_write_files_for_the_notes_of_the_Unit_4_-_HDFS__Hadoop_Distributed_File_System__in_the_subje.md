# Unit 4 - HDFS (Hadoop Distributed File System)

## Introduction

- HDFS is a distributed file system that handles large data sets running on commodity hardware.
- It is one of the major components of Apache Hadoop, the others being MapReduce and YARN.
- It is designed to be highly fault-tolerant, scalable, and efficient.
- It has many similarities with existing distributed file systems, but also some significant differences.

## Architecture

- HDFS employs a master/slave architecture, where a single NameNode manages the namespace and metadata of the file system, and multiple DataNodes store and serve the actual data blocks.
- A file in HDFS is split into fixed-size blocks (typically 128 MB), and each block is replicated across a configurable number of DataNodes (typically 3) for fault tolerance.
- The NameNode maintains the mapping of files to blocks, and blocks to DataNodes, in memory and on disk. It also handles operations such as file creation, deletion, renaming, and replication.
- The DataNodes are responsible for storing, reading, and writing data blocks, as well as sending periodic heartbeats and block reports to the NameNode.
- The clients interact with the NameNode to obtain the location of the data blocks, and then directly communicate with the DataNodes to perform read and write operations.

## Features

- HDFS supports a write-once-read-many model, where a file can be written only by one client, and only once, in a sequential manner. This simplifies the consistency and concurrency issues, and enables high throughput for large data sets.
- HDFS provides a command-line interface and a Java API for accessing the file system. It also supports a web-based UI for monitoring and administration.
- HDFS supports a rack-aware replica placement policy, where the replicas of a block are distributed across different racks to improve availability and network bandwidth utilization.
- HDFS supports a checksum mechanism, where each data block is associated with a checksum that is verified by the DataNodes and the clients during read and write operations. This helps to detect and correct data corruption.
- HDFS supports a snapshot mechanism, where a point-in-time image of the file system can be created and restored. This helps to protect the data from accidental deletion or modification.
- HDFS supports a federation mechanism, where multiple NameNodes can coexist in the same cluster, each managing a separate namespace. This helps to scale the file system horizontally and improve the performance and reliability.