To set up a Hadoop cluster in Hadoop environment, you will need to configure the environment and the parameters for the Hadoop daemons. Hadoop daemons are processes that run in the background and perform the core functions of the Hadoop system. They include:

- NameNode: The master node that manages the metadata of the distributed file system (HDFS).
- SecondaryNameNode: The backup node that periodically merges the edits log from the NameNode and saves the namespace image.
- DataNode: The worker node that stores the actual data blocks of the files in HDFS.
- ResourceManager: The master node that manages the resources and the scheduling of the applications running on the cluster.
- NodeManager: The worker node that launches and monitors the containers that run the application tasks.
- WebAppProxy: The proxy node that handles the web interface requests for the applications.

To set up a Hadoop cluster, you will need to follow these steps:

1. Create a Hadoop user and group on each node of the cluster. For example, you can use the following commands:

```bash
sudo groupadd hadoop
sudo useradd -g hadoop hdfs
sudo useradd -g hadoop yarn
```

2. Create a host file on each node of the cluster. For each node to communicate with each other by name, edit the `/etc/hosts` file to add the IP address and hostname of each node. For example, you can use the following format:

```bash
192.168.0.1 master
192.168.0.2 slave1
192.168.0.3 slave2
```

3. Distribute authentication key-pairs for the Hadoop user. The master node will use an SSH connection to connect to other nodes and start or stop the daemons. To enable passwordless SSH, you will need to generate a public-private key pair for the Hadoop user on the master node and copy the public key to the authorized keys file of the Hadoop user on the other nodes. For example, you can use the following commands:

```bash
# On the master node, as the Hadoop user
ssh-keygen -t rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub hdfs@slave1
ssh-copy-id -i ~/.ssh/id_rsa.pub hdfs@slave2
ssh-copy-id -i ~/.ssh/id_rsa.pub yarn@slave1
ssh-copy-id -i ~/.ssh/id_rsa.pub yarn@slave2
```

4. Download and unpack Hadoop on each node of the cluster. You can download the latest stable release of Hadoop from the official website and extract it to a directory of your choice. For example, you can use the following commands:

```bash
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar -xzf hadoop-3.3.1.tar.gz
mv hadoop-3.3.1 /usr/local/hadoop
```

5. Configure the environment variables for Hadoop on each node of the cluster. You will need to set the `HADOOP_HOME`, `HADOOP_CONF_DIR`, `JAVA_HOME`, and `PATH` variables for the Hadoop user. You can edit the `.bashrc` file of the Hadoop user and add the following lines:

```bash
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

6. Configure the Hadoop daemons parameters on each node of the cluster. You will need to edit the XML files in the `$HADOOP_CONF_DIR` directory and set the appropriate values for the configuration properties. The main files are:

- `core-site.xml`: This file contains the core configuration for HDFS and YARN, such as the default file system URI, the I/O settings, and the security options.
- `hdfs-site.xml`: This file contains the configuration for HDFS, such as the replication factor, the block size, and the directories for the NameNode and DataNode.
- `yarn-site.xml`: This file contains the configuration for YARN, such as the resource allocation, the scheduler, and the web interface.
- `mapred-site.xml`: This file contains the configuration for MapReduce, such as the framework, the memory settings, and the output compression.

You can refer to the official documentation