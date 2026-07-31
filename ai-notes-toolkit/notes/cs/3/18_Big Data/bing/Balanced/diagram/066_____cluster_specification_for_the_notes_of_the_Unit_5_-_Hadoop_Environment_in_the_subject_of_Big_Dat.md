### Cluster Specification for the Notes of the Unit 5 - Hadoop Environment in the Subject of Big Data

- A Hadoop cluster is a collection of computers, known as nodes, that are networked together to perform parallel computations on big data sets  .
- A Hadoop cluster is designed to store and analyze large amounts of structured, semi-structured, and unstructured data in a distributed environment. It is often referred to as a shared-nothing system because the only thing that is shared between the nodes is the network itself.
- A Hadoop cluster consists of two types of nodes: master nodes and worker nodes .
  - Master nodes are responsible for managing and coordinating the cluster activities, such as scheduling jobs, monitoring resources, and maintaining metadata .
  - Worker nodes are responsible for executing the tasks assigned by the master nodes, such as storing and processing data blocks, and reporting their status to the master nodes .
- A Hadoop cluster can be divided into four distinctive layers:
  - Distributed Storage Layer: Each node in a Hadoop cluster has its own disk space, memory, bandwidth, and processing. The incoming data is split into individual data blocks, which are then stored within the Hadoop Distributed File System (HDFS) distributed storage layer.
  - Data Processing Layer: The data processing layer consists of two frameworks: MapReduce and YARN. MapReduce is a programming model that allows parallel processing of large data sets across the cluster. YARN is a resource management system that allocates and schedules the resources for the MapReduce jobs.
  - Data Abstraction Layer: The data abstraction layer provides various tools and libraries that simplify the data access and manipulation for the users and applications. Some of the examples are Hive, Pig, Spark, and HBase.
  - Application Layer: The application layer is where the users and applications interact with the Hadoop cluster. It provides various interfaces and services that allow the users to query, analyze, and visualize the data stored in the cluster. Some of the examples are Sqoop, Flume, Oozie, and Zeppelin.