## Downloading and installing Hadoop; Understanding different Hadoop modes. Startup scripts, Configuration files.

- Hadoop is an open-source framework for distributed storage and processing of large-scale data sets using clusters of commodity hardware.
- To download and install Hadoop, follow these steps:
  - Visit the official website of Hadoop at https://hadoop.apache.org/ and download the latest stable release of Hadoop.
  - Extract the downloaded file to a desired location on your system.
  - Set the environment variables for Hadoop by editing the ~/.bashrc file and adding the following lines:

    ```bash
    export HADOOP_HOME=/path/to/hadoop
    export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
    export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
    ```

  - Save and close the file, and run the command `source ~/.bashrc` to apply the changes.
  - Verify the installation by running the command `hadoop version` and checking the output.

- Hadoop can run in different modes depending on the configuration and the number of nodes in the cluster. The main modes are:
  - Standalone mode: This is the default mode of Hadoop, where it runs as a single Java process on a single node, without using HDFS or YARN. This mode is useful for testing and debugging purposes, but not for production use.
  - Pseudo-distributed mode: This mode simulates a distributed environment by running all the Hadoop daemons (namenode, datanode, resourcemanager, nodemanager, etc.) on a single node, using HDFS and YARN. This mode is useful for development and learning purposes, but not for production use.
  - Fully-distributed mode: This is the mode where Hadoop runs on a cluster of multiple nodes, using HDFS and YARN. This mode is suitable for production use, as it provides high availability, scalability, and fault tolerance.

- Startup scripts are the scripts that are used to start and stop the Hadoop daemons on the cluster nodes. They are located in the $HADOOP_HOME/sbin directory. Some of the common scripts are:
  - start-dfs.sh: This script starts the HDFS daemons (namenode, datanode, secondary namenode, etc.) on the cluster nodes.
  - stop-dfs.sh: This script stops the HDFS daemons on the cluster nodes.
  - start-yarn.sh: This script starts the YARN daemons (resourcemanager, nodemanager, etc.) on the cluster nodes.
  - stop-yarn.sh: This script stops the YARN daemons on the cluster nodes.
  - start-all.sh: This script starts both the HDFS and YARN daemons on the cluster nodes.
  - stop-all.sh: This script stops both the HDFS and YARN daemons on the cluster nodes.

- Configuration files are the files that are used to customize the behavior and settings of Hadoop and its components. They are located in the $HADOOP_CONF_DIR directory. Some of the important configuration files are:
  - core-site.xml: This file contains the core configuration settings for Hadoop, such as the default file system URI, the I/O buffer size, the replication factor, etc.
  - hdfs-site.xml: This file contains the configuration settings for HDFS, such as the namenode and datanode directories, the block size, the checkpoint interval, etc.
  - yarn-site.xml: This file contains the configuration settings for YARN, such as the resourcemanager and nodemanager addresses, the memory and CPU allocation, the scheduler type, etc.
  - mapred-site.xml: This file contains the configuration settings for MapReduce, such as the framework name, the job tracker address, the map and reduce task numbers, etc.