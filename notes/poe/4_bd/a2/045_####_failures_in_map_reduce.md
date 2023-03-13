 Here is the content in markdown format on the topic #### failures in map reduce:

#### Failures in Map Reduce

Map Reduce is a distributed programming model and hence failures are bound to happen. Some common failures and ways to handle them are:

1. Task failure: If a task fails due to some reason, it will be re-executed on some other node. The task tracker will detect the failure and trigger the re-execution.
2. Node failure: If a node fails, all the tasks running on that node will fail. The job tracker will detect the node failure and re-execute the failed tasks on some other available nodes.
3. Job tracker failure: If the job tracker fails, all the jobs in progress will fail. The job tracker failure will be detected by the task trackers which will then request the Hadoop Master node to restart the job tracker. Once the job tracker is restarted, the failed tasks will be re-executed.

**Mnemonics:** *Try running the task, if node fell. Job tracker will save, by redoing in its trail.*

Some advantages of handling failures in Map Reduce are:

- Fault Tolerance: Map Reduce is fault tolerant in nature and can handle failures efficiently without human intervention.
- Scalability: It scales to large clusters with thousands of nodes as the failed tasks are re-executed on other available nodes.
- Reliability: The jobs will eventually complete even after some failures leading to a reliable system.

Some disadvantages are:

- Degraded performance: Due to re-executions of failed tasks, the performance of Map Reduce degrades as the complete job takes more time to finish.
- Resource wastage: The re-execution of tasks leads to some resource wastage as the previously completed work is repeated.