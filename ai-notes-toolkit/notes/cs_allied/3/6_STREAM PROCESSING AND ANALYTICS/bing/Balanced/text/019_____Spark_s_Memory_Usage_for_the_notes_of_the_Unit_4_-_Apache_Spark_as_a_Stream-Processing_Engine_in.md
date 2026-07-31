### Spark’s Memory Usage

- Memory usage in Spark largely falls under one of two categories: execution and storage.
- Execution memory refers to that used for computation in shuffles, joins, sorts and aggregations, while storage memory refers to that used for caching and propagating internal data across the cluster.
- In Spark, execution and storage share a unified region (M) in the executor's on-heap memory .
- The size of M can be configured by setting `spark.executor.memory`.
- Spark also supports off-heap memory, which can be used for caching and execution.
- The size of off-heap memory can be configured by setting `spark.memory.offHeap.size`.
- Spark uses a memory manager to allocate and evict memory for execution and storage.
- Spark has two types of memory managers: static and unified.
- The static memory manager divides M into two regions: a fixed-size region for storage and the remaining region for execution.
- The unified memory manager dynamically allocates memory between execution and storage based on the current workload.
- The unified memory manager is the default and recommended memory manager for Spark.
- Spark also uses a mechanism called tungsten to optimize the memory layout and performance of binary data.
- Tungsten uses off-heap memory, cache-aware computation, and code generation to reduce memory usage and improve execution speed.
- Spark provides several techniques to optimize memory usage, such as tuning data structures, caching strategies, serialization formats, and memory fractions  .
- Spark also provides a web UI that displays useful information about the application's memory usage, such as a summary of RDD sizes and memory usage, environmental information, and information about the running executors.
- Spark's memory usage is a key aspect of optimizing the execution of Spark jobs, as it affects the performance, scalability, and reliability of the application .