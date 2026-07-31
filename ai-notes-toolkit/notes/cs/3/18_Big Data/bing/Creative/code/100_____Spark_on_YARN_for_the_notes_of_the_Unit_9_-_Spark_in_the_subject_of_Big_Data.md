# Spark on YARN

- Spark on YARN is a mode of running Spark applications on a cluster of nodes managed by YARN (Yet Another Resource Negotiator), which is a resource management framework for distributed systems.
- Spark on YARN requires a binary distribution of Spark which is built with YARN support. Binary distributions can be downloaded from the downloads page of the project website   .
- Spark on YARN supports two deploy modes: cluster mode and client mode.
  - In cluster mode, the Spark driver runs inside an application master process which is managed by YARN on the cluster, and the client can go away after initiating the application.
  - In client mode, the Spark driver runs in the client process, and the application master is only used for requesting resources from YARN.
- Spark on YARN can use two ways to ship the Spark runtime jars to the YARN cluster: spark.yarn.archive and spark.yarn.jars.
  - spark.yarn.archive is a compressed archive file (e.g. zip or tar.gz) that contains all the Spark runtime jars. It can be stored on HDFS or a local file system accessible by YARN.
  - spark.yarn.jars is a comma-separated list of jars that contain the Spark runtime jars. It can be a local file path, an HDFS path, or a HTTP/HTTPS/FTP URI.
- Spark on YARN can be configured by setting various properties in spark-defaults.conf, spark-env.sh, or the command line. Some of the common properties are   :
  - spark.yarn.appMasterEnv: a prefix for environment variables to be set on the application master process.
  - spark.yarn.executor.memoryOverhead: the amount of off-heap memory to be allocated per executor, in megabytes.
  - spark.yarn.maxAppAttempts: the maximum number of attempts to run the application before failing it.
  - spark.yarn.queue: the name of the YARN queue to which the application is submitted.
  - spark.yarn.submit.waitAppCompletion: whether to wait for the application to finish before exiting the launcher process.