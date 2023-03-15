Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of Resilient Distributed Databases for the Unit 9 - Spark in the subject of Big Data.

### Resilient Distributed Databases

- Resilient Distributed Databases (RDDs) are the primary data structure in Spark   .
- RDDs are immutable distributed collections of objects    that can be operated on in parallel.
- RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes .
- Each dataset in RDD is divided into logical partitions, which may be computed on different nodes of the cluster   .
- RDDs are reliable and memory-efficient when it comes to parallel processing .
- RDDs are fault-tolerant, meaning they can recover from failures and errors   .
- RDDs support two types of operations: transformations and actions .
  - Transformations create a new RDD from an existing one, such as map, filter, join, etc .
  - Actions return a value to the driver program or write data to an external storage system, such as count, collect, save, etc .
- RDDs can be created from various sources, such as external files, parallelized collections, or existing RDDs .
- RDDs can be cached or persisted in memory or disk for faster access   .
- RDDs can be manipulated using a low-level API that offers fine-grained control over the data partitioning and distribution .
