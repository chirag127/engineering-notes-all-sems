# Unit 4 - HDFS (Hadoop Distributed File System)

## Introduction

- HDFS is a distributed file system that handles large data sets running on commodity hardware.
- It is one of the major components of Apache Hadoop, the others being MapReduce and YARN .
- It is designed to be highly fault-tolerant, scalable, and efficient .

## Architecture

- HDFS employs a NameNode and DataNode architecture to implement a distributed file system.
- The NameNode is the master node that manages the file system namespace and regulates access to files by clients.
- The DataNodes are the worker nodes that store the actual data in the form of blocks.
- The NameNode and DataNodes communicate with each other using heartbeats and block reports.
- The NameNode maintains the metadata of the file system, such as the file names, directories, permissions, and locations of blocks.
- The DataNodes are responsible for serving read and write requests from clients, and performing block operations such as creation, deletion, and replication.

## Features

- HDFS supports files that are very large, typically in the range of gigabytes to terabytes.
- HDFS follows a write-once-read-many model, where a file once created, written, and closed, cannot be modified.
- HDFS provides high throughput access to data by streaming data in parallel from multiple DataNodes.
- HDFS can handle failures of nodes by replicating blocks across multiple DataNodes, and automatically recovering from lost or corrupted blocks.
- HDFS can scale up to thousands of nodes and store petabytes of data.
- HDFS allows users to specify the replication factor, block size, and checksum type for each file or directory.
- HDFS supports a command-line interface, a web-based interface, and a Java API for interacting with the file system.

## Summary

- HDFS is a distributed file system that is part of Apache Hadoop.
- HDFS has a NameNode and DataNode architecture, where the NameNode manages the file system namespace and the DataNodes store the data blocks.
- HDFS supports large files, high throughput, fault tolerance, scalability, and configurability.