## Unit 5 - Spark’s Distributed Processing Model

- Apache Spark is a general-purpose distributed data processing engine that can handle large-scale data analysis and machine learning tasks   .
- Spark provides high-level APIs in Java, Scala, Python and R, and an optimized engine that supports general execution graphs .
- Spark also supports a rich set of higher-level tools including Spark SQL for SQL and structured data processing, MLlib for machine learning, GraphX for graph processing, and Spark Streaming for stream processing.
- Spark's distributed processing model is based on the concept of Resilient Distributed Datasets (RDDs), which are immutable collections of data that can be partitioned across multiple nodes in a cluster and operated on in parallel .
- RDDs can be created from various sources, such as files, databases, or existing collections in memory, and can be transformed using functional programming operations, such as map, filter, reduce, join, etc .
- RDDs can also be cached in memory or on disk for faster reuse, and can be checkpointed to external storage for fault tolerance .
- Spark's execution model is based on the concept of Directed Acyclic Graphs (DAGs), which are graphs of RDDs and their dependencies that represent the logical flow of a computation .
- Spark's scheduler divides a DAG into stages, which are groups of tasks that can be executed in parallel, and assigns them to available executors, which are processes that run on the cluster nodes and perform the actual computation .
- Spark's performance is enhanced by several features, such as in-memory computation, lazy evaluation, pipelining, dynamic resource allocation, adaptive query execution, and code generation .
- Spark's scalability is achieved by its ability to run on various cluster managers, such as Hadoop YARN, Apache Mesos, Kubernetes, or its own standalone mode, and to interact with various data sources, such as HDFS, S3, Cassandra, Hive, Kafka, etc  .