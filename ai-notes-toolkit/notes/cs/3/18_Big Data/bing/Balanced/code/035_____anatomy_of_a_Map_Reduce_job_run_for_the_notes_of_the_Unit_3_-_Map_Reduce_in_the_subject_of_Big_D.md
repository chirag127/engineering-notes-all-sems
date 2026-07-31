### Anatomy of a Map Reduce job run

- A Map Reduce job is a unit of work that consists of a map function and a reduce function, applied to a set of input data.
- A Map Reduce job run is the process of executing a Map Reduce job on a cluster of nodes, using a framework such as Hadoop or Spark.
- The anatomy of a Map Reduce job run can be divided into four phases: input, map, shuffle, and reduce.

#### Input phase

- In the input phase, the input data is split into fixed-size chunks called input splits, each of which is assigned to a map task.
- The input data can be stored in various formats and sources, such as text files, binary files, databases, or distributed file systems.
- The input splits are distributed across the cluster nodes, where the map tasks are executed.

#### Map phase

- In the map phase, each map task applies the map function to its assigned input split, producing a set of intermediate key-value pairs.
- The map function is user-defined and can perform any kind of transformation, filtering, or aggregation on the input data.
- The intermediate key-value pairs are stored in local files on the same node where the map task is executed.

#### Shuffle phase

- In the shuffle phase, the intermediate key-value pairs are transferred from the map nodes to the reduce nodes, based on the intermediate keys.
- The shuffle phase is performed by the framework and is transparent to the user.
- The shuffle phase ensures that all the intermediate values for a given key are sent to the same reduce node, where they can be combined by the reduce function.

#### Reduce phase

- In the reduce phase, each reduce task applies the reduce function to the intermediate values for each key, producing a set of final output key-value pairs.
- The reduce function is user-defined and can perform any kind of aggregation, summarization, or computation on the intermediate values.
- The final output key-value pairs are stored in output files on the reduce nodes, or sent to other destinations, such as databases or distributed file systems.