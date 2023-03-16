## Installation of HBase, Installing thrift along with Practice examples

HBase is a distributed, scalable, and column-oriented database that runs on top of the Hadoop Distributed File System (HDFS). It provides random, real-time read/write access to large datasets. HBase is modeled after Google's Bigtable, a distributed storage system for structured data.

To install HBase, you need to have Java and Hadoop installed on your Linux machine. HBase can be installed in three modes: standalone, pseudo-distributed, and fully distributed. In this note, we will focus on the standalone mode, which is the simplest and easiest way to get started with HBase.

### Steps to install HBase in standalone mode

1. Download the latest stable version of HBase from http://www.interior-dsgn.com/apache/hbase/stable/ and unzip it with the following commands:

```bash
$ wget http://www.interior-dsgn.com/apache/hbase/stable/hbase-2.4.9-bin.tar.gz
$ tar xzf hbase-2.4.9-bin.tar.gz
$ cd hbase-2.4.9
```

2. Edit the `conf/hbase-env.sh` file and set the `JAVA_HOME` variable to point to your Java installation directory. For example:

```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

3. Edit the `conf/hbase-site.xml` file and add the following properties:

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

4. Start HBase by running the `bin/start-hbase.sh` script. This will start a HBase master server and a region server on your local machine. You can check the status of HBase by visiting http://localhost:16010 in your browser.

5. Connect to your running instance of HBase using the `bin/hbase shell` command. This will launch an interactive shell where you can execute HBase commands. For example, you can create a table, insert some data, and scan the table using the following commands:

```bash
hbase(main):001:0> create 'test', 'cf'
Created table test
Took 1.2345 seconds
hbase(main):002:0> put 'test', 'row1', 'cf:a', 'value1'
Took 0.1234 seconds
hbase(main):003:0> put 'test', 'row2', 'cf:b', 'value2'
Took 0.1234 seconds
hbase(main):004:0> scan 'test'
ROW                   COLUMN+CELL
 row1                 column=cf:a, timestamp=1637047684123, value=value1
 row2                 column=cf:b, timestamp=1637047685123, value=value2
2 row(s)
Took 0.1234 seconds
```

6. To stop HBase, run the `bin/stop-hbase.sh` script. This will stop the HBase master and region server processes.

### Steps to install thrift in HBase

Thrift is a framework for cross-language services development. It allows you to define data types and service interfaces in a simple definition file, and generates code for different languages to communicate with each other. Thrift supports many languages, including Java, Python, Ruby, C++, and PHP.

To install thrift in HBase, you need to have thrift installed on your machine. You can download the latest version of thrift from https://thrift.apache.org/download and follow the instructions to install it. Alternatively, you can use a package manager to install thrift, such as `apt-get` or `yum`.

After installing thrift, you need to enable the thrift server in HBase. To do this, edit the `conf/hbase-site.xml` file and add the following property:

```xml
<property>
  <name>hbase.regionserver.thrift