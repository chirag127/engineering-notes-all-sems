## Unit 5 - Spark’s Distributed Processing Model

1. Apache Spark is a distributed computing system that processes large amounts of data in parallel across a cluster of computers.
2. Spark's distributed processing model is based on the Resilient Distributed Dataset (RDD) abstraction, which is a fault-tolerant collection of data partitioned across the nodes of a cluster.
3. RDDs can be created from data stored in Hadoop Distributed File System (HDFS), local file systems, or other data sources.
4. Spark's processing model involves applying a series of transformations to the data in RDDs, such as map, filter, and reduce operations.
5. These transformations are executed in parallel across the cluster, with the results of each operation being stored in a new RDD.
6. Spark also supports a wide range of actions that can be performed on RDDs, such as count, collect, and save operations.
7. The results of these actions are returned to the driver program, which can then use them for further processing or output.
8. Spark's distributed processing model is designed to be fast, flexible, and easy to use, making it a popular choice for big data processing tasks.