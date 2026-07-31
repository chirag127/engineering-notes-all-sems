## Installation of Hive along with practice examples

Hive is a data warehouse software that facilitates querying and managing large datasets residing in distributed storage. Hive provides a SQL-like interface to data stored in Hadoop. Hive can also be used to create tables, load data, and perform various transformations on the data.

To install Hive on Ubuntu, follow these steps:

- Download the latest version of Hive from the official website. For example, to download Hive 3.1.2, use this command:

```bash
wget http://archive.apache.org/dist/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz
```

- Extract the downloaded file using the tar command:

```bash
tar -xvzf apache-hive-3.1.2-bin.tar.gz
```

- Move the extracted folder to a desired location, such as /usr/local/hive:

```bash
sudo mv apache-hive-3.1.2-bin /usr/local/hive
```

- Set the environment variables for Hive in the ~/.bashrc file. Add these lines at the end of the file:

```bash
export HIVE_HOME=/usr/local/hive
export PATH=$PATH:$HIVE_HOME/bin
```

- Source the ~/.bashrc file to apply the changes:

```bash
source ~/.bashrc
```

- Edit the hive-config.sh file in the $HIVE_HOME/bin directory. Add these lines at the beginning of the file:

```bash
export HADOOP_HOME=/usr/local/hadoop
export HIVE_CONF_DIR=$HIVE_HOME/conf
```

- Create a hive-site.xml file in the $HIVE_HOME/conf directory. Add these lines to the file:

```xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:derby:;databaseName=/usr/local/hive/metastore_db;create=true</value>
    <description>JDBC connect string for a JDBC metastore</description>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>org.apache.derby.jdbc.EmbeddedDriver</value>
    <description>Driver class name for a JDBC metastore</description>
  </property>
  <property>
    <name>hive.metastore.warehouse.dir</name>
    <value>/user/hive/warehouse</value>
    <description>location of default database for the warehouse</description>
  </property>
</configuration>
```

- Start the Hive shell by typing hive in the terminal. You should see something like this:

```bash
$ hive
Hive Session ID = 7f0a9c0d-0f8c-4f0f-9f0a-9c0d0f8c4f0f
hive>
```

- To verify the installation, run some basic Hive commands, such as:

```sql
hive> show databases;
OK
default
Time taken: 0.546 seconds, Fetched: 1 row(s)
hive> create database testdb;
OK
Time taken: 0.323 seconds
hive> use testdb;
OK
Time taken: 0.018 seconds
hive> create table testtable (id int, name string);
OK
Time taken: 0.246 seconds
hive> show tables;
OK
testtable
Time taken: 0.049 seconds, Fetched: 1 row(s)
hive> insert into testtable values (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');
OK
Time taken: 1.234 seconds
hive> select * from testtable;
OK
1	Alice
2	Bob
3	Charlie
Time taken: 0.123 seconds, Fetched: 3 row(s)
hive> drop table testtable;
OK
Time taken: 0.098 seconds
hive> drop database testdb;
OK
Time taken: 0.087 seconds
hive> exit;
```

- Congratulations, you have successfully installed Hive and performed some basic operations on it. For more information and practice examples, refer to the official documentation or some online tutorials .