# Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

## Benefits of HDFS:
1. Scalability: HDFS can easily scale to handle petabytes of data by simply adding more nodes to the cluster.
2. Fault Tolerance: HDFS is designed to be highly fault-tolerant, with data automatically replicated across multiple nodes to ensure data availability in the event of node failure.
3. Cost-Effective: HDFS is built on top of commodity hardware, making it a cost-effective solution for storing large amounts of data.
4. Data Locality: HDFS stores data on the nodes where it is being processed, reducing the need for data transfer and improving performance.
5. High Throughput: HDFS is optimized for high-throughput, batch processing of large data sets.

## Challenges of HDFS:
1. Limited Random Access: HDFS is not designed for low-latency, random access to data. It is optimized for high-throughput, batch processing of large data sets.
2. Complexity: HDFS can be complex to set up and manage, requiring specialized knowledge and expertise.
3. Single Point of Failure: In earlier versions of HDFS, the NameNode was a single point of failure. However, this has been addressed in more recent versions with the introduction of the Secondary NameNode and the ability to run multiple NameNodes in an active-active configuration.
4. Data Skew: Data skew can occur in HDFS if data is not evenly distributed across the nodes in the cluster, leading to some nodes being overworked while others are underutilized.
5. Small Files: HDFS is not well-suited for storing large numbers of small files, as each file, regardless of size, occupies a full block on the file system. This can lead to inefficient use of storage space and increased overhead in managing the file system metadata.