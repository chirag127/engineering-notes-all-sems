#### Hadoop configuration in Hadoop Environment

Hadoop configuration refers to the process of setting up and managing the parameters and environment for the Hadoop daemons and applications. Hadoop configuration can be done in different modes, depending on the scale and purpose of the Hadoop cluster. The following are the main modes of Hadoop configuration:

- **Local or standalone mode**: This is the default mode of Hadoop, where it runs as a single Java process on one machine. This mode is useful for debugging and testing purposes, but it does not use the Hadoop Distributed File System (HDFS) or the MapReduce framework. To run Hadoop in this mode, no configuration files are required.

- **Pseudo-distributed mode**: This mode simulates a distributed environment by running each Hadoop daemon as a separate Java process on one machine. This mode allows the use of HDFS and MapReduce, but it does not provide fault tolerance or scalability. To run Hadoop in this mode, some configuration files need to be edited, such as `core-site.xml`, `hdfs-site.xml`, and `mapred-site.xml`. Additionally, passphraseless SSH needs to be set up to allow the Hadoop scripts to start and stop the daemons remotely.

- **Fully-distributed mode**: This mode is the actual distributed mode of Hadoop, where it runs on a cluster of multiple machines, each hosting one or more Hadoop daemons. This mode provides the full functionality and benefits of Hadoop, such as parallel processing, fault tolerance, scalability, and high availability. To run Hadoop in this mode, more configuration files need to be edited, such as `masters`, `slaves`, `yarn-site.xml`, and `mapred-site.xml`. Moreover, the Hadoop environment variables, such as `HADOOP_HOME`, `JAVA_HOME`, and `HADOOP_CONF_DIR`, need to be set up on each node in the cluster.

Some of the common configuration properties for Hadoop are:

- `fs.defaultFS`: This property specifies the default file system URI for Hadoop, such as `hdfs://localhost:9000` for HDFS.
- `hadoop.tmp.dir`: This property specifies the temporary directory for Hadoop, where it stores intermediate data and logs. It should be a local directory on each node in the cluster.
- `dfs.replication`: This property specifies the number of replicas for each block in HDFS. It should be set according to the size and availability of the cluster.
- `mapreduce.framework.name`: This property specifies the framework for running MapReduce jobs, such as `yarn` for using YARN as the resource manager.
- `yarn.resourcemanager.address`: This property specifies the address of the YARN resource manager, such as `localhost:8032`.
- `yarn.nodemanager.resource.memory-mb`: This property specifies the amount of memory in MB that can be allocated for containers on each node in the cluster.
- `yarn.nodemanager.resource.cpu-vcores`: This property specifies the number of virtual CPU cores that can be allocated for containers on each node in the cluster.

Hadoop configuration can be done by editing the XML files in the `etc/hadoop` directory of the Hadoop distribution, or by using the `hadoop` command-line tool with the `-conf` option. Hadoop configuration can also be done programmatically by using the `Configuration` class in the Hadoop API.