A spark application is a distributed program that runs on a cluster of nodes. It consists of four main components: the driver, the executors, the cluster manager, and the worker nodes. The driver is the process that coordinates the execution of the application and communicates with the cluster manager. The executors are the processes that run the tasks assigned by the driver and store the data in memory or disk. The cluster manager is the service that allocates resources to the spark application and manages the worker nodes. The worker nodes are the machines that host the executors and provide the computing and storage resources.

The following diagram illustrates the basic architecture of a spark application using ASCII art:

```
+-----------------+         +-----------------+
|                 |         |                 |
|  Cluster        |         |  Cluster        |
|  Manager        |         |  Manager        |
|                 |         |                 |
+-----------------+         +-----------------+
       ^    ^                    ^    ^
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
+-----------------+         +-----------------+
|                 |         |                 |
|  Worker Node    |         |  Worker Node    |
|                 |         |                 |
+-----------------+         +-----------------+
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
+-----------------+         +-----------------+
|                 |         |                 |
|  Executor       |         |  Executor       |
|                 |         |                 |
+-----------------+         +-----------------+
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
+-----------------+         +-----------------+
|                 |         |                 |
|  Task           |         |  Task           |
|                 |         |                 |
+-----------------+         +-----------------+
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
       |    |                    |    |
+-----------------+         +-----------------+
|                 |         |                 |
|  Data           |         |  Data           |
|                 |         |                 |
+-----------------+         +-----------------+
```

The driver and the executors can run in different modes: local, standalone, Mesos, YARN, or Kubernetes. The cluster manager can be Spark's own standalone cluster manager, Mesos, YARN, or Kubernetes. The worker nodes can be physical machines, virtual machines, or containers. The data can be stored in memory, disk, or external sources such as HDFS, S3, or Cassandra.