#### Administering Hadoop in Hadoop Environment

Administering Hadoop in Hadoop environment involves the following tasks:

- Setting up and configuring the Hadoop cluster, which consists of HDFS daemons (NameNode, SecondaryNameNode, and DataNode) and YARN daemons (ResourceManager, NodeManager, and WebAppProxy).
- Managing and monitoring the Hadoop cluster using tools such as Ambari, Cloudera Manager, or Hadoop web UIs.
- Performing regular maintenance activities such as backup, recovery, security, patching, and upgrading of the Hadoop components.
- Troubleshooting and resolving any issues related to the Hadoop cluster performance, availability, or functionality.
- Providing support and guidance to the Hadoop users and developers, and ensuring the compliance with the Hadoop best practices and standards .

To administer Hadoop in Hadoop environment, one needs to have the following skills and knowledge:

- Proficiency in Linux/Unix operating system and shell scripting, as Hadoop runs on Linux/Unix platforms and uses shell scripts to start and stop the Hadoop daemons.
- Familiarity with Java programming language and JVM options, as Hadoop is written in Java and uses JVM to run the Hadoop processes.
- Understanding of the Hadoop architecture, components, configuration, and parameters, as well as the Hadoop distributed file system (HDFS) and the Hadoop resource management framework (YARN).
- Experience in using Hadoop command-line interface (CLI) and Hadoop web UIs to interact with the Hadoop cluster and perform various operations on the Hadoop file system and the Hadoop applications.
- Ability to use Hadoop administration tools such as Ambari, Cloudera Manager, or Hadoop web UIs to manage and monitor the Hadoop cluster, and to perform tasks such as adding or removing nodes, balancing the data across the cluster, checking the cluster health and status, viewing the logs and metrics, etc. .
- Knowledge of the Hadoop security mechanisms and best practices, such as Kerberos authentication, encryption, authorization, auditing, etc..
- Awareness of the Hadoop performance tuning techniques and tools, such as benchmarking, profiling, debugging, etc..

Here is an example of a shell script that can be used to start the Hadoop daemons in pseudo distributed mode:

```bash
# Set Hadoop environment variables
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin

# Format the HDFS namenode
hdfs namenode -format

# Start the HDFS daemons
start-dfs.sh

# Start the YARN daemons
start-yarn.sh
```