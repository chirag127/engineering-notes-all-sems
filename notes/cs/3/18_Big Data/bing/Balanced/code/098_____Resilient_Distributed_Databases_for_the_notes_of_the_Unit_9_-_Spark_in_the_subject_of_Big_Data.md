Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of resilient distributed databases for the unit 9 - Spark in the subject of big data.

### Resilient Distributed Databases for the Unit 9 - Spark

- Resilient Distributed Datasets (RDDs) are the primary data structure in Spark   .
- RDDs are immutable distributed collections of objects that can be operated on in parallel    .
- Each dataset in RDD is divided into logical partitions, which may be computed on different nodes of the cluster    .
- RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes  .
- RDDs are reliable and memory-efficient when it comes to parallel processing  .
- By storing and processing data in RDDs, Spark speeds up MapReduce processes  .
- RDDs are fault-tolerant, meaning they can recover from failures and errors automatically  .
- RDDs support two types of operations: transformations and actions   .
- Transformations create a new RDD from an existing one, such as map, filter, join, etc   .
- Actions perform a computation on an RDD and return a result to the driver program, such as count, collect, save, etc   .
- RDDs can be created from external data sources, such as HDFS, S3, Cassandra, etc   .
- RDDs can also be created from existing collections in the driver program, such as lists, arrays, etc   .
- RDDs can be cached or persisted in memory or disk for faster access   .
- RDDs can be partitioned and repartitioned to optimize data locality and parallelism   .
- RDDs can be manipulated using functional programming concepts, such as lambda expressions, closures, etc   .
