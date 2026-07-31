# Spark's Memory Usage

- Memory usage in Spark largely falls under one of two categories: **execution** and **storage**.
- Execution memory refers to that used for computation in shuffles, joins, sorts and aggregations, while storage memory refers to that used for caching and propagating internal data across the cluster.
- In Spark, execution and storage share a unified region (M) in the executor's heap memory.
- The size of M can be configured by setting `spark.executor.memory`.
- Spark also supports off-heap memory allocation for caching and computation, which can be configured by setting `spark.memory.offHeap.enabled` to true and `spark.memory.offHeap.size` to the desired amount.
- Spark uses a memory manager to dynamically allocate and reclaim memory between execution and storage.
- The memory manager can be either **static** or **dynamic**, depending on the value of `spark.memory.useLegacyMode`.
- In static mode, Spark pre-allocates a fixed amount of memory for storage (`spark.storage.memoryFraction`) and execution (`spark.shuffle.memoryFraction`), and does not allow them to borrow from each other.
- In dynamic mode, Spark sets a minimum amount of memory for storage (`spark.memory.storageFraction`) and execution (`spark.memory.fraction`), and allows them to borrow from the free memory pool when needed.
- Spark also uses a mechanism called **spill** to free up memory when it is insufficient for execution or storage.
- Spill means writing some of the data to disk temporarily, and reading it back when needed.
- Spill can happen in two scenarios: when an RDD is cached with `MEMORY_ONLY` or `MEMORY_AND_DISK` level, or when a shuffle operation is performed.
- Spill can improve the performance of Spark applications by avoiding out-of-memory errors, but it can also introduce additional I/O overhead.
- Spark provides several metrics and tools to monitor and tune the memory usage of Spark applications, such as web UI, REST API, logs, and Dropwizard metrics.
- Some of the important memory-related metrics are: `jvm.heap.used`, `jvm.heap.committed`, `jvm.heap.max`, `jvm.pools.PS-Eden-Space.used`, `jvm.pools.PS-Old-Gen.used`, `jvm.pools.PS-Survivor-Space.used`, `executor.memoryUsed`, `executor.diskUsed`, `executor.totalShuffleRead`, `executor.totalShuffleWrite`, `executor.shuffleSpill.disk`, `executor.shuffleSpill.memory`.
- Some of the best practices for successfully managing memory for Spark applications are: choosing the right instance type, setting the right number of executors, cores, and memory, choosing the right serialization format, choosing the right persistence level, tuning the garbage collection, and using memory-optimized data structures.