### Cluster Setup and Installation for Hadoop

- A Hadoop cluster is a collection of machines that run the Hadoop software and store the data in a distributed manner.
- There are three main types of Hadoop clusters: standalone, pseudo-distributed, and fully-distributed.
- Standalone cluster: A single machine that runs all the Hadoop components without any network communication. It is useful for testing and debugging purposes.
- Pseudo-distributed cluster: A single machine that runs all the Hadoop components but simulates a distributed environment by using different ports and configuration files. It is useful for development and learning purposes.
- Fully-distributed cluster: A multi-node cluster that runs the Hadoop components on different machines and communicates over the network. It is useful for production and performance purposes.
- To set up and install a Hadoop cluster, the following steps are required:
  - Install Java on all the machines in the cluster. Java is the prerequisite for running Hadoop. See the [Hadoop Wiki](https://cwiki.apache.org/confluence/display/HADOOP2/Java+version+support) for the supported Java versions.
  - Download a stable version of Hadoop from [Apache mirrors](https://hadoop.apache.org/releases.html) and extract it on all the machines in the cluster. The extracted directory is referred to as `HADOOP_HOME`.
  - Set up the environment variables for Hadoop and Java on all the machines in the cluster. The environment variables include `HADOOP_HOME`, `JAVA_HOME`, and `PATH`.
  - Configure the Hadoop components on all the machines in the cluster. The configuration files are located in the `HADOOP_HOME/etc/hadoop` directory. The main configuration files are:
    - `core-site.xml`: Contains the core settings for Hadoop, such as the default file system and the I/O settings.
    - `hdfs-site.xml`: Contains the settings for the Hadoop Distributed File System (HDFS), such as the replication factor and the block size.
    - `mapred-site.xml`: Contains the settings for the MapReduce framework, such as the job tracker and the task tracker.
    - `yarn-site.xml`: Contains the settings for the Yet Another Resource Negotiator (YARN), such as the resource manager and the node manager.
  - Set up the passphraseless SSH on all the machines in the cluster. This allows the Hadoop components to communicate with each other without prompting for passwords.
  - Format the namenode on the machine that runs the HDFS master. This creates the metadata for the HDFS file system.
  - Start the Hadoop cluster on all the machines in the cluster. This launches the Hadoop daemons, such as the namenode, the datanode, the resource manager, the node manager, etc.
  - Test the Hadoop cluster by running some sample commands and applications. For example, use the `hdfs dfs` command to interact with the HDFS file system, or use the `yarn jar` command to run a MapReduce job.