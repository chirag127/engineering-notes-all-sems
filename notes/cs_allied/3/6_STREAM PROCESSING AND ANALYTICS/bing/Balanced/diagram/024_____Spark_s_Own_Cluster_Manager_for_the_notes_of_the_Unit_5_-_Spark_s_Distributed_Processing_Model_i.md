### Spark’s Own Cluster Manager

- Spark’s own cluster manager is also known as **standalone mode** .
- It is a simple cluster manager that is included with Spark and can run on Linux, Windows, or Mac OSX .
- It is often the simplest way to run Spark applications in a clustered environment.
- It allows Spark to manage its own cluster and allocate resources across applications.
- It supports both static and dynamic resource allocation.
- It does not support advanced features like high availability, security, or resource isolation.
- It requires a master node and one or more worker nodes to form a cluster .
- The master node runs a master daemon that coordinates the worker nodes and assigns tasks to them .
- The worker nodes run worker daemons that execute the tasks assigned by the master and report their status .
- The driver program (the main program that creates the SparkContext) can run either on the master node or on a separate node.
- The driver program communicates with the master daemon to request resources for its executors (the processes that run the Spark tasks).
- The master daemon assigns the executors to the worker nodes based on the available resources and the configuration parameters.
- The driver program then communicates directly with the executors to launch and monitor the Spark tasks.
- The following diagram illustrates the architecture of Spark’s own cluster manager:

```
+--------+     +--------+
| Driver |     | Master |
|Program |<--->| Daemon |
+--------+     +--------+
                  |
                  v
+--------+     +--------+     +--------+
|Worker  |     |Worker  |     |Worker  |
|Daemon  |     |Daemon  |     |Daemon  |
+--------+     +--------+     +--------+
|Executor|     |Executor|     |Executor|
+--------+     +--------+     +--------+
|  Task  |     |  Task  |     |  Task  |
+--------+     +--------+     +--------+
```