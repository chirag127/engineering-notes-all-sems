A cluster setup and installation in Hadoop environment involves the following steps:

- Installing Java on all the machines in the cluster.
- Downloading a stable version of Hadoop from Apache mirrors.
- Unpacking the software on all the machines in the cluster or installing it via a packaging system as appropriate for your operating system.
- Configuring the environment of Hadoop daemons using the etc/hadoop/hadoop-env.sh, etc/hadoop/mapred-env.sh and etc/hadoop/yarn-env.sh scripts.
- Configuring the Hadoop daemons using the etc/hadoop/core-site.xml, etc/hadoop/hdfs-site.xml, etc/hadoop/yarn-site.xml and etc/hadoop/mapred-site.xml files.
- Setting up passphraseless ssh between the machines in the cluster.
- Starting the Hadoop cluster using the bin/start-all.sh script or the bin/start-dfs.sh and bin/start-yarn.sh scripts.

The following diagram illustrates the basic architecture of a Hadoop cluster:

#### Cluster setup and installation in Hadoop Environment

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NameNode     |    | SecondaryNameNode |  |    ResourceManager   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       ^                      ^                      ^
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    DataNode     |    |    DataNode     |    |    DataNode     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       ^                      ^                      ^
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NodeManager  |    |    NodeManager  |    |    NodeManager  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```