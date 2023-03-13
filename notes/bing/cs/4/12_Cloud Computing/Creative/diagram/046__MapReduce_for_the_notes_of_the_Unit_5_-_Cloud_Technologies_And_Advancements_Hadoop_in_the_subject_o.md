MapReduce is a programming model and a software framework for processing large amounts of data in parallel over a distributed cluster of nodes. It consists of two main stages: Map and Reduce. The Map stage applies a user-defined function to each input record and produces a set of intermediate key-value pairs. The Reduce stage aggregates the intermediate values associated with the same key and produces the final output.

The following diagram illustrates the basic architecture of a MapReduce job using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Input Data   |    |    Input Data   |    |    Input Data   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
         v                     v                     v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Mapper      |    |     Mapper      |    |     Mapper      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
         v                     v                     v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Partitioner   |    |   Partitioner   |    |   Partitioner   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +----------+----------+----------+----------+
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    v                     v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Reducer     |    |     Reducer     |    |     Reducer     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +----------+----------+----------+----------+
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    v                     v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Output Data  |    |    Output Data  |    |    Output Data  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```