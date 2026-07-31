### Spark on YARN

- **YARN** stands for **Yet Another Resource Negotiator** and is the resource management layer of Hadoop.
- **Apache Spark** can run on YARN, allowing it to take advantage of the resource management capabilities of YARN.
- When running Spark on YARN, the Spark driver runs inside an application master process, which is managed by YARN on the cluster.
- Spark executors are launched as containers by the application master, and YARN is responsible for allocating resources to these containers.
- Running Spark on YARN allows for dynamic allocation of cluster resources, as YARN can allocate more or fewer containers to a Spark application based on its resource needs.
- This allows for better utilization of cluster resources and can improve the performance of Spark applications.
- To run Spark on YARN, the `spark-submit` script must be used with the `--master yarn` option.
- Additional configuration options can be set to control the behavior of Spark on YARN, such as the amount of memory and CPU resources allocated to Spark executors.