### Spark’s Own Cluster Manager

- Spark’s own cluster manager is also known as **standalone mode** .
- It is a simple cluster manager that is included with Spark and makes it easy to set up a cluster that Spark itself manages .
- It can run on Linux, Windows, or Mac OSX.
- It is often the simplest way to run Spark applications in a clustered environment.
- It supports pluggable cluster management, meaning that the SparkContext can connect to different types of cluster managers (such as YARN, Mesos, or Kubernetes) that allocate resources across applications.
- The standalone mode has a master node and worker nodes that communicate with each other.
- The master node is responsible for launching driver programs and executor processes on the worker nodes, and for scheduling tasks among them.
- The worker nodes are responsible for running the tasks assigned by the master node and reporting their status.
- The standalone mode supports two types of deployment modes: **client mode** and **cluster mode**.
- In client mode, the driver program runs on the machine that launches the Spark application, and the executor processes run on the worker nodes.
- In cluster mode, the driver program runs on one of the worker nodes, and the executor processes run on the other worker nodes.
- The standalone mode supports high availability of the master node by using ZooKeeper to elect a leader among multiple masters.
- The standalone mode also supports dynamic resource allocation, meaning that Spark can scale the number of executor processes up and down based on the workload.