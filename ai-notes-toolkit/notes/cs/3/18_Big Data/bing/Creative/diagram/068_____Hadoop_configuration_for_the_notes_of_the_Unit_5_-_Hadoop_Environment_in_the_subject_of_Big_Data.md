### Hadoop configuration

- Hadoop configuration is the process of setting the parameters and properties of the Hadoop system and its components, such as HDFS, YARN, and MapReduce.
- Hadoop configuration is driven by two types of important configuration files  :
  - Read-only default configuration files that are provided by Hadoop and contain the default values for the configuration parameters. These files are located in the `share/hadoop/common` directory and have names like `core-default.xml`, `hdfs-default.xml`, `yarn-default.xml`, and `mapred-default.xml`.
  - Site-specific configuration files that are created by the user and contain the customized values for the configuration parameters. These files are located in the `etc/hadoop` directory and have names like `core-site.xml`, `hdfs-site.xml`, `yarn-site.xml`, and `mapred-site.xml`.
- The site-specific configuration files override the default configuration files, and the configuration parameters can be accessed by the Hadoop system and its components through the `Configuration` class in Java.
- To configure the Hadoop cluster, the user needs to configure the environment and the parameters for the Hadoop daemons :
  - HDFS daemons are NameNode, SecondaryNameNode, and DataNode. They are responsible for storing and managing the data blocks across the cluster.
  - YARN daemons are ResourceManager, NodeManager, and WebAppProxy. They are responsible for allocating and managing the resources and the applications across the cluster.
  - MapReduce daemons are JobTracker and TaskTracker. They are responsible for scheduling and executing the map and reduce tasks across the cluster.
- The environment configuration involves setting the Java and SSH properties, such as the Java home directory, the SSH public and private keys, and the Hadoop environment variables, such as `HADOOP_HOME`, `HADOOP_CONF_DIR`, and `HADOOP_LOG_DIR`.
- The parameter configuration involves setting the values for the Hadoop daemons in the site-specific configuration files, such as the `fs.defaultFS` and `dfs.replication` for HDFS, the `yarn.resourcemanager.address` and `yarn.nodemanager.resource.memory-mb` for YARN, and the `mapreduce.framework.name` and `mapreduce.job.reduces` for MapReduce.
- The configuration files can be edited manually using a text editor, or using a graphical user interface, such as Ambari or Cloudera Manager, that provide tools for managing and monitoring the Hadoop cluster.