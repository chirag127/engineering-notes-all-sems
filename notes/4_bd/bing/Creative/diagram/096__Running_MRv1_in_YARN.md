#### Running MRv1 in YARN

The following diagram illustrates the basic architecture of a MRv1 application running on a YARN cluster:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Client Node    |       |  Resource       |       |  Node Manager   |
|                 |       |  Manager Node   |       |  Node           |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  yarn jar       |       |  ResourceManager|       |  NodeManager    |
|  command        |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Application    |       |  Application    |       |  Application    |
|  Master         |       |  Master         |       |  Master         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  MapReduce      |       |  MapReduce      |       |  MapReduce      |
|  Job            |       |  Job            |       |  Job            |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Map/Reduce     |       |  Map/Reduce     |       |  Map/Reduce     |
|  Tasks          |       |  Tasks          |       |  Tasks          |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The client node is where the user submits the MRv1 application using the yarn jar command. The Resource Manager node is where the ResourceManager daemon runs, which is responsible for allocating resources and scheduling applications on the cluster. The Node Manager node is where the NodeManager daemon runs, which is responsible for launching and monitoring containers on the worker node. The Application Master is a framework-specific library that negotiates resources from the ResourceManager and works with the NodeManagers to run and monitor the tasks. The MapReduce Job is the MRv1 application that consists of one or more map and reduce tasks. The Map/Reduce Tasks are the actual computation units that process the input data and produce the output data.

To monitor the MRv1 applications running on a YARN cluster, you can use the ResourceManager web interface, which shows the basic cluster metrics, list of applications, and nodes associated with the cluster. The web interface can be accessed at http://<ResourceManagerHost>:8088/. You can also use the command-line tools such as yarn application and yarn logs to get information about the applications and their logs.