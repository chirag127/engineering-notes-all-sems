# Unit 4 - HDFS (Hadoop Distributed File System)

## Introduction

- HDFS is a distributed file system that handles large data sets running on commodity hardware .
- It is used to scale a single Apache Hadoop cluster to hundreds (and even thousands) of nodes .
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN .
- HDFS is designed to be highly fault-tolerant, reliable, scalable, and efficient .

## Components and Architecture

- The design of HDFS is based on two types of nodes: a NameNode and multiple DataNodes .
- The NameNode is the master node that manages the metadata of the file system, such as the file names, directories, permissions, and locations of the file blocks on the DataNodes .
- The DataNodes are the slave nodes that store the actual data in the form of blocks, which are typically 64 MB or 128 MB in size .
- The NameNode and the DataNodes communicate with each other using heartbeats and block reports .
- The NameNode also maintains the replication factor of the blocks, which is the number of copies of each block stored on different DataNodes for fault tolerance .
- The default replication factor is 3, which means that each block is replicated on three DataNodes .
- The NameNode also handles the read and write requests from the clients, and directs them to the appropriate DataNodes .

## Features and Benefits

- HDFS provides several features and benefits for storing and processing large data sets, such as :

  - High availability: HDFS can tolerate the failure of nodes by replicating the data blocks on multiple DataNodes. If a DataNode fails, the NameNode can automatically redirect the read and write requests to another DataNode that has the same block. If a NameNode fails, a secondary NameNode can take over its role.
  - High throughput: HDFS can achieve high data transfer rates by splitting the data into blocks and distributing them across the cluster. This allows parallel processing of the data by multiple nodes. HDFS also supports data locality, which means that the computation is moved to the nodes where the data is stored, reducing the network overhead.
  - Scalability: HDFS can scale up to thousands of nodes and petabytes of data by adding more nodes to the cluster. HDFS can also scale down by removing nodes from the cluster. HDFS can handle any type of data, structured or unstructured, and any size of files, small or large.
  - Cost-effectiveness: HDFS can run on commodity hardware, which is low-cost and easily available. HDFS can also reduce the storage cost by compressing the data and using a lower replication factor for less critical data. HDFS can also reduce the processing cost by using MapReduce and YARN, which are efficient and parallel frameworks for data analysis.