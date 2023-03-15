## Unit 2 - Hadoop and Map Reduce

Here is an ASCII diagram that illustrates the basic architecture of Hadoop and MapReduce:

```
+----------------+      +----------------+
|   Input Data   |      |   Input Data   |
+-------+--------+      +-------+--------+
        |                       |
        v                       v
+-------+--------+      +-------+--------+
|     Mapper     |      |     Mapper     |
+-------+--------+      +-------+--------+
        |                       |
        v                       v
+-------+--------+      +-------+--------+
|   Shuffle and  |      |   Shuffle and  |
|     Sort       |      |     Sort       |
+-------+--------+      +-------+--------+
        |                       |
        v                       v
+-------+--------+      +-------+--------+
|     Reducer    |      |     Reducer    |
+-------+--------+      +-------+--------+
        |                       |
        v                       v
+----------------+      +----------------+
|   Output Data  |      |   Output Data  |
+----------------+      +----------------+
```

In this diagram, the input data is first split into multiple chunks and fed into the mappers. The mappers then process the data and generate intermediate key-value pairs. These key-value pairs are then shuffled and sorted before being fed into the reducers. The reducers then aggregate the data based on the keys and generate the final output.
