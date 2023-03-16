### Spark's Memory Usage

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
- Spill can happen during shuffles, sorts, joins, aggregations, and caching.
- Spill can degrade the performance of Spark applications, so it is advisable to monitor the spill metrics and tune the memory parameters accordingly  .
- Spark also provides some options to tune the data structures and serialization formats used for memory management, such as `spark.serializer`, `spark.rdd.compress`, `spark.broadcast.compress`, and `spark.io.compression.codec`.
- These options can affect the memory footprint, CPU usage, and network traffic of Spark applications.