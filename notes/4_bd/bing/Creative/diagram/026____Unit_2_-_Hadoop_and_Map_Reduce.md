## Unit 2 - Hadoop and Map Reduce

Hadoop and Map Reduce are part of the Apache Hadoop ecosystem, a framework that develops large-scale data processing using distributed and parallel algorithms. Hadoop uses a distributed file system called HDFS to store the data across multiple nodes in a cluster. Map Reduce is a processing layer that divides a large task into smaller subtasks and executes them on the nodes in parallel. The basic idea of Map Reduce is to apply a map function to each input data block, which transforms the data into intermediate key-value pairs, and then apply a reduce function to the intermediate key-value pairs, which aggregates the values based on the keys and produces the final output.

The following diagram shows the data flow of a Map Reduce job in Hadoop:

```
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |     Input       |     |     Output      |     |     Output      |
    |     Data        |     |     Data        |     |     Data        |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           v                       v                       v
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |     Input       |     |     Output      |     |     Output      |
    |     Splitter    |     |     Partitioner |     |     Merger      |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           v                       v                       v
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |     Mapper      |     |     Reducer     |     |     Output      |
    |                 |     |                 |     |     Writer      |
    +-----------------+     +-----------------+     +-----------------+
```

The input data is split into fixed-size blocks by the input splitter and assigned to the mapper nodes. Each mapper node applies the map function to the input block and produces intermediate key-value pairs. The intermediate key-value pairs are then partitioned by a partitioner based on the keys and sent to the reducer nodes. Each reducer node applies the reduce function to the intermediate key-value pairs and produces the final output. The output data is then merged by a merger and written to the output file by the output writer.

The Map Reduce framework handles the failures, load balancing, and data locality of the nodes in the cluster. The framework consists of two main components: the JobTracker and the TaskTracker. The JobTracker is the master node that coordinates the execution of the Map Reduce job. The TaskTracker is the worker node that runs the map and reduce tasks assigned by the JobTracker. The JobTracker and the TaskTracker communicate through a heartbeat mechanism to monitor the status of the nodes and the tasks.