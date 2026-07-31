# Spark’s Own Cluster Manager

Spark’s own cluster manager is a simple and lightweight cluster manager that is included with Spark. It allows Spark to run on a cluster of machines without depending on any external resource manager. It is also known as the standalone cluster manager.

Some of the features and benefits of Spark’s own cluster manager are:

- It is easy to set up and configure. It only requires a list of hostnames or IP addresses of the machines that will act as master and worker nodes.
- It supports both static and dynamic resource allocation. Static allocation means that each worker node is assigned a fixed number of cores and memory at the start of the application. Dynamic allocation means that the cluster manager can scale up or down the number of executors based on the workload and available resources.
- It supports high availability of the master node. The master node is responsible for managing the cluster and assigning tasks to the worker nodes. If the master node fails, another master node can take over its role. This can be achieved by using ZooKeeper or by launching multiple master nodes in a single cluster.
- It supports running multiple applications concurrently on the same cluster. Each application gets its own set of executors and can run independently of other applications. The cluster manager ensures fair sharing of resources among the applications.
- It supports running Spark applications on Linux, Windows, or Mac OS X. It does not require any special installation or configuration of the operating system or the network.

Some of the limitations and drawbacks of Spark’s own cluster manager are:

- It does not support advanced features and functionalities of other cluster managers, such as security, authentication, authorization, quotas, isolation, etc.
- It does not integrate well with other frameworks and tools that run on the same cluster, such as Hadoop, Hive, HBase, etc.
- It does not provide a web UI or a REST API for monitoring and managing the cluster. It only provides a simple web UI for viewing the status of the applications and the executors.
- It does not support running Spark applications on containers, such as Docker or Kubernetes. It only supports running Spark applications on bare-metal machines or virtual machines.