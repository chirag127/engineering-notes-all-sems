#### Cluster specification in Hadoop Environment

A Hadoop cluster is a collection of computers, known as nodes, that are networked together to store and analyze large amounts of structured, semi-structured, and unstructured data in a distributed computing environment. A Hadoop cluster is often referred to as a shared-nothing system because the only thing that is shared between the nodes is the network itself  .

To configure a Hadoop cluster, you will need to set up the environment and the configuration parameters for the Hadoop daemons. The Hadoop daemons are NameNode, DataNode, JobTracker, and TaskTracker .

The environment of the Hadoop daemons can be configured by editing the following files:

- `hadoop-env.sh`: This file sets the environment variables such as `JAVA_HOME`, `HADOOP_CONF_DIR`, `HADOOP_LOG_DIR`, etc. that are used by the Hadoop scripts.
- `core-site.xml`: This file contains the core configuration properties for Hadoop, such as `fs.default.name` (the default file system name), `hadoop.tmp.dir` (the base directory for temporary files), etc.
- `hdfs-site.xml`: This file contains the configuration properties for the Hadoop Distributed File System (HDFS), such as `dfs.replication` (the default block replication factor), `dfs.name.dir` (the directory where the NameNode stores the metadata), `dfs.data.dir` (the directory where the DataNodes store the data blocks), etc.
- `mapred-site.xml`: This file contains the configuration properties for the MapReduce framework, such as `mapred.job.tracker` (the host and port of the JobTracker), `mapred.local.dir` (the directory where the TaskTrackers store intermediate data), `mapred.reduce.tasks` (the default number of reduce tasks per job), etc.

These files should be copied to all the nodes in the cluster and edited accordingly. Alternatively, you can use a configuration management tool such as Ansible, Puppet, Chef, etc. to automate the process of deploying and configuring the Hadoop cluster.