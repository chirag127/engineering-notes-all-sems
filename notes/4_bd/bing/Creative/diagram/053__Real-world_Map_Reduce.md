MapReduce is a programming model and an associated implementation for processing and generating large data sets. Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key.

#### Real-world Map Reduce

The following diagram illustrates the basic architecture of a MapReduce system using ASCII art:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input Data   +---->+     Mapper     +---->+  Intermediate  |
|                |     |                |     |     Data       |
+----------------+     +----------------+     +----------------+
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
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input Data   +---->+     Mapper     +---->+  Intermediate  |
|                |     |                |     |     Data       |
+----------------+     +----------------+     +----------------+
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
       |                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input Data   +---->+     Mapper     +---->+  Intermediate  |
|                |     |                |     |     Data       |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input Data   +---->+     Mapper     +---->+  Intermediate  |
|                |     |                |     |     Data       |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input Data   +---->+     Mapper     +---->+  Intermediate  |
|                |     |                |     |     Data       |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input Data   +---->+     Mapper     +---->+  Intermediate  |
|                |     |                |     |     Data       |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input Data   +---->+     Mapper     +---->+  Intermediate  |
|                |     |                |     |     Data       |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |