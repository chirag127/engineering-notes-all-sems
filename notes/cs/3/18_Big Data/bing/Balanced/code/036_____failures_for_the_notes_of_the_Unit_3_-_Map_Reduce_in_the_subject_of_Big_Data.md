### Failures in MapReduce

MapReduce is a programming model and framework for processing large-scale data sets in parallel and distributed manner. However, MapReduce is not immune to failures, and there are three main types of failures that can occur in a MapReduce job: task failure, tasktracker failure, and jobtracker failure. Here are some points to note about each type of failure:

- Task failure: A task is a unit of work assigned to a worker node (tasktracker) by the master node (jobtracker). A task can fail due to various reasons, such as user code errors, hardware failures, network failures, etc. When a task fails, the jobtracker will detect the failure and reassign the task to another tasktracker. The jobtracker will also keep track of the number of failed attempts for each task, and if the number exceeds a certain threshold (configured by `mapreduce.map.failures.maxpercent` and `mapreduce.reduce.failures.maxpercent` properties), the jobtracker will mark the task as failed and abort the whole job.   

- Tasktracker failure: A tasktracker is a worker node that runs map and reduce tasks assigned by the jobtracker. A tasktracker can fail due to various reasons, such as hardware failures, network failures, power outages, etc. When a tasktracker fails, the jobtracker will detect the failure and mark the tasktracker as dead. The jobtracker will also reassign the tasks that were running on the failed tasktracker to other tasktrackers. However, if the failed tasktracker was running map tasks, the output of those tasks will be lost, as they are stored in the local disk of the tasktracker. Therefore, the jobtracker will have to re-execute those map tasks on other tasktrackers. On the other hand, if the failed tasktracker was running reduce tasks, the output of those tasks will not be lost, as they are stored in the global file system (such as HDFS). Therefore, the jobtracker will not have to re-execute those reduce tasks on other tasktrackers.  

- Jobtracker failure: A jobtracker is a master node that coordinates and monitors the execution of a MapReduce job. A jobtracker can fail due to various reasons, such as hardware failures, network failures, power outages, etc. When a jobtracker fails, the whole MapReduce job will be aborted, as there is no backup or recovery mechanism for the jobtracker. The jobtracker is a single point of failure in the MapReduce framework, and it can affect the availability and reliability of the system. Therefore, it is important to ensure that the jobtracker is running on a reliable and fault-tolerant machine, and that it is backed up regularly.  

- References:

: https://sungsoo.github.io/2014/04/07/failures-in-classic-mapreduce.html

: https://www.geeksforgeeks.org/how-mapreduce-completes-a-task/

: https://www.datasciencecentral.com/what-is-map-reduce-programming-and-how-does-it-work/

: https://en.wikipedia.org/wiki/MapReduce

: https://stackoverflow.com/questions/40204001/how-does-mapreduce-recover-from-errors-if-failure-happens-in-an-intermediate-sta