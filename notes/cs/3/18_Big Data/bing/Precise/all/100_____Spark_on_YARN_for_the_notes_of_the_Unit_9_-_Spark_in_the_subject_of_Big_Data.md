# Unit 9 - Spark

### Spark on YARN

- Apache Spark is a fast and general-purpose cluster computing system.
- It can run on several cluster managers, including YARN (Yet Another Resource Negotiator).
- YARN is a resource management layer of Hadoop, which allows multiple data processing engines to handle data stored in a single platform.
- Running Spark on YARN allows you to take advantage of the benefits of both Spark and Hadoop.
- Spark can access data stored in HDFS (Hadoop Distributed File System) and can use YARN to dynamically allocate resources.
- To run Spark on YARN, you need to build Spark with YARN support and configure it to use YARN as the cluster manager.
- You can then submit Spark applications to the YARN cluster using the `spark-submit` script.
- When running Spark on YARN, you can choose between two deployment modes: client mode and cluster mode.
- In client mode, the driver program runs on the client machine, while in cluster mode, the driver program runs on a node in the YARN cluster.
- Both modes have their advantages and disadvantages, and the choice depends on the specific use case.