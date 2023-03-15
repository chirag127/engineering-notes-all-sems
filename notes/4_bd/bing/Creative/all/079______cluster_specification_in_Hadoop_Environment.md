# Cluster Specification in Hadoop Environment

- A Hadoop cluster is a special type of computational cluster designed specifically for storing and analyzing huge amounts of unstructured data in a distributed computing environment  .
- A Hadoop cluster is often referred to as a shared-nothing system because the only thing that is shared between the nodes is the network itself.
- A Hadoop cluster consists of a collection of computers, known as nodes, that are networked together to perform parallel computations on big data sets.
- A Hadoop cluster has two types of nodes: master nodes and worker nodes.
- Master nodes are responsible for coordinating the tasks and managing the resources of the cluster. They run the Hadoop daemons such as NameNode, SecondaryNameNode, JobTracker, and ResourceManager .
- Worker nodes are responsible for executing the tasks and storing the data. They run the Hadoop daemons such as DataNode and TaskTracker .
- A Hadoop cluster can be configured by setting the environment variables and the configuration parameters for the Hadoop daemons .
- A Hadoop cluster can be scaled up or down by adding or removing nodes as needed. The Hadoop framework is designed to handle node failures and data replication automatically.