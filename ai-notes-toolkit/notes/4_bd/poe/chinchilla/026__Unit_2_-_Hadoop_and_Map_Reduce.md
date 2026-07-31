## Unit 2 - Hadoop and Map Reduce

Hadoop is an open-source framework that is widely used for distributed storage and processing of large-scale data. Map Reduce is a programming model used for processing large data sets in a distributed computing environment. In this unit, we will explore Hadoop and Map Reduce in detail.

### What is Hadoop?

Hadoop is a framework that provides a distributed file system and a set of tools for distributed processing of large-scale data. It is based on the Google File System (GFS) and Map Reduce programming model. Hadoop is designed to scale-out horizontally, meaning it can handle large amounts of data by adding more nodes to the cluster.

### Components of Hadoop

Hadoop consists of the following components:

- Hadoop Distributed File System (HDFS): HDFS is a distributed file system that stores data on multiple nodes in a Hadoop cluster. It provides high-throughput access to large data sets and is designed to handle large files.

- Map Reduce: Map Reduce is a programming model for processing large data sets in a distributed computing environment. It consists of two phases, the map phase, and the reduce phase.

- YARN: Yet Another Resource Negotiator (YARN) is a cluster management technology that enables Hadoop to run a wide variety of applications beyond Map Reduce. It manages resources in a Hadoop cluster and schedules applications to run on the available resources.

### What is Map Reduce?

Map Reduce is a programming model used for processing large data sets in a distributed computing environment. It consists of two phases, the map phase, and the reduce phase. The map phase takes a set of input data and produces a set of intermediate key-value pairs. The reduce phase takes the intermediate key-value pairs and produces a set of output key-value pairs.

### Map Reduce Workflow

The Map Reduce workflow consists of the following steps:

1. Input: The input data is divided into a set of input splits, and each split is processed by a separate map task.

2. Map: The map function is applied to each input split, and intermediate key-value pairs are generated.

3. Shuffle and Sort: The intermediate key-value pairs are shuffled and sorted by key, and the output is written to disk.

4. Reduce: The reduce function is applied to the output of the shuffle and sort phase, and the final output key-value pairs are generated.

5. Output: The final output key-value pairs are written to the output file.

### Advantages of Hadoop and Map Reduce

Hadoop and Map Reduce have several advantages, including:

- Scalability: Hadoop can handle large-scale data by adding more nodes to the cluster.

- Fault tolerance: Hadoop is designed to be fault-tolerant, meaning it can continue to function even if some of the nodes in the cluster fail.

- Flexibility: Map Reduce can be used to process a wide variety of data, including structured, semi-structured, and unstructured data.

- Cost-effective: Hadoop is based on commodity hardware, which makes it more cost-effective than traditional enterprise storage solutions.

### Conclusion

In this unit, we have explored Hadoop and Map Reduce, which are widely used for distributed storage and processing of large-scale data. We have learned about the components of Hadoop, the Map Reduce programming model, and the workflow of Map Reduce. We have also discussed the advantages of Hadoop and Map Reduce, including scalability, fault tolerance, flexibility, and cost-effectiveness.