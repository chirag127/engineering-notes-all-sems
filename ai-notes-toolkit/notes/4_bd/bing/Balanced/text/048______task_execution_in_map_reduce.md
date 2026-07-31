#### Task execution in MapReduce

- MapReduce is a programming model designed to process large amounts of data in parallel by dividing the job into several independent local tasks.
- The execution of tasks is controlled by the MapReduce Execution Service, which plays the role of the worker process in the Google MapReduce implementation.
- The service manages the execution of map and reduce tasks and performs other operations, such as sorting and merging intermediate files.
- The complete execution process is also supervised by two types of entities called a JobTracker and multiple TaskTrackers.
- The JobTracker acts like a master, responsible for scheduling, monitoring and re-executing the failed tasks .
- The TaskTrackers act like slaves, each of them performing the map or reduce tasks assigned by the JobTracker on their local data .
- The map tasks read the input data from the file system and apply a user-defined function to each record, producing a set of intermediate key-value pairs.
- The reduce tasks receive the intermediate key-value pairs from the map tasks, group them by key, and apply another user-defined function to each group, producing the final output.
- The framework sorts the outputs of the maps, which are then input to the reduce tasks.
- The framework also handles the failures of tasks, by re-executing them on different nodes if necessary .
- The framework also optimizes the performance of the tasks, by using techniques such as locality-aware scheduling, speculative execution, and combiners.