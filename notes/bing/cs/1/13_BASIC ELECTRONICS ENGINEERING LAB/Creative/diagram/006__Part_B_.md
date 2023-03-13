## Part B:

The following diagram illustrates the basic architecture of a MapReduce program using ASCII characters:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Input Data   |    |    Input Data   |    |    Input Data   |
|                 |    |                 |    |                 |
+--------+--------+    +--------+--------+    +--------+--------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         v                      v                      v
+--------+--------+    +--------+--------+    +--------+--------+
|                 |    |                 |    |                 |
|      Mapper     |    |      Mapper     |    |      Mapper     |
|                 |    |                 |    |                 |
+--------+--------+    +--------+--------+    +--------+--------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         +----------+-----------+-----------+----------+
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    v                      v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|      Shuffle    |    |      Shuffle    |    |      Shuffle    |
|                 |    |                 |    |                 |
+--------+--------+    +--------+--------+    +--------+--------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         +----------+-----------+-----------+----------+
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    v                      v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|      Reduce     |    |      Reduce     |    |      Reduce     |
|                 |    |                 |    |                 |
+--------+--------+    +--------+--------+    +--------+--------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         +----------+-----------+-----------+----------+
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    v                      v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Output Data  |    |    Output Data  |    |    Output Data  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram shows the following steps:

- The input data is split into chunks and distributed across multiple nodes in the cluster.
- Each node runs a mapper function on its chunk of data, which transforms the data into key-value pairs and emits them to the shuffle phase.
- The shuffle phase partitions, sorts, and groups the key-value pairs by key and sends them to the reduce phase.
- Each node runs a reduce