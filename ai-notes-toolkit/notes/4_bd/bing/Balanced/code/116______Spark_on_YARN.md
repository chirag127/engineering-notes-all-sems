#### Spark on YARN

- Spark is a distributed computing framework that can run on various cluster managers, such as YARN, Mesos, Kubernetes, or standalone mode .
- YARN is a resource manager that can allocate and manage resources (such as CPU, memory, disk, network) for applications running on a Hadoop cluster .
- Running Spark on YARN allows Spark applications to leverage the benefits of YARN, such as security, resource isolation, scalability, and fault tolerance .
- Running Spark on YARN requires a binary distribution of Spark which is built with YARN support. Binary distributions can be downloaded from the downloads page of the project website  .
- There are two deploy modes that can be used to launch Spark applications on YARN: cluster mode and client mode .
  - In cluster mode, the Spark driver runs inside an application master process which is managed by YARN on the cluster, and the client can go away after initiating the application .
  - In client mode, the Spark driver runs in the client machine, and the application master is only used for requesting resources from YARN .
- To run Spark on YARN, some configuration parameters need to be set, such as spark.master, spark.yarn.archive, spark.yarn.jars, spark.yarn.queue, etc  .
- To submit a Spark application to YARN, the spark-submit script can be used with the appropriate options, such as --master, --deploy-mode, --queue, --num-executors, --executor-cores, --executor-memory, etc  .
- To monitor and manage Spark applications on YARN, the YARN web UI and the Spark web UI can be used  .