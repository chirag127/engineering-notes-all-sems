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

- Edit the `conf/hbase-env.sh` file and set the `JAVA_HOME` variable to point to your Java installation directory. For example:

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

- Edit the `conf/hbase-site.xml` file and add the following properties:

```xml
<configuration>
  <property>
    <name>hbase.rootdir</name>
    <value>file:///home/hadoop/hbase</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.dataDir</name>
    <value>/home/hadoop/zookeeper</value>
  </property>
</configuration>
```

The `hbase.rootdir` property specifies the directory where HBase stores its data. The `hbase.zookeeper.property.dataDir` property specifies the directory where ZooKeeper, a distributed coordination service for HBase, stores its data. You can change these directories according to your preference, but make sure they exist and have proper permissions.

- Start HBase by running the `bin/start-hbase.sh` script. You should see a message like this:

```bash
$ bin/start-hbase.sh
running master, logging to /home/hadoop/hbase-2.4.8/logs/hbase-hadoop-master-localhost.localdomain.out
```

- Verify that HBase is running by connecting to the HBase shell, a command-line interface for interacting with HBase. You can launch the shell by running the `bin/hbase shell` command. You should see a prompt like this:

```bash
$ bin/hbase shell
HBase Shell
Use "help" to get list of supported commands.
Use "exit" to quit this interactive shell.
For Reference, please visit: http://hbase.apache.org/2.0/book.html#shell
Version 2.4.8, rUnknown, Mon Sep 13 15:12:16 PDT 2021
Took 0.0050 seconds
hbase(main):001:0>
```

- You can use the HBase shell to create, list, scan, and delete tables, as well as perform other operations on HBase. For example, to create a table called `test` with a column family called `cf`, you can use the following command:

```bash
hbase(main):002:0> create 'test', 'cf'
Created table test
Took 1.234 seconds
=> Hbase::Table - test
```

- To list all the tables in HBase, you can use the following command:

```bash
hbase(main):003:0> list
TABLE
test
1 row(s)
Took 0.012 seconds
=> ["test"]
```

- To scan the contents of a table, you can use the following command:

```bash
hbase(main):004:0> scan 'test'
ROW                   COLUMN+CELL
0 row(s)
Took 0.010 seconds
```

- To insert a row into a table, you can use the following command:

```bash
hbase(main):005:0> put 'test', 'row1', 'cf:col1', 'value1'
Took 0.012 seconds
```

- To get a row