## Unit 5 - Spark’s Distributed Processing Model

Apache Spark is a distributed processing system that can handle large amounts of data by distributing the processing across multiple nodes in a cluster. This allows for faster processing times and more efficient use of resources.

1. **Resilient Distributed Datasets (RDDs):** RDDs are the fundamental data structure in Spark. They are immutable, partitioned collections of objects that can be processed in parallel across a cluster of machines.
2. **Transformations and Actions:** Spark operations can be divided into two types: transformations and actions. Transformations create new RDDs from existing ones, while actions trigger computation and return a result to the driver program.
3. **Distributed Processing:** Spark distributes data and processing across a cluster of machines, allowing for faster processing times and more efficient use of resources. Data is partitioned and processed in parallel across multiple nodes.
4. **Fault Tolerance:** Spark is designed to be fault-tolerant, meaning that it can recover from failures of individual nodes in the cluster. This is achieved through the use of lineage information, which allows Spark to recompute lost data.
5. **Caching:** Spark allows users to cache data in memory, which can significantly speed up iterative algorithms and interactive data analysis.