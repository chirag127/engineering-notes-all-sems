#### Anatomy of a Map Reduce job run

- A Map Reduce job is a unit of work that consists of a map function and a reduce function, applied to a set of input data.
- A Map Reduce job run is the process of executing a Map Reduce job on a cluster of nodes, using a framework such as Hadoop or Spark.
- The anatomy of a Map Reduce job run can be divided into four main phases: split, map, shuffle, and reduce.

##### Split phase

- In the split phase, the input data is divided into fixed-size chunks called input splits, each of which is assigned to a map task.
- The input splits are distributed across the cluster nodes, where the map tasks run in parallel.
- The number of input splits and map tasks depends on the size of the input data and the configuration of the cluster.

##### Map phase

- In the map phase, each map task applies the map function to its assigned input split, producing a set of intermediate key-value pairs.
- The intermediate key-value pairs are stored in the local disk of the node where the map task runs, and are partitioned by a hash function based on the keys.
- The number of partitions and the hash function can be customized by the user.

##### Shuffle phase

- In the shuffle phase, the intermediate key-value pairs are transferred from the map nodes to the reduce nodes, where the reduce tasks run in parallel.
- The shuffle phase involves sorting and merging the intermediate key-value pairs by key, so that all the values associated with the same key are grouped together.
- The shuffle phase can be optimized by using combiners, which are mini-reduce functions that run on the map nodes and aggregate the intermediate key-value pairs by key, reducing the amount of data transferred.

##### Reduce phase

- In the reduce phase, each reduce task applies the reduce function to the sorted and merged intermediate key-value pairs, producing a set of final key-value pairs.
- The final key-value pairs are stored in the output file system, such as HDFS or S3, and can be accessed by the user or other applications.
- The number of reduce tasks and the output file system can be customized by the user.