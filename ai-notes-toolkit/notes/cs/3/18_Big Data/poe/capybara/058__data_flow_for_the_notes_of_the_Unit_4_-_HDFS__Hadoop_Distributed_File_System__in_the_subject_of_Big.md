

### Data Flow for the Notes of Unit 4 - HDFS (Hadoop Distributed File System)

In this unit, we will study about HDFS, which is a distributed file system designed to store and manage large datasets reliably and efficiently. Let's understand the data flow of HDFS.

1. Data ingestion: The process of transferring data into the HDFS system is known as data ingestion. The data can be ingested from various sources like web servers, social media platforms, sensors, and log files.

2. Data storage: Once the data is ingested, it is stored in HDFS. HDFS stores data in a distributed manner across multiple nodes in a cluster. The data is divided into blocks of a fixed size, and each block is replicated across different nodes for fault tolerance.

3. Data processing: After the data is stored, it can be processed using various tools like MapReduce, Hive, and Pig. MapReduce is a programming model used to process large datasets in parallel across a cluster of nodes. Hive and Pig are higher-level tools used to query and analyze data in HDFS.

4. Data retrieval: Once the data is processed, it can be retrieved from HDFS using various tools like Hadoop File System Shell, Hadoop API, and Hadoop Streaming. Hadoop File System Shell is a command-line interface to interact with HDFS. Hadoop API is a programming interface used to interact with HDFS programmatically. Hadoop Streaming is a utility that allows us to create and run MapReduce jobs in any programming language.

5. Data backup: HDFS provides a backup mechanism to ensure data availability even in case of node failures. The data is replicated across different nodes, and any node failure can be handled by retrieving the data from the replicated blocks stored on other nodes.

In conclusion, HDFS provides a robust and scalable solution for storing and managing large datasets. Its distributed nature ensures high availability and fault tolerance, and its processing capabilities enable us to analyze and extract insights from the data. Understanding the data flow of HDFS is essential for effectively working with Hadoop and Big Data.