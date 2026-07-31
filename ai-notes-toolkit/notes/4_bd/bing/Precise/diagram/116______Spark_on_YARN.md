#### Spark on YARN

- Apache Spark is a fast and general-purpose cluster computing system.
- It provides high-level APIs in Java, Scala, Python, and R, and an optimized engine that supports general computation graphs for data analysis.
- YARN (Yet Another Resource Negotiator) is the resource management layer of Hadoop.
- Spark can run on YARN, allowing it to take advantage of the resource management capabilities of YARN.
- When running Spark on YARN, each Spark executor runs as a YARN container.
- YARN allocates resources (CPU, memory, etc.) to the Spark application based on the resource requests specified in the Spark configuration.
- Spark on YARN can be run in two modes: client mode and cluster mode.
- In client mode, the Spark driver runs on the client machine, and the application master is only used for requesting resources from YARN.
- In cluster mode, the Spark driver runs inside an application master process, which is managed by YARN on the cluster.
- Running Spark on YARN allows for dynamic allocation of cluster resources, improving the efficiency of resource utilization.