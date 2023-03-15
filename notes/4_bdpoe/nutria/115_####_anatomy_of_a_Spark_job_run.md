
#### Anatomy of a Spark Job Run

1. **Submission**: This is the very first step in a Spark job run. The user submits the job to the cluster manager which is responsible for scheduling the tasks.
2. **Scheduling**: After the job is submitted, the cluster manager is responsible for scheduling the tasks. It assigns the tasks to the nodes in the cluster.
3. **Execution**: Once the tasks are scheduled, the nodes start executing the tasks. The nodes process the data and the results are stored in the memory or disk.
4. **Shuffle**: During the execution phase, the data is shuffled between the nodes. This is done to ensure that the data is evenly distributed among the nodes.
5. **Reduce**: After the data is shuffled, the reduce phase is executed. This phase aggregates the data from the nodes and computes the final result.
6. **Result**: The final result is then returned to the user.

Mnemonic: 
SSEERR - Submit, Schedule, Execute, Shuffle, Reduce, Result.