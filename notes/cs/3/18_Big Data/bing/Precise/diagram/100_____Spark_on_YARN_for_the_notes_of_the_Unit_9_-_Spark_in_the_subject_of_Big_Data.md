### Spark on YARN

- **YARN** stands for **Yet Another Resource Negotiator** and is the resource management layer of Hadoop.
- **Spark** can run on YARN, allowing it to take advantage of the resource management capabilities of YARN.
- When running Spark on YARN, the Spark driver runs inside an application master process, which is managed by YARN on the cluster.
- The Spark executors run as containers in the YARN cluster, allowing them to be dynamically allocated and released based on the resource needs of the Spark application.
- Running Spark on YARN allows for dynamic allocation of cluster resources, improving the efficiency of resource utilization.
- To run Spark on YARN, the `spark-submit` script must be used with the `--master yarn` option.
- The `spark-submit` script takes care of setting up the necessary environment and configuration for running Spark on YARN.
- When running Spark on YARN, it is important to configure the memory and CPU resources for the Spark application appropriately, as these will affect the performance of the application.
- Spark on YARN can be used with both the client and cluster deployment modes, allowing for flexibility in how the Spark application is run.
- Running Spark on YARN allows for integration with other Hadoop ecosystem tools, such as Hive and HBase, as well as with other YARN applications.