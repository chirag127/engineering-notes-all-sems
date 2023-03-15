#### Spark on YARN

- Apache Spark is a fast and general-purpose cluster computing system.
- It provides high-level APIs in Java, Scala, Python, and R, and an optimized engine that supports general computation graphs for data analysis.
- YARN (Yet Another Resource Negotiator) is the resource management layer of Hadoop.
- Spark can run on YARN, allowing it to take advantage of the resource management capabilities of YARN.
- When running Spark on YARN, each Spark executor runs as a YARN container.
- YARN allocates resources (CPU, memory, etc.) to the Spark application based on the configured resource allocation policies.
- This allows multiple Spark applications to run concurrently on the same cluster, sharing resources fairly.
- To run Spark on YARN, the `spark-submit` script must be configured to use the `yarn` master.
- The `spark-submit` script takes care of uploading the Spark application JAR and any dependencies to the Hadoop Distributed File System (HDFS), and launching the application on the YARN cluster.
- Running Spark on YARN provides several benefits, including dynamic resource allocation, data locality, and integration with other Hadoop ecosystem tools.