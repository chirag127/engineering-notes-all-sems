MapReduce is a programming model or pattern within the Hadoop framework that is used to access big data stored in the Hadoop File System (HDFS). It is a core component, integral to the functioning of the Hadoop framework. MapReduce facilitates concurrent processing by splitting petabytes of data into smaller chunks, and processing them in parallel on Hadoop commodity servers. In the end, it aggregates all the data from multiple servers to return a consolidated output back to the application.

MapReduce consists of two distinct tasks – Map and Reduce. The map function takes input data, pairs, processes, and produces another set of intermediate pairs as output. The reduce function takes the intermediate pairs, groups them by key, and performs some aggregation or computation on the values.

The MapReduce framework consists of a single master ResourceManager, one worker NodeManager per cluster-node, and MRAppMaster per application. The ResourceManager is responsible for allocating resources and scheduling tasks. The NodeManager is responsible for launching and monitoring the tasks on each node. The MRAppMaster is responsible for coordinating the tasks and communicating with the ResourceManager.

The following diagram illustrates the basic architecture of a MapReduce framework:

```
+-------------------+       +-------------------+
|                   |       |                   |
|    Application    |       |    Application    |
|                   |       |                   |
+-------------------+       +-------------------+
          |                         |
          |                         |
          v                         v
+-------------------+       +-------------------+
|                   |       |                   |
|    MRAppMaster    |       |    MRAppMaster    |
|                   |       |                   |
+-------------------+       +-------------------+
          |                         |
          |                         |
          v                         v
+-------------------+       +-------------------+
|                   |       |                   |
|   ResourceManager |       |   ResourceManager |
|                   |       |                   |
+-------------------+       +-------------------+
          |                         |
          |                         |
          v                         v
+-------------------+       +-------------------+
|                   |       |                   |
|    NodeManager    |       |    NodeManager    |
|                   |       |                   |
+-------------------+       +-------------------+
          |                         |
          |                         |
          v                         v
+-------------------+       +-------------------+
|                   |       |                   |
|      Mapper       |       |      Mapper       |
|                   |       |                   |
+-------------------+       +-------------------+
          |                         |
          |                         |
          v                         v
+-------------------+       +-------------------+
|                   |       |                   |
|      Reducer      |       |      Reducer      |
|                   |       |                   |
+-------------------+       +-------------------+
```