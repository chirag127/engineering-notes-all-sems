# Unit 5 - Spark’s Distributed Processing Model

- Spark is a distributed computing framework that allows processing large-scale data in parallel across multiple nodes in a cluster.
- Spark's distributed processing model is based on two main concepts: resilient distributed datasets (RDDs) and directed acyclic graphs (DAGs).
- RDDs are immutable collections of data that can be partitioned and distributed across the cluster. RDDs support two types of operations: transformations and actions.
- Transformations are lazy operations that create new RDDs from existing ones, such as map, filter, join, etc. Transformations are not executed until an action is performed on the RDD.
- Actions are eager operations that trigger the computation of the RDD and return a value to the driver program, such as count, collect, save, etc. Actions are the final steps of a Spark job.
- DAGs are graphs that represent the logical execution plan of a Spark job. Each node in the DAG is an RDD, and each edge is a transformation. Spark optimizes the DAG by applying various techniques, such as pipelining, caching, and shuffling.
- Spark executes the DAG in stages, where each stage consists of a series of tasks that can be performed in parallel on the same data partition. Spark assigns tasks to the available executors in the cluster, and monitors their progress and status.
- Spark handles failures and faults by using lineage information, which is the history of transformations that created an RDD. Spark can recompute the lost partitions of an RDD by using the lineage information, without requiring replication or checkpointing.