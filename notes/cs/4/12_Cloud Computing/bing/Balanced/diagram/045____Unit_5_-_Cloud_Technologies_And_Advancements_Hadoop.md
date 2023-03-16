## Unit 5 - Cloud Technologies And Advancements Hadoop

Hadoop is a framework of the open source set of tools distributed under Apache License. It is used to manage data, store data, and process data for various big data applications running under clustered systems.

Some of the main features and benefits of Hadoop are:

- It can handle large datasets ranging from gigabytes to petabytes of data.
- It can scale up from a single computer to thousands of clustered computers, with each machine offering local computation and storage .
- It can provide massive storage for any kind of data, such as structured, unstructured, or semi-structured data.
- It can provide enormous processing power and the ability to handle virtually limitless concurrent tasks or jobs.
- It can use simple programming models, such as MapReduce, to distribute the data and computation across the cluster.
- It can be resilient to failures, as it replicates the data across multiple nodes and can recover from node failures.
- It can be compatible with various data sources and formats, such as text, images, videos, XML, JSON, etc.
- It can be integrated with other tools and frameworks, such as Spark, Hive, Pig, etc., to perform different types of data analysis.

Hadoop consists of four main components:

- Hadoop Distributed File System (HDFS): It is the storage layer of Hadoop that stores the data in a distributed manner across the cluster. It splits the data into blocks and replicates them across multiple nodes for fault tolerance.
- Hadoop MapReduce: It is the processing layer of Hadoop that performs the parallel processing of the data using the MapReduce programming model. It consists of two phases: map and reduce. The map phase applies a function to each data block and produces intermediate key-value pairs. The reduce phase aggregates the intermediate key-value pairs based on the keys and produces the final output.
- Hadoop YARN: It is the resource management layer of Hadoop that allocates the resources and schedules the tasks across the cluster. It consists of two components: a resource manager that manages the resources of the cluster, and a node manager that manages the resources of each node.
- Hadoop Common: It is the utility layer of Hadoop that provides the common libraries and utilities that are used by the other components. It also provides the interfaces and protocols for communication and data transfer between the components.

Hadoop is one of the most popular and widely used frameworks for big data processing and analysis. It has many applications in various domains, such as web analytics, social media analysis, recommendation systems, fraud detection, etc.