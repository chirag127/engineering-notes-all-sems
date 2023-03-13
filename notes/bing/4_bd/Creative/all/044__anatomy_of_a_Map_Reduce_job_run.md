#### Anatomy of a MapReduce job run

- A MapReduce job is a unit of work that consists of a map phase and a reduce phase, which operate on a large dataset in parallel.
- A MapReduce job can be executed by calling the `submit()` or `waitForCompletion()` methods on a `Job` object, which represents the configuration and status of the job.
- The `Job` object communicates with the `JobTracker`, which is a master service that coordinates the execution of the job across the cluster.
- The `JobTracker` assigns the job a unique ID and splits the input data into fixed-size pieces called `input splits`, each of which is processed by a single map task.
- The `JobTracker` also determines the number of reduce tasks to create, based on the `mapred.reduce.tasks` property in the `JobConf`, which can be set by the `setNumReduceTasks()` method.
- The `JobTracker` then schedules the map and reduce tasks to run on the available `TaskTrackers`, which are slave services that run on each node in the cluster and execute the tasks assigned by the `JobTracker`.
- The `TaskTrackers` launch separate JVM processes for each map and reduce task, and report their progress and status to the `JobTracker`.
- The map tasks read the input data from the `Hadoop Distributed File System (HDFS)` or other sources, and apply the user-defined map function to each key-value pair in the input split.
- The map function emits intermediate key-value pairs, which are partitioned, sorted, and written to the local disk of the `TaskTracker`.
- The reduce tasks fetch the intermediate data from the map tasks, either directly or through an intermediate service called `ShuffleHandler`, and merge and sort them by key.
- The reduce tasks then apply the user-defined reduce function to each group of values that share the same key, and emit the final output key-value pairs, which are written to the `HDFS` or other destinations.
- The `JobTracker` monitors the progress and status of the tasks, and handles failures and retries if necessary.
- The `JobTracker` also provides a web interface for the user to view the details and statistics of the job, such as the number of tasks, the input and output sizes, the execution time, and the counters.
- The `Job` object returns the final status of the job to the user, and cleans up any temporary files and resources used by the job.