# Setting up a Hadoop cluster

A Hadoop cluster is a collection of machines that run the Hadoop distributed computing framework. A Hadoop cluster can be used to store and process large amounts of data using the MapReduce programming model. A Hadoop cluster consists of two types of nodes: a master node and one or more worker nodes.

The master node runs the NameNode and the ResourceManager services, which are responsible for managing the file system metadata and the cluster resources, respectively. The worker nodes run the DataNode and the NodeManager services, which are responsible for storing and processing the data blocks and executing the tasks assigned by the ResourceManager, respectively.

To set up a Hadoop cluster, you will need to perform the following steps:

- Configure the system: You will need to create a dedicated user account for Hadoop, set up passwordless SSH access between the nodes, and edit the /etc/hosts file to map the node names to their IP addresses.
- Download and unpack Hadoop: You will need to download the latest stable release of Hadoop from the official website and extract it to a common location on all the nodes. You will also need to set the HADOOP_HOME and JAVA_HOME environment variables for the Hadoop user.
- Configure Hadoop: You will need to edit the configuration files in the $HADOOP_HOME/etc/hadoop directory to specify the cluster settings, such as the node names, the replication factor, the memory and CPU allocation, and the network ports. The main configuration files are core-site.xml, hdfs-site.xml, mapred-site.xml, and yarn-site.xml.
- Format and start HDFS: You will need to format the distributed file system on the master node using the hdfs namenode -format command. This will create the necessary directories and files on the NameNode and the DataNodes. You will then need to start the HDFS services on all the nodes using the start-dfs.sh script.
- Start YARN: You will need to start the YARN services on all the nodes using the start-yarn.sh script. This will launch the ResourceManager on the master node and the NodeManagers on the worker nodes.
- Verify the cluster: You will need to check the status of the cluster using the web interfaces provided by Hadoop. The NameNode web interface can be accessed at http://master:9870, where master is the name of the master node. The ResourceManager web interface can be accessed at http://master:8088. You can also use the hdfs dfsadmin -report and yarn node -list commands to view the details of the HDFS and YARN nodes, respectively.

These are the basic steps to set up a Hadoop cluster. For more details and examples, you can refer to the following sources:

-  Quickstart: Apache Hadoop, Apache Hive & Azure HDInsight portal
-  Cluster Setup - Apache Hadoop
-  Apache Hadoop 3.3.4 – Hadoop Cluster Setup
-  How to Install and Set Up a 3-Node Hadoop Cluster | Linode