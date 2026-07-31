### Spark’s Own Cluster Manager

- Spark’s own cluster manager is also known as **standalone mode** .
- It is a simple cluster manager that is included with Spark and makes it easy to set up a cluster that Spark itself manages .
- It can run on Linux, Windows, or Mac OSX.
- It is often the simplest way to run Spark applications in a clustered environment.
- It supports pluggable cluster management, meaning that the SparkContext can connect to different types of cluster managers (such as YARN, Mesos, or Kubernetes) that allocate resources across applications.
- The standalone mode has a master node and worker nodes that communicate with each other.
- The master node is responsible for launching driver programs and executor processes on the worker nodes, and for scheduling tasks among them.
- The worker nodes are responsible for running the tasks assigned by the master node and reporting their status.
- The standalone mode supports high availability by allowing multiple master nodes to be configured in a cluster, and using ZooKeeper to elect a leader among them.
- The standalone mode also supports dynamic resource allocation, which means that Spark can scale the number of executors up and down based on the workload.
- The standalone mode can be configured using the `spark-env.sh` file or the `spark-submit` command.
- The standalone mode can be monitored using the web UI that shows the status of the cluster, the applications, and the stages and tasks.