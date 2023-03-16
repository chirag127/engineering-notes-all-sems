# Running Apache Spark with a Cluster Manager

- Apache Spark is a distributed computing framework that can run on different cluster managers, such as Standalone, YARN, Mesos, and Kubernetes.
- A cluster manager is a platform that provides resources and coordinates the execution of Spark applications across multiple nodes in a cluster.
- Depending on the cluster manager, Spark can run in two modes: local mode and cluster mode.
- In local mode, Spark runs on a single machine, using all the available cores. This mode is useful for testing and debugging purposes, but not for production use.
- In cluster mode, Spark runs on multiple machines, using a master node and worker nodes. The master node is responsible for scheduling tasks and managing resources, while the worker nodes are responsible for running the tasks and storing the data.
- Spark supports the following cluster managers:

  - Standalone: This is the simplest and easiest way to set up a Spark cluster. It is a built-in cluster manager that comes with Spark and can run on any platform. It does not depend on any external service or library. It allows users to configure the number of cores and memory for each node, and supports dynamic resource allocation and high availability.
  - YARN: This is the resource manager in Hadoop 2 and 3. It allows Spark to run alongside other Hadoop applications and share the same cluster resources. It supports security, resource isolation, and fine-grained resource management. It also allows users to access Hadoop data sources, such as HDFS, Hive, and HBase, from Spark.
  - Mesos: This is a general cluster manager that can run various types of applications, such as Hadoop, Spark, and Kubernetes. It supports fault tolerance, scalability, and resource sharing. It also allows users to run Spark on different frameworks, such as Marathon, Chronos, and Aurora.
  - Kubernetes: This is an open-source system for automating deployment, scaling, and management of containerized applications. It supports dynamic resource allocation, load balancing, and service discovery. It also allows users to run Spark on different cloud platforms, such as AWS, GCP, and Azure.

- To run Spark on a cluster manager, users need to specify the --master option in the spark-submit command, followed by the URL of the cluster manager. For example:

  - To run Spark on Standalone, use --master spark://<master-host>:<master-port>
  - To run Spark on YARN, use --master yarn
  - To run Spark on Mesos, use --master mesos://<mesos-master-host>:<mesos-master-port>
  - To run Spark on Kubernetes, use --master k8s://<kubernetes-api-server-host>:<kubernetes-api-server-port>

- Users can also specify other options, such as --executor-cores, --executor-memory, --driver-cores, and --driver-memory, to control the resources allocated to each node.