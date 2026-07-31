# Spark on YARN

- Spark on YARN is a mode of running Spark applications on a cluster of nodes managed by YARN (Yet Another Resource Negotiator), which is a resource management framework for distributed systems.
- Spark on YARN requires a binary distribution of Spark which is built with YARN support. Binary distributions can be downloaded from the downloads page of the project website. To build Spark yourself, refer to Building Spark  .
- There are two variants of Spark binary distributions you can download. One is pre-built with Scala 2.12 and the other is pre-built with Scala 2.13. They are both compatible with Spark 3.3.2, but you need to choose the one that matches the Scala version of your application code.
- There are two deploy modes that can be used to launch Spark applications on YARN. In cluster mode, the Spark driver runs inside an application master process which is managed by YARN on the cluster, and the client can go away after initiating the application. In client mode, the Spark driver runs in the client process, and the application master is only used for requesting resources from YARN.
- To run Spark on YARN, you need to configure some environment variables and Spark properties. For example, you need to set HADOOP_CONF_DIR or YARN_CONF_DIR to point to the directory that contains the configuration files for your YARN cluster. You also need to set spark.master to yarn and specify the deploy mode with spark.submit.deployMode.
- To make Spark runtime jars accessible from YARN side, you can specify spark.yarn.archive or spark.yarn.jars. For details, see Spark Properties .
- To submit a Spark application to YARN, you can use spark-submit script with the following syntax:

```bash
./bin/spark-submit \
  --class <main-class> \
  --master yarn \
  --deploy-mode <deploy-mode> \
  --conf <key>=<value> \
  ... # other options
  <application-jar> \
  [application-arguments]
```

- For more information on running Spark on YARN, see the official documentation .