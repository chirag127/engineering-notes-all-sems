 Here is the formal content in Markdown format without any emojis or external links:

## Unit 11 - Hadoop Eco System Frameworks

1. Hadoop Common: Hadoop Common module provides the common utilities and libraries that support other Hadoop modules. It includes following libraries and utilities:
- File System: Hadoop File System (HDFS) is a distributed file system that provides high throughput access to application data.
- Java Archives (JARs): Hadoop module provides utility JAR files for data processing applications.
- Scripts: Hadoop Common provides various shell scripts to start Hadoop daemons.

2. Hadoop Distributed File System (HDFS): HDFS is the primary storage system used by Hadoop applications. It is designed to store very large data sets reliably, and to stream those data sets at high bandwidth to user applications. It has following key features:
- Fault Tolerance: HDFS is designed to be fault-tolerant and reliable in storing very large data sets. It splits files into large blocks and stores multiple replicas of these blocks across nodes in a cluster.
- Scalability: HDFS has a master-slave architecture. The master is called NameNode and slaves are called DataNodes. This architecture allows HDFS to scale to very large clusters and store and process extremely large data sets.
- Data Movement: HDFS provides high throughput access to application data.

3. Hadoop YARN: Hadoop YARN is a cluster management technology for Hadoop. It provides a centralized system for scheduling and resource management. Key features of YARN are:
- Scalability: YARN has a modular design and is scalable to clusters of more than ten thousand nodes.
- Utilization: YARN optimizes utilization of cluster resources by scheduling applications based on resource availability.
- Multi-tenancy: YARN supports running multiple applications simultaneously to enable real-time or batch processing.

[Additional points and explanations can be added here in the same format]