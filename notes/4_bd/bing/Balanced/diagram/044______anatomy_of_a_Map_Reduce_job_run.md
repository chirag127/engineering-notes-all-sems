A MapReduce job is a unit of work that consists of a map phase and a reduce phase, which operate on a distributed file system (DFS). The map phase reads the input data, splits it into key-value pairs, and applies a user-defined function to each pair. The reduce phase aggregates the values with the same key, and applies another user-defined function to produce the final output.

The following diagram shows the anatomy of a MapReduce job run:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|    Client      |    |    JobTracker  |    |    TaskTracker |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       |                     |                      |
       | submit job          |                      |
       |-------------------> |                      |
       |                     |                      |
       |                     | assign map tasks     |
       |                     |------------------->  |
       |                     |                      |
       |                     |                      | run map tasks
       |                     |                      |---------------> DFS
       |                     |                      |                 |
       |                     |                      |                 | write intermediate output
       |                     |                      |                 |-------------------------> DFS
       |                     |                      |                 |
       |                     |                      |                 |
       |                     |                      |<-------------- DFS
       |                     |                      | run reduce tasks
       |                     |                      |---------------> DFS
       |                     |                      |                 |
       |                     |                      |                 | write final output
       |                     |                      |                 |-------------------------> DFS
       |                     |                      |                 |
       |                     |                      |<-------------- DFS
       |                     |                      |
       |                     | report job status    |
       |<--------------------|                      |
       |                     |                      |
```

The main components involved in a MapReduce job run are:

- Client: The program that submits the job to the JobTracker and monitors its progress.
- JobTracker: The master node that coordinates the job execution and assigns tasks to the TaskTrackers.
- TaskTracker: The slave node that runs the map and reduce tasks and reports their status to the JobTracker.
- DFS: The distributed file system that stores the input and output data, as well as the intermediate results.