### Spark on YARN

- Spark on YARN is a mode of running Spark applications on a cluster of nodes managed by YARN (Yet Another Resource Negotiator), which is a resource manager for Hadoop.
- Spark on YARN requires a binary distribution of Spark which is built with YARN support. Binary distributions can be downloaded from the downloads page of the project website   .
- Spark on YARN supports two deploy modes: cluster mode and client mode.
  - In cluster mode, the Spark driver runs inside an application master process which is managed by YARN on the cluster, and the client can go away after initiating the application.
  - In client mode, the Spark driver runs in the client process, and the application master is only used for requesting resources from YARN.
- Spark on YARN can use either HDFS or a local file system as the source of Spark archives and configuration files. To make Spark runtime jars accessible from YARN side, you can specify `spark.yarn.archive` or `spark.yarn.jars` in `spark-defaults.conf`.
- Spark on YARN can also use dynamic allocation of executors, which allows Spark to request or release executors based on the workload. This feature requires an external shuffle service to be enabled on each node in the cluster.
- Spark on YARN can be configured using various properties in `spark-defaults.conf`, `spark-env.sh`, and `yarn-site.xml`. Some of the common properties are:
  - `spark.yarn.queue`: The name of the YARN queue to which the application is submitted.
  - `spark.yarn.am.memory`: The amount of memory to use for the application master.
  - `spark.yarn.am.cores`: The number of cores to use for the application master.
  - `spark.executor.instances`: The number of executors to launch for the application.
  - `spark.executor.memory`: The amount of memory to use per executor.
  - `spark.executor.cores`: The number of cores to use per executor.
  - `spark.yarn.maxAppAttempts`: The maximum number of attempts to submit the application before giving up.
  - `spark.yarn.am.attemptFailuresValidityInterval`: The interval after which a new application attempt will not be counted against the maximum number of attempts.
  - `spark.yarn.max.executor.failures`: The maximum number of executor failures before failing the application.
  - `spark.yarn.executor.failuresValidityInterval`: The interval after which a new executor failure will not be counted against the maximum number of failures.