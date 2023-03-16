## Installation of HBase

HBase is a distributed, scalable, and column-oriented database that runs on top of the Hadoop Distributed File System (HDFS). It provides random, real-time read/write access to large datasets. HBase can be installed in three modes: standalone, pseudo-distributed, and fully distributed. In this note, we will focus on the standalone mode, which is the simplest and easiest way to get started with HBase.

### Installing HBase in Standalone Mode

To install HBase in standalone mode, you need to follow these steps:

1. Download the latest stable version of HBase from https://hbase.apache.org/downloads.html. For example, you can download the hbase-2.4.9-bin.tar.gz file.
2. Unzip the downloaded file and place it in a desired location, such as /usr/local/hbase or C:/Document/hbase-2.4.9.
3. Edit the hbase-2.4.9/conf/hbase-env.sh file and set the JAVA_HOME environment variable to point to your Java installation directory. For example, you can add the following line to the file:

   `export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64`

4. Edit the hbase-2.4.9/conf/hbase-site.xml file and add the following properties to configure HBase to use the local file system instead of HDFS:

   ```xml
   <configuration>
     <property>
       <name>hbase.rootdir</name>
       <value>file:///home/hduser/hbase</value>
     </property>
     <property>
       <name>hbase.zookeeper.property.dataDir</name>
       <value>/home/hduser/zookeeper</value>
     </property>
   </configuration>
   ```

   Note: You can change the values of the properties according to your preferences, but make sure the directories exist and have proper permissions.

5. Start HBase by running the hbase-2.4.9/bin/start-hbase.sh script. You should see a message like this:

   `starting master, logging to /usr/local/hbase/logs/hbase-hduser-master-hduser.out`

6. Verify that HBase is running by opening the web UI at http://localhost:16010. You should see a dashboard like this:

   ![HBase web UI](https://www.guru99.com/images/1/010318_0618_HBaseInstal1.png)

7. You can also use the hbase-2.4.9/bin/hbase shell command to interact with HBase using the HBase shell, which is a command-line interface that supports various operations on tables, regions, and data. For example, you can create a table, insert some data, scan the table, and drop the table using the following commands:

   ```shell
   hbase(main):001:0> create 'test', 'cf'
   Created table test
   Took 1.3785 seconds
   => Hbase::Table - test
   hbase(main):002:0> put 'test', 'row1', 'cf:col1', 'value1'
   Took 0.0198 seconds
   hbase(main):003:0> put 'test', 'row2', 'cf:col2', 'value2'
   Took 0.0045 seconds
   hbase(main):004:0> scan 'test'
   ROW                   COLUMN+CELL
    row1                 column=cf:col1, timestamp=1639639472613, value=value1
    row2                 column=cf:col2, timestamp=1639639476660, value=value2
   2 row(s)
   Took 0.0129 seconds
   hbase(main):005:0> disable 'test'
   Took 0.4598 seconds
   hbase(main):006:0> drop 'test'
   Took 0.2169 seconds
   ```