### Stages and Tasks for the Notes of the Unit 9 - Spark in the Subject of Big Data

- Spark is a distributed computing framework that can process large-scale data in parallel using resilient distributed datasets (RDDs).
- Spark jobs, stages and tasks are the logical and physical units of execution for the computation of RDDs.
- A **job** is a sequence of stages, triggered by an action such as `.count()`, `.foreachRdd()`, `.sortBy()`, `.read()` or `.write()`.
- A **stage** is a set of tasks that can be executed in parallel without data shuffling. Stages are divided by wide transformations that require data movement across the cluster, such as `.reduceByKey()`, `.join()` or `.groupBy()`.
- A **task** is a single operation (such as `.map()` or `.filter()`) applied to a single partition of an RDD. Tasks are executed by executors on worker nodes.
- There are two types of stages in Spark: **ShuffleMapStage** and **ResultStage**.
  - A **ShuffleMapStage** is an intermediate stage that produces data for shuffle operation. The output of this stage acts as an input for the other following stages.
  - A **ResultStage** is a final stage that performs an action on the RDD, such as writing to disk or displaying the result.
- The number of tasks in a stage equals the number of partitions in the RDD. The number of partitions can be specified by the user or determined by Spark based on the data source and the cluster configuration.
- Spark uses a **DAGScheduler** to create a directed acyclic graph (DAG) of stages for each job and submit them to the cluster manager for execution.
- Spark also uses a **TaskScheduler** to assign tasks to executors and monitor their status.
- Spark stages and tasks can be visualized using the Spark UI, which provides information about the execution time, shuffle size, memory usage, and errors for each stage and task.