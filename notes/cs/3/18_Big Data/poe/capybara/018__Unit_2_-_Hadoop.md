## Unit 2 - Hadoop

Hadoop is an open-source software framework used for distributed storage and processing of big data sets. It provides a scalable, reliable and cost-effective solution for storing and processing large amounts of data.

### Hadoop Architecture

Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce. 

#### Hadoop Distributed File System (HDFS)

HDFS is the storage component of Hadoop. It is designed to store large datasets across a distributed environment. The HDFS architecture is based on a master-slave model, where the master node is called the NameNode and the slave nodes are called DataNodes. The NameNode manages the file system metadata, while the DataNodes store the actual data.

#### MapReduce

MapReduce is the processing component of Hadoop. It is a programming model used to process large datasets in a distributed environment. The MapReduce model consists of two main functions: Map and Reduce. The Map function processes the input data and produces intermediate results, which are then processed by the Reduce function to produce the final output.

### Hadoop Ecosystem

The Hadoop ecosystem consists of a wide range of tools and applications that are built on top of the Hadoop framework. Some of the popular tools in the Hadoop ecosystem are:

- Apache Pig: A high-level data processing tool that allows developers to write data transformation scripts in a simple language called Pig Latin.
- Apache Hive: A data warehouse system that allows users to query and analyze large datasets using SQL-like language called HiveQL.
- Apache Spark: A fast and general-purpose data processing engine that supports in-memory processing and can be used for batch processing, stream processing, and machine learning.
- Apache HBase: A NoSQL database that provides real-time read/write access to data stored in HDFS.
- Apache ZooKeeper: A distributed coordination service that provides synchronization, configuration management, and group services.

### Advantages of Hadoop

Hadoop provides several advantages over traditional data processing systems:

- Scalability: Hadoop allows organizations to store and process large datasets by distributing the workload across multiple nodes in a cluster.
- Reliability: Hadoop is designed to be fault-tolerant, which means that it can recover from hardware failures and other issues without losing data.
- Cost-effectiveness: Hadoop is an open-source software, which means that it is free to use and does not require expensive licenses or hardware.
- Flexibility: Hadoop supports a wide range of data sources and data formats, making it easy to integrate with existing systems and tools.

### Conclusion

Hadoop is a powerful and flexible framework that enables organizations to store and process large datasets in a distributed environment. It provides a scalable, reliable, and cost-effective solution for big data processing. With its wide range of tools and applications, Hadoop has become an essential component of modern data processing systems.