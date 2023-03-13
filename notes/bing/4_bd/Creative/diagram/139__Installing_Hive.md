Hive is a data warehouse software that facilitates querying and managing large datasets residing in distributed storage. To install Hive on Ubuntu, you need to follow these steps:

1. Download and untar Hive from the official website or use the command `wget http://archive.apache.org/dist/hive/hive-2.1.0/apache-hive-2.1.0-bin.tar.gz` in the terminal.
2. Configure Hive environment variables by editing the `.bashrc` file in your home directory. You need to set the `$HIVE_HOME` variable to point to the Hive installation directory and add `$HIVE_HOME/bin` to the `$PATH` variable. You also need to set the `$HADOOP_HOME` variable to point to the Hadoop installation directory if you have not done so already.
3. Edit the `hive-config.sh` file in the `$HIVE_HOME/bin` directory and add the following lines:

```
export HADOOP_HOME=/path/to/hadoop
export HIVE_CONF_DIR=$HIVE_HOME/conf
```

4. Create a `hive-site.xml` file in the `$HIVE_HOME/conf` directory and add the following configuration properties:

```
<configuration>
  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:derby:;databaseName=/path/to/metastore_db;create=true</value>
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

5. Start the Hive shell by running the command `hive` in the terminal. You should see a prompt like this:

```
hive>
```

You can now run Hive queries and commands in the shell.

#### Installing Hive

The following diagram illustrates the basic architecture of a Hive installation:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Hive Client   |    |   Hive Server   |    |   Hadoop DFS    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   hive shell    |    |   metastore     |    |   /user/hive    |
|   JDBC/ODBC     |    |   thrift server |    |   /tmp          |
|   applications  |    |   hive service  |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       |                     |                       |
       +---------------------+-----------------------+
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |