### Setting up a Hadoop cluster

- A Hadoop cluster is a collection of machines that run the Hadoop software and store and process large amounts of data using the Hadoop Distributed File System (HDFS) and the MapReduce framework.
- A Hadoop cluster can be classified into two types: single-node cluster and multi-node cluster.
- A single-node cluster is a cluster that runs on one machine and is used for testing and development purposes. A multi-node cluster is a cluster that runs on multiple machines and is used for production and deployment purposes.
- To set up a Hadoop cluster, the following steps are required:

  1. Install Java on all the machines in the cluster. Java is a prerequisite for running Hadoop and its components.
  2. Download and extract the Hadoop software from the official website or a mirror site. The latest stable version of Hadoop is 3.3.1 as of March 2023.
  3. Configure the Hadoop environment variables on all the machines in the cluster. These variables include HADOOP_HOME, HADOOP_CONF_DIR, JAVA_HOME, PATH, etc.
  4. Configure the Hadoop configuration files on all the machines in the cluster. These files include core-site.xml, hdfs-site.xml, mapred-site.xml, yarn-site.xml, etc. These files specify the parameters and properties of the Hadoop components and services.
  5. Configure the SSH access between the machines in the cluster. SSH is used for secure and remote communication between the machines. The master node should be able to access all the slave nodes without password authentication using SSH keys.
  6. Format the HDFS on the master node. This step initializes the HDFS and creates the metadata for the file system. This step should be done only once before starting the cluster.
  7. Start the Hadoop daemons on all the machines in the cluster. These daemons include NameNode, DataNode, ResourceManager, NodeManager, etc. These daemons are responsible for managing the HDFS and the MapReduce jobs on the cluster.
  8. Verify the status and health of the cluster using the web interfaces or the command-line tools. The web interfaces can be accessed using the URLs http://master:9870 for the NameNode, http://master:8088 for the ResourceManager, http://slave:9864 for the DataNode, and http://slave:8042 for the NodeManager. The command-line tools include hdfs dfsadmin, yarn node, etc.
  9. Run some sample Hadoop jobs on the cluster to test its functionality and performance. Some sample Hadoop jobs are provided in the $HADOOP_HOME/share/hadoop/mapreduce directory. These jobs include wordcount, pi, teragen, terasort, etc. These jobs can be executed using the hadoop jar command.