MapReduce is a programming model and a software framework for processing large amounts of data in parallel across a cluster of nodes. It consists of two phases: Map and Reduce. The Map phase applies a user-defined function to each input record and produces a set of intermediate key-value pairs. The Reduce phase aggregates the intermediate values associated with the same key and produces the final output.

The following diagram illustrates the basic architecture of a MapReduce job:

### Map Reduce
```
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|    Input Data     |      |    Input Data     |      |    Input Data     |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          v                         v                         v
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|      Mapper       |      |      Mapper       |      |      Mapper       |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          v                         v                         v
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|  Intermediate     |      |  Intermediate     |      |  Intermediate     |
|  Key-Value Pairs  |      |  Key-Value Pairs  |      |  Key-Value Pairs  |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          +-------------------------+-------------------------+
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          v                         v                         v
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|      Reducer      |      |      Reducer      |      |      Reducer      |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          +-------------------------+-------------------------+
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          |                         |                         |
          v                         v                         v
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|    Output Data    |      |    Output Data    |      |    Output Data    |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
```

The MapReduce framework consists of a single master node called the JobTracker and multiple slave nodes called the TaskTrackers. The JobTracker is responsible for scheduling the jobs' component tasks on the TaskTrackers, monitoring them and re-executing the failed tasks. The TaskTrackers execute the tasks as directed by the JobTracker. [^5