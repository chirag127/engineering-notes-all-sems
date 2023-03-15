#### Spark on YARN

- Spark is a distributed computing framework that can run on various cluster managers, such as YARN, Mesos, Kubernetes, or standalone mode .
- YARN is a resource manager that can allocate resources (such as CPU, memory, disk, network) to different applications running on a Hadoop cluster .
- Spark on YARN allows Spark applications to run on a YARN cluster, leveraging the advantages of both frameworks .
- Some of the benefits of running Spark on YARN are :
  - Dynamic resource allocation: Spark can request and release resources from YARN based on the workload, avoiding resource wastage or contention.
  - Security: Spark can integrate with YARN's security features, such as Kerberos authentication, encryption, and access control.
  - Compatibility: Spark can access data from HDFS, HBase, Hive, and other sources that are supported by YARN.
  - Scalability: Spark can scale up to thousands of nodes and handle large amounts of data using YARN's resource management capabilities.
- To run Spark on YARN, the following requirements must be met :
  - A binary distribution of Spark that is built with YARN support. This can be downloaded from the project website or built from source code.
  - A Hadoop cluster that is running YARN. The cluster should have the same version of Hadoop as the Spark distribution.
  - The environment variables HADOOP_CONF_DIR or YARN_CONF_DIR must point to the directory that contains the configuration files of the Hadoop cluster.
  - The Spark jars must be accessible from the YARN nodes. This can be achieved by using the spark.yarn.archive or spark.yarn.jars configuration properties.
- There are two deploy modes that can be used to launch Spark applications on YARN :
  - Cluster mode: The Spark driver runs inside an application master process that is managed by YARN on the cluster, and the client can go away after initiating the application. This mode is suitable for production environments, where the client machine may not be reliable or available.
  - Client mode: The Spark driver runs on the client machine that submits the application, and the application master is only responsible for requesting resources from YARN. This mode is suitable for development and testing environments, where the client machine can monitor and interact with the application.