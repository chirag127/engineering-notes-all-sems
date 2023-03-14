#### Resilient Distributed Databases in spark

- Resilient Distributed Databases (RDDs) are the fundamental data structure of Spark .
- RDDs are immutable distributed collections of objects that can be operated on in parallel .
- RDDs can be created from external data sources, such as Hadoop file systems, or from existing Scala, Java, or Python collections in the driver program.
- RDDs support two types of operations: transformations and actions.
  - Transformations create a new RDD from an existing one, such as map, filter, or join.
  - Actions return a value to the driver program or write data to an external storage system, such as count, reduce, or saveAsTextFile.
- RDDs can be persisted in memory or disk for reuse across multiple operations.
- RDDs are fault-tolerant, meaning they can automatically recover from node failures or data loss .
- RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes .
- RDDs are divided into logical partitions, which may be computed on different nodes of the cluster .
- RDDs can be controlled by two parameters: the number of partitions and the storage level.
  - The number of partitions determines the degree of parallelism and the data distribution across the cluster.
  - The storage level determines how the RDD is stored in memory or disk, such as serialized, replicated, or compressed.