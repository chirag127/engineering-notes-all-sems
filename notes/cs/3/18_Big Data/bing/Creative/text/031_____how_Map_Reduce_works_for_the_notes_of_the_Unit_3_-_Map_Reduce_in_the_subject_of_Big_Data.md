### How MapReduce works

- MapReduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- MapReduce can perform distributed and parallel computations using large datasets across a large number of nodes.
- A MapReduce job usually splits the input datasets and then process each of them independently by the Map tasks in a completely parallel manner. The output is then sorted and input to reduce tasks.
- The MapReduce algorithm contains two important tasks, namely Map and Reduce.
  - Map: each worker node applies the map function to the local data, and writes the output to a temporary storage. A master node ensures that only one copy of the redundant input data is processed.
  - Reduce: the master node collects the outputs of the map tasks and assigns them to reduce tasks. The reduce tasks then combine the outputs of the map tasks to form a smaller set of values.
- MapReduce also supports two optional tasks, namely Combine and Partition.
  - Combine: the combine function is run on each mapper node to perform a local aggregation of the intermediate outputs, which helps to reduce the amount of data transferred to the reducers.
  - Partition: the partition function is used to control the partitioning of the intermediate outputs of the map tasks. The partition function determines which reducer is responsible for a particular key.
- MapReduce generally divides input data into pieces and distributes them among other computers. The input data is broken up into key-value pairs.
- On computers in a cluster, parallel map jobs process the chunked data. The map function takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key-value pairs).
- The framework shuffles and sorts the results before passing them on to the reduce tasks. The reduce function takes the output from the map as input and combines those data tuples into a smaller set of tuples.