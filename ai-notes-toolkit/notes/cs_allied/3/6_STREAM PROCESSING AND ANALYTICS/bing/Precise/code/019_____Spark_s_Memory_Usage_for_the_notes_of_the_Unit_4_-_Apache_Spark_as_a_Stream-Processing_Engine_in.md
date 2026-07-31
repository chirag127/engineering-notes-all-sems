### Spark’s Memory Usage

Apache Spark is a stream-processing engine that relies heavily on cluster memory (RAM) as it performs parallel computing in memory across nodes to reduce the I/O and execution times of tasks. Memory usage in Spark largely falls under one of two categories: execution and storage.

1. **Execution memory** refers to that used for computation in shuffles, joins, sorts, and aggregations.
2. **Storage memory** is used for storing all of the cached data, broadcast variables are also stored here. Any persist option which includes MEMORY in it, Spark will store that data in this segment. Spark clears space for new cache requests by removing old cached objects based on the Least Recently Used (LRU) mechanism.

In Spark, execution and storage share a unified region (M). By default, Spark uses On-memory heap only. The On-heap memory area in the Executor can be roughly divided into the following four blocks: Storage Memory, which is mainly used to store Spark cache data, such as RDD cache, Unroll data, and so on.

Every SparkContext launches a Web UI, by default on port 4040, that displays useful information about the application. This includes a list of scheduler stages and tasks, a summary of RDD sizes and memory usage, environmental information, and information about the running executors.