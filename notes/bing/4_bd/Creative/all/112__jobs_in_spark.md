#### Jobs in Spark

- A job in Spark is a parallel computation that consists of multiple tasks that get spawned in response to a Spark action (e.g., save, collect); you can also use the web UI to check the jobs that have been scheduled or run.
- A Spark job can consist of more than one stage, which are the smaller units of a job and are scheduled by Spark's scheduler. A stage contains tasks based on the same shuffle dependency. Spark tries to pipeline as many RDD operations as possible within a stage, but it has to break the pipeline if one of the RDD operations relies on a shuffle (e.g., reduceByKey, join, groupByKey).
- The boundaries of a stage are often referred to as shuffle boundaries, or just shuffles. A shuffle is a data exchange that copies data across the executors and the network. Shuffles are expensive operations because they involve disk I/O, data serialization, and network I/O. To organize data for the shuffle, Spark creates buckets of data called shuffle partitions (or just partitions), which are configurable through spark.sql.shuffle.partitions or spark.default.parallelism depending on whether you are working in SQL or RDDs.
- A task is a unit of execution that runs on a single executor (a process running on a worker node). One task is executed for each partition of the shuffled data; tasks are multithreaded and share the same executor JVM. The number of tasks to run is the same as the number of partitions of the data. Each task performs a range of transformations on a single partition of the data, and optionally writes out a result.
- A simple way to remember the relationship between jobs, stages, and tasks is: one action triggers one job, which consists of one or more stages, each of which has one or more tasks. The following diagram illustrates this relationship:

```
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
|     |     |     |     |     |     |     |     |     |     |     |     |
|  A  |  B  |  C  |  D  |  E  |  F  |  G  |  H  |  I  |  J  |  K  |  L  |
|     |     |     |     |     |     |     |     |     |     |     |     |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
|                             |                             |           |
|          Stage 1            |          Stage 2            |  Stage 3  |
|                             |                             |           |
+-----------------------------+-----------------------------+-----------+
|                                                 |                     |
|                      Job 1                      |        Job 2        |
|                                                 |                     |
+-------------------------------------------------+---------------------+
|                                                                     |
|                              Action 1                               |
|                                                                     |
+---------------------------------------------------------------------+
```

- In this example, action 1 triggers job 1, which has two stages: stage 1 and stage 2. Stage 1 has four tasks: A, B, C, and D; stage 2 has four tasks: E, F, G, and H. There is a shuffle boundary between stage 1 and stage 2. Job 2 is triggered by a different action and has one stage: stage 3, which has four tasks: I, J, K, and L. There is no shuffle boundary between job 1 and job 2, as they are independent computations.
- To optimize the performance of your Spark applications, you should minimize the number of shuffles and the amount of data shuffled, and tune the level of parallelism to match the resources available. You can use the Spark UI to monitor the progress and performance of your Spark jobs, stages, and tasks, and identify the bottlenecks or skewness in your data or computation.