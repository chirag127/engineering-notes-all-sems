# Setting up a Hadoop cluster

A Hadoop cluster is a collection of machines that run the Hadoop distributed computing framework. A Hadoop cluster can be used to store and process large amounts of data using the MapReduce programming model. A Hadoop cluster consists of two types of nodes: a master node and one or more worker nodes.

The master node runs the Hadoop daemons that coordinate and manage the cluster, such as the NameNode, the SecondaryNameNode, the ResourceManager, and the JobTracker. The worker nodes run the Hadoop daemons that perform the actual data processing, such as the DataNode, the NodeManager, and the TaskTracker.

To set up a Hadoop cluster, you need to follow these steps:

1. Install Java on all the nodes. Hadoop requires Java 8 or higher to run. You can use the following command to install Java on Ubuntu:

    ```bash
    sudo apt update
    sudo apt install openjdk-8-jdk
    ```

2. Configure the environment of the Hadoop daemons on all the nodes. You need to set the `HADOOP_HOME` and `JAVA_HOME` environment variables, and add the Hadoop bin directory to the `PATH` variable. You can use the following commands to do so:

    ```bash
    export HADOOP_HOME=/path/to/hadoop
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    export PATH=$PATH:$HADOOP_HOME/bin
    ```

3. Configure the host file on each node. For each node to communicate with each other by name, edit the `/etc/hosts` file to add the IP address and hostname of each node. For example:

    ```text
    192.168.0.1 master
    192.168.0.2 worker1
    192.168.0.3 worker2
    ```

4. Distribute authentication key-pairs for the Hadoop user. The master node will use an SSH connection to connect to other nodes and execute commands. To enable passwordless SSH, you need to generate a public-private key pair for the Hadoop user on the master node, and copy the public key to the authorized_keys file of the Hadoop user on all the nodes. You can use the following commands to do so:

    ```bash
    # On the master node, as the Hadoop user
    ssh-keygen -t rsa
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
    chmod 600 ~/.ssh/authorized_keys

    # On each worker node, as the Hadoop user
    mkdir ~/.ssh
    touch ~/.ssh/authorized_keys
    chmod 600 ~/.ssh/authorized_keys

    # On the master node, as the Hadoop user
    ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@worker1
    ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@worker2
    ```

5. Download and unpack Hadoop on all the nodes. You can download the latest stable release of Hadoop from the official website, and extract it to a desired location. For example:

    ```bash
    wget https://downloads.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
    tar -xzf hadoop-3.3.1.tar.gz
    mv hadoop-3.3.1 /path/to/hadoop
    ```

6. Configure the Hadoop parameters on all the nodes. You need to edit the XML files in the `$HADOOP_HOME/etc/hadoop` directory to set the configuration properties for the Hadoop daemons. The main configuration files are:

    - `core-site.xml`: This file contains the core configuration for the Hadoop cluster, such as the default file system URI, the I/O settings, and the security options.
    - `hdfs-site.xml`: This file contains the configuration for the Hadoop Distributed File System (HDFS), such as the replication factor, the block size, and the NameNode and DataNode directories.
    - `mapred-site.xml`: This file contains the configuration for the MapReduce framework, such as the MapReduce execution mode, the resource allocation, and the job history server settings.
    - `yarn-site.xml`: This file contains the configuration for the Yet Another Resource Negotiator (YARN), which is the resource management layer of Hadoop, such as the ResourceManager and NodeManager settings, the scheduler options, and the application master settings.

    You