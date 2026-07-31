### Anatomy of a Spark Job Run

1. **Client Mode**: In client mode, the driver program runs on the client machine, and the application master is only used for requesting resources from the cluster manager.

2. **Cluster Mode**: In cluster mode, the driver program runs on a worker node in the cluster, and the client can go away after submitting the application.

3. **Job Submission**: When an action is called on an RDD, a job is submitted to the DAGScheduler. The DAGScheduler divides the job into stages, where each stage contains a sequence of transformations that can be pipelined.

4. **Stage Creation**: The DAGScheduler creates stages by breaking the RDD lineage graph at shuffle boundaries. Each stage contains a sequence of narrow transformations that can be pipelined.

5. **Task Scheduling**: The TaskScheduler assigns tasks to workers based on data locality and available resources.

6. **Task Execution**: Each task computes a partition of the final RDD and stores the result in memory or on disk.

7. **Shuffle**: If a stage depends on the output of another stage, the data is shuffled across the network.

8. **Result Retrieval**: Once all tasks have completed, the result is returned to the driver program.