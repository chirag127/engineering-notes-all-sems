### Running Apache Spark with a Cluster Manager

- Apache Spark is a distributed processing framework that can run on multiple nodes in a cluster.
- A cluster manager is a service that allocates resources (such as CPU, memory, disk, network) to Spark applications and manages the lifecycle of Spark executors and drivers.
- Spark supports three types of cluster managers: Standalone, YARN, and Mesos.
- Standalone cluster manager is the simplest and native one that comes with Spark. It allows Spark to run on any machine without any external dependencies.
- YARN cluster manager is the resource manager in Hadoop 2 and 3. It allows Spark to run on top of Hadoop clusters and access Hadoop data sources (such as HDFS, Hive, HBase, etc.).
- Mesos cluster manager is a general and flexible one that can also run other types of applications (such as Hadoop MapReduce, service applications, etc.).
- To run Spark with a cluster manager, the following steps are required:
  - Install and configure the cluster manager on the cluster nodes.
  - Install and configure Spark on the cluster nodes or on a gateway machine that can access the cluster.
  - Set the `SPARK_MASTER` environment variable or the `--master` command-line option to the URL of the cluster manager (such as `spark://host:port`, `yarn`, or `mesos://host:port`).
  - Submit the Spark application using the `spark-submit` script or the Spark launcher API.
  - Monitor the Spark application using the Spark web UI or the cluster manager web UI.