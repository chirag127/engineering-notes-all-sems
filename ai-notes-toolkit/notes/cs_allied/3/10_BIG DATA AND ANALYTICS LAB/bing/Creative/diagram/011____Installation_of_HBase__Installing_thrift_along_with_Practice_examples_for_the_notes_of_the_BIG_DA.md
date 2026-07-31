## Installation of HBase, Installing thrift along with Practice examples for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

HBase is a distributed, scalable, and column-oriented database that runs on top of the Hadoop Distributed File System (HDFS). It provides random, real-time read/write access to large datasets. HBase is modeled after Google's Bigtable, a distributed storage system for structured data.

To install HBase, you need to have Java and Hadoop installed on your Linux machine. HBase can be installed in three modes: standalone, pseudo-distributed, and fully distributed. In this note, we will focus on the standalone mode, which is the simplest and easiest way to get started with HBase.

### Installing HBase in Standalone Mode

- Download the latest stable version of HBase from http://www.interior-dsgn.com/apache/hbase/stable/ and unzip it with the following commands:

```bash
$ wget http://www.interior-dsgn.com/apache/hbase/stable/hbase-2.4.8-bin.tar.gz
$ tar xzf hbase-2.4.8-bin.tar.gz
$ cd hbase-2.4.8
```

- Edit the `conf/hbase-env.sh` file and set the `JAVA_HOME` environment variable to point to your Java installation directory :

```bash
$ vi conf/hbase-env.sh
# Uncomment the following line and set the path to your Java installation
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

- Edit the `conf/hbase-site.xml` file and add the following properties to configure HBase to use the local file system instead of HDFS:

```xml
<configuration>
  <property>
    <name>hbase.rootdir</name>
    <value>file:///home/hadoop/hbase-2.4.8/data</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.dataDir</name>
    <value>/home/hadoop/hbase-2.4.8/zookeeper</value>
  </property>
</configuration>
```

- Start HBase by running the `bin/start-hbase.sh` script:

```bash
$ bin/start-hbase.sh
```

- Verify that HBase is running by using the `jps` command, which should show the `HMaster` and `HRegionServer` processes:

```bash
$ jps
1234 HMaster
5678 HRegionServer
9012 Jps
```

- Connect to your running instance of HBase using the `bin/hbase shell` command, which is an interactive shell for HBase commands:

```bash
$ bin/hbase shell
HBase Shell
Use "help" to get list of supported commands.
Use "exit" to quit this interactive shell.
Version 2.4.8, rUnknown, Mon Oct 11 18:29:03 UTC 2021
Took 0.0050 seconds
hbase(main):001:0>
```

- You can use the `help` command to get a list of supported commands, or use `help 'command'` to get more information about a specific command. For example, to get help on the `create` command, which is used to create a table, you can type:

```bash
hbase(main):002:0> help 'create'
Create table; pass table name, a dictionary of specifications per column family,
and optionally a dictionary of table configuration.
Dictionaries are described below in the GENERAL NOTES section.
Examples:

  hbase> create 't1', {NAME => 'f1', VERSIONS => 5}
  hbase> create 't1', {NAME => 'f1'}, {NAME => 'f2'}, {NAME => 'f3'}
  hbase> # The above in shorthand would be the following:
  hbase> create 't1', 'f1', 'f2', 'f3'
  hbase> create 't1', {NAME => 'f1', VERSIONS => 1, TTL => 2592000, BLOCKCACHE => true}
  hbase> create 't1', {NAME => 'f1', CONFIGURATION => {'hbase.hstore.blockingStoreFiles' => '10'}}
  hbase> create 't1

```
