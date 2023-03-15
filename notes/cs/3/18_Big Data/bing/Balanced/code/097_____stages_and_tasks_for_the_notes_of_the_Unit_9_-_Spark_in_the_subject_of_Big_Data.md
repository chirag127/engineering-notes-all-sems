# Stages and Tasks for the Notes of the Unit 9 - Spark in the Subject of Big Data

- Spark is a distributed computing framework that can process large-scale data in parallel using resilient distributed datasets (RDDs).
- Spark divides the data processing into jobs, stages and tasks, which are controlled by the directed acyclic graph (DAG) scheduler.
- A job is a sequence of stages, triggered by an action such as `.count()`, `.foreachRdd()`, `.sortBy()`, `.read()` or `.write()`.
- A stage is a physical unit of execution for the computation of multiple tasks. A stage is composed of tasks that can run in parallel without a shuffle.
- A task is a single operation (such as `.map()` or `.filter()`) applied to a single partition of the data.
- There are two types of stages in Spark: ShuffleMapStage and ResultStage.
  - ShuffleMapStage is an intermediate stage that produces data for shuffle operation. The output of this stage acts as an input for the other following stages.
  - ResultStage is a final stage that performs the action for the job and returns the result to the driver or writes it to the storage.
- The number of tasks in a stage equals the number of partitions in the data. The number of partitions can be specified by the user or determined by Spark based on the data size and the configuration.
- Spark optimizes the execution of jobs by pipelining the tasks that can run consecutively without a shuffle within a stage. This reduces the data movement and the disk I/O.
- Spark also caches the intermediate data in memory or disk to avoid recomputation of the same data in case of failures or multiple actions.