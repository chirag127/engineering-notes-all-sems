Spark on YARN is a way of running Spark applications on a Hadoop cluster that uses YARN as the resource manager. YARN is responsible for allocating resources such as CPU and memory to the Spark application, and launching and monitoring the Spark processes on the cluster nodes. Spark on YARN can run in two modes: cluster mode and client mode. In cluster mode, the Spark driver runs inside an application master process that is managed by YARN, and the client can disconnect after initiating the application. In client mode, the driver runs in the client process, and the application master is only used for requesting resources from YARN.

The following diagram illustrates the basic architecture of Spark on YARN in cluster mode:

```
+-----------------+         +-----------------+
|                 |         |                 |
|    Client       |         |    Resource     |
|                 +-------->+    Manager      |
|                 |         |                 |
+-----------------+         +-----------------+
                                  |
                                  |
                                  v
+-----------------+         +-----------------+
|                 |         |                 |
|    Node         |         |    Node         |
|    Manager      |         |    Manager      |
|                 |         |                 |
+-----------------+         +-----------------+
    |     |                     |     |
    |     |                     |     |
    v     v                     v     v
+---+-----+---+         +-------+-----+---+
|   |     |   |         |       |     |   |
|   | AM  |   |         |       |     |   |
|   |     |   |         |       |     |   |
+---+-----+---+         +-------+-----+---+
    |     |                     |     |
    |     |                     |     |
    v     v                     v     v
+---+-----+---+         +-------+-----+---+
|   |     |   |         |       |     |   |
|   | D   |   |         |       | E   |   |
|   |     |   |         |       |     |   |
+---+-----+---+         +-------+-----+---+

AM: Application Master
D: Driver
E: Executor
```