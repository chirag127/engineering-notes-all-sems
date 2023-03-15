#### Cluster setup and installation in Hadoop Environment

- A Hadoop cluster is a collection of machines that run the Hadoop software and store the data in a distributed manner.
- A Hadoop cluster can be classified into two types: single-node cluster and multi-node cluster.
- A single-node cluster is a cluster that consists of only one machine, which acts as both the master and the worker node. It is useful for testing and development purposes, but not for production use.
- A multi-node cluster is a cluster that consists of more than one machine, which are divided into master nodes and worker nodes. The master nodes are responsible for managing the cluster resources and coordinating the tasks, while the worker nodes are responsible for executing the tasks and storing the data.
- To set up and install a Hadoop cluster, the following steps are required:

  1. Install Java on all the machines, as Hadoop is written in Java and requires Java Runtime Environment (JRE) to run.
  2. Download and extract the Hadoop software from the official website or a mirror site on all the machines.
  3. Configure the Hadoop software by editing the configuration files in the etc/hadoop directory. The main configuration files are core-site.xml, hdfs-site.xml, mapred-site.xml, and yarn-site.xml. These files specify the parameters for the Hadoop components, such as the location of the NameNode and the DataNodes, the replication factor, the memory and CPU allocation, and the scheduler.
  4. Set up the SSH connection between the machines, so that the master node can communicate with the worker nodes without password authentication. This can be done by generating and exchanging the SSH keys using the ssh-keygen and ssh-copy-id commands.
  5. Format the Hadoop Distributed File System (HDFS) by running the hdfs namenode -format command on the master node. This will initialize the NameNode and create the metadata for the file system.
  6. Start the Hadoop cluster by running the start-all.sh script on the master node. This will start the NameNode, the DataNode, the ResourceManager, the NodeManager, and the JobHistoryServer on the respective nodes.
  7. Verify the status of the Hadoop cluster by using the web interface or the command-line tools. The web interface can be accessed by using the URLs http://master-node:50070 for the NameNode, http://master-node:8088 for the ResourceManager, and http://master-node:19888 for the JobHistoryServer. The command-line tools include the hdfs dfsadmin -report, the yarn node -list, and the mapred job -list commands.