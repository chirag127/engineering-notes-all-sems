## Unit 2 - Hadoop and Map Reduce

Hadoop is an open-source software framework for storing and processing large datasets in a distributed computing environment. It is designed to scale up from a single server to thousands of machines, each offering local computation and storage.

MapReduce is a programming model and an associated implementation for processing and generating large datasets. It is used to split the input data into independent chunks that are processed by the map tasks in a completely parallel manner. The framework sorts the outputs of the maps, which are then input to the reduce tasks.

1. Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce.
2. HDFS is a distributed file system that provides high-throughput access to application data.
3. MapReduce is a software framework for processing large datasets in parallel across a Hadoop cluster.
4. MapReduce works by dividing the input data into independent chunks that are processed by the map tasks in a completely parallel manner.
5. The framework then sorts the outputs of the maps, which are then input to the reduce tasks.
6. The reduce tasks combine the intermediate results to produce the final output.
7. Hadoop is designed to handle large datasets by distributing the data and processing across multiple machines.
8. Hadoop is highly scalable, allowing for the addition of more machines to the cluster as the data grows.
9. Hadoop is fault-tolerant, meaning that it can continue to operate even if individual machines in the cluster fail.
10. Hadoop is widely used in big data applications, including data mining, data analysis, and machine learning.

A mnemonic to remember the steps of the MapReduce process is "MRSORT" - Map, Reduce, Shuffle, Output, Reduce, and Task.

An example of a MapReduce job is counting the number of occurrences of each word in a large text file. The map function would take the input data and output key-value pairs where the key is the word and the value is 1. The reduce function would then sum the values for each key, resulting in the final count for each word.

Advantages of using Hadoop and MapReduce include:
- Scalability: Hadoop can handle large datasets by distributing the data and processing across multiple machines.
- Fault-tolerance: Hadoop can continue to operate even if individual machines in the cluster fail.
- Flexibility: Hadoop can handle structured, semi-structured, and unstructured data.
- Cost-effectiveness: Hadoop is an open-source software, making it a cost-effective solution for big data processing.

Disadvantages of using Hadoop and MapReduce include:
- Complexity: Hadoop and MapReduce can be complex to set up and manage.
- Limited functionality: MapReduce is not suitable for all types of data processing tasks.
- Performance: MapReduce can be slower than other data processing solutions for certain types of tasks.

Applications of Hadoop and MapReduce include:
- Data mining: Hadoop can be used to mine large datasets to discover patterns and insights.
- Data analysis: Hadoop can be used to analyze large datasets to extract useful information.
- Machine learning: Hadoop can be used to train machine learning models on large datasets.
- Log analysis: Hadoop can be used to analyze large log files to identify trends and patterns.