#### Anatomy of a Map Reduce job run

- A Map Reduce job is a unit of work that consists of a map function and a reduce function, applied to a set of input data.
- A Map Reduce job run is the process of executing a Map Reduce job on a distributed system, such as Hadoop.
- A Map Reduce job run involves the following steps:

  - The job client submits the job to the job tracker, which is the master node that coordinates the job execution.
  - The job tracker assigns a unique ID to the job and splits the input data into fixed-size chunks called input splits. Each input split is assigned to a map task, which is a unit of work for the map function.
  - The job tracker locates the data nodes that store the input splits and assigns the map tasks to the task trackers, which are the worker nodes that run the map and reduce tasks.
  - The task trackers launch the map tasks and run the map function on each input split. The map function processes the input key-value pairs and emits intermediate key-value pairs as the output.
  - The intermediate key-value pairs are partitioned by a partitioner function, which determines which reduce task will receive them. The default partitioner uses a hash function on the intermediate keys.
  - The intermediate key-value pairs are sorted by the intermediate keys and grouped by the same keys. The sorted and grouped intermediate key-value pairs are called shuffle output.
  - The shuffle output is transferred to the reduce tasks, which are assigned by the job tracker to the task trackers. The reduce tasks run the reduce function on each group of intermediate key-value pairs with the same key. The reduce function combines the values and emits the final output key-value pairs.
  - The final output key-value pairs are written to the output files in the output directory specified by the job client. The output files are stored in the distributed file system, such as HDFS.
  - The job tracker monitors the progress and status of the map and reduce tasks. If a task fails or times out, the job tracker reschedules it to another task tracker. The job tracker also handles the speculative execution of tasks, which is a technique to improve the performance by running backup tasks on idle nodes.
  - The job tracker notifies the job client when the job is completed or failed. The job client can also query the job tracker for the job status and statistics.