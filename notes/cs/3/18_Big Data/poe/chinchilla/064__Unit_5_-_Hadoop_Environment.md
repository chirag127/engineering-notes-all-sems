## Unit 5 - Hadoop Environment

Hadoop is a distributed computing framework that stores and processes large datasets on clusters of commodity hardware. In this unit, we will explore the Hadoop environment, including its components and their interactions.

### Hadoop Environment Components

The Hadoop environment consists of the following components:

1. Hadoop Distributed File System (HDFS): HDFS is the primary storage system of Hadoop. It stores large files in a distributed manner across multiple machines in a cluster.

2. Yet Another Resource Negotiator (YARN): YARN is the resource management layer of Hadoop. It manages resources such as CPU, memory, and disk space across the cluster.

3. MapReduce: MapReduce is a programming model used to process large datasets in parallel across the Hadoop cluster. It consists of two phases: Map and Reduce.

4. Hadoop Common: Hadoop Common provides the common functionality required by all the Hadoop components, such as logging, configuration, and security.

5. Hadoop Eco-System: Hadoop Eco-System consists of various tools and technologies built on top of Hadoop, such as Pig, Hive, HBase, Spark, etc.

### Hadoop Environment Interactions

The components of the Hadoop environment interact with each other in the following ways:

1. The client machine sends a request to the NameNode, which is the master node of HDFS. The NameNode responds with the location of the data requested by the client.

2. The client machine sends a job request to the Resource Manager, which is the master node of YARN. The Resource Manager assigns resources to the job and schedules it on the appropriate Node Manager.

3. The MapReduce program runs on the assigned Node Manager, which reads the data from HDFS, processes it, and writes the output back to HDFS.

4. The Hadoop Eco-System tools interact with Hadoop components to provide additional functionality, such as data analysis, querying, and visualization.

### Conclusion

In this unit, we have learned about the components of the Hadoop environment and their interactions. Understanding the Hadoop environment is essential for developing and deploying Hadoop applications. In the next unit, we will delve deeper into HDFS, the primary storage system of Hadoop.