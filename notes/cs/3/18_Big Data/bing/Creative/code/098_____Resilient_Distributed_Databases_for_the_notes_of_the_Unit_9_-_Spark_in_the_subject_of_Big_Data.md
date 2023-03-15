### Resilient Distributed Databases for the notes of the Unit 9 - Spark in the subject of Big Data

- Resilient Distributed Datasets (RDDs) are the primary data structure in Spark .
- RDDs are immutable distributed collections of objects that can be operated on in parallel     .
- RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes .
- RDDs are reliable and memory-efficient when it comes to parallel processing .
- RDDs are fault-tolerant, meaning they can recover from failures and errors  .
- RDDs are created by applying transformations on existing RDDs or by loading data from external sources.
- RDDs support two types of operations: transformations and actions.
  - Transformations create a new RDD from an existing one, such as map, filter, join, etc.
  - Actions return a value to the driver program or write data to an external storage system, such as count, collect, save, etc.
- RDDs can be cached or persisted in memory or disk for faster access  .
- RDDs can be partitioned across different nodes of the cluster to enable parallelism and load balancing  .
- RDDs can be created from two types of sources: parallelized collections and external datasets.
  - Parallelized collections are created by calling SparkContext.parallelize() on an existing collection in the driver program, such as a list or an array.
  - External datasets are created by loading data from a storage system, such as HDFS, S3, Cassandra, etc.