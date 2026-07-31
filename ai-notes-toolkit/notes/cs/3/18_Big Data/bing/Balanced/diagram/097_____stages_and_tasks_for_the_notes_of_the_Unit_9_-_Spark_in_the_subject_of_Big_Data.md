### Stages and Tasks for the Notes of the Unit 9 - Spark in the Subject of Big Data

- Spark is a distributed computing framework that can process large-scale data in parallel using clusters of nodes.
- Spark applications consist of a driver program that runs the main function and coordinates with a number of executors that run on different nodes and perform the actual computation.
- Spark applications can be submitted using the `spark-submit` command or using interactive shells like `spark-shell` or `pyspark`.
- Spark applications can be written in Scala, Python, Java, R, or SQL.
- Spark applications can perform various operations on data, such as transformations, actions, and queries.
- Spark operations can be divided into two types: narrow and wide.
  - Narrow operations, such as `map`, `filter`, or `union`, do not require data to be shuffled across partitions or nodes. They can be performed within a single stage.
  - Wide operations, such as `groupBy`, `join`, or `reduceByKey`, require data to be shuffled across partitions or nodes. They create boundaries between stages.
- A Spark job is a sequence of operations that result in an action, such as `count`, `collect`, or `save`. A job can have one or more stages, depending on the number of wide operations involved.
- A Spark stage is a smaller set of tasks that depend on each other. A stage is a physical unit of execution that corresponds to a subset of the DAG (Directed Acyclic Graph) of operations. A stage can have one or more tasks, depending on the number of partitions of the input data.
- A Spark task is a unit of work that is sent to an executor. A task is a logical unit of execution that corresponds to a single operation on a partition of the data. A task can perform a narrow or a wide operation, depending on the type of the stage.
- Spark stages and tasks are created and scheduled by the DAGScheduler and the TaskScheduler components of the Spark engine. The DAGScheduler splits a job into stages based on the shuffle boundaries and submits them to the TaskScheduler. The TaskScheduler launches tasks on the available executors and monitors their progress and failures.
- Spark stages and tasks can be visualized using the Spark UI, which shows the DAG of operations, the timeline of stages and tasks, and the metrics of the executors and the resources. The Spark UI can help to monitor and debug the performance and the behavior of the Spark applications.