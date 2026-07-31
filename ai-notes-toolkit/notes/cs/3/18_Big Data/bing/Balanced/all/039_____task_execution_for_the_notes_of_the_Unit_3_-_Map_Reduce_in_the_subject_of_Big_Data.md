# Task Execution for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- MapReduce is a programming model that allows processing and generating big data sets with a parallel, distributed algorithm on a cluster.
- MapReduce consists of two phases: Map and Reduce.
- Map phase: This is the first phase in the execution of a MapReduce job. In this phase, the input data is split into small subsets of data called input splits. Each input split is assigned to a map task that works on it and produces intermediate key-value pairs as output .
- Reduce phase: This is the second phase in the execution of a MapReduce job. In this phase, the intermediate key-value pairs from the map tasks are shuffled and sorted by their keys and then sent to the reduce tasks. Each reduce task works on a subset of keys and values and performs a summary operation on them to generate the final output .
- MapReduce can be implemented using various frameworks, such as Apache Hadoop, Apache Spark, or cloud systems like Amazon Elastic MapReduce (EMR)  .
- MapReduce can be used for various applications, such as word count, inverted index, web log analysis, machine learning, and data mining .
- MapReduce can also face some challenges, such as straggler tasks, load balancing, fault tolerance, and security.