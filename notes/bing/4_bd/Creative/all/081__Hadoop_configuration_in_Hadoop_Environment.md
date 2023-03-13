#### Hadoop configuration in Hadoop Environment

- Hadoop configuration is the process of setting up the parameters and properties of the Hadoop system, such as the number of nodes, the memory size, the block size, the replication factor, the network topology, the security settings, etc.
- Hadoop configuration files are XML files that contain the key-value pairs of the configuration properties and their values. These files are stored in the $HADOOP_CONF_DIR directory, which is usually /etc/hadoop/conf or /usr/local/hadoop/etc/hadoop.
- The main Hadoop configuration files are:
  - core-site.xml: This file contains the core settings of the Hadoop system, such as the default file system URI, the I/O settings, the RPC settings, etc.
  - hdfs-site.xml: This file contains the settings of the Hadoop Distributed File System (HDFS), such as the block size, the replication factor, the name node and data node directories, the checkpoint settings, etc.
  - mapred-site.xml: This file contains the settings of the MapReduce framework, such as the job tracker and task tracker addresses, the number of map and reduce tasks, the resource allocation, the compression settings, etc.
  - yarn-site.xml: This file contains the settings of the Yet Another Resource Negotiator (YARN), which is the resource management layer of Hadoop, such as the resource manager and node manager addresses, the scheduler settings, the container settings, the security settings, etc.
- To configure Hadoop in a Hadoop environment, the following steps are required:
  - Edit the configuration files according to the desired settings and the cluster specifications. For example, set the fs.defaultFS property in core-site.xml to the name node URI, set the dfs.replication property in hdfs-site.xml to the desired replication factor, set the mapreduce.framework.name property in mapred-site.xml to yarn, set the yarn.resourcemanager.hostname property in yarn-site.xml to the resource manager hostname, etc.
  - Copy the configuration files to all the nodes in the cluster. This can be done using the scp command or the Hadoop distributed copy command (distcp).
  - Restart the Hadoop services on all the nodes. This can be done using the start-all.sh script or the start-dfs.sh and start-yarn.sh scripts.
- Some mnemonics and learning tricks for Hadoop configuration are:
  - Remember the four main configuration files by the acronym CHMY: Core, HDFS, MapReduce, YARN.
  - Remember the default configuration directory by the acronym CHEC: /etc/hadoop/conf.
  - Remember the default file system URI by the acronym HDFS: hdfs://namenode:port.
  - Remember the default replication factor by the number 3: dfs.replication=3.