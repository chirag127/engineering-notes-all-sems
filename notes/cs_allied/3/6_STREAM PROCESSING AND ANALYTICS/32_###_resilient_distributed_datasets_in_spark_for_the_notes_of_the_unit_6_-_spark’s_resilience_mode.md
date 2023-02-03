### Resilient Distributed Datasets in Spark for the notes of the Unit 6 - Spark’s Resilience Model in the subject of STREAM PROCESSING AND ANALYTICS

Resilient Distributed Datasets (RDDs) are a fundamental data structure in Apache Spark for distributed data processing. They provide a resilient, fault-tolerant model for processing large-scale data sets across a cluster of computers.

The key features of RDDs include:
1. Immutable: RDDs are immutable, meaning that once created, their contents cannot be changed.

2. Partitioned: RDDs are partitioned across multiple nodes in a cluster, allowing for parallel processing of data.

3. Resilience: RDDs provide a resilient, fault-tolerant model for processing data, allowing the system to recover from node failures and continue processing.

4. Lazy evaluation: RDDs use lazy evaluation, meaning that transformations on RDDs are not executed until an action is called. This allows Spark to optimize the processing pipeline and minimize the amount of data that needs to be processed.

5. Caching: RDDs can be cached in memory, allowing for faster access to frequently used data.

In summary, Resilient Distributed Datasets (RDDs) are a fundamental data structure in Apache Spark for distributed data processing. They provide an immutable, partitioned, resilient, lazy evaluated and cacheable model for processing large-scale data sets across a cluster of computers.
