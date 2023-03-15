#### Resilient Distributed Databases in Spark

- Resilient Distributed Databases (RDDs) are the fundamental data structure of Spark   .
- RDDs are immutable distributed collections of objects that can be operated on in parallel    .
- Each dataset in RDD is divided into logical partitions, which may be computed on different nodes of the cluster   .
- RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes .
- RDDs are resilient, meaning they can recover from failures and errors by using a lineage graph that records how the dataset was constructed   .
- RDDs support two types of operations: transformations and actions   .
  - Transformations create a new RDD from an existing one, such as map, filter, join, etc   .
  - Actions return a value or write data to an external system, such as count, collect, save, etc   .
- RDDs can be created from various sources, such as parallelizing an existing collection, reading from a file system, or applying a transformation to an existing RDD   .
- RDDs can be cached or persisted in memory or disk for faster reuse   .
- RDDs can be partitioned based on a key or a custom function to optimize data locality and parallelism   .
- RDDs are the low-level API of Spark, and they are often used by higher-level APIs such as DataFrames, Datasets, and SQL .