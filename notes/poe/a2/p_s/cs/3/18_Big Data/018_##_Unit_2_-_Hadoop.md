 Here is the content written in markdown format for the topic ## Unit 2 - Hadoop:

## Unit 2 - Hadoop

1. HDFS - Hadoop Distributed File System
- HDFS is the primary storage system used by Hadoop.
- It splits files into large blocks and distributes them across multiple nodes in a cluster.
- It provides fault tolerance by replicating the blocks across multiple nodes.
- It is designed for streaming access of large files.
- The blocks are typically 128MB to 256MB in size.
- The master node consists of a NameNode which manages the file system namespace and regulates access to files by clients.
- The slave nodes consist of DataNodes which store the blocks and serve read/write requests from the clients.

2. MapReduce
- MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a Hadoop cluster.
- It consists of two major tasks - Map and Reduce.
- The Map task performs filtration and sorting.
- The Reduce task performs summarization.
- The output of the Map task is input for the Reduce task.
- Hadoop handles all the scheduling, distributing the tasks, monitoring, and re-executing the failed tasks.

[Additional details, diagrams, examples, advantages, disadvantages, and applications can be added here for HDFS and MapReduce.]