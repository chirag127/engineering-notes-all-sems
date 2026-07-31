#### Hadoop configuration in Hadoop Environment

Hadoop configuration is the process of setting the parameters and properties for the Hadoop daemons and services. Hadoop configuration can be done at different levels, such as HDFS, Yarn, Oozie, etc. Hadoop configuration can be done by editing the XML files in the etc/hadoop directory or by using the hadoop-config command.

Hadoop configuration for HDFS:

HDFS is the distributed file system of Hadoop that stores the data across multiple nodes. HDFS configuration can be done by editing the following XML files:

- core-site.xml: This file contains the core configuration settings for Hadoop, such as the default file system URI, the I/O settings, the RPC settings, etc.
- hdfs-site.xml: This file contains the HDFS-specific configuration settings, such as the replication factor, the block size, the name node and data node directories, etc.
- hadoop-env.sh: This file contains the environment variables for the Hadoop daemons, such as the JAVA_HOME, HADOOP_HOME, HADOOP_CONF_DIR, etc.

Hadoop configuration for Yarn:

Yarn is the resource management and scheduling framework of Hadoop that allocates the resources to the applications running on the cluster. Yarn configuration can be done by editing the following XML files:

- yarn-site.xml: This file contains the Yarn-specific configuration settings, such as the resource manager address, the node manager address, the web app proxy address, the resource allocation settings, etc.
- mapred-site.xml: This file contains the MapReduce-specific configuration settings, such as the map and reduce task settings, the job history server address, the shuffle settings, etc.
- yarn-env.sh: This file contains the environment variables for the Yarn daemons, such as the YARN_HOME, YARN_CONF_DIR, etc.

Hadoop configuration for Oozie:

Oozie is the workflow scheduler and coordinator of Hadoop that executes the jobs based on the predefined dependencies and triggers. Oozie configuration can be done by editing the following XML files:

- oozie-site.xml: This file contains the Oozie-specific configuration settings, such as the Oozie server address, the database settings, the security settings, etc.
- oozie-env.sh: This file contains the environment variables for the Oozie daemon, such as the OOZIE_HOME, OOZIE_CONF_DIR, etc.

To apply the Hadoop configuration changes, the Hadoop daemons need to be restarted. This can be done by using the following commands:

- To stop all the Hadoop daemons: `sbin/stop-all.sh`
- To start all the Hadoop daemons: `sbin/start-all.sh`
- To stop a specific Hadoop daemon: `sbin/hadoop-daemon.sh stop <daemon>`
- To start a specific Hadoop daemon: `sbin/hadoop-daemon.sh start <daemon>`

where `<daemon>` can be one of the following: namenode, secondarynamenode, datanode, resourcemanager, nodemanager, webappproxy, jobhistoryserver, oozie.