# Spark’s Memory Usage

- Memory usage in Spark largely falls under one of two categories: **execution** and **storage**.
- Execution memory refers to that used for computation in shuffles, joins, sorts and aggregations, while storage memory refers to that used for caching and propagating internal data across the cluster.
- In Spark, execution and storage share a unified region (M) in the executor's heap memory.
- The size of M can be configured by setting `spark.executor.memory`.
- Spark also supports off-heap memory, which is allocated outside the JVM and is not subject to garbage collection.
- The size of off-heap memory can be configured by setting `spark.memory.offHeap.enabled` and `spark.memory.offHeap.size`.
- Spark uses a memory manager to allocate and evict memory for different purposes.
- There are two types of memory managers in Spark: **static** and **dynamic**.
- The static memory manager divides the memory region M into two fixed-size regions: one for execution and one for storage.
- The dynamic memory manager adjusts the size of the regions based on the workload and the amount of free memory.
- The dynamic memory manager is the default and recommended one for Spark.
- Spark also provides several techniques to optimize memory usage, such as tuning data structures, compressing data, spilling data to disk, and using memory-efficient serialization formats .
- Spark also offers a web UI that displays useful information about the application's memory usage, such as a summary of RDD sizes and memory usage, environmental information, and information about the running executors.
- Spark memory management is a key aspect of optimizing the performance and scalability of Spark applications.

: https://spark.apache.org/docs/latest/tuning.html
: https://medium.com/analytics-vidhya/spark-memory-management-583a16c1253f
: https://learn.microsoft.com/en-us/azure/hdinsight/spark/optimize-memory-usage
: https://spark.apache.org/docs/latest/monitoring.html
: https://aws.amazon.com/blogs/big-data/best-practices-for-successfully-managing-memory-for-apache-spark-applications-on-amazon-emr/