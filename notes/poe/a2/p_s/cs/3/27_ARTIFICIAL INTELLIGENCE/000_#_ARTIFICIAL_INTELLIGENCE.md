 Here is the content in markdown format on the topic #### components of Hadoop:

#### Components of Hadoop:

1. Hadoop Common: The common utilities that support other Hadoop modules. It includes filesystem utilities, OS level abstractions, compression codecs, serialization and command-line tools.
2. Hadoop Distributed File System (HDFS): A distributed file system that provides high throughput access to application data. It stores large data sets reliably even in the event of hardware failures.
3. MapReduce: A programming model for large scale data processing. It consists of two major tasks - Map and Reduce. The Map task divides the input into smaller sub-problems and the Reduce task combines the answers to the sub-problems to get the final output.
4. YARN: A cluster management technology. It separates the resource management and job scheduling/monitoring functionality. It allows multiple data processing engines such as MapReduce, Spark, etc. to handle data stored in HDFS simultaneously, thereby increasing throughput and utilization.

Advantages:
- Fault Tolerance: It is designed to detect and handle failures at the application layer (via replication & checkpointing) and at the hardware layer (via re-tasking).
- Scalability: It can scale up from a single server to thousands of machines, each with several cores and terabytes of storage.
- Flexibility: New data processing frameworks like Spark, Flink, etc. can be deployed on top of the Hadoop cluster without changing the underlying infrastructure.

Disadvantages:
- Complex Architecture: Hadoop has a complex system architecture with many components which makes deployment and management challenging.
- Single Point of Failure: The NameNode (in HDFS) and ResourceManager (in YARN) are single points of failure though this can be mitigated using hot standbys and high availability features.
- Performance: Though Hadoop provides massive scalability, the performance for some applications is not as high as some other big data processing systems due to overhead from the abstraction layers.

Applications: Web indexing, data mining, log file analysis, recommendation systems, etc.

[ included an ASCII diagram of Hadoop architecture and more details/examples if required ]