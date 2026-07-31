### Anatomy of a MapReduce Job Run

- A MapReduce job is a unit of work that consists of a map phase and a reduce phase, which operate on a distributed file system (such as HDFS).
- A MapReduce job can be executed by calling the `submit()` or `waitForCompletion()` methods on a `Job` object, which represents the configuration and status of the job.
- The `Job` object communicates with the `JobTracker`, which is a daemon process that runs on a master node and coordinates the execution of MapReduce jobs across the cluster.
- The `JobTracker` assigns a unique ID to the job and splits the input data into fixed-size pieces called `input splits`, which are the units of work for the map tasks.
- The `JobTracker` also determines the number of map and reduce tasks to create, based on the input data size, the cluster capacity, and the configuration parameters.
- The `JobTracker` then contacts the `TaskTrackers`, which are daemon processes that run on the worker nodes and execute the map and reduce tasks assigned by the `JobTracker`.
- The `TaskTrackers` launch `Child` processes in separate JVMs to run the map and reduce tasks, and report their progress and status to the `JobTracker`.
- The map tasks read the input splits from the distributed file system and apply the user-defined map function to each record, which produces a set of intermediate key-value pairs.
- The map tasks partition the intermediate key-value pairs by a user-defined partition function, which determines which reduce task will receive the values for a given key.
- The map tasks also sort and spill the intermediate key-value pairs to the local disk, and optionally combine them by a user-defined combine function, which reduces the amount of data to be transferred to the reduce tasks.
- The reduce tasks fetch the intermediate key-value pairs from the map tasks via HTTP, and merge and sort them by key.
- The reduce tasks then apply the user-defined reduce function to each key and its list of values, which produces the final output key-value pairs.
- The reduce tasks write the output key-value pairs to the distributed file system, and notify the `JobTracker` of their completion.
- The `JobTracker` monitors the progress and status of the map and reduce tasks, and handles failures and retries by reassigning the tasks to different `TaskTrackers`.
- The `JobTracker` also provides a web interface for the user to view the details and statistics of the job, such as the number of tasks, the input and output data size, the execution time, and the counters.
- The `JobTracker` marks the job as successful when all the map and reduce tasks are completed, and returns the control to the `Job` object, which reports the final status to the user.