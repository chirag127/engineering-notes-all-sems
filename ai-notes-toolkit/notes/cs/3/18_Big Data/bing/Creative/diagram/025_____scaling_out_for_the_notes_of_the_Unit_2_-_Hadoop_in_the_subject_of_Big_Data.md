### Scaling Out for the Notes of the Unit 2 - Hadoop in the Subject of Big Data

- Scaling out is the process of adding more nodes to a cluster to increase its processing power and storage capacity, rather than upgrading the hardware of existing nodes (scaling up).
- Hadoop is a framework that enables scaling out of large data sets across clusters of commodity hardware, using simple programming models such as MapReduce and Spark.
- Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and Hadoop MapReduce.
- HDFS is a distributed file system that stores data in blocks of fixed size (typically 128 MB or 256 MB) across multiple nodes, and replicates each block for fault tolerance and availability.
- Hadoop MapReduce is a programming model that allows parallel processing of large data sets by dividing them into smaller chunks (called splits) and assigning them to different nodes (called mappers) for processing. The results of the mappers are then shuffled and sorted, and sent to other nodes (called reducers) for aggregation and final output.
- Hadoop also supports other tools and frameworks that can run on top of HDFS and MapReduce, such as Hive, Pig, HBase, Spark, etc. These tools provide higher-level abstractions and functionalities for data analysis, querying, manipulation, and storage.
- Scaling out with Hadoop has several advantages, such as:
  - Cost-effectiveness: Hadoop can run on commodity hardware, which is cheaper and easier to procure and maintain than specialized hardware.
  - Scalability: Hadoop can handle large and growing data sets by adding more nodes to the cluster, without affecting the performance or reliability of the system.
  - Fault tolerance: Hadoop can handle node failures and data loss by replicating data blocks across multiple nodes, and automatically reassigning tasks to other nodes in case of failures.
  - Flexibility: Hadoop can process various types of data, such as structured, semi-structured, or unstructured, and support various data formats, such as text, binary, XML, JSON, etc.
  - Parallelism: Hadoop can leverage the parallel processing power of multiple nodes to speed up the data analysis and processing tasks, and distribute the workload evenly across the cluster.