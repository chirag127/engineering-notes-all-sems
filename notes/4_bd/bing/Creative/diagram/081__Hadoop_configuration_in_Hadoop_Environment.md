Hadoop configuration in Hadoop environment refers to the process of setting up and customizing the parameters and environment variables for the Hadoop daemons and services. Hadoop daemons include NameNode, DataNode, SecondaryNameNode, JobTracker, TaskTracker, ResourceManager, NodeManager, and WebAppProxy. Hadoop services include HDFS, YARN, MapReduce, and Oozie.

The following diagram illustrates the basic architecture of a Hadoop cluster in a pseudo-distributed mode, where each Hadoop daemon runs in a separate Java process on a single node.

```
+-------------------+
|                   |
|    NameNode       |
|                   |
+-------------------+
|                   |
| SecondaryNameNode |
|                   |
+-------------------+
|                   |
|    DataNode       |
|                   |
+-------------------+
|                   |
|   JobTracker      |
|                   |
+-------------------+
|                   |
|   TaskTracker     |
|                   |
+-------------------+
|                   |
|  ResourceManager   |
|                   |
+-------------------+
|                   |
|   NodeManager     |
|                   |
+-------------------+
|                   |
|   WebAppProxy     |
|                   |
+-------------------+
|                   |
|     Oozie         |
|                   |
+-------------------+
```

To configure the Hadoop cluster, you will need to edit the following files in the etc/hadoop directory:

- hadoop-env.sh: This file sets the environment variables for the Hadoop daemons, such as JAVA_HOME, HADOOP_PID_DIR, HADOOP_*_OPTS, etc.
- core-site.xml: This file sets the core configuration parameters for Hadoop, such as fs.defaultFS, hadoop.tmp.dir, io.file.buffer.size, etc.
- hdfs-site.xml: This file sets the configuration parameters for HDFS, such as dfs.replication, dfs.namenode.name.dir, dfs.datanode.data.dir, etc.
- mapred-site.xml: This file sets the configuration parameters for MapReduce, such as mapreduce.framework.name, mapreduce.jobtracker.address, mapreduce.tasktracker.map.tasks.maximum, etc.
- yarn-site.xml: This file sets the configuration parameters for YARN, such as yarn.resourcemanager.address, yarn.nodemanager.resource.memory-mb, yarn.nodemanager.resource.cpu-vcores, etc.
- oozie-site.xml: This file sets the configuration parameters for Oozie, such as oozie.service.AuthorizationService.security.enabled, oozie.service.HadoopAccessorService.hadoop.configurations, oozie.service.JPAService.create.db.schema, etc.

For more details on the configuration parameters and their values, please refer to the official documentation of Hadoop  .