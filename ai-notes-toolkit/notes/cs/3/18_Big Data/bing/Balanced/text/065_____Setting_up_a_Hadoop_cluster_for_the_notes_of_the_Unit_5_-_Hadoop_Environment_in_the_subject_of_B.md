### Setting up a Hadoop cluster

- A Hadoop cluster is a collection of machines that run the Hadoop software and store and process large amounts of data using the Hadoop Distributed File System (HDFS) and the MapReduce framework.
- A Hadoop cluster can be classified into two types: single-node cluster and multi-node cluster.
- A single-node cluster is a cluster that runs on one machine and is used for testing and development purposes. A multi-node cluster is a cluster that runs on multiple machines and is used for production and deployment purposes.
- To set up a Hadoop cluster, the following steps are required:

  1. Install Java on all the machines in the cluster, as Hadoop is written in Java and requires Java to run.
  2. Download and extract the Hadoop software from the official website or a mirror site on all the machines in the cluster.
  3. Configure the Hadoop software by editing the configuration files in the etc/hadoop directory. The main configuration files are core-site.xml, hdfs-site.xml, mapred-site.xml, and yarn-site.xml. These files specify the parameters for the Hadoop components, such as the name node, the data nodes, the resource manager, the node managers, and the job history server.
  4. Set up passwordless SSH access between the machines in the cluster, as Hadoop uses SSH to communicate and execute commands on the remote machines.
  5. Format the HDFS on the name node machine, which is the master machine that manages the metadata of the HDFS. This will create the HDFS directory structure and initialize the name node.
  6. Start the Hadoop daemons on all the machines in the cluster using the start-all.sh script or the start-dfs.sh and start-yarn.sh scripts. This will launch the name node, the data nodes, the resource manager, the node managers, and the job history server processes on the respective machines.
  7. Verify the status of the Hadoop cluster by using the web interfaces or the command-line tools. The web interfaces can be accessed by using the URLs http://<name node IP>:9870 for the name node, http://<resource manager IP>:8088 for the resource manager, and http://<job history server IP>:19888 for the job history server. The command-line tools can be used by using the hadoop, hdfs, mapred, and yarn commands with various options and arguments.