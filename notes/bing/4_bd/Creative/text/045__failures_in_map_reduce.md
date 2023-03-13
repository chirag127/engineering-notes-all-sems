#### Failures in MapReduce

MapReduce is a programming model and framework for processing large-scale data sets in parallel using clusters of commodity machines. However, MapReduce applications may encounter various types of failures during their execution, which can affect their performance, correctness, and availability. Some of the common failures in MapReduce are:

- **Task failure**: This occurs when a map or reduce task fails due to a runtime exception in the user code, a bad input record, a corrupted intermediate file, or a hardware error. The task may also be killed by the user or the system for various reasons, such as exceeding the memory limit, running too slowly, or being preempted by a higher priority task. When a task fails, the tasktracker reports the error to the jobtracker, which then schedules a new attempt of the task on a different tasktracker. The jobtracker keeps track of the number of failed attempts for each task, and if it exceeds a certain threshold (usually four), the job is marked as failed and aborted.  

- **Tasktracker failure**: This occurs when a tasktracker node becomes unavailable due to a network partition, a power outage, a hardware failure, or a software crash. When a tasktracker fails, the jobtracker detects the failure by a periodic heartbeat mechanism, and marks all the tasks that were running on the failed tasktracker as failed. The jobtracker then reassigns those tasks to other available tasktrackers, and also redistributes the map output files that were stored on the failed tasktracker to other tasktrackers. The jobtracker also updates the status of the failed tasktracker in the cluster, and removes it from the list of available tasktrackers.  

- **Jobtracker failure**: This occurs when the jobtracker node becomes unavailable due to a similar reason as the tasktracker failure. When the jobtracker fails, the entire MapReduce cluster becomes inoperable, as the jobtracker is responsible for coordinating all the jobs and tasks in the cluster. The jobtracker failure also causes the loss of all the job and task metadata, such as the job configuration, the task assignments, the task progress, and the task output locations. To recover from the jobtracker failure, the jobtracker node needs to be restarted, and all the running jobs need to be resubmitted by the users. The jobtracker also needs to reinitialize the cluster state by communicating with all the tasktrackers and collecting their status.  

- **References**:

: https://sungsoo.github.io/2014/04/07/failures-in-classic-mapreduce.html

: https://www.researchgate.net/publication/320027419_Performance_Implications_of_Failures_on_MapReduce_Applications

: https://www.geeksforgeeks.org/how-mapreduce-completes-a-task/

: https://stackoverflow.com/questions/32255196/error-handling-in-hadoop-map-reduce

: https://stackoverflow.com/questions/40204001/how-does-mapreduce-recover-from-errors-if-failure-happens-in-an-intermediate-sta