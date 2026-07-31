# Task Execution for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- MapReduce is a programming model that allows processing and generating big data sets with a parallel, distributed algorithm on a cluster.
- MapReduce consists of two phases: Map and Reduce, which are executed by two types of functions: Map() and Reduce().
- Map() function takes an input key-value pair and produces a set of intermediate key-value pairs. The input and output types of the Map() function can be different.
- Reduce() function takes an intermediate key and a set of values associated with that key, and merges the values to produce a smaller set of values. The input and output types of the Reduce() function are usually the same.
- The execution flow of a MapReduce job occurs as follows:
  - Input data is split into small subsets of data called input splits.
  - Map tasks work on these data splits and apply the Map() function to each record.
  - The intermediate key-value pairs from Map tasks are then partitioned, sorted, and shuffled to the Reduce tasks.
  - The Reduce tasks work on the shuffled data and apply the Reduce() function to each group of values with the same key.
  - The output of the Reduce tasks is written to the distributed file system as the final result of the MapReduce job.
- MapReduce is a scalable and fault-tolerant model that can handle large volumes of data on clusters of commodity hardware.
- MapReduce is widely used for various big data applications, such as data mining, machine learning, text processing, web indexing, and log analysis.