MapReduce is a programming model for processing large data sets in parallel on multiple nodes in a distributed system. It consists of two phases: map and reduce. The map phase takes an input data set and applies a user-defined function to each element, producing a set of intermediate key-value pairs. The reduce phase takes the intermediate key-value pairs and merges them according to the user-defined function, producing the final output.

Here is a detailed ASCII diagram for MapReduce:

### Map Reduce
```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input Data   |     |   Input Data   |     |   Input Data   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
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
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|     Mapper     |     |     Mapper     |     |     Mapper     |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
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
                   |                     |
                   |                     |
                   |                     |
                   |                     |
                   v                     v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|     Reducer    |     |     Reducer    |     |     Reducer    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
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
                   |                     |
                   |                     |
                   |                     |
                   |                     |
                   v                     v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Output Data  |     |   Output Data  |     |   Output Data  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```