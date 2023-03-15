# Unit 4 - HDFS (Hadoop Distributed File System)

## Introduction

- HDFS is a distributed file system that handles large data sets running on commodity hardware.
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN .
- HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware.
- HDFS provides high-performance access to data across highly scalable Hadoop clusters.

## Architecture

- HDFS employs a NameNode and DataNode architecture to implement a distributed file system.
- The NameNode is the master node that manages the file system namespace and regulates access to files by clients.
- The DataNodes are the slave nodes that store the actual data in the form of blocks.
- The NameNode and DataNodes communicate with each other using TCP/IP protocols.

## Features

- HDFS supports files that are very large, typically in the range of gigabytes to terabytes.
- HDFS is optimized for streaming data access, meaning that it is suitable for applications that need to read or write entire files sequentially.
- HDFS provides a command-line interface and a web-based user interface for users to interact with the file system.
- HDFS supports replication of data blocks across multiple DataNodes to ensure data availability and reliability.
- HDFS supports rack awareness, which means that it can place replicas of data blocks on different racks to improve network bandwidth and fault tolerance.