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
# Uncomment the following line and set the correct path
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

- Edit the `conf/hbase-site.xml` file and add the following properties to configure HBase to use the local file system instead of HDFS :

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

- Start HBase by running the `bin/start-hbase.sh` script :

```bash
$ bin/start-hbase.sh
```

- Verify that HBase is running by using the `jps` command, which should show the `HMaster` and `HRegionServer` processes :

```bash
$ jps
1234 HMaster
5678 HRegionServer
9012 Jps
```

- Connect to your running instance of HBase using the `hbase shell` command, located in the `bin/` directory of your HBase install:

```bash
$ bin/hbase shell
HBase Shell
Use "help" to get list of supported commands.
Use "exit" to quit this interactive shell.
For Reference, please visit: http://hbase.apache.org/2.0/book.html#shell
Version 2.4.8, rUnknown, Mon Oct 18 18:22:01 UTC 2021
Took 0.0051 seconds
hbase(main):001:0>
```

### Installing Thrift

Thrift is a software framework that allows cross-language service development. It supports several languages, including Java, Python, Ruby, C++, and PHP. Thrift can be used to access HBase from languages other than Java, using a Thrift server that acts as a proxy between the client and the HBase cluster.

To install Thrift, you need to have some prerequisites installed, such as automake, libtool, bison, flex, and libboost:

```bash
$ sudo apt-get install automake libtool flex bison pkg-config g++ libssl-dev libboost-all-dev
```

Then, you can download the latest stable version of Thrift from https://thrift.apache.org/download and compile it from source:

```bash
$ wget https://downloads.apache.org/thrift/0.15.0/thrift-0.15.0.tar.gz
$ tar xzf thrift-0.15.0.tar.gz
$ cd thrift-0.15.0
$ ./configure --with-java --with-python --with-ruby --with-cpp --with-php
$ make
$ sudo make install
```

To verify that Thrift is installed correctly, you