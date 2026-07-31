### Cluster Specification for the Notes of the Unit 5 - Hadoop Environment in the Subject of Big Data

- A Hadoop cluster is a collection of computers, known as nodes, that are networked together to perform parallel computations on big data sets .
- A Hadoop cluster is designed to store and analyze large amounts of structured, semi-structured, and unstructured data in a distributed environment. It is often referred to as a shared-nothing system because the only thing that is shared between the nodes is the network itself.
- A Hadoop cluster consists of two types of nodes: master nodes and worker nodes. Master nodes are responsible for coordinating and managing the cluster, while worker nodes are responsible for storing and processing the data.
- A Hadoop cluster can be divided into four distinctive layers: distributed storage layer, distributed processing layer, resource management layer, and application layer.
- The distributed storage layer is based on the Hadoop Distributed File System (HDFS), which splits the incoming data into individual data blocks and distributes them across the cluster nodes.
- The distributed processing layer is based on the MapReduce framework, which allows the cluster nodes to perform parallel processing of the data blocks using a two-phase approach: map and reduce.
- The resource management layer is based on the Yet Another Resource Negotiator (YARN), which allocates and manages the resources (such as CPU, memory, disk, and network) among the cluster nodes and the applications.
- The application layer is based on the various tools and frameworks that run on top of the Hadoop cluster, such as Hive, Pig, Spark, HBase, etc. These tools and frameworks provide different functionalities and abstractions for the users to interact with the data.