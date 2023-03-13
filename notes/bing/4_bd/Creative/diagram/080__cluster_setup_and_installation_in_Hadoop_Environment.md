A cluster setup and installation in Hadoop environment involves the following steps:

- Installing the required software on all the nodes in the cluster, such as Java, SSH, and Hadoop.
- Unpacking the Hadoop software on all the nodes or installing it via a packaging system as appropriate for your operating system.
- Dividing up the hardware into functions, such as NameNode, DataNode, JobTracker, and TaskTracker. Typically, one machine in the cluster is designated as the NameNode and another machine as the JobTracker, exclusively. These are the masters. The rest of the machines in the cluster act as both DataNode and TaskTracker. These are the workers.
- Configuring the environment variables, such as JAVA_HOME, HADOOP_HOME, HADOOP_CONF_DIR, etc.
- Configuring the Hadoop configuration files, such as core-site.xml, hdfs-site.xml, mapred-site.xml, etc. These files specify the properties of the cluster, such as the location of the NameNode, the replication factor, the memory and CPU allocation, etc.
- Formatting the Hadoop file system (HDFS) on the NameNode.
- Starting the Hadoop daemons on all the nodes, such as NameNode, DataNode, JobTracker, and TaskTracker.
- Verifying the status of the cluster using web interfaces or command-line tools, such as jps, hadoop dfsadmin, hadoop job, etc.

The following diagram illustrates the basic architecture of a Hadoop cluster:

```
+-----------------+    +-----------------+    +-----------------+
|     Client      |    |     Client      |    |     Client      |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
+-----------------+    +-----------------+    +-----------------+
|     NameNode     |    |    JobTracker    |    |  Secondary NN   |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
+-----------------+    +-----------------+    +-----------------+
|    DataNode     |    |    DataNode     |    |    DataNode     |
|   TaskTracker   |    |   TaskTracker   |    |   TaskTracker   |
+-----------------+    +-----------------+    +-----------------+
```