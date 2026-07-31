#### Anatomy of a Map Reduce job run

- A Map Reduce job is a unit of work that consists of a map function and a reduce function, applied to a set of input data.
- The map function takes a key-value pair as input and produces a list of intermediate key-value pairs as output. The intermediate keys and values can be of different types than the input keys and values.
- The reduce function takes an intermediate key and a list of values associated with that key as input and produces a list of final key-value pairs as output. The final keys and values can be of different types than the intermediate keys and values.
- A Map Reduce job run consists of the following phases:

  - Input: The input data is split into fixed-size chunks called input splits. Each input split is assigned to a map task, which runs the map function on the key-value pairs in the split.
  - Map: The map tasks process the input splits in parallel and emit intermediate key-value pairs to a distributed file system called HDFS (Hadoop Distributed File System). The intermediate key-value pairs are partitioned by a partitioner function based on the intermediate keys and sent to different reduce tasks.
  - Shuffle: The reduce tasks fetch the intermediate key-value pairs from HDFS and sort them by the intermediate keys. This phase is called shuffle because it involves transferring data across the network.
  - Reduce: The reduce tasks run the reduce function on the sorted intermediate key-value pairs and produce the final output key-value pairs. The output key-value pairs are written to HDFS or another output destination.
  - Output: The output data is the result of the Map Reduce job run. It can be consumed by other applications or stored for further analysis.

- The following diagram illustrates the anatomy of a Map Reduce job run:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Input split 1 +---->+  Map task 1    +---->+  Reduce task 1 |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
     |                                                  |
     |                                                  |
     |                                                  |
     |                                                  v
     |                                        +----------------+
     |                                        |                |
     +--------------------------------------->+  Output file 1 |
                                              |                |
+----------------+     +----------------+     +----------------+
|                |     |                |           ^
|  Input split 2 +---->+  Map task 2    +-----------+
|                |     |                |           |
+----------------+     +----------------+           |
     |                                              |
     |                                              |
     |                                              |
     |                                              v
     |                                        +----------------+
     |                                        |                |
     +--------------------------------------->+  Output file 2 |
                                              |                |
+----------------+     +----------------+     +----------------+
|                |     |                |           ^
|  Input split 3 +---->+  Map task 3    +-----------+
|                |     |                |           |
+----------------+     +----------------+           |
     |                                              |
     |                                              |
     |                                              |
     |                                              v
     |                                        +----------------+
     |                                        |                |
     +--------------------------------------->+  Output file 3 |
                                              |                |
+----------------+     +----------------+     +----------------+
|                |     |                |           ^
|  Input split 4 +---->+  Map task 4    +-----------+
|                |     |                |           |
+----------------+     +----------------+           |
     |                                              |
     |                                              |
     |                                              |
     |                                              v
     |                                        +----------------+
     |                                        |                |
     +--------------------------------------->+  Output file 4 |
                                              |                |
                                              +----------------+
```