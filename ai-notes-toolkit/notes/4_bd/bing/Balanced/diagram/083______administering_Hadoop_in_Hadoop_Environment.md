Administering Hadoop in Hadoop Environment involves setting up, configuring, monitoring, and maintaining a cluster of Hadoop nodes that run various Hadoop services and applications. A Hadoop administrator is responsible for ensuring the availability, performance, security, and scalability of the Hadoop cluster, as well as troubleshooting any issues that may arise.

A Hadoop cluster consists of a master node and one or more worker nodes. The master node runs the NameNode service, which manages the metadata of the Hadoop Distributed File System (HDFS), and the ResourceManager service, which allocates resources and schedules tasks for the worker nodes. The worker nodes run the DataNode service, which stores the actual data blocks of HDFS, and the NodeManager service, which executes the tasks assigned by the ResourceManager. Optionally, the master node can also run a SecondaryNameNode service, which performs periodic checkpoints of the NameNode metadata, and a WebAppProxy service, which provides a web interface for accessing the Hadoop applications.

To administer a Hadoop cluster, one needs to set up the environment variables, configuration files, and scripts for the Hadoop daemons on each node. The environment variables include JAVA_HOME, which specifies the location of the Java installation, and HADOOP_CLIENT_OPTS, which specifies the Java options and Hadoop options for the end-user operations. The configuration files include core-site.xml, which defines the common properties for the Hadoop cluster, such as the HDFS URI and the default file system; hdfs-site.xml, which defines the properties for the HDFS, such as the replication factor and the block size; mapred-site.xml, which defines the properties for the MapReduce framework, such as the map and reduce task memory and the number of reducers; and yarn-site.xml, which defines the properties for the YARN framework, such as the resource manager address and the node manager memory and CPU. The scripts include hadoop-env.sh, which sets the environment variables for the Hadoop daemons; mapred-env.sh, which sets the environment variables for the MapReduce daemons; and yarn-env.sh, which sets the environment variables for the YARN daemons.

The following is a possible ASCII diagram for administering Hadoop in Hadoop Environment:

#### Administering Hadoop in Hadoop Environment

```
+-----------------+       +-----------------+
| Master Node     |       | Worker Node     |
|                 |       |                 |
| +-------------+ |       | +-------------+ |
| | NameNode    | |       | | DataNode    | |
| | (HDFS)      | |       | | (HDFS)      | |
| +-------------+ |       | +-------------+ |
|                 |       |                 |
| +-------------+ |       | +-------------+ |
| | ResourceManager|<---->| | NodeManager | |
| | (YARN)      | |       | | (YARN)      | |
| +-------------+ |       | +-------------+ |
|                 |       |                 |
| +-------------+ |       |                 |
| | SecondaryNameNode|    |                 |
| | (HDFS)      | |       |                 |
| +-------------+ |       |                 |
|                 |       |                 |
| +-------------+ |       |                 |
| | WebAppProxy | |       |                 |
| | (YARN)      | |       |                 |
| +-------------+ |       |                 |
+-----------------+       +-----------------+
```