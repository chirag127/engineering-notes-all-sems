### Spark’s Own Cluster Manager

- Spark’s own cluster manager is a built-in option for running Spark on a cluster of machines without any external dependencies.
- It is also known as the standalone cluster manager or the Spark master.
- It is the simplest way to deploy Spark applications, as it only requires a Java installation and some basic configuration.
- It supports both static and dynamic allocation of resources, meaning that Spark can either reserve a fixed amount of resources for each application or adjust the resources based on the workload.
- It also supports high availability, meaning that Spark can recover from failures of the master node or the worker nodes.
- To use Spark’s own cluster manager, the following steps are required:
  - Install Java and Spark on each node of the cluster.
  - Configure the `SPARK_MASTER_HOST` environment variable on the master node to point to its own hostname or IP address.
  - Start the master node by running `sbin/start-master.sh` on the master node.
  - Start the worker nodes by running `sbin/start-slave.sh <master-spark-URL>` on each worker node, where `<master-spark-URL>` is the URL of the master node, such as `spark://master:7077`.
  - Submit Spark applications to the cluster by using the `--master` option with the master node URL, such as `spark-submit --master spark://master:7077 <application-jar> <application-arguments>`.
  - Monitor the cluster status and the application progress by using the web UIs on the master node and the worker nodes, which are available at `http://<master-node>:8080` and `http://<worker-node>:8081` respectively.