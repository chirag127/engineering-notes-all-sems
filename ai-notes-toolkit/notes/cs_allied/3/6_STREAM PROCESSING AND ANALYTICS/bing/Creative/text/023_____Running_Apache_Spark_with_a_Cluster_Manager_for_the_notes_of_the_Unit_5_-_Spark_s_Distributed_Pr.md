### Running Apache Spark with a Cluster Manager

- Apache Spark can run on different cluster managers that provide resources and scheduling for distributed applications.
- The cluster manager can be specified by the `--master` option when submitting a Spark application or when starting the Spark shell.
- The cluster manager can be one of the following types:
  - **Standalone** – a simple cluster manager included with Spark that makes it easy to set up a cluster.
  - **Apache Mesos** – a general cluster manager that can also run Hadoop MapReduce and service applications. (Deprecated)
  - **Hadoop YARN** – the resource manager in Hadoop 2 and 3.
  - **Kubernetes** – an open-source system for automating deployment, scaling, and management of containerized applications.
- Each cluster manager has its own way of setting up and configuring the cluster, as well as launching and monitoring the Spark applications.
- To access Hadoop data from Spark, the cluster manager needs to have access to the Hadoop configuration files and the HDFS URL (typically `hdfs://<namenode>:9000/path`).
- The cluster manager also needs to have the Spark binaries and libraries installed on the worker nodes, or use a shared file system to distribute them.
- The cluster manager allocates resources to the Spark applications based on the configuration parameters and the available resources in the cluster.
- The cluster manager also handles the failure and recovery of the worker nodes and the executor processes.
- The cluster manager communicates with the Spark driver and the Spark master, which are responsible for coordinating and executing the Spark tasks.
- The cluster manager can be configured to run Spark in different modes, such as:
  - **Local mode** – runs Spark on a single machine, using one thread per core. Useful for testing and debugging purposes.
  - **Client mode** – runs the driver on the machine that submits the application, and the executors on the worker nodes. Useful for interactive sessions and monitoring the application.
  - **Cluster mode** – runs both the driver and the executors on the worker nodes. Useful for production deployments and batch jobs.