#### Task execution in MapReduce

- MapReduce is a programming model designed to process large amount of data in parallel by dividing the job into several independent local tasks.
- A MapReduce job consists of two types of tasks: map tasks and reduce tasks.
- Map tasks take input data and apply a user-defined function to generate intermediate key-value pairs.
- Reduce tasks take intermediate key-value pairs and apply another user-defined function to aggregate them and produce the final output.
- The execution of tasks is controlled by two types of entities: a JobTracker and multiple TaskTrackers.
- The JobTracker acts like a master, responsible for scheduling, monitoring and coordinating the tasks. It also handles the failures and retries of tasks.
- The TaskTrackers act like slaves, each of them performing the tasks assigned by the JobTracker and reporting the progress and status to it.
- The JobTracker and the TaskTrackers communicate through a heartbeat mechanism, where the TaskTrackers periodically send a message to the JobTracker indicating their availability and health.
- The framework sorts the outputs of the map tasks, which are then input to the reduce tasks. Typically both the input and the output of the job are stored in a file-system, such as HDFS.
- The framework takes care of distributing the data, balancing the load, and optimizing the performance of the tasks.