# Resilient Distributed Datasets in Spark

- Resilient Distributed Datasets (RDDs) are the fundamental data structure of Spark    .
- RDDs are immutable distributed collections of objects that can be operated on in parallel    .
- RDDs can contain any type of Python, Java, Scala, or user-defined objects, including classes .
- RDDs are divided into logical partitions, which may be computed on different nodes of the cluster    .
- RDDs are resilient, meaning they can recover from failures and errors by recomputing the lost partitions based on lineage information   .
- RDDs support two types of operations: transformations and actions  .
  - Transformations create a new RDD from an existing one, such as map, filter, join, etc  .
  - Actions return a value to the driver program or write data to an external storage system, such as count, collect, save, etc  .
  - Transformations are lazy, meaning they are only executed when an action is triggered  .
  - Actions are eager, meaning they are executed immediately  .
- RDDs can be created in two ways: parallelizing an existing collection in the driver program, or referencing a dataset in an external storage system, such as a shared filesystem, HDFS, HBase, etc  .
- RDDs can be cached or persisted in memory or disk for faster access in subsequent operations  .
- RDDs can be checkpointed, meaning they can be saved to a reliable storage system to cut off the lineage dependency and reduce the cost of recomputation .
- RDDs can be partitioned, meaning they can be split into smaller subsets based on a partitioning function, such as hash partitioning or range partitioning .
- RDDs can be coalesced, meaning they can be merged into fewer partitions to reduce the overhead of shuffling data across the network .
- RDDs can be repartitioned, meaning they can be reshuffled into a different number of partitions to balance the workload or optimize the performance .
- RDDs can be broadcasted, meaning they can be sent to all the nodes in the cluster to avoid fetching them repeatedly from the driver program or the external storage system .
- RDDs can be accumulated, meaning they can be used to aggregate values from multiple partitions in a fault-tolerant way .