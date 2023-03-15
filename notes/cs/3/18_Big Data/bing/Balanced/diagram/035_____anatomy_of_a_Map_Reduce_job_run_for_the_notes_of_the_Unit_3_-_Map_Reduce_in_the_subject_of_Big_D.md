### Anatomy of a Map Reduce Job Run

- A Map Reduce job is a unit of work that consists of a map phase and a reduce phase, which operate on a distributed file system (DFS) such as HDFS.
- A Map Reduce job can be submitted to a Hadoop cluster by calling the `submit()` or `waitForCompletion()` methods on a `Job` object, which encapsulates the configuration and input/output specifications of the job.
- A Map Reduce job is divided into a set of map tasks and reduce tasks, which are assigned to different nodes in the cluster by a scheduler.
- A map task takes a split of the input data (usually a file block) and applies a user-defined map function to each record, which produces a set of intermediate key-value pairs.
- A reduce task takes a set of intermediate key-value pairs that share the same key and applies a user-defined reduce function to them, which produces a set of output key-value pairs.
- The intermediate key-value pairs are shuffled and sorted by the framework, which transfers them from the map nodes to the reduce nodes according to a partitioning function.
- The output key-value pairs are written to the DFS by the reduce tasks, which can be accessed by the client or other applications.

The following diagram illustrates the anatomy of a Map Reduce job run:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Client       |       |    JobTracker   |       |    TaskTracker  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Submit Job     |------>|  Schedule Job   |------>|  Run Map Task   |
|                 |       |                 |       |                 |
|  Monitor Job    |<------|  Report Status  |<------|  Report Status  |
|                 |       |                 |       |                 |
|  Fetch Output   |<-----------------------------|  Write Output    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```