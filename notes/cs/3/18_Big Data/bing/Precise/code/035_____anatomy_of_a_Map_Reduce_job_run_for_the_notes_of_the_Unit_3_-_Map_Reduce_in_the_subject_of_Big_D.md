### Anatomy of a MapReduce Job Run

1. **Job Submission:** The client submits the job to the JobTracker, which then initializes the job and divides it into input splits. Each input split is then assigned to a map task.

2. **Task Assignment:** The JobTracker assigns map and reduce tasks to TaskTrackers. The TaskTracker spawns a new JVM to run the task.

3. **Task Execution:** The map tasks read the input data, apply the map function, and write the output to the local disk. The reduce tasks fetch the map output, apply the reduce function, and write the final output to HDFS.

4. **Progress and Status Updates:** The TaskTrackers send heartbeat messages to the JobTracker, which include the progress and status of the tasks. The JobTracker uses this information to monitor the progress of the job and to reassign failed tasks.

5. **Job Completion:** Once all the tasks have completed successfully, the JobTracker marks the job as complete and notifies the client. The client can then retrieve the final output from HDFS.