#### Spark on YARN

- Spark is a distributed computing framework that can run on various cluster managers, such as YARN, Mesos, Kubernetes, or standalone mode .
- YARN (Yet Another Resource Negotiator) is a cluster manager that is part of the Hadoop ecosystem and can manage the resources and scheduling of various applications running on a Hadoop cluster .
- Running Spark on YARN allows Spark applications to leverage the benefits of YARN, such as security, resource isolation, scalability, and dynamic resource allocation .
- Running Spark on YARN requires a binary distribution of Spark that is built with YARN support. Binary distributions can be downloaded from the downloads page of the project website  .
- There are two deploy modes that can be used to launch Spark applications on YARN: cluster mode and client mode .
  - In cluster mode, the Spark driver runs inside an application master process that is managed by YARN on the cluster, and the client can go away after initiating the application .
  - In client mode, the Spark driver runs on the client machine that submits the application, and the application master is only used for requesting resources from YARN .
- To run Spark on YARN, some configuration options need to be set, such as spark.master, spark.yarn.archive, spark.yarn.jars, spark.yarn.queue, etc  .
- To submit a Spark application to YARN, the spark-submit script can be used with the appropriate options, such as --master, --deploy-mode, --queue, --num-executors, --executor-cores, --executor-memory, etc  .
- To monitor and manage Spark applications on YARN, the YARN web UI and the Spark web UI can be used  .