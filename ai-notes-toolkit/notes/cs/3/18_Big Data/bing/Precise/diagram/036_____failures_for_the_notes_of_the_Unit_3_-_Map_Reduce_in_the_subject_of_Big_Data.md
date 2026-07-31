### Unit 3 - MapReduce: Failures

1. **Task Failure:** A task may fail due to various reasons such as bugs in the code, hardware failure, or network issues. In such cases, the MapReduce framework reschedules the failed task on another node.
2. **Worker Failure:** If a worker node fails, the master node detects the failure and reschedules all the tasks that were assigned to the failed worker on other nodes.
3. **Master Failure:** If the master node fails, the entire MapReduce job fails. To recover from a master failure, the job must be restarted from the beginning.
4. **Data Loss:** Data loss can occur due to disk failure, network issues, or other reasons. The MapReduce framework replicates the input data across multiple nodes to prevent data loss.
5. **Network Issues:** Network issues such as congestion or partitioning can cause delays or failures in the MapReduce job. The framework tries to schedule tasks on nodes that are close to the data to minimize network traffic.
