Spark on YARN is a way of running Spark applications on a Hadoop cluster that uses YARN as the resource manager. Spark can run in two modes on YARN: cluster mode and client mode. In cluster mode, the Spark driver runs inside an application master process that is managed by YARN, and the client can go away after initiating the application. In client mode, the driver runs in the client process, and the application master is only used for requesting resources from YARN.

#### Spark on YARN

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Spark Driver  |     |  Spark Driver  |     |  Spark Driver  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  YARN Client  |     |  YARN Client  |     |  YARN Client  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  YARN Master  |     |  YARN Master  |     |  YARN Master  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  YARN Node    |     |  YARN Node    |     |  YARN Node    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Spark Worker |     |  Spark Worker |     |  Spark Worker |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The above diagram illustrates the basic architecture of Spark on YARN. The Spark driver can run either on the YARN client or on the YARN master, depending on the deploy mode. The Spark workers run on the YARN nodes, and communicate with the driver and the YARN master. The YARN master is responsible for allocating resources and scheduling tasks for the Spark application. The YARN client is the entry point for submitting the Spark application to the cluster.