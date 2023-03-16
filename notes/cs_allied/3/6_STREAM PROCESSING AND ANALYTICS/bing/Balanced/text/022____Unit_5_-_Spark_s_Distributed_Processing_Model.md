## Unit 5 - Spark’s Distributed Processing Model

- Apache Spark is a general-purpose distributed data processing engine that can handle large-scale data analysis and machine learning tasks   .
- Spark provides high-level APIs in Java, Scala, Python and R, and an optimized engine that supports general execution graphs .
- Spark also supports a rich set of higher-level tools including Spark SQL for SQL and structured data processing, MLlib for machine learning, GraphX for graph processing, and Spark Streaming for stream processing.
- Spark's distributed processing model is based on the concept of Resilient Distributed Datasets (RDDs), which are immutable collections of data that can be partitioned across multiple nodes in a cluster and operated on in parallel .
- RDDs can be created from various sources, such as files, databases, or existing collections in memory, and can be transformed using functional programming operations, such as map, filter, reduce, join, etc .
- RDDs can also be cached in memory or on disk for faster access, and can be automatically recovered from failures or node losses .
- Spark's execution model is based on the concept of Directed Acyclic Graphs (DAGs), which are sequences of RDD transformations that form a logical computation plan .
- Spark's scheduler divides a DAG into stages, which are groups of tasks that can be executed in parallel, and assigns them to available executors, which are processes that run on the cluster nodes and perform the actual computation .
- Spark's performance is enhanced by various features, such as lazy evaluation, which delays the execution of transformations until an action (such as count, collect, save, etc) is performed, allowing for optimization and pipelining of operations .
- Spark also supports broadcast variables, which are read-only variables that can be distributed to all the executors, and accumulators, which are write-only variables that can be updated by the executors and aggregated by the driver .
- Spark also supports user-defined functions (UDFs), which are custom functions that can be applied to RDDs or Spark SQL dataframes, and user-defined aggregate functions (UDAFs), which are custom functions that can be used to aggregate data in Spark SQL .