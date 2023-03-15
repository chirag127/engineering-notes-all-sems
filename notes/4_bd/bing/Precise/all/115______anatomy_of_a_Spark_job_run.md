#### Anatomy of a Spark Job Run

1. **Client Mode**: In client mode, the driver program runs on the client machine, and the application master is only used for requesting resources from the cluster manager.

2. **Cluster Mode**: In cluster mode, the driver program runs on a worker node in the cluster, and the client can go away after submitting the application.

3. **Job Submission**: When a Spark action is called, the driver program converts the RDD transformations into a directed acyclic graph (DAG) of stages.

4. **Stage Creation**: The DAG is divided into stages at the shuffle boundaries. Each stage contains a sequence of narrow transformations that can be pipelined together.

5. **Task Scheduling**: The stages are submitted to the cluster manager in topological order. The cluster manager launches tasks to process the data partitions.

6. **Task Execution**: Each task applies the sequence of transformations to its input data partition and writes the result to a local file or sends it over the network to the next stage.

7. **Result Collection**: When all the tasks of a stage have completed, the driver program collects the results and moves on to the next stage. When all the stages have completed, the final result is returned to the driver program.

8. **Job Completion**: Upon completion of the job, the driver program releases the resources it has acquired from the cluster manager and exits. In client mode, the client can submit another job or terminate the session. In cluster mode, the application master exits and the worker node is released for other applications.