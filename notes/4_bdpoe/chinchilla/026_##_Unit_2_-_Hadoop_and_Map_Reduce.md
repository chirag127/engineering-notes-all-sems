## Unit 2 - Hadoop and Map Reduce

Hadoop is an open-source framework that is used for distributed storage and processing of large data sets on commodity hardware. It provides a distributed file system (HDFS) and a framework for distributed processing of large data sets using the MapReduce programming model.

MapReduce is a programming model for processing large data sets in a distributed environment. It works by splitting the input data set into independent chunks, which are processed in parallel across multiple nodes in a cluster. The output of each node is then combined to produce the final output.

### Hadoop Architecture

Hadoop consists of the following components:

- HDFS: Hadoop Distributed File System, which is used to store and manage large data sets across multiple nodes in a cluster.
- MapReduce: A programming model for distributed processing of large data sets.
- YARN: Yet Another Resource Negotiator, which is used to manage resources in a Hadoop cluster and schedule jobs for MapReduce.
- Hadoop Common: A set of common libraries and utilities used by other Hadoop components.

### MapReduce Workflow

The MapReduce workflow consists of the following steps:

1. Input data is divided into independent chunks and distributed across nodes in a cluster.
2. Map function is applied to each chunk of data in parallel to generate intermediate key-value pairs.
3. Shuffle and Sort phase: The intermediate key-value pairs are sorted and grouped by key.
4. Reduce function is applied to each group of intermediate key-value pairs in parallel to generate the final output.

### Advantages of Hadoop and MapReduce

- Hadoop is highly scalable and can handle large data sets that cannot be processed by traditional systems.
- Hadoop is fault-tolerant and can continue to function even if a node in the cluster fails.
- Hadoop is open-source and can be run on commodity hardware, making it cost-effective.
- MapReduce is a simple and easy-to-use programming model for distributed processing of large data sets.

### Disadvantages of Hadoop and MapReduce

- Hadoop has a steep learning curve and requires knowledge of Java programming.
- Hadoop requires a large amount of storage and processing power, which can be expensive to set up and maintain.
- Hadoop is not suitable for real-time processing of data.

### Learning Tricks

- Mnemonic: "Hadoop Has Distributed File System" can help in remembering the components of Hadoop.
- To understand the MapReduce workflow, remember the acronym "MRSR" which stands for Map, Reduce, Shuffle, and Sort.
- Practice coding MapReduce programs on small data sets before moving on to larger data sets to get a better understanding of the programming model.