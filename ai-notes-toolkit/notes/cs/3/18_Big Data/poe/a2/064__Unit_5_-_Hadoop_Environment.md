 Here is the content in markdown format with formal tone and without emojis:

## Unit 5 - Hadoop Environment

1. Hadoop Distributed File System (HDFS)
- HDFS is the primary storage system used by Hadoop.
- It splits files into large blocks and distributes them across multiple nodes in a cluster.
- It is designed to hold very large amounts of data (terabytes or even petabytes) and provide high-throughput access to this data.
- The master node consists of a NameNode, which manages the file system namespace and regulates access to files by clients.
- DataNodes store the blocks and serve read/write requests from clients.

2. MapReduce
- MapReduce is a programming model for processing large amounts of data in a distributed fashion.
- It consists of two major tasks - Map and Reduce.
- The Map task splits the input data into key-value pairs and the Reduce task merges the output of the Map tasks.
- Hadoop's implementation of MapReduce utilizes the HDFS and is responsible for scheduling tasks, monitoring them, and re-executing any failed tasks.

3. Hadoop YARN
- YARN (Yet Another Resource Negotiator) is the cluster resource management technology in Hadoop.
- It replaces the original JobTracker/TaskTracker system and separates the resource management and job scheduling/monitoring functions.
- The central ResourceManager service allocates resources across the cluster and assigns resources to applications.
- ApplicationMaster processes are responsible for negotiating resources from the ResourceManager and working with the NodeManager processes to execute and monitor the containers and their resource usage.

[No external links included as requested]