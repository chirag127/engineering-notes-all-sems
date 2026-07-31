
### Anatomy of a Spark Job Run

1. **Job Submission**: A Spark job is submitted to the cluster manager, which can be either a standalone cluster manager, YARN, or Kubernetes. The job is composed of a set of tasks that need to be executed.

2. **Task Scheduling**: The cluster manager assigns tasks to nodes in the cluster. The scheduling algorithm takes into account the data locality of the tasks and the available resources on the nodes.

3. **Task Execution**: The tasks are executed on the nodes. The tasks can be either map tasks or reduce tasks. In a map task, the data is processed in parallel and the output is written to disk. In a reduce task, the output of the map tasks is combined and written to disk.

4. **Job Completion**: Once all the tasks have been completed, the job is marked as complete. The output of the job is written to disk.