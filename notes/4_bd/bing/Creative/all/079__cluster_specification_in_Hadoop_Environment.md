#### Cluster specification in Hadoop Environment

- A Hadoop cluster is a special type of computational cluster designed specifically for storing and analyzing huge amounts of unstructured data in a distributed computing environment.
- A Hadoop cluster is often referred to as a shared-nothing system because the only thing that is shared between the nodes is the network itself.
- A Hadoop cluster consists of two types of nodes: master nodes and worker nodes.
- Master nodes are responsible for managing the cluster resources and coordinating the data processing tasks. There are two master nodes in a Hadoop cluster: NameNode and ResourceManager.
- NameNode is the master node for the Hadoop Distributed File System (HDFS), which is the storage layer of Hadoop. It maintains the metadata of the files and directories stored in HDFS, such as the location of the data blocks, the replication factor, the permissions, etc. It also handles the requests from the clients to read or write data to HDFS.
- ResourceManager is the master node for the Hadoop YARN (Yet Another Resource Negotiator), which is the resource management and scheduling layer of Hadoop. It allocates the cluster resources (such as CPU, memory, disk, network) to the applications running on the cluster, and monitors their status and progress. It also interacts with the NodeManagers, which are the worker nodes for YARN.
- Worker nodes are the nodes that perform the actual data processing tasks assigned by the master nodes. There are two types of worker nodes in a Hadoop cluster: DataNode and NodeManager.
- DataNode is the worker node for HDFS. It stores the data blocks of the files in HDFS on its local disk, and serves the read and write requests from the clients or other DataNodes. It also reports the status of its data blocks to the NameNode periodically.
- NodeManager is the worker node for YARN. It manages the containers, which are the units of execution for the applications running on the cluster. It launches and monitors the containers, and reports their resource usage and health to the ResourceManager. It also communicates with the ApplicationMaster, which is the process that coordinates the execution of a specific application on the cluster.
- A Hadoop cluster can be set up in different modes, such as single-node mode, pseudo-distributed mode, fully-distributed mode, or high-availability mode, depending on the number of nodes and the configuration of the cluster.
- A Hadoop cluster can be configured by editing the configuration files in the etc/hadoop directory of the Hadoop distribution, such as core-site.xml, hdfs-site.xml, yarn-site.xml, mapred-site.xml, hadoop-env.sh, yarn-env.sh, etc .
- A Hadoop cluster can be monitored and managed by using the web interfaces provided by the master nodes, such as the NameNode web UI, the ResourceManager web UI, the JobHistory web UI, etc .
- A Hadoop cluster can be started and stopped by using the scripts in the bin directory of the Hadoop distribution, such as start-all.sh, stop-all.sh, start-dfs.sh, stop-dfs.sh, start-yarn.sh, stop-yarn.sh, etc .
- A Hadoop cluster can be made aware of the physical topology of the network by using the rack awareness feature, which maps the nodes to the racks they belong to. This can improve the data locality and the fault tolerance of the cluster.

The following is an example of a fully-distributed Hadoop cluster with four nodes: one master node (M) and three worker nodes (W1, W2, W3). The master node runs the NameNode and the ResourceManager, and the worker nodes run the DataNode and the NodeManager. The cluster also has a SecondaryNameNode (S), which is an optional node that performs periodic checkpoints of the NameNode metadata.

```
+-----------------+      +-----------------+
| NameNode (M)    |      | SecondaryNameNode (