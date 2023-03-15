#### Spark on YARN

- Spark is a distributed computing framework that can run on various cluster managers, such as YARN, Mesos, Kubernetes, or standalone mode .
- YARN (Yet Another Resource Negotiator) is a cluster manager that is part of the Apache Hadoop project. It is responsible for allocating resources and scheduling tasks on a Hadoop cluster .
- Running Spark on YARN allows users to leverage the benefits of both Spark and YARN, such as scalability, fault tolerance, security, and resource management .
- To run Spark on YARN, users need to have a binary distribution of Spark that is built with YARN support. Binary distributions can be downloaded from the downloads page of the project website .
- There are two deploy modes that can be used to launch Spark applications on YARN: cluster mode and client mode .
  - In cluster mode, the Spark driver runs inside an application master process that is managed by YARN on the cluster, and the client can go away after initiating the application .
  - In client mode, the Spark driver runs on the client machine that submits the application, and the application master is only used for requesting resources from YARN .
- To run Spark on YARN, users need to configure some Spark and YARN properties, such as spark.yarn.archive, spark.yarn.jars, spark.yarn.queue, spark.yarn.am.memory, etc  .
- Users can use spark-submit, spark-shell, or pyspark commands to launch Spark applications on YARN, with the --master option set to yarn and the --deploy-mode option set to either cluster or client .
- Users can monitor and manage their Spark applications on YARN using the YARN web UI, the Spark web UI, or the Spark history server .