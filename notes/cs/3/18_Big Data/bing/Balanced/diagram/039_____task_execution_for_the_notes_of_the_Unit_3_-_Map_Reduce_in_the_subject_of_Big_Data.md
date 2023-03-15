### Task Execution for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- MapReduce is a programming model that allows processing and generating big data sets with a parallel, distributed algorithm on a cluster.
- MapReduce consists of two phases: Map and Reduce.
- Map phase: This is the first phase in the execution of a MapReduce job. In this phase, the input data is split into small subsets of data called input splits. Each input split is assigned to a map task that works on it and produces intermediate output values. The map task applies a mapping function to each record in the input split and emits a key-value pair as the output .
- Reduce phase: This is the second phase in the execution of a MapReduce job. In this phase, the intermediate output values from the map tasks are shuffled and sorted by key and then sent to the reduce tasks. The reduce task applies a reducing function to each group of values that share the same key and emits a final output value .
- MapReduce can run on various platforms, such as Apache Hadoop, Amazon Elastic MapReduce, Google Cloud Platform, etc.
- MapReduce can be used for various applications, such as word count, inverted index, web log analysis, recommendation systems, etc.