A MapReduce job is a unit of work that consists of a map phase and a reduce phase. The map phase takes input data and transforms it into key-value pairs. The reduce phase takes the key-value pairs from the map phase and aggregates them by key. The following diagram illustrates the basic architecture of a MapReduce job run:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Input data   |      |   Map tasks    |      |   Reduce tasks |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Split 1      |----->|   Map task 1   |----->|   Reduce task 1|
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Split 2      |----->|   Map task 2   |----->|   Reduce task 2|
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Split 3      |----->|   Map task 3   |----->|   Reduce task 3|
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Split 4      |----->|   Map task 4   |----->|   Reduce task 4|
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The input data is split into small chunks called splits, which are distributed across the cluster. Each split is processed by a map task, which runs on a node where the split is located. The map task applies a user-defined function to each record in the split and emits key-value pairs as intermediate output. The intermediate output is partitioned by key and shuffled across the network to the nodes where the reduce tasks are running. Each reduce task receives a subset of the intermediate output that corresponds to a key range. The reduce task applies another user-defined function to the values associated with each key and produces the final output. The final output is written to the distributed file system.   
