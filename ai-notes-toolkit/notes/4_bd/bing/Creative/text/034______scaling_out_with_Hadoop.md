#### Scaling out with Hadoop

- Hadoop is an open-source framework that allows distributed processing of large-scale data sets across clusters of computers using simple programming models.
- Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce.
- HDFS is a distributed file system that provides high-throughput access to data stored on multiple nodes in a cluster. HDFS replicates data blocks across different nodes to ensure fault tolerance and availability.
- MapReduce is a programming model that enables parallel processing of data on HDFS. MapReduce consists of two phases: map and reduce. The map phase applies a user-defined function to each input data block and produces intermediate key-value pairs. The reduce phase aggregates the intermediate values associated with the same key and produces the final output.
- Hadoop enables scaling out by adding more nodes to a cluster without changing the application code. Hadoop automatically distributes the data and the computation across the nodes and handles failures and load balancing.
- Hadoop can scale out to thousands of nodes and handle petabytes of data. Hadoop is suitable for applications that require batch processing of large and unstructured data, such as web log analysis, text mining, recommendation systems, etc.