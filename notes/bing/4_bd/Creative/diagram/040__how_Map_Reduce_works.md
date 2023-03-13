MapReduce is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster. It consists of two phases: Map and Reduce. The Map phase takes a set of data and converts it into another set of data, where individual elements are broken down into key-value pairs. The Reduce phase takes the output from the Map phase and merges those data tuples into a smaller set of tuples.

#### How MapReduce works

The following is a detailed ASCII diagram for how MapReduce works:

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
        |                     |                     |
        v                     v                     v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Intermediate  |     |  Intermediate  |     |  Intermediate  |
|    Output      |     |    Output      |     |    Output      |
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
        v                     v                     v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|     Shuffle    |     |     Shuffle    |     |     Shuffle    |
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
        v                     v                     v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|     Sort       |     |     Sort       |     |     Sort       |
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
        +-------------------> +-------------------> +
        |                     |                     |
        |                     |                     |
        v                     v                     v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|     Reduce     |     |     Reduce     |     |     Reduce     |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +-------------------> +-------------------> +
        |