#### Cluster Specification in Hadoop Environment

- A Hadoop cluster is a special type of computational cluster designed specifically for storing and analyzing huge amounts of unstructured data in a distributed computing environment  .
- A Hadoop cluster consists of a collection of computers, known as nodes, that are networked together to perform parallel computations on big data sets.
- A Hadoop cluster is often referred to as a shared-nothing system because the only thing that is shared between the nodes is the network itself.
- A Hadoop cluster typically has two types of nodes: master nodes and worker nodes.
- Master nodes are responsible for coordinating the distribution of data and tasks among the worker nodes, as well as maintaining the overall health and status of the cluster.
- Worker nodes are responsible for storing and processing the data assigned to them by the master nodes, as well as reporting their progress and status to the master nodes.
- The most common master nodes in a Hadoop cluster are the NameNode and the JobTracker, while the most common worker nodes are the DataNodes and the TaskTrackers.
- The NameNode is the master node that manages the distributed file system (HDFS) and maintains the metadata of the files and directories stored in the cluster.
- The DataNodes are the worker nodes that store the actual data blocks of the files in the cluster and serve read and write requests from the clients.
- The JobTracker is the master node that manages the execution of MapReduce jobs and assigns tasks to the TaskTrackers.
- The TaskTrackers are the worker nodes that run the tasks of the MapReduce jobs and report their status to the JobTracker.
- To configure the Hadoop cluster, you will need to configure the environment in which the Hadoop daemons execute as well as the configuration parameters for the Hadoop daemons .
- The environment configuration includes setting up the SSH access, the JAVA_HOME variable, and the HADOOP_CONF_DIR variable for the Hadoop daemons.
- The configuration parameters include setting up the core-site.xml, hdfs-site.xml, mapred-site.xml, and yarn-site.xml files for the Hadoop daemons.
- The core-site.xml file contains the basic settings for the Hadoop cluster, such as the default file system URI, the default block size, and the default replication factor.
- The hdfs-site.xml file contains the settings for the HDFS, such as the location of the NameNode and DataNode directories, the checkpoint interval, and the block scanner interval.
- The mapred-site.xml file contains the settings for the MapReduce framework, such as the location of the JobTracker and TaskTracker directories, the number of map and reduce slots, and the memory limits for the tasks.
- The yarn-site.xml file contains the settings for the YARN framework, which is the resource management layer of Hadoop, such as the location of the ResourceManager and NodeManager directories, the resource allocation policies, and the scheduler options.