## Unit 11 - Hadoop Eco System Frameworks

Hadoop is a distributed framework that allows for the processing of large data sets across a cluster of computers. It provides a variety of tools and frameworks that enable data processing, storage, and analysis. In this unit, we will discuss some of the popular Hadoop ecosystem frameworks that are used for big data processing.

### 1. HDFS (Hadoop Distributed File System)
- HDFS is a distributed file system that provides reliable and scalable storage for large data sets.
- It allows for the storage and retrieval of data across a cluster of computers.
- HDFS is fault-tolerant, which means it can handle failures of individual nodes without losing any data.
- The data in HDFS is stored in blocks, which are replicated across multiple nodes in the cluster.

### 2. MapReduce
- MapReduce is a programming model used for processing large data sets in parallel.
- It breaks down the processing into two phases: Map and Reduce.
- The Map phase takes input data and converts it into a set of key-value pairs.
- The Reduce phase takes the output of the Map phase and combines the values, based on the keys, to produce a smaller set of output data.

### 3. Apache Pig
- Apache Pig is a high-level programming language used for processing and analyzing large data sets.
- It provides a simple and intuitive syntax for defining data processing tasks.
- Pig scripts are compiled into MapReduce jobs that can be executed on a Hadoop cluster.
- Pig supports a wide range of data sources and data types, including structured and unstructured data.

### 4. Apache Hive
- Apache Hive is a data warehousing framework used for querying and analyzing large data sets.
- It provides a SQL-like interface for querying data stored in Hadoop.
- Hive queries are compiled into MapReduce jobs that can be executed on a Hadoop cluster.
- Hive supports a variety of data sources and data formats, including structured and semi-structured data.

### 5. Apache Spark
- Apache Spark is a fast and general-purpose cluster computing system used for processing large data sets.
- It provides a unified engine for processing data in various formats, including batch processing, streaming, and machine learning.
- Spark is designed to be highly scalable and can process data in-memory, which makes it faster than traditional MapReduce.
- Spark provides APIs for working with various data sources, including HDFS, Hive, and Cassandra.

In conclusion, the Hadoop ecosystem provides a variety of tools and frameworks that enable large-scale data processing, storage, and analysis. Understanding these frameworks is essential for anyone working with big data and wanting to harness its power for their organization.