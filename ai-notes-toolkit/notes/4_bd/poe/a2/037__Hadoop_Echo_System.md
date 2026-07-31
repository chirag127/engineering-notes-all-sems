 Here is the formal content on Hadoop Echo System in markdown format without any emojis or external links:

#### Hadoop Echo System

1. Hadoop Common: The common utilities that support the other Hadoop modules. It includes:
- File System: The Hadoop Distributed File System (HDFS) that stores data on commodity machines, providing very high aggregate bandwidth across the cluster.
- Tools: Command line tools used to interact with HDFS and MapReduce.

2. Hadoop YARN: A framework for job scheduling and cluster resource management. It determines what runs on the cluster, allocates resources and monitors applications.

3. Hadoop MapReduce: A programming model for large scale data processing. Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key.

4. Hadoop Distributed File System (HDFS): A distributed file system that provides high-throughput access to application data. It splits files into large blocks and distributes them across nodes in a cluster. HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware.

5. Others: There are other modules in the Hadoop ecosystem such as Pig, Hive, HBase, Oozie, Zookeeper, etc. that are built on top of core Hadoop to solve specific problems.