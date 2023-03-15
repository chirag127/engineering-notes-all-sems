# Anatomy of a Spark Job Run

1. **Client Mode**: In client mode, the driver program runs on the client machine, and the application master is only used for requesting resources from the cluster manager.
2. **Cluster Mode**: In cluster mode, the driver program runs on a worker node in the cluster, and the client can go away after submitting the application.
3. **Job Submission**: When a Spark action is called, the driver program converts the RDD transformations into a physical execution plan called a stage.
4. **Stage Creation**: A stage is a sequence of transformations that can be completed without shuffling data between partitions.
5. **Task Scheduling**: The stages are submitted to the cluster manager, which launches tasks to compute the stages on the worker nodes.
6. **Task Execution**: Each task computes a partition of an RDD and stores the result in memory or on disk.
7. **Result Collection**: Once all the tasks have completed, the driver program collects the results and returns them to the user.
