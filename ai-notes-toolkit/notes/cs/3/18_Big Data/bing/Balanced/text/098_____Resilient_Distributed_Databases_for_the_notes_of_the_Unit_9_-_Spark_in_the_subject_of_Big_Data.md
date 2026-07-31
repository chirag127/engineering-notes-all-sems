### Resilient Distributed Databases for the notes of the Unit 9 - Spark in the subject of Big Data

- Resilient Distributed Datasets (RDDs) are the primary data structure in Spark    .
- RDDs are immutable distributed collections of objects that can be operated on in parallel  .
- RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes.
- RDDs are reliable and memory-efficient when it comes to parallel processing .
- RDDs are fault-tolerant, meaning they can recover from failures and errors .
- RDDs are divided into logical partitions, which may be computed on different nodes of the cluster  .
- RDDs support two types of operations: transformations and actions.
  - Transformations create a new RDD from an existing one, such as map, filter, join, etc .
  - Actions return a value to the driver program or write data to an external storage system, such as count, collect, save, etc .
- RDDs can be created from various sources, such as parallelizing an existing collection, reading from a file system, or applying a transformation to an existing RDD .
- RDDs can be cached or persisted in memory or on disk for faster access  .
- RDDs can be manipulated using a low-level API that offers fine-grained control over the data distribution and partitioning.