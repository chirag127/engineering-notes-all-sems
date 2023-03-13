#### Anatomy of a Map Reduce job run

- A Map Reduce job is a distributed computation that processes a large amount of data in parallel on a cluster of machines.
- A Map Reduce job consists of two phases: the map phase and the reduce phase.
- In the map phase, the input data is split into smaller chunks called input splits, and each input split is assigned to a mapper task.
- A mapper task reads the input split and applies a user-defined map function to each record in the input split, producing a set of intermediate key-value pairs.
- The intermediate key-value pairs are then partitioned and shuffled across the cluster, based on their keys, to the reducer tasks.
- In the reduce phase, each reducer task receives a subset of the intermediate key-value pairs that share the same key, and applies a user-defined reduce function to them, producing a set of final output key-value pairs.
- The final output key-value pairs are then written to the output files in the distributed file system.
- A Map Reduce job is coordinated by a master node called the JobTracker, which assigns tasks to the worker nodes called the TaskTrackers, and monitors their progress and status.
- A Map Reduce job can be configured with various parameters, such as the number of mapper and reducer tasks, the input and output formats, the compression and serialization options, the partitioning and sorting functions, and the combiner and counter functions.