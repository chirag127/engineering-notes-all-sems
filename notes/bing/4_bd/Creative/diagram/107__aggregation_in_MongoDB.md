Aggregation in MongoDB is the process of selecting data from a collection and performing various operations on the data to produce a computed result. Aggregation can be done using two methods: single-purpose aggregation and aggregation pipeline. Single-purpose aggregation consists of helper methods that apply a specific operation to a collection, such as count, distinct, or group. Aggregation pipeline consists of one or more stages that process documents in a sequence. Each stage performs an operation on the input documents and outputs modified documents to the next stage. Some of the common stages are match, group, sort, project, and unwind.

The following diagram illustrates the basic architecture of an aggregation pipeline in MongoDB using ASCII art:

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|   Collection   |     |    $match      |     |    $group      |     |    $sort       |
|                |     |                |     |                |     |                |
|  +----------+  |     |  +----------+  |     |  +----------+  |     |  +----------+  |
|  | Document |  |     |  | Document |  |     |  | Document |  |     |  | Document |  |
|  +----------+  |     |  +----------+  |     |  +----------+  |     |  +----------+  |
|  +----------+  |     |  +----------+  |     |  +----------+  |     |  +----------+  |
|  | Document |  | --> |  | Document |  | --> |  | Document |  | --> |  | Document |  |
|  +----------+  |     |  +----------+  |     |  +----------+  |     |  +----------+  |
|  +----------+  |     |  +----------+  |     |  +----------+  |     |  +----------+  |
|  | Document |  |     |  | Document |  |     |  | Document |  |     |  | Document |  |
|  +----------+  |     |  +----------+  |     |  +----------+  |     |  +----------+  |
|  +----------+  |     |  +----------+  |     |  +----------+  |     |  +----------+  |
|  | Document |  |     |  | Document |  |     |  | Document |  |     |  | Document |  |
|  +----------+  |     |  +----------+  |     |  +----------+  |     |  +----------+  |
+----------------+     +----------------+     +----------------+     +----------------+
```