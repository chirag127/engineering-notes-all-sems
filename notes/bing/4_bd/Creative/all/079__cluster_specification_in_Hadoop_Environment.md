#### Cluster specification in Hadoop Environment

- A Hadoop cluster is a special type of computational cluster designed specifically for storing and analyzing huge amounts of unstructured data in a distributed computing environment .
- A Hadoop cluster is often referred to as a shared-nothing system because the only thing that is shared between the nodes is the network itself.
- A Hadoop cluster consists of a network of master and slave nodes that are connected to each other. The master nodes are responsible for managing the cluster resources and coordinating the data processing tasks, while the slave nodes are responsible for storing and processing the data.
- The main components of a Hadoop cluster are:
  - Hadoop Distributed File System (HDFS): A distributed file system that provides high-throughput access to the data stored in the cluster. HDFS consists of a NameNode that manages the file system metadata and a number of DataNodes that store the actual data blocks .
  - MapReduce: A programming model and framework for parallel data processing on large-scale datasets. MapReduce consists of a JobTracker that assigns and monitors the data processing tasks and a number of TaskTrackers that execute the tasks on the DataNodes .
  - YARN: A resource management layer that allocates and manages the cluster resources for different applications running on the cluster. YARN consists of a Resource Manager that arbitrates the cluster resources and a number of Node Managers that monitor and report the resource usage of the nodes.
- The types of Hadoop clusters are:
  - Single-node cluster: A cluster with only one node that acts as both master and slave. This type of cluster is suitable for testing and development purposes, but not for production use.
  - Multi-node cluster: A cluster with more than one node that are configured as master and slave nodes. This type of cluster is suitable for production use and can scale up to thousands of nodes.
  - Pseudo-distributed cluster: A cluster with only one node that acts as both master and slave, but runs multiple processes to simulate the distributed environment. This type of cluster is suitable for testing and development purposes, but not for production use.

- A possible mnemonic to remember the components of a Hadoop cluster is: **H**ave **M**any **Y**ummy **M**apReduce **H**amburgers, where H stands for HDFS, M stands for master nodes, Y stands for YARN, and H stands for slave nodes.