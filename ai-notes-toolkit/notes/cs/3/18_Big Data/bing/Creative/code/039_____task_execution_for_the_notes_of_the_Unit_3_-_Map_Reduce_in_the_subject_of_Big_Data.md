### Task execution for the notes of the Unit 3 - Map Reduce in the subject of Big Data

- MapReduce is a programming model that allows processing and generating big data sets with a parallel, distributed algorithm on a cluster.
- A MapReduce job consists of two phases: map and reduce, which are executed by two types of functions: map() and reduce().
- The map() function takes an input key-value pair and produces a set of intermediate key-value pairs. The input key-value pair can be a line of text, a record, a document, or any other data unit.
- The reduce() function takes an intermediate key and a set of values associated with that key, and merges those values to produce a smaller set of values or a single value. The output of the reduce() function can be a summary, an aggregation, a filter, or any other transformation of the input values.
- The execution flow of a MapReduce job occurs as follows:
  - Input data is split into small subsets of data called input splits. Input split is a chunk of the input that is consumed by a single map task.
  - Map tasks work on these data splits and apply the map() function to each input key-value pair to produce intermediate key-value pairs. The intermediate key-value pairs are stored in local disks of the map nodes.
  - The intermediate key-value pairs from map tasks are then submitted to reduce tasks after an intermediate process called shuffle. The shuffle process involves sorting and grouping the intermediate key-value pairs by their keys and transferring them to the reduce nodes.
  - The reduce tasks work on the shuffled data and apply the reduce() function to each intermediate key and its associated values to generate the output of the MapReduce job. The output of the reduce tasks is stored in the distributed file system of the cluster.
- MapReduce is a scalable, fault-tolerant, and flexible model that can handle various types of big data analysis, such as word count, inverted index, page rank, k-means clustering, and more  .
- MapReduce can also be implemented on different platforms, such as Apache Hadoop, Apache Spark, Google Cloud Platform, Amazon Web Services, and more  .
- MapReduce can face some challenges, such as straggler tasks, load imbalance, data skew, network congestion, and security issues. These challenges can be addressed by using different techniques, such as speculative execution, dynamic partitioning, data sampling, compression, encryption, and authentication.