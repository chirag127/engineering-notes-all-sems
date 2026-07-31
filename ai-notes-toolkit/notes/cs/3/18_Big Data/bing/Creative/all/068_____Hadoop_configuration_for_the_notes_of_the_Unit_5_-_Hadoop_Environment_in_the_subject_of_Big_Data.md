# Hadoop Configuration

Hadoop configuration is the process of setting the parameters and properties of the Hadoop system and its components, such as HDFS, YARN, and MapReduce. Hadoop configuration files are XML files that contain the key-value pairs of the configuration options and their values. Hadoop configuration files are stored in the HADOOP_CONF_DIR directory, which is usually /etc/hadoop on Linux systems.

Some of the main Hadoop configuration files are:

- core-site.xml: This file contains the core configuration of the Hadoop system, such as the default file system URI, the I/O settings, and the security options.
- hdfs-site.xml: This file contains the configuration of the Hadoop Distributed File System (HDFS), such as the replication factor, the block size, and the name node and data node directories.
- yarn-site.xml: This file contains the configuration of the Yet Another Resource Negotiator (YARN), which is the resource management and scheduling framework of Hadoop, such as the resource manager and node manager addresses, the memory and CPU allocation, and the application master settings.
- mapred-site.xml: This file contains the configuration of the MapReduce framework, which is the data processing engine of Hadoop, such as the map and reduce task settings, the job tracker and task tracker addresses, and the output compression options.

To configure the Hadoop cluster, you will need to edit these files according to your cluster specifications and requirements. You will also need to configure the environment variables and the SSH settings for the Hadoop daemons, such as the name node, the data node, the resource manager, the node manager, and the job tracker. You can use the start-all.sh and stop-all.sh scripts to start and stop the Hadoop daemons on the cluster nodes. You can also use the hadoop command to run various Hadoop commands and utilities.