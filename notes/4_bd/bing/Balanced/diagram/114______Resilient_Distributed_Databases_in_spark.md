#### Resilient Distributed Databases in Spark

- Resilient Distributed Databases (RDDs) are the fundamental data structure of Spark   .
- RDDs are immutable distributed collections of objects that can be operated on in parallel    .
- Each dataset in RDD is divided into logical partitions, which may be computed on different nodes of the cluster   .
- RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes .
- RDDs are resilient, meaning they can recover from failures and errors by using a lineage graph that records how the dataset was constructed   .
- RDDs support two types of operations: transformations and actions   .
  - Transformations create a new RDD from an existing one, such as map, filter, join, etc   .
  - Actions return a value to the driver program or write data to an external storage system, such as count, collect, save, etc   .
- RDDs can be created from various sources, such as parallelizing an existing collection, reading from a file system, or applying a transformation to an existing RDD   .
- RDDs can be cached or persisted in memory or disk for faster reuse   .
- RDDs can be controlled by specifying the number of partitions and the preferred location of each partition (e.g., on the same node as a dataset it depends on) .
- RDDs offer a low-level API that gives users more control over the data distribution and computation  .