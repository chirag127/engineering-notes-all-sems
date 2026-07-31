#### Setting up a Hadoop cluster in Hadoop Environment

Hadoop is a framework for distributed processing of large-scale data using a cluster of computers. A Hadoop cluster consists of a master node and one or more worker nodes. The master node runs the NameNode and the ResourceManager, which are responsible for managing the file system and the resources of the cluster. The worker nodes run the DataNode and the NodeManager, which store and process the data.

To set up a Hadoop cluster, you need to follow these steps:

1. Install Java and Hadoop on each node of the cluster. You can download the latest version of Hadoop from https://hadoop.apache.org/releases.html and follow the installation instructions from https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SingleCluster.html#Installation .
2. Configure the environment of the Hadoop daemons by editing the following files in the $HADOOP_HOME/etc/hadoop directory: 
    - core-site.xml: This file contains the core configuration of Hadoop, such as the default file system URI and the I/O settings. You need to set the fs.defaultFS property to the URI of the NameNode, such as hdfs://master:9000.
    - hdfs-site.xml: This file contains the configuration of the Hadoop Distributed File System (HDFS), such as the replication factor and the block size. You need to set the dfs.replication property to the number of replicas you want for each block, and the dfs.namenode.name.dir and dfs.datanode.data.dir properties to the directories where the NameNode and the DataNode store their metadata and data, respectively.
    - yarn-site.xml: This file contains the configuration of the Yet Another Resource Negotiator (YARN), which is the resource management and scheduling system of Hadoop. You need to set the yarn.resourcemanager.hostname property to the hostname of the ResourceManager, and the yarn.nodemanager.aux-services and yarn.nodemanager.aux-services.mapreduce_shuffle.class properties to enable the MapReduce shuffle service on the NodeManager.
    - mapred-site.xml: This file contains the configuration of the MapReduce framework, which is the programming model for processing data in Hadoop. You need to set the mapreduce.framework.name property to yarn, and the mapreduce.jobhistory.address and mapreduce.jobhistory.webapp.address properties to the hostname and port of the JobHistory server, which is a web interface for viewing the history of MapReduce jobs.
3. Configure the SSH access for the Hadoop user on each node of the cluster. You need to generate a public-private key pair for the Hadoop user and copy the public key to the authorized_keys file of the same user on each node. This will allow the Hadoop user to log in to any node of the cluster without entering a password. You can follow the instructions from https://www.linode.com/docs/guides/how-to-install-and-set-up-hadoop-cluster/#distribute-authentication-key-pairs-for-the-hadoop-user.
4. Format the HDFS file system on the NameNode. You need to run the command $HADOOP_HOME/bin/hdfs namenode -format as the Hadoop user on the master node. This will initialize the file system and create the necessary directories and files on the NameNode. You only need to do this once when you set up the cluster for the first time.
5. Start the Hadoop daemons on each node of the cluster. You need to run the following commands as the Hadoop user on the master node:
    - $HADOOP_HOME/sbin/start-dfs.sh: This will start the NameNode, the SecondaryNameNode, and the DataNode on each node.
    - $HADOOP_HOME/sbin/start-yarn.sh: This will start the ResourceManager and the NodeManager on each node.
    - $HADOOP_HOME/sbin/mr-jobhistory-daemon.sh start historyserver: This will start the JobHistory server on the master node.
6. Verify the status of the Hadoop cluster by using the following web interfaces:
    - NameNode: http://master:9870
    - ResourceManager: http://master:8088
    - JobHistory: http://master:19888
    - DataNode: http://worker:9864 (replace worker with the hostname of any worker node)
    - NodeManager: http://worker:8042 (replace worker with the hostname of any worker node)

You have successfully set up a Hadoop cluster in Hadoop environment. You can now run Hadoop commands