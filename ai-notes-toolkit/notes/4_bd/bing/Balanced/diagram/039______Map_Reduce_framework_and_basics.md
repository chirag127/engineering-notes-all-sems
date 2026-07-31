MapReduce is a software framework and programming model used for processing huge amounts of data in a distributed and parallel fashion over a cluster of machines. MapReduce program work in two phases, namely, Map and Reduce. Map tasks deal with splitting and mapping of data while Reduce tasks shuffle and reduce the data   .

#### Map Reduce framework and basics

The MapReduce framework consists of a single master ResourceManager, one worker NodeManager per cluster-node, and MRAppMaster per application. The ResourceManager is responsible for allocating resources and scheduling tasks. The NodeManager is responsible for launching and monitoring the tasks on each node. The MRAppMaster is responsible for coordinating the execution of a MapReduce job.

The MapReduce framework operates as follows:

1. The input data is split into fixed-size pieces called input splits. Each input split is assigned to a map task.
2. The map task reads the input split and applies a user-defined map function to each record. The map function emits key-value pairs as intermediate output.
3. The intermediate output is partitioned, sorted, and shuffled across the reducers. Each reducer receives the intermediate output for a subset of keys.
4. The reduce task applies a user-defined reduce function to each group of values that share the same key. The reduce function emits final output key-value pairs.
5. The final output is written to the output files in the Hadoop File System (HDFS).

The following diagram illustrates the MapReduce framework and its basic components:

```
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|   Input File 1   +---->+   Input Split 1  +---->+     Map Task 1   |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
                                                        |
                                                        |
+------------------+     +------------------+           |   +------------------+
|                  |     |                  |           |   |                  |
|   Input File 2   +---->+   Input Split 2  +--------------->+     Map Task 2   |
|                  |     |                  |           |   |                  |
+------------------+     +------------------+           |   +------------------+
                                                        |
                                                        |
+------------------+     +------------------+           |   +------------------+
|                  |     |                  |           |   |                  |
|   Input File 3   +---->+   Input Split 3  +--------------->+     Map Task 3   |
|                  |     |                  |           |   |                  |
+------------------+     +------------------+           |   +------------------+
                                                        |
                                                        |
                                                        v
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Intermediate    +---->+  Partition 1     +---->+   Reduce Task 1  |
|  Output File 1   |     |                  |     |                  |
|                  |     +------------------+     +------------------+
+------------------+                                      
                                                       
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Intermediate    +---->+  Partition 2     +---->+   Reduce Task 2  |
|  Output File 2   |     |                  |     |                  |
|                  |     +------------------+     +------------------+
+------------------+                                      
                                                       
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Intermediate    +---->+  Partition 3     +---->+   Reduce Task 3  |
|  Output File 3   |     |                  |     |                  |
|                  |     +------------------+     +------------------+
+------------------+                                      
                                                        |
                                                        |
                                                        v
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|   Output File 1  <-----+   Output Split 1 <-----+   Reduce Task 1  |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
                                                       
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|   Output File 2  <-----+   Output Split 2 <-----+   Reduce Task 2  |
|                  |     |                  |     |                  |
+------------------+

```
