#### Resilient Distributed Databases in Spark

- Resilient Distributed Databases (RDDs) are the fundamental data structure of Spark     .
- RDDs are immutable distributed collections of objects that can be operated on in parallel   .
- Each dataset in RDD is divided into logical partitions, which may be computed on different nodes of the cluster   .
- RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes  .
- RDDs are fault-tolerant, meaning they can recover from failures and errors by using a lineage graph that tracks the dependencies between the partitions    .
- RDDs support two types of operations: transformations and actions  .
  - Transformations create a new RDD from an existing one by applying a function to each element or partition  .
  - Actions return a value or write data to an external storage system by performing a computation on an RDD  .
- RDDs can be created from various sources, such as files, parallelized collections, or other RDDs .
- RDDs can be cached or persisted in memory or disk to improve performance and reduce recomputation   .
- RDDs can be manipulated using a low-level API that offers a rich set of operators and functions .
- RDDs are the basis for higher-level abstractions in Spark, such as DataFrames, Datasets, and SQL.