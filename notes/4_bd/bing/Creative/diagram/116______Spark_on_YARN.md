#### Spark on YARN

- Spark is a distributed computing framework that can run on various cluster managers, such as YARN, Mesos, Kubernetes, or standalone mode .
- YARN (Yet Another Resource Negotiator) is a cluster manager that is part of the Hadoop ecosystem and can manage the resources and scheduling of various applications running on a Hadoop cluster .
- Running Spark on YARN allows users to leverage the benefits of both Spark and YARN, such as:
  - Scalability: YARN can scale up to thousands of nodes and Spark can handle large-scale data processing tasks .
  - Compatibility: Spark can access data stored in HDFS, Hive, HBase, or other Hadoop data sources, and can also run SQL, streaming, machine learning, or graph processing applications on YARN .
  - Security: YARN supports Kerberos authentication and authorization, and Spark can integrate with YARN security features .
  - Resource utilization: YARN can dynamically allocate and release resources to Spark applications based on their demand, and Spark can adjust the number of executors and cores per executor according to the workload .
- Running Spark on YARN requires a binary distribution of Spark which is built with YARN support. Binary distributions can be downloaded from the downloads page of the project website .
- There are two deploy modes that can be used to launch Spark applications on YARN:
  - In cluster mode, the Spark driver runs inside an application master process which is managed by YARN on the cluster, and the client can go away after initiating the application .
  - In client mode, the Spark driver runs on the client machine that submits the application, and the application master is only responsible for requesting resources from YARN and launching executors .
- To run Spark on YARN, users need to set some configuration parameters, such as:
  - spark.master: the master URL for the cluster, which should be yarn for YARN mode .
  - spark.submit.deployMode: the deploy mode for the application, which can be either cluster or client .
  - spark.yarn.archive or spark.yarn.jars: the location of the Spark runtime jars, which can be either a local file, an HDFS path, or a comma-separated list of Maven coordinates .
  - spark.yarn.appMasterEnv or spark.yarn.executorEnv: the environment variables to be set for the application master or the executors .
  - spark.yarn.am.memory or spark.yarn.am.cores: the amount of memory or cores to be allocated for the application master .
  - spark.executor.memory or spark.executor.cores: the amount of memory or cores to be allocated for each executor .
  - spark.dynamicAllocation.enabled: whether to enable dynamic allocation of executors, which requires an external shuffle service to be running on each node .
- To submit a Spark application to YARN, users can use the spark-submit script with the appropriate arguments, such as:
  - --master yarn: to specify the master URL as yarn .
  - --deploy-mode cluster or client: to specify the deploy mode as cluster or client .
  - --class: to specify the main class of the application .
  - --jars: to specify any additional jars required by the application .
  - --files: to specify any additional files required by the application .
  - --conf: to specify any additional configuration properties .
  - application-jar: to specify the application jar file .
  - application-arguments: to specify any arguments for the application .
- For example, to submit a Spark Pi application to YARN in cluster mode, users can run the following command:

  ```bash
  spark-submit --master yarn --deploy-mode cluster --class org.apache.spark.examples.S