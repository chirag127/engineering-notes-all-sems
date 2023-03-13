Jobs in Spark are parallel computations of tasks that are triggered by actions such as count, collect, read or write. Each job is divided into one or more stages, which are further divided into one or more tasks. Each task is a unit of work that is executed by an executor on a worker node. A stage is a collection of tasks that have the same shuffle dependency. A job can have multiple stages if there are wide transformations that require data to be shuffled across the cluster. The following diagram illustrates the basic architecture of a job in Spark:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Driver       |    |    Driver       |    |    Driver       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
       v                      v                      v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Job 1        |    |    Job 2        |    |    Job 3        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Stage 1      |    |    Stage 1      |    |    Stage 1      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Task 1       |    |    Task 1       |    |    Task 1       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Executor     |    |    Executor     |    |    Executor     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```