## Unit 2 - Hadoop

Hadoop is an open-source distributed computing framework that is used to store and process large datasets. It provides a reliable, scalable, and fault-tolerant way to process data across different nodes in a cluster. Here are some key concepts related to Hadoop that you should be familiar with:

### Hadoop Distributed File System (HDFS)

Hadoop Distributed File System (HDFS) is a distributed file system that is designed to store large data sets reliably and efficiently across multiple machines. HDFS has a master-slave architecture where the NameNode acts as the master and DataNodes act as slaves. The NameNode manages the file system namespace and regulates access to files by clients, while the DataNodes store the actual data.

### MapReduce

MapReduce is a programming model used to process large datasets in a distributed environment. It consists of two stages: the map stage and the reduce stage. In the map stage, the input data is divided into chunks and processed by multiple nodes in parallel. In the reduce stage, the intermediate outputs from the map stage are combined to produce the final output.

### Hadoop Cluster

A Hadoop cluster is a group of computers that work together to process large datasets using Hadoop. The cluster consists of a master node, which manages the cluster, and multiple worker nodes, which perform the data processing tasks. Hadoop clusters can scale horizontally by adding more worker nodes to the cluster.

### Advantages of Hadoop

- Hadoop can process large datasets that cannot be processed on a single machine.
- Hadoop provides fault tolerance by replicating data across multiple nodes in the cluster.
- Hadoop is scalable and can handle increasing amounts of data by adding more nodes to the cluster.
- Hadoop is open-source and can be run on commodity hardware, which reduces the cost of deploying a Hadoop cluster.

### Disadvantages of Hadoop

- Hadoop has a steep learning curve and requires knowledge of distributed computing concepts.
- Hadoop has a high overhead for processing small datasets.
- Hadoop does not provide real-time processing capabilities.

### Examples of Hadoop Applications

- Apache Hadoop is used by many companies to process large datasets, including Facebook, Yahoo, and LinkedIn.
- Hadoop is used for log processing, machine learning, and data warehousing.

In conclusion, Hadoop is a powerful distributed computing framework that allows for the processing of large datasets. The Hadoop ecosystem provides many tools and technologies that can be used to build scalable and fault-tolerant data processing systems. Understanding the core concepts of Hadoop is important for anyone working with big data.