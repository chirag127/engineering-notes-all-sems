#### Spark on YARN

- Spark on YARN is a mode of running Spark applications on a cluster of machines managed by YARN (Yet Another Resource Negotiator), which is a resource management framework for Hadoop.
- Spark on YARN requires a binary distribution of Spark which is built with YARN support. Binary distributions can be downloaded from the downloads page of the project website. To build Spark yourself, refer to Building Spark    .
- Spark on YARN supports two deployment modes: **client mode** and **cluster mode**.
  - In client mode, the Spark driver runs on the machine that launches the Spark application, and the Spark executors run on the YARN nodes. The driver communicates with the YARN ResourceManager to request resources for the executors, and communicates with the executors to coordinate the execution of tasks. The driver also exposes a web UI for monitoring the application.
  - In cluster mode, the Spark driver runs on a YARN node, and the Spark executors run on other YARN nodes. The driver is launched by the YARN ApplicationMaster, which is a process that runs on a YARN node and manages the lifecycle of the Spark application. The driver communicates with the YARN ResourceManager to request resources for the executors, and communicates with the executors to coordinate the execution of tasks. The driver also exposes a web UI for monitoring the application, which can be accessed through the YARN ResourceManager web UI.
- To run a Spark application on YARN, you need to set some configuration properties, such as `spark.master`, `spark.submit.deployMode`, `spark.yarn.archive` or `spark.yarn.jars`, etc. For details, please refer to Spark Properties .
- To submit a Spark application to YARN, you can use the `spark-submit` script, which is located in the `bin` directory of the Spark distribution. For example, to submit a Spark application in cluster mode, you can use the following command:

```bash
./bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master yarn \
  --deploy-mode cluster \
  --driver-memory 4g \
  --executor-memory 2g \
  --executor-cores 1 \
  --queue thequeue \
  /path/to/examples.jar \
  10
```

- The command above will launch a Spark application that runs the `SparkPi` example with 10 partitions. The application will run on the YARN cluster with the specified driver and executor memory, cores, and queue. The application jar file (`examples.jar`) needs to be accessible from the YARN nodes, either by using a shared file system (such as HDFS) or by uploading it to the distributed cache (by using `spark.yarn.archive` or `spark.yarn.jars`).
- To monitor the status of the Spark application, you can use the YARN ResourceManager web UI, which shows the list of running and completed applications, and the details of each application, such as the ApplicationMaster URL, the driver log, the allocated resources, etc. You can also use the Spark driver web UI, which shows the list of running and completed stages, tasks, executors, etc. The Spark driver web UI can be accessed through the ApplicationMaster URL, which is shown in the YARN ResourceManager web UI.
- To stop a Spark application on YARN, you can use the `yarn application -kill <applicationId>` command, where `<applicationId>` is the YARN application ID of the Spark application, which can be obtained from the YARN ResourceManager web UI or the `spark-submit` output.

- Some advantages of running Spark on YARN are:
  - You can leverage the existing YARN cluster and its features, such as security, resource management, high availability, etc.
  - You can run multiple Spark applications on the same YARN cluster, and share the resources among them.
  - You can use different versions of Spark on the same YARN cluster, by specifying different Spark binaries for each application.
  - You can dynamically adjust the number of executors for a Spark application, by using `spark.dynamicAllocation.enabled` and `spark.shuffle.service.enabled` properties.

- Some disadvantages of running Spark on YARN are:
  - You need to install and configure both Spark and YARN on the cluster machines, and ensure their compatibility and interoperability.
  - You need to tune the Spark and YARN configuration properties to optimize the performance and resource utilization of