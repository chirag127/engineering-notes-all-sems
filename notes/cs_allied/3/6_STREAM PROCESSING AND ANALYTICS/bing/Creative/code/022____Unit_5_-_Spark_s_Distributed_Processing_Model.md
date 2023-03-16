## Unit 5 - Spark’s Distributed Processing Model

- Apache Spark is a general-purpose distributed data processing engine that can handle various big data scenarios  .
- Spark provides high-level APIs in Java, Scala, Python and R, and an optimized engine that supports general execution graphs .
- Spark also supports a rich set of higher-level tools including Spark SQL for SQL and structured data processing, MLlib for machine learning, GraphX for graph processing, and Spark Streaming for stream processing.
- Spark's distributed processing model is based on the concept of Resilient Distributed Datasets (RDDs), which are immutable collections of data that can be partitioned across multiple nodes in a cluster.
- RDDs can be created from various sources, such as files, databases, or parallelized collections in memory.
- RDDs support two types of operations: transformations and actions.
- Transformations are lazy operations that create new RDDs from existing ones, such as map, filter, join, etc.
- Actions are eager operations that trigger the computation of RDDs and return values to the driver program or write data to external storage, such as count, collect, save, etc.
- Spark uses a directed acyclic graph (DAG) to represent the dependencies between RDDs and optimize the execution plan.
- Spark also uses a master-slave architecture, where a driver program coordinates the execution of tasks on multiple executor processes that run on different nodes in the cluster.
- Spark can run on various cluster managers, such as Hadoop YARN, Apache Mesos, or its own standalone cluster manager.
- Spark can also leverage the distributed storage systems, such as Hadoop Distributed File System (HDFS), Amazon S3, or Apache Cassandra, to read and write data in parallel.