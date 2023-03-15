#### Task execution in MapReduce

- MapReduce is a programming model designed to process large amounts of data in parallel by dividing the job into several independent local tasks.
- The execution of tasks is controlled by the MapReduce Execution Service, which plays the role of the worker process in the Google MapReduce implementation.
- The service manages the execution of map and reduce tasks and performs other operations, such as sorting and merging intermediate files.
- The complete execution process is also supervised by two types of entities called a JobTracker and multiple TaskTrackers.
- The JobTracker acts like a master, responsible for scheduling, monitoring and re-executing the failed tasks .
- The TaskTrackers act like slaves, each of them performing the tasks assigned by the JobTracker on their local nodes .
- The tasks are executed by a Java application whose main class is YarnChild.
- The tasks can fail due to various reasons, such as user code errors, runtime exceptions, hardware failures, etc.
- The framework handles the task failures by reporting the errors to the JobTracker and the user logs, and by retrying the tasks on different nodes .