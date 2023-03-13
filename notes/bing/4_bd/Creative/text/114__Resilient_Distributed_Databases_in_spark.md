#### Resilient Distributed Databases in spark

- Resilient Distributed Databases (RDDs) are the primary data structure in Spark   .
- RDDs are immutable distributed collections of objects that can be operated on in parallel    .
- Each dataset in RDD is divided into logical partitions, which may be computed on different nodes of the cluster  .
- RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes  .
- RDDs support two types of operations: transformations and actions .
  - Transformations create a new RDD from an existing one, such as map, filter, join, etc .
  - Actions return a value to the driver program or write data to an external storage system, such as count, collect, save, etc .
- RDDs are fault-tolerant, meaning they can recover from failures or errors by using lineage information   .
  - Lineage is the sequence of transformations that produced an RDD.
  - Spark can recompute the lost partitions of an RDD by using the lineage information.
- RDDs are memory-efficient, meaning they can cache or persist data in memory or disk for faster access   .
  - Spark can cache an RDD in memory across the nodes in the cluster.
  - Spark can persist an RDD on disk or a combination of memory and disk.
  - Spark can specify the storage level of an RDD, such as MEMORY_ONLY, DISK_ONLY, MEMORY_AND_DISK, etc.
- RDDs are lazy-evaluated, meaning they are only computed when an action is performed on them .
  - Spark can optimize the execution plan of an RDD by applying transformations lazily.
  - Spark can avoid unnecessary computations by applying transformations lazily.
- RDDs are the core of Spark's programming model and enable parallel and distributed processing of large-scale data  .