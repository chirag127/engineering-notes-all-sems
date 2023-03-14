#### Spark on YARN

Spark on YARN is a mode of running Spark applications on a cluster managed by YARN (Yet Another Resource Negotiator), which is the resource management framework of Hadoop. Spark on YARN allows Spark to leverage the benefits of YARN, such as security, resource isolation, scalability, and cluster utilization.

Some of the main features and benefits of Spark on YARN are:

- Spark can run on YARN without any pre-installation or root access required. Spark can use the existing Hadoop configuration and security settings, and can access Hadoop data sources such as HDFS, HBase, or Hive.
- Spark can dynamically scale the number of executors (processes that run computations and store data) based on the workload and the available resources in the cluster. YARN can also enforce memory and CPU limits on the executors to ensure fair sharing and avoid resource starvation.
- Spark can run in two deploy modes on YARN: cluster mode and client mode. In cluster mode, the Spark driver (the process that coordinates the execution of a Spark application) runs inside an application master (a YARN container that manages the application lifecycle and resource allocation). In client mode, the driver runs on the client machine, and the application master is only used for requesting resources from YARN. Cluster mode is more suitable for production environments, as it allows the client to disconnect after launching the application. Client mode is more convenient for interactive sessions and debugging.
- Spark can integrate with the external shuffle service, which is a YARN auxiliary service that runs on each node and serves shuffle files (intermediate data used for grouping, aggregating, or joining data) to other executors. The external shuffle service can improve the performance and reliability of Spark applications, as it reduces the network traffic and the dependency on executor memory.
- Spark can launch applications with Apache Oozie, which is a workflow scheduler for Hadoop. Oozie can orchestrate multiple jobs, such as MapReduce, Pig, Hive, or Spark, and support complex branching and retry logic.
- Spark can use the Spark history server to replace the Spark web UI, which is the web interface that shows the details and status of Spark applications. The Spark web UI is only available when the application is running, and is lost after the application finishes or fails. The Spark history server can display the web UI of completed or failed applications, as long as the event logs are persisted in a storage system.

To run Spark on YARN, some of the prerequisites and steps are:

- Running Spark on YARN requires a binary distribution of Spark that is built with YARN support. Binary distributions can be downloaded from the [downloads page](https://spark.apache.org/downloads.html) of the project website. To build Spark yourself, refer to [Building Spark](https://spark.apache.org/docs/latest/building-spark.html).
- Ensure that `HADOOP_CONF_DIR` or `YARN_CONF_DIR` points to the directory that contains the client-side configuration files for the Hadoop cluster. These configs are used to write to HDFS and connect to the YARN ResourceManager. The configuration contained in this directory will be distributed to the YARN cluster so that all containers used by the application use the same configuration.
- Use the `spark-submit` script to launch Spark applications on YARN. The script supports several options and arguments to specify the application details, such as the main class, the application jar, the number of executors, the executor memory, the queue name, and the deploy mode. For example, to launch the SparkPi example in cluster mode:

```
$ ./bin/spark-submit --class org.apache.spark.examples.SparkPi \
    --master yarn \
    --deploy-mode cluster \
    --driver-memory 4g \
    --executor-memory 2g \
    --executor-cores 1 \
    --queue thequeue \
    examples/jars/spark-examples*.jar \
    10
```

- Optionally, configure the Spark properties and environment variables to customize the behavior and performance of Spark on YARN. For example, you can set `spark.yarn.maxAppAttempts` to control the maximum number of application attempts, or `SPARK_LOCAL_DIRS` to specify the local directories used by Spark. For a complete list of Spark properties and environment variables, refer to the [Spark Configuration](https://spark.apache.org/docs/latest/configuration.html) and the [Running Spark on YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) documentation.

Some of the mnemonics and learning tricks for Spark on YARN are:

- Remember the acronym YARN: Yet Another