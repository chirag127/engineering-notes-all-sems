#### Spark on YARN

- Spark is a distributed computing framework that can run on various cluster managers, such as YARN, Mesos, Kubernetes, or standalone mode .
- YARN (Yet Another Resource Negotiator) is a cluster manager that is part of the Hadoop ecosystem and can manage the resources and scheduling of various applications running on a Hadoop cluster .
- Running Spark on YARN allows Spark to leverage the benefits of YARN, such as security, resource isolation, scalability, and compatibility with other Hadoop components .
- Running Spark on YARN requires a binary distribution of Spark which is built with YARN support. Binary distributions can be downloaded from the downloads page of the project website. To build Spark yourself, refer to Building Spark  .
- There are two deploy modes that can be used to launch Spark applications on YARN: cluster mode and client mode .
  - In cluster mode, the Spark driver runs inside an application master process which is managed by YARN on the cluster, and the client can go away after initiating the application. This mode is suitable for production environments where the client machine may not be reliable or available .
  - In client mode, the Spark driver runs on the client machine that submits the application, and the application master is only used for requesting resources from YARN. This mode is suitable for development and testing environments where the client machine can be used to monitor and interact with the application .
- To run Spark on YARN, some configuration options need to be set, such as the number of executors, the amount of memory and cores per executor, the application name, the queue name, etc. These options can be set either through command-line arguments, configuration files, or SparkSession builder .
- To make Spark runtime jars accessible from YARN side, you can specify spark.yarn.archive or spark.yarn.jars options to point to a compressed archive or a directory of jars that contain the Spark dependencies. Alternatively, you can use the --archives or --jars options when submitting the application  .
- To run Spark applications on a Kerberos-enabled YARN cluster, you need to provide the principal and keytab for the Spark user, and enable the spark.yarn.principal and spark.yarn.keytab options. You also need to ensure that the Hadoop configuration files (such as core-site.xml and hdfs-site.xml) are available on the client machine and the Spark classpath .
- To monitor and debug Spark applications running on YARN, you can use the YARN web UI, the Spark web UI, the Spark history server, or the YARN logs. You can also use the spark.yarn.report.interval option to control how often the Spark driver reports its status to the YARN application master .

: Running Spark on YARN - Spark 2.4.7 Documentation - Apache Spark
: Running Spark on YARN - Spark 3.3.2 Documentation
: Running Spark on YARN - Spark 2.2.0 Documentation - Apache Spark
: Running Spark on YARN - Spark 3.3.2 Documentation - Apache Spark