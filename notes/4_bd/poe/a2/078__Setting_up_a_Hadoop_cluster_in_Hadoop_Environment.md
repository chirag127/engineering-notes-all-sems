 Here is the formal content in markdown format without any emojis or external links on the given topic:

#### Setting up a Hadoop cluster in Hadoop Environment.

1.  Gather Hardware - Obtain the necessary hardware required for your Hadoop cluster. This will include servers to act as NameNode, DataNodes, and Edge nodes. The number of DataNodes will depend on the size of your cluster and data.
2.  Install Hadoop - Download the latest stable release of Hadoop and install it on all the nodes in your cluster. Follow the official documentation to install Hadoop on each machine.
3.  Set up network - Ensure your Hadoop cluster nodes are in the same network and can communicate with each other through SSH without a password. This can be done by generating SSH keys and distributing them across the nodes.
4.  Configure Hadoop - Update the necessary configuration files in the $HADOOP_HOME/etc/hadoop directory to configure your Hadoop cluster. This includes configurations for memory usage, number of DataNodes, etc.
5.  Start Hadoop services - Start the NameNode, DataNode, and other necessary services on each node in your cluster.
6.  Test the cluster - You can run a sample MapReduce job or upload a file to the distributed filesystem (HDFS) to test that your Hadoop cluster is set up correctly and all the components are working as expected.
7.  Launch Edge node - If you are using an Edge node, launch it and install the necessary tools to interact with your cluster. The Edge node can be used to submit jobs or access the HDFS.

The key steps are gathering hardware, installing Hadoop, setting up networking, configuring Hadoop, starting Hadoop services and testing the cluster. Following these steps will help in setting up a Hadoop cluster and getting it ready for use in a Hadoop environment.