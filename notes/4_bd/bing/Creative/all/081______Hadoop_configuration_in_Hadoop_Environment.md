#### Hadoop configuration in Hadoop Environment

- Hadoop configuration is the process of setting up the parameters and properties for the Hadoop daemons and services that run in a Hadoop cluster.
- Hadoop configuration can be done by editing the XML files in the etc/hadoop directory of the Hadoop installation, or by using the Hadoop configuration command-line tool.
- Hadoop configuration can be divided into three main categories: HDFS, YARN, and Oozie.

  - HDFS configuration: HDFS is the distributed file system that stores the data in a Hadoop cluster. HDFS configuration involves setting the parameters for the NameNode, the SecondaryNameNode, and the DataNodes. Some of the important HDFS configuration files are:

    - core-site.xml: This file contains the core configuration settings for HDFS, such as the default file system URI, the default block size, and the default replication factor.
    - hdfs-site.xml: This file contains the HDFS-specific configuration settings, such as the directories for storing the NameNode and DataNode metadata, the number of backup NameNodes, and the permissions and quotas for HDFS directories and files.
    - hadoop-env.sh: This file contains the environment variables for the Hadoop daemons, such as the Java home directory, the heap size, and the log directory.

  - YARN configuration: YARN is the resource management and scheduling framework that allocates the resources and executes the jobs in a Hadoop cluster. YARN configuration involves setting the parameters for the ResourceManager, the NodeManager, and the WebAppProxy. Some of the important YARN configuration files are:

    - yarn-site.xml: This file contains the YARN-specific configuration settings, such as the address and port of the ResourceManager, the minimum and maximum memory and CPU allocation for each container, and the scheduler class and policies.
    - mapred-site.xml: This file contains the MapReduce-specific configuration settings, such as the framework name, the number of map and reduce tasks per node, and the output compression codec and format.
    - yarn-env.sh: This file contains the environment variables for the YARN daemons, such as the Java home directory, the heap size, and the log directory.

  - Oozie configuration: Oozie is the workflow engine that orchestrates the execution of multiple Hadoop jobs in a predefined sequence. Oozie configuration involves setting the parameters for the Oozie server and the Oozie client. Some of the important Oozie configuration files are:

    - oozie-site.xml: This file contains the Oozie-specific configuration settings, such as the database connection string, the Oozie service URL, and the security and authentication options.
    - oozie-env.sh: This file contains the environment variables for the Oozie server, such as the Java home directory, the heap size, and the log directory.
    - oozie-default.xml: This file contains the default configuration settings for the Oozie workflows, such as the action retry policy, the email notification settings, and the Hadoop job tracker and name node URLs.

- Hadoop configuration can be verified by using the Hadoop configuration command-line tool, which can list, print, or set the configuration properties for a given Hadoop service. For example, the following command can list the configuration properties for the HDFS service:

  ```bash
  hadoop configuration -list hdfs
  ```

- Hadoop configuration can be modified by using the Hadoop configuration command-line tool, which can set or unset the configuration properties for a given Hadoop service. For example, the following command can set the replication factor for HDFS to 3:

  ```bash
  hadoop configuration -set hdfs dfs.replication 3
  ```

- Hadoop configuration can also be modified by editing the XML files in the etc/hadoop directory of the Hadoop installation, and then restarting the Hadoop daemons for the changes to take effect. For example, the following XML snippet can set the replication factor for HDFS to 3 in the hdfs-site.xml file:

  ```xml
  <property>
    <name>dfs.replication</name>
    <value>3</value>
  </property>
  ```

- Hadoop configuration can be customized for different Hadoop clusters by using the HADOOP_CONF_DIR environment variable, which can point to a different directory that contains the configuration files for a specific cluster. For example, the following command can run a Hadoop job using the configuration files in the /etc/hadoop/cluster1 directory:

  ```bash