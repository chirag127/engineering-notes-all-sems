#### Resilient Distributed Databases in Spark

- Resilient Distributed Databases (RDDs) are the primary data structure in Spark   .
- RDDs are immutable distributed collections of objects that can be operated on in parallel  .
- RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes .
- RDDs are reliable and memory-efficient when it comes to parallel processing .
- RDDs support two types of operations: transformations and actions   .
- Transformations create a new RDD from an existing one, such as map, filter, join, etc   .
- Actions return a value to the driver program or write data to an external storage system, such as count, collect, save, etc   .
- RDDs are lazy evaluated, meaning that they are only computed when an action is performed on them   .
- RDDs can be created from any storage source supported by Hadoop, such as local file system, HDFS, Cassandra, HBase, Amazon S3, etc.
- RDDs can also be created from an existing collection in the driver program using the parallelize method  .
- RDDs can be cached or persisted in memory or disk for faster reuse   .
- RDDs can be checkpointed to a reliable storage system to recover from failures   .
- RDDs are resilient because they can be reconstructed from lineage information (the sequence of transformations that produced them) or from checkpoints   .
- RDDs are distributed because they are partitioned across nodes in the cluster and can be computed in parallel   .