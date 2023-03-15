#### Anatomy of a Spark Job Run

1. **Client Mode**: In client mode, the driver program runs on the client machine, and the application master is only used for requesting resources from YARN.

2. **Cluster Mode**: In cluster mode, the driver program runs on a worker node inside the cluster, and the application master is used for both requesting resources from YARN and managing the driver program.

3. **Job Submission**: When a Spark job is submitted, the driver program converts the user's code into a series of tasks to be executed on the cluster.

4. **Task Scheduling**: The driver program communicates with the cluster manager to schedule tasks on the worker nodes.

5. **Task Execution**: Each task is executed on a worker node, and the results are sent back to the driver program.

6. **Shuffling**: If the tasks require data to be exchanged between worker nodes, a shuffle operation is performed.

7. **Result Collection**: Once all tasks have completed, the driver program collects the results and returns them to the user.