# Cluster Setup and Installation for Hadoop

- Hadoop is a framework for distributed processing of large-scale data using a cluster of machines.
- A cluster is a group of machines that work together as a single system.
- There are different types of clusters in Hadoop, such as single node, pseudo-distributed, and fully-distributed.
- Each cluster has different configuration and installation steps.

## Single Node Cluster

- A single node cluster is the simplest type of cluster, where Hadoop runs on a single machine.
- It is useful for testing and development purposes, but not for production use.
- To set up a single node cluster, the following steps are required:

  - Install Java on the machine and verify the installation by running `javac -version`.
  - Download a stable version of Hadoop from Apache mirrors and extract it at a desired location, such as `C:\Hadoop`.
  - Set up the `HADOOP_HOME` and `JAVA_HOME` environment variables to point to the Hadoop and Java directories respectively.
  - Set up the `PATH` environment variable to include the Hadoop and Java bin directories.
  - Configure the Hadoop files in the `etc\hadoop` directory, such as `core-site.xml`, `hdfs-site.xml`, `mapred-site.xml`, and `yarn-site.xml` .
  - Format the namenode folder by running `hdfs namenode -format`.
  - Start the Hadoop services by running `start-all.cmd`.
  - Test the setup by running some Hadoop commands, such as `hdfs dfs -ls /` or `yarn jar hadoop-mapreduce-examples-*.jar pi 16 1000`.

## Pseudo-Distributed Cluster

- A pseudo-distributed cluster is a type of cluster where Hadoop runs on a single machine, but each Hadoop daemon runs in a separate Java process.
- It is useful for simulating a distributed cluster on a single machine, but not for production use.
- To set up a pseudo-distributed cluster, the following steps are required:

  - Follow the same steps as for the single node cluster, except for the configuration files.
  - Configure the Hadoop files in the `etc\hadoop` directory, such as `core-site.xml`, `hdfs-site.xml`, `mapred-site.xml`, and `yarn-site.xml` to use `localhost` as the hostname for the namenode, datanode, resourcemanager, and nodemanager .
  - Set up passphraseless ssh on the machine, so that Hadoop can start and stop the daemons without prompting for password .
  - Start the Hadoop services by running `start-dfs.sh` and `start-yarn.sh` .
  - Test the setup by running some Hadoop commands, such as `hdfs dfs -ls /` or `yarn jar hadoop-mapreduce-examples-*.jar pi 16 1000`.

## Fully-Distributed Cluster

- A fully-distributed cluster is a type of cluster where Hadoop runs on multiple machines, with each machine having a specific role, such as namenode, datanode, resourcemanager, or nodemanager.
- It is useful for production use, where the data and computation are distributed across the cluster for scalability and fault-tolerance.
- To set up a fully-distributed cluster, the following steps are required:

  - Install Java on all the machines in the cluster and verify the installation by running `javac -version`.
  - Download a stable version of Hadoop from Apache mirrors and extract it at the same location on all the machines, such as `/usr/local/hadoop`.
  - Set up the `HADOOP_HOME` and `JAVA_HOME` environment variables to point to the Hadoop and Java directories respectively on all the machines.
  - Set up the `PATH` environment variable to include the Hadoop and Java bin directories on all the machines.
  - Configure the Hadoop files in the `etc\hadoop` directory, such as `core-site.xml`, `hdfs-site.xml`, `mapred-site.xml`, and `yarn-site.xml` to use the hostnames or IP addresses of the machines for the