

### Cluster Setup and Installation in Hadoop Environment

* Hadoop is an open-source software framework for distributed storage and processing of large datasets on computer clusters. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage.
* Clusters in Hadoop are made up of a set of machines (nodes) connected to each other through a network. Each node can be a master node or a slave node. The master node is responsible for allocating resources and scheduling tasks. The slave nodes are responsible for executing tasks.
* To set up a Hadoop cluster, the following steps need to be taken:
  1. Install the Hadoop software on all the nodes in the cluster.
  2. Configure the cluster by setting up the master and slave nodes.
  3. Set up a distributed file system (DFS) across all the nodes in the cluster.
  4. Set up the required services such as HDFS, YARN, MapReduce, Pig, Hive, etc.
  5. Set up the security features such as authentication and authorization.
* Once the cluster is set up, applications can be deployed on the cluster.
* Mnemonics and learning tricks:
  * Hadoop: Helping Allocate Resources On Parallel Processors
  * HDFS: Hadoop Distributed File System
  * YARN: Yet Another Resource Negotiator
  * MapReduce: Map (input) -> Reduce (output)