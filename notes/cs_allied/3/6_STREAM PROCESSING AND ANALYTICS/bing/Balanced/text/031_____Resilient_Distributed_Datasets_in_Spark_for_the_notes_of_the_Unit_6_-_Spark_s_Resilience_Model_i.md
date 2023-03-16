### Resilient Distributed Datasets in Spark

- Resilient Distributed Datasets (RDDs) are the fundamental data structure of Spark    .
- RDDs are immutable distributed collections of objects that can be operated on in parallel   .
- RDDs can contain any type of Python, Java, Scala, or user-defined objects, including classes .
- RDDs are divided into logical partitions, which may be computed on different nodes of the cluster    .
- RDDs are resilient, meaning they can recover from failures and errors by recomputing the lost partitions based on lineage information   .
- RDDs support two types of operations: transformations and actions  .
  - Transformations create a new RDD from an existing one, such as map, filter, join, etc  .
  - Actions return a value to the driver program or write data to an external storage system, such as count, collect, save, etc  .
- RDDs can be created in two ways: parallelizing an existing collection in the driver program, or referencing a dataset in an external storage system, such as a shared file system, HDFS, HBase, etc  .
- RDDs can be cached or persisted in memory or disk for faster reuse  .
- RDDs can be checkpointed to save their lineage information to a reliable storage system and truncate the dependency graph .
- RDDs can be controlled by specifying the number of partitions, the preferred locations of partitions, and the storage level .
- RDDs are the low-level API of Spark and provide more flexibility and control over the data processing . However, they are less expressive and less optimized than the higher-level APIs, such as DataFrames and Datasets .