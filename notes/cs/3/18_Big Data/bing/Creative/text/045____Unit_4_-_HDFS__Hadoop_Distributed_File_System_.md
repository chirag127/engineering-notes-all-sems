## Unit 4 - HDFS (Hadoop Distributed File System)

- HDFS is a distributed file system that handles large data sets running on commodity hardware.
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN .
- HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware.
- HDFS employs a NameNode and DataNode architecture to implement a distributed file system that provides high-performance access to data across highly scalable Hadoop clusters.
- HDFS has the following features and benefits:
  - High throughput: HDFS supports high bandwidth streaming of data to and from the cluster, which is suitable for batch processing of large data sets.
  - High availability: HDFS replicates data blocks across multiple DataNodes to ensure data reliability and availability in case of node failures.
  - Scalability: HDFS can scale up to thousands of nodes and petabytes of data by adding more hardware resources to the cluster.
  - Compatibility: HDFS can store any type of data, regardless of its structure or format, and can integrate with various data processing frameworks such as MapReduce, Spark, Hive, etc.
  - Security: HDFS supports authentication, authorization, encryption, and auditing of data access through Kerberos, ACLs, SSL, and HDFS Erasure Coding.