### Task Execution for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- MapReduce is a programming model that allows processing and generating big data sets with a parallel, distributed algorithm on a cluster.
- MapReduce consists of two phases: Map and Reduce, which are executed by two types of functions: map() and reduce().
- The map() function takes an input key-value pair and produces a set of intermediate key-value pairs. The intermediate keys are grouped by a partitioner and sent to different reducers.
- The reduce() function takes an intermediate key and a set of values associated with that key, and merges those values to produce a smaller set of values, or a single value. The output of the reduce() function is the final result of the MapReduce job.
- The execution flow of a MapReduce job is as follows:
  - Input data is split into small subsets of data, called input splits. Each input split is assigned to a map task, which runs on a node in the cluster.
  - Map tasks work on the input splits and apply the map() function to each key-value pair in the split. The output of the map() function is a set of intermediate key-value pairs, which are stored in the local disk of the node.
  - The intermediate key-value pairs are then shuffled and sorted by a process called shuffle and sort. The shuffle and sort process transfers the intermediate data from the map tasks to the reduce tasks, based on the partitioning of the intermediate keys. The partitioning determines which reducer will receive which intermediate key.
  - The reduce tasks work on the shuffled and sorted intermediate data and apply the reduce() function to each intermediate key and its associated values. The output of the reduce() function is a set of final key-value pairs, which are stored in the distributed file system of the cluster.
  - The final output of the MapReduce job can be retrieved from the distributed file system by the client application.