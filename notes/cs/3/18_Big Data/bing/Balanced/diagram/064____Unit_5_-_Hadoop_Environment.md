## Unit 5 - Hadoop Environment

- Hadoop is an open-source framework that allows distributed processing of large-scale data using clusters of commodity hardware.
- Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and Hadoop MapReduce.
- HDFS is a distributed file system that provides high-throughput access to data across multiple nodes in a cluster.
- HDFS follows a master-slave architecture, where a single NameNode manages the metadata of the file system, and multiple DataNodes store the actual data blocks.
- HDFS provides fault tolerance, scalability, and data locality by replicating data blocks across different DataNodes, and by placing data blocks close to the nodes that process them.
- Hadoop MapReduce is a programming model that enables parallel processing of large-scale data using a map and a reduce function.
- MapReduce follows a master-slave architecture, where a single JobTracker coordinates the execution of multiple jobs, and multiple TaskTrackers run the map and reduce tasks on the DataNodes.
- MapReduce provides fault tolerance, scalability, and load balancing by splitting the input data into fixed-size chunks called input splits, and by assigning map and reduce tasks to different TaskTrackers based on their availability and data locality.
- Hadoop also provides a set of common libraries and utilities that support the core components, such as Hadoop Common, Hadoop Configuration, and Hadoop Streaming.
- Hadoop also supports a number of subprojects that extend the functionality of the core components, such as Hadoop YARN, Hadoop Hive, Hadoop Pig, Hadoop HBase, and Hadoop Spark.