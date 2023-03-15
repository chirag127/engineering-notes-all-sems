#### Hadoop Configuration in Hadoop Environment

To configure Hadoop in a Hadoop environment, you need to edit the configuration files located in the `$HADOOP_HOME/etc/hadoop` directory. Here are the steps to configure Hadoop:

1. Edit the `core-site.xml` file to set the Hadoop configuration properties such as the default file system name and the default block size.

```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
    <property>
        <name>io.file.buffer.size</name>
        <value>131072</value>
    </property>
</configuration>
```

2. Edit the `hdfs-site.xml` file to set the HDFS configuration properties such as the replication factor and the name directory.

```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///usr/local/hadoop/hadoop_data/hdfs/namenode</value>
    </property>
</configuration>
```

3. Edit the `mapred-site.xml` file to set the MapReduce configuration properties such as the framework name and the job tracker address.

```xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.jobtracker.address</name>
        <value>localhost:54311</value>
    </property>
</configuration>
```

4. Edit the `yarn-site.xml` file to set the YARN configuration properties such as the resource manager address and the node manager address.

```xml
<configuration>
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>localhost</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
</configuration>
```

After editing the configuration files, you need to format the HDFS file system and start the Hadoop daemons.

```sh
$HADOOP_HOME/bin/hdfs namenode -format
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh
```
