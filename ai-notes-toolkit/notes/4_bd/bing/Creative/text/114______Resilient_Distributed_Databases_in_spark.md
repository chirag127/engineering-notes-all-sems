#### Resilient Distributed Databases in Spark

- Resilient Distributed Databases (RDDs) are the fundamental data structure of Spark    .
- RDDs are immutable distributed collections of objects that can be operated on in parallel    .
- Each dataset in RDD is divided into logical partitions, which may be computed on different nodes of the cluster .
- RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes .
- RDDs are reliable and memory-efficient when it comes to parallel processing.
- RDDs are fault-tolerant, meaning they can recover from failures and errors by using a lineage graph that records how the dataset was constructed .
- RDDs offer two types of operations: transformations and actions.
  - Transformations create a new RDD from an existing one, such as map, filter, join, etc.
  - Actions return a value to the driver program or write data to an external storage system, such as count, collect, save, etc.
- RDDs can be created from various sources, such as parallelizing an existing collection, reading from a file system, or applying a transformation to an existing RDD.
- RDDs can be cached or persisted in memory or disk for faster access in future operations .
- RDDs can be controlled by two parameters: persistence level and partitioning scheme.
  - Persistence level determines how and where the RDD is stored, such as memory only, memory and disk, disk only, etc.
  - Partitioning scheme determines how the RDD is split into partitions, such as hash partitioning, range partitioning, custom partitioning, etc.