MapReduce is a software framework and programming model used for processing huge amounts of data in a distributed and parallel fashion over a cluster of machines. MapReduce program work in two phases, namely, Map and Reduce. Map tasks deal with splitting and mapping of data while Reduce tasks shuffle and reduce the data  .

#### Map Reduce framework and basics
```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input Data   |     |   Output Data  |     |   Application  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      ^                      |
       |                      |                      |
       v                      |                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Map Task    |---->|  Shuffle Task  |---->|  Reduce Task   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   NodeManager  |     |   NodeManager  |     |   NodeManager  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   ResourceManager   |<---->|  MRAppMaster  |<---->|   ApplicationMaster  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```
The MapReduce framework consists of a single master ResourceManager, one worker NodeManager per cluster-node, and MRAppMaster per application (see YARN Architecture Guide). Minimally, applications specify the input/output locations and supply map and reduce functions via implementations of appropriate interfaces and/or abstract-classes.

The map function takes input pairs, processes, and produces another set of intermediate pairs as output. The shuffle task sorts and groups the intermediate pairs by key and sends them to the reduce task. The reduce task takes the intermediate pairs and performs some aggregation or computation on them to produce the final output pairs .