### Failures in MapReduce

MapReduce is a programming model and framework for processing large-scale data sets in parallel and distributed manner. However, it is not immune to failures, which can occur at different levels and affect the performance and correctness of the computation. Some of the common types of failures in MapReduce are:

- **Task failure**: This happens when a map or reduce task throws a runtime exception, such as out of memory error, divide by zero error, or invalid input error. The task may also fail due to hardware or network issues, such as disk failure, power outage, or network partition. When a task fails, the tasktracker that was running the task notifies the jobtracker, which then schedules a new attempt of the same task on a different tasktracker. The jobtracker keeps track of the number of attempts for each task, and if the number exceeds a predefined threshold (default is 4), the job is marked as failed and terminated. The user can control the maximum number of attempts for map and reduce tasks separately using the `mapreduce.map.maxattempts` and `mapreduce.reduce.maxattempts` properties.

- **Tasktracker failure**: This happens when a tasktracker becomes unresponsive or crashes due to hardware or software issues. The jobtracker periodically sends heartbeat messages to all the tasktrackers, and if it does not receive a response from a tasktracker within a certain timeout period (default is 10 minutes), it marks the tasktracker as dead and removes it from the cluster. The jobtracker then reschedules all the tasks that were running or completed on the failed tasktracker, as their output may be inaccessible or corrupted. The user can control the timeout period using the `mapreduce.tasktracker.expiry.interval` property.

- **Jobtracker failure**: This happens when the jobtracker becomes unresponsive or crashes due to hardware or software issues. The jobtracker is a single point of failure in the MapReduce framework, as it is responsible for coordinating the execution of all the jobs in the cluster. If the jobtracker fails, all the running jobs are lost and have to be resubmitted by the user. There is no automatic recovery mechanism for the jobtracker failure, although some solutions have been proposed, such as using a backup jobtracker, a distributed coordination service, or a high-availability cluster.

- **Data corruption**: This happens when the input or output data of a map or reduce task is corrupted due to hardware or software issues, such as disk failure, network failure, or malicious attack. Data corruption can cause incorrect or incomplete results, or even task or job failure. MapReduce provides some mechanisms to detect and handle data corruption, such as checksum verification, speculative execution, and output committer .

- **References**:

: https://sungsoo.github.io/2014/04/07/failures-in-classic-mapreduce.html

: https://www.geeksforgeeks.org/how-mapreduce-completes-a-task/

: https://www.datasciencecentral.com/what-is-map-reduce-programming-and-how-does-it-work/

: https://stackoverflow.com/questions/32255196/error-handling-in-hadoop-map-reduce

: https://en.wikipedia.org/wiki/MapReduce