#### Anatomy of a Spark Job Run

1. **Client Mode**: In client mode, the driver program runs on the client machine, and the application master is only used for requesting resources from the cluster manager.
2. **Cluster Mode**: In cluster mode, the driver program runs on a worker node in the cluster, and the client can go away after submitting the application.
3. **Job Submission**: When an action is called on an RDD, a job is submitted to the Spark scheduler.
4. **Stages**: A job is divided into stages, where each stage contains a sequence of narrow transformations that can be pipelined together.
5. **Tasks**: Each stage is further divided into tasks, where each task corresponds to a partition of the input data.
6. **Task Scheduling**: The scheduler assigns tasks to available executors based on data locality and available resources.
7. **Task Execution**: Each task is executed on an executor, reading its input data, applying the transformations, and writing its output data.
8. **Shuffling**: Wide transformations require data to be shuffled between executors, which can be a costly operation.
9. **Result Collection**: Once all tasks have completed, the result is collected and returned to the driver program.