## Downloading and installing Hadoop; Understanding different Hadoop modes. Startup scripts, Configuration files.

- Hadoop is an open-source framework for distributed storage and processing of large-scale data using clusters of commodity hardware.
- To download and install Hadoop, follow these steps:
  - Download the latest stable release of Hadoop from https://hadoop.apache.org/releases.html
  - Extract the downloaded file to a desired location, such as /usr/local/hadoop
  - Set the environment variables HADOOP_HOME, HADOOP_CONF_DIR, and PATH to point to the Hadoop installation directory, the configuration directory, and the bin directory respectively. For example, in Linux, you can add these lines to your ~/.bashrc file:

    ```bash
    export HADOOP_HOME=/usr/local/hadoop
    export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
    export PATH=$PATH:$HADOOP_HOME/bin
    ```

  - Edit the configuration files in the $HADOOP_CONF_DIR directory, such as core-site.xml, hdfs-site.xml, mapred-site.xml, and yarn-site.xml, to suit your cluster settings and preferences. For example, you can specify the default file system, the replication factor, the memory and CPU allocation, and the scheduler options. You can refer to the official documentation for more details: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html
  - Optionally, you can also enable SSH access to the cluster nodes without password, by generating and copying SSH keys using the ssh-keygen and ssh-copy-id commands. This will allow you to use the start-all.sh and stop-all.sh scripts to start and stop the Hadoop daemons on all nodes from the master node.
- Hadoop can run in different modes, depending on the number and type of nodes in the cluster. The main modes are:
  - Local mode (or standalone mode): This is the default mode, where Hadoop runs as a single Java process on a single node, using the local file system for storage. This mode is useful for testing and debugging purposes, but not for production use.
  - Pseudo-distributed mode: This mode simulates a distributed environment on a single node, where Hadoop runs as multiple Java processes, using the Hadoop Distributed File System (HDFS) for storage. This mode is also useful for testing and debugging purposes, but not for production use.
  - Fully distributed mode (or cluster mode): This is the mode where Hadoop runs on a cluster of multiple nodes, using HDFS for storage and YARN for resource management. This mode is suitable for production use, as it provides high availability, scalability, and fault tolerance.
- Startup scripts are shell scripts that are used to start and stop the Hadoop daemons on the cluster nodes. The main scripts are:
  - start-dfs.sh and stop-dfs.sh: These scripts start and stop the HDFS daemons, namely the NameNode, the SecondaryNameNode, and the DataNodes, on the master and slave nodes respectively.
  - start-yarn.sh and stop-yarn.sh: These scripts start and stop the YARN daemons, namely the ResourceManager and the NodeManagers, on the master and slave nodes respectively.
  - start-all.sh and stop-all.sh: These scripts start and stop both the HDFS and YARN daemons on all nodes. These scripts are deprecated and should be avoided, as they do not provide any error handling or feedback.
  - mr-jobhistory-daemon.sh: This script starts and stops the MapReduce JobHistory server on the master node, which provides a web interface for viewing the job history and statistics.
- Configuration files are XML files that are used to specify the properties and parameters of the Hadoop components and services. The main configuration files are:
  - core-site.xml: This file contains the core configuration of Hadoop, such as the default file system URI, the I/O settings, and the security options.
  - hdfs-site.xml: This file contains the configuration of HDFS, such as the replication factor, the block size, the name directory, and the data directory.
  - mapred-site.xml: This file contains the configuration of MapReduce, such as the framework name, the job tracker address, and the map and reduce task settings.
  - yarn-site.xml: This file contains the configuration of YARN, such as the resource manager address, the node manager address, the memory and CPU allocation, and the scheduler options.