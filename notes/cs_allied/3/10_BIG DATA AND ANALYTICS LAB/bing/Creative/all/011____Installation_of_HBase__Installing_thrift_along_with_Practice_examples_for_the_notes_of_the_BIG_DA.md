# Installation of HBase, Installing thrift along with Practice examples for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

HBase is a distributed, scalable, and column-oriented database that runs on top of the Hadoop Distributed File System (HDFS). It provides random, real-time read/write access to large datasets. HBase is modeled after Google's Bigtable, a distributed storage system for structured data.

To install HBase, you need to have Java and Hadoop installed on your Linux machine. HBase can be installed in three modes: standalone, pseudo-distributed, and fully distributed. In this note, we will focus on the standalone mode, which is the simplest and easiest way to get started with HBase.

## Installing HBase in Standalone Mode

- Download the latest stable version of HBase from http://www.interior-dsgn.com/apache/hbase/stable/ and unzip it with the following commands:

  ```bash
  wget http://www.interior-dsgn.com/apache/hbase/stable/hbase-2.4.8-bin.tar.gz
  tar xzf hbase-2.4.8-bin.tar.gz
  ```

- Move the extracted folder to a preferred location, such as `/usr/local/hbase`:

  ```bash
  sudo mv hbase-2.4.8 /usr/local/hbase
  ```

- Edit the `hbase-env.sh` file in the `conf` directory of your HBase installation and set the `JAVA_HOME` variable to point to your Java installation directory:

  ```bash
  sudo nano /usr/local/hbase/conf/hbase-env.sh
  ```

  Add the following line:

  ```bash
  export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
  ```

  Save and exit the file.

- Edit the `hbase-site.xml` file in the same directory and add the following configuration properties:

  ```bash
  sudo nano /usr/local/hbase/conf/hbase-site.xml
  ```

  Add the following lines between the `<configuration>` and `</configuration>` tags:

  ```xml
  <property>
    <name>hbase.rootdir</name>
    <value>file:///usr/local/hbase/data</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.dataDir</name>
    <value>/usr/local/hbase/zookeeper</value>
  </property>
  ```

  Save and exit the file.

- Start HBase by running the `start-hbase.sh` script in the `bin` directory of your HBase installation:

  ```bash
  sudo /usr/local/hbase/bin/start-hbase.sh
  ```

- Verify that HBase is running by connecting to it using the `hbase shell` command, also located in the `bin` directory:

  ```bash
  /usr/local/hbase/bin/hbase shell
  ```

  You should see a prompt that ends with a `>` character.

- You can now use the HBase shell to create, list, and manipulate tables. For example, to create a table called `test` with a column family called `cf`, you can use the following command:

  ```bash
  create 'test', 'cf'
  ```

  To list all the tables in HBase, you can use the following command:

  ```bash
  list
  ```

  To insert a row with a key of `row1` and a value of `value1` in the column `cf:a` of the table `test`, you can use the following command:

  ```bash
  put 'test', 'row1', 'cf:a', 'value1'
  ```

  To scan the table `test` and see all the rows, you can use the following command:

  ```bash
  scan 'test'
  ```

  To exit the HBase shell, you can use the following command:

  ```bash
  exit
  ```

- To stop HBase, you can run the `stop-hbase.sh` script in the `bin` directory of your HBase installation:

  ```bash
  sudo /usr/local/hbase/bin/stop-hbase.sh
  ```

## Installing Thrift

Thrift is a software framework that allows cross-language communication between