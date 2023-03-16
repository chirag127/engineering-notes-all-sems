## Installation of HBase, Installing thrift along with Practice examples for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

HBase is a distributed, scalable, and column-oriented database that runs on top of the Hadoop Distributed File System (HDFS). It provides random, real-time read/write access to large datasets. HBase is modeled after Google's Bigtable, a distributed storage system for structured data.

To install HBase, you need to have Java and Hadoop installed on your Linux machine. HBase can be installed in three modes: standalone, pseudo-distributed, and fully distributed. In this note, we will focus on the standalone mode, which is the simplest and easiest way to get started with HBase.

### Steps to install HBase in standalone mode

1. Download the latest stable version of HBase from http://www.interior-dsgn.com/apache/hbase/stable/ and unzip it with the following commands:

```
$ wget http://www.interior-dsgn.com/apache/hbase/stable/hbase-2.4.8-bin.tar.gz
$ tar xzf hbase-2.4.8-bin.tar.gz
$ cd hbase-2.4.8
```

2. Edit the `conf/hbase-env.sh` file and set the `JAVA_HOME` variable to point to your Java installation directory. For example:

```
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

3. Edit the `conf/hbase-site.xml` file and add the following properties:

```
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

The `hbase.rootdir` property specifies the directory where HBase stores its data. The `hbase.zookeeper.property.dataDir` property specifies the directory where ZooKeeper, a distributed coordination service used by HBase, stores its data. You can change these directories according to your preference, but make sure they exist and have proper permissions.

4. Start HBase by running the `bin/start-hbase.sh` script. You should see a message like this:

```
$ bin/start-hbase.sh
running master, logging to /home/hadoop/hbase-2.4.8/logs/hbase-hadoop-master-localhost.localdomain.out
```

5. Connect to your running instance of HBase using the `bin/hbase shell` command, located in the `bin/` directory of your HBase installation. You should see a prompt like this:

```
$ bin/hbase shell
HBase Shell
Use "help" to get list of supported commands.
Use "exit" to quit this interactive shell.
For Reference, please visit: http://hbase.apache.org/2.0/book.html#shell
Version 2.4.8, rUnknown, Mon Oct 11 16:08:28 PDT 2021
Took 0.0059 seconds
hbase(main):001:0>
```

You can use the `help` command to get a list of supported commands, or visit the HBase reference guide for more details.

### Steps to install thrift in standalone mode

Thrift is a software framework that allows cross-language service development. It supports several languages, including Java, Python, Ruby, C++, and PHP. Thrift can be used to communicate with HBase from different languages using a common interface definition language (IDL).

To install thrift in standalone mode, you need to have the following prerequisites:

- A C++ compiler, such as GCC or Clang
- Automake, Autoconf, and Libtool
- Bison and Flex
- Boost C++ libraries
- OpenSSL
- Java Development Kit (JDK)
- Ant

You can install these dependencies using your package manager, such as `apt`, `yum`, or `brew`.

To install thrift, follow these steps:

1. Download the latest stable version of thrift from https://thrift.apache.org/download and unzip it with the following commands:

```
$ wget https://downloads.apache.org/thrift/0.15.0/thrift-0.15.0.tar.gz
$ tar xzf thrift-0.15.0.tar.gz
$ cd thrift-0.15.0
```

2. Configure