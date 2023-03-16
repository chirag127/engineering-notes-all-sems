# Resilient Distributed Datasets in Spark

- Resilient Distributed Datasets (RDDs) are the fundamental data structure of Spark    .
- RDDs are immutable distributed collections of objects that can be operated on in parallel    .
- RDDs can contain any type of Python, Java, Scala, or user-defined objects, including user-defined classes    .
- RDDs are divided into logical partitions, which may be computed on different nodes of the cluster    .
- RDDs are fault-tolerant, meaning they can recover from failures and errors by using a lineage graph that tracks how each partition was derived from the original data source  .
- RDDs support two types of operations: transformations and actions  .
  - Transformations create a new RDD from an existing one, such as map, filter, join, etc. Transformations are lazy, meaning they are not executed until an action is performed on the RDD  .
  - Actions return a value to the driver program or write data to an external storage system, such as count, collect, save, etc. Actions trigger the execution of the transformations that precede them  .
- RDDs can be created in two ways: parallelizing an existing collection in the driver program, or referencing a dataset in an external storage system, such as a shared filesystem, HDFS, HBase, etc  .
- RDDs can be cached or persisted in memory or disk for faster access in subsequent operations  .
- RDDs can be manipulated using either low-level APIs that provide more control and flexibility, or high-level APIs that provide more abstraction and convenience, such as Spark SQL, DataFrames, and Datasets .