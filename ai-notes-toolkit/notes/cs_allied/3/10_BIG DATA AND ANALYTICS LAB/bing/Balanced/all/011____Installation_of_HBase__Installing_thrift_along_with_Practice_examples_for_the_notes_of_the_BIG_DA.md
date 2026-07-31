# Installation of HBase, Installing thrift along with Practice examples

HBase is a distributed, scalable, and column-oriented database that runs on top of the Hadoop Distributed File System (HDFS). It provides random, real-time read/write access to large datasets. HBase is modeled after Google's Bigtable, a distributed storage system for structured data.

To install HBase, you need to have Java and Hadoop installed on your Linux machine. HBase can be installed in three modes: standalone, pseudo-distributed, and fully distributed. In this note, we will focus on the standalone mode, which is the simplest and easiest way to get started with HBase.

## Steps to install HBase in standalone mode

1. Download the latest stable version of HBase from http://www.interior-dsgn.com/apache/hbase/stable/ and unzip it with the following commands:

```bash
$ wget http://www.interior-dsgn.com/apache/hbase/stable/hbase-2.4.8-bin.tar.gz
$ tar xzf hbase-2.4.8-bin.tar.gz
$ cd hbase-2.4.8
```

2. Edit the `conf/hbase-env.sh` file and set the `JAVA_HOME` environment variable to point to your Java installation directory. For example:

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

3. Edit the `conf/hbase-site.xml` file and add the following properties to configure HBase to use the local file system instead of HDFS:

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

4. Start HBase by running the `bin/start-hbase.sh` script. This will launch a single HBase master server and a single region server, as well as a ZooKeeper server, which is used for coordination and configuration management.

```bash
$ bin/start-hbase.sh
```

5. Connect to your running instance of HBase using the `bin/hbase shell` command, which provides a command-line interface to interact with HBase. You can use the `help` command to see the available commands and options.

```bash
$ bin/hbase shell
HBase Shell
Use "help" to get list of supported commands.
Use "exit" to quit this interactive shell.
For Reference, please visit: http://hbase.apache.org/2.0/book.html#shell
Version 2.4.8, rUnknown, Mon Sep 13 18:42:10 PDT 2021
Took 0.0050 seconds
hbase(main):001:0> help
```

## Steps to install thrift in standalone mode

Thrift is a software framework that allows cross-language service development. It supports multiple programming languages, such as Java, Python, Ruby, C++, etc. Thrift can be used to access HBase from different languages using a common interface.

To install thrift in standalone mode, you need to have the following prerequisites:

- A C++ compiler, such as gcc or g++
- Automake, autoconf, and libtool
- Boost C++ libraries
- Bison and flex
- OpenSSL
- Java Development Kit (JDK)
- Ant

You can install these dependencies using the package manager of your Linux distribution. For example, on Ubuntu, you can use the following command:

```bash
$ sudo apt-get install build-essential automake autoconf libtool libboost-all-dev bison flex libssl-dev openjdk-8-jdk ant
```

Then, you can follow these steps to install thrift:

1. Download the latest stable version of thrift from https://thrift.apache.org/download and unzip it with the following commands:

```bash
$ wget https://downloads.apache.org/thrift/0.15.0/thrift-0.15.0.tar.gz
$ tar xzf thrift-0.15.0.tar.gz
$ cd thrift-0.15.0
```

2. Configure and build thrift with the following commands:

```bash
$ ./configure --with-java --with-cpp
$ make
$ sudo make install
```

3. Verify that thrift is installed correctly by running the `thrift -version` command. You should see something