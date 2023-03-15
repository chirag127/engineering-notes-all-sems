### Setting up a Hadoop cluster

A Hadoop cluster is a collection of computers, known as nodes, that are networked together to perform distributed processing of large data sets using the Hadoop framework. A Hadoop cluster can be classified into two types: single-node cluster and multi-node cluster.

A single-node cluster is a cluster that consists of only one node, which acts as both the master and the slave. A single-node cluster is useful for testing and development purposes, but not for production or large-scale data analysis.

A multi-node cluster is a cluster that consists of multiple nodes, which are divided into two roles: master and slave. A master node is responsible for coordinating and managing the cluster, while a slave node is responsible for storing and processing the data. A multi-node cluster can scale up to thousands of nodes and handle petabytes of data.

The steps to set up a Hadoop cluster are as follows:

1. Install Java on all the nodes, as Hadoop is written in Java and requires Java Runtime Environment (JRE) to run.
2. Download and extract the Hadoop distribution from the official website (https://hadoop.apache.org/) on all the nodes. The latest stable version is 3.3.1 as of March 2023.
3. Configure the Hadoop environment variables on all the nodes by editing the ~/.bashrc file and adding the following lines:

```bash
export JAVA_HOME=/path/to/java
export HADOOP_HOME=/path/to/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

4. Configure the Hadoop configuration files on all the nodes by editing the following files in the $HADOOP_HOME/etc/hadoop directory:

- core-site.xml: This file contains the core configuration of the Hadoop cluster, such as the location of the Hadoop file system (HDFS) name node and the default block size.
- hdfs-site.xml: This file contains the configuration of the HDFS, such as the replication factor and the directories for storing the data and metadata.
- mapred-site.xml: This file contains the configuration of the MapReduce framework, such as the number of map and reduce tasks and the memory allocation for each task.
- yarn-site.xml: This file contains the configuration of the YARN (Yet Another Resource Negotiator) framework, which is responsible for managing the resources and scheduling the jobs in the cluster.
- slaves: This file contains the list of slave nodes in the cluster, one per line.

5. Format the HDFS on the master node by running the following command:

```bash
hdfs namenode -format
```

This command will initialize the HDFS and create the metadata for the name node.

6. Start the Hadoop cluster by running the following command on the master node:

```bash
start-all.sh
```

This command will start the name node, the data nodes, the resource manager, and the node managers on the respective nodes.

7. Verify the status of the Hadoop cluster by running the following commands on the master node:

```bash
jps
```

This command will show the Java processes running on the node. You should see the following processes: NameNode, DataNode, ResourceManager, NodeManager, and Jps.

```bash
hdfs dfsadmin -report
```

This command will show the report of the HDFS, such as the number of live and dead data nodes, the total and used capacity, and the block information.

```bash
yarn node -list
```

This command will show the list of node managers in the cluster, along with their status and resource usage.

You can also use the web interfaces to monitor the Hadoop cluster, such as:

- http://master-node:9870/ for the name node
- http://master-node:8088/ for the resource manager
- http://slave-node:9864/ for the data node
- http://slave-node:8042/ for the node manager

8. Stop the Hadoop cluster by running the following command on the master node:

```bash
stop-all.sh
```

This command will stop the name node, the data nodes, the resource manager, and the node managers on the respective nodes.