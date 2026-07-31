# Failures in Classic MapReduce

- MapReduce is a programming model and framework for processing large-scale data sets in parallel and distributed manner.
- MapReduce consists of two phases: map and reduce, where each phase can be executed by multiple tasks on different nodes of a cluster.
- MapReduce also provides fault tolerance and reliability by handling various types of failures that may occur during the execution of a job.
- In this note, we will discuss the following types of failures in classic MapReduce:

  - Task failure
  - Tasktracker failure
  - Jobtracker failure

## Task failure

- A task failure occurs when a map or reduce task throws a runtime exception, runs out of memory, or exceeds the time limit.
- A task failure can be caused by various reasons, such as:

  - Bugs or errors in the user code
  - Malformed or corrupted input data
  - Hardware or network problems
  - Resource contention or starvation

- When a task fails, the tasktracker notifies the jobtracker, which marks the task as failed and reschedules it to run on another node.
- The jobtracker also keeps track of the number of attempts for each task, and kills the task if it exceeds the maximum number of attempts (default is 4).
- The maximum number of attempts can be configured by the properties `mapreduce.map.maxattempts` and `mapreduce.reduce.maxattempts`.
- The jobtracker also allows specifying the maximum percentage of failed tasks for a job, using the properties `mapreduce.map.failures.maxpercent` and `mapreduce.reduce.failures.maxpercent`.
- If the percentage of failed tasks exceeds the threshold, the jobtracker kills the entire job.

## Tasktracker failure

- A tasktracker failure occurs when a node running one or more map or reduce tasks becomes unavailable, due to hardware failure, network partition, or software crash.
- When a tasktracker fails, the jobtracker detects the failure by using a heartbeat mechanism, where each tasktracker periodically sends a heartbeat message to the jobtracker, along with the status of the tasks it is running.
- If the jobtracker does not receive a heartbeat from a tasktracker for a certain period of time (default is 10 minutes), it assumes that the tasktracker has failed and marks it as lost.
- The jobtracker then reschedules all the tasks that were running on the lost tasktracker to run on other nodes.
- The jobtracker also invalidates the output of the completed map tasks on the lost tasktracker, as they are stored on the local disk and are not accessible anymore.
- The jobtracker does not invalidate the output of the completed reduce tasks on the lost tasktracker, as they are stored on the global file system and are still accessible.

## Jobtracker failure

- A jobtracker failure occurs when the master node running the jobtracker becomes unavailable, due to hardware failure, network partition, or software crash.
- When the jobtracker fails, the entire MapReduce cluster becomes unusable, as the jobtracker is responsible for coordinating and monitoring all the jobs and tasks in the cluster.
- The jobtracker failure is the most serious failure mode, as it affects all the jobs and tasks, and requires manual intervention to recover.
- The jobtracker failure can be mitigated by using the following techniques:

  - Checkpointing: The jobtracker periodically saves its state to a persistent storage, such as a file system or a database. The state includes the information about the jobs, tasks, tasktrackers, and counters. If the jobtracker fails, it can be restarted from the last checkpoint and resume the execution of the jobs and tasks.
  - Backup: The jobtracker can be configured to run a backup jobtracker on another node, which receives the same heartbeat messages and state updates from the tasktrackers as the primary jobtracker. If the primary jobtracker fails, the backup jobtracker can take over and become the new primary jobtracker.
  - High availability: The jobtracker can be configured to run in a high availability mode, where multiple jobtrackers run on different nodes and use a shared storage and a consensus protocol to maintain a consistent state. If one jobtracker fails, another jobtracker can take over and continue the execution of the jobs and tasks.

## References

- [1] Apache Hadoop. http://hadoop.apache.org.
- [2] Failures in Classic MapReduce. https://sungsoo.github.io/2014/04/07/failures-in-classic-mapreduce.html.