#### Data replication in HDFS

Hadoop Distributed File System (HDFS) is a distributed file system designed to store large data sets reliably and to stream those data sets at high bandwidth to user applications. One of the key features of HDFS is its ability to replicate data across multiple nodes in a cluster to ensure data availability and durability.

Here is an example of how data replication can be configured in HDFS using the `hdfs-site.xml` configuration file:

```xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>3</value>
    <description>Default block replication.
    The actual number of replications can be specified when the file is created.
    The default is used if replication is not specified in create time.
    </description>
  </property>
</configuration>
```

In this example, the `dfs.replication` property is set to `3`, which means that HDFS will create 3 replicas of each data block by default. This value can be adjusted to meet the specific needs of the cluster and the data being stored.