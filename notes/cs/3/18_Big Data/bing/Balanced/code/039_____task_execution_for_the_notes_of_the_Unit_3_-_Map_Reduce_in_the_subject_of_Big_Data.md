# Task Execution for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- MapReduce is a programming model that allows processing and generating big data sets with a parallel, distributed algorithm on a cluster.
- MapReduce consists of two phases: Map and Reduce.
- Map phase: This is the first phase in the execution of a MapReduce job. In this phase, the input data is split into small subsets of data called input splits. Each input split is processed by a map function that performs filtering and sorting operations on the data and produces intermediate key-value pairs as output .
- Reduce phase: This is the second phase in the execution of a MapReduce job. In this phase, the intermediate key-value pairs from the map phase are shuffled and sorted by their keys and then passed to a reduce function that performs a summary operation on the values and generates the final output of the MapReduce job .
- MapReduce can run on various platforms, such as Apache Hadoop, Amazon Elastic MapReduce, Google Cloud Platform, etc.
- MapReduce can be used for various applications, such as word count, inverted index, web log analysis, recommendation systems, etc.