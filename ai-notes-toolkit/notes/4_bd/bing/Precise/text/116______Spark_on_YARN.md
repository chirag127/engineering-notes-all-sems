#### Spark on YARN

- Apache Spark is a fast and general-purpose cluster computing system.
- It provides high-level APIs in Java, Scala, Python and R, and an optimized engine that supports general execution graphs.
- YARN (Yet Another Resource Negotiator) is the resource management layer of Hadoop.
- Spark can run on YARN, which allows it to integrate with Hadoop environments and access Hadoop data.
- To run Spark on YARN, the following requirements must be met:
  - Spark must be built with YARN support.
  - The Hadoop configuration must be available on the Spark driver and executor machines.
  - The Hadoop configuration must specify the YARN resource manager address and scheduler address.
- When running Spark on YARN, the Spark driver runs in the client machine or in a YARN application master container.
- The Spark executors run in YARN containers.
- Spark on YARN supports dynamic allocation of cluster resources, which allows it to scale up and down based on the workload.
- Spark on YARN also supports running in client mode or cluster mode.
- In client mode, the Spark driver runs on the client machine, while in cluster mode, the driver runs in a YARN application master container.
- Running Spark on YARN provides several benefits, including integration with Hadoop data and security, and the ability to dynamically allocate resources based on the workload.