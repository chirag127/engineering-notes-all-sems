### Failures in MapReduce

MapReduce is a programming model and framework for processing large-scale data sets in parallel and distributed manner. However, MapReduce is not immune to failures, and there are three main types of failures that can occur in MapReduce: task failure, tasktracker failure, and jobtracker failure. Here are some points to note about each type of failure:

- Task failure: This happens when a map or reduce task throws a runtime exception, or when the task is killed by the tasktracker due to timeout or exceeding memory limits. The tasktracker reports the failure to the jobtracker, which then schedules a new attempt of the task on a different tasktracker. The maximum number of attempts for a task can be configured by the properties `mapreduce.map.failures.maxpercent` and `mapreduce.reduce.failures.maxpercent`. If a task fails more than the maximum number of attempts, the whole job is considered as failed.
- Tasktracker failure: This happens when a tasktracker node crashes or becomes unreachable due to network issues. The jobtracker detects the failure by periodically sending heartbeat messages to the tasktrackers. If a tasktracker does not respond to the heartbeat within a certain time interval, the jobtracker marks it as lost and reassigns its tasks to other tasktrackers. The output of the completed map tasks on the failed tasktracker is also lost, as it is stored in the local disk of the node. Therefore, the map tasks have to be re-executed on other nodes. The output of the completed reduce tasks on the failed tasktracker is not lost, as it is stored in the global file system (such as HDFS). Therefore, the reduce tasks do not have to be re-executed.
- Jobtracker failure: This happens when the jobtracker node crashes or becomes unreachable due to network issues. The jobtracker is the master node that coordinates the execution of the MapReduce job and maintains the state of the job. If the jobtracker fails, the whole job is aborted and has to be restarted from scratch. The jobtracker is a single point of failure in MapReduce, and there is no automatic recovery mechanism for it. However, there are some solutions to make the jobtracker more fault-tolerant, such as using a backup jobtracker, using a high-availability cluster, or using a distributed coordination service (such as ZooKeeper).

References:

: Failures in Classic MapReduce - GitHub Pages
: How MapReduce completes a task? - GeeksforGeeks
: What is Map Reduce Programming and How Does it Work
: MapReduce - Wikipedia