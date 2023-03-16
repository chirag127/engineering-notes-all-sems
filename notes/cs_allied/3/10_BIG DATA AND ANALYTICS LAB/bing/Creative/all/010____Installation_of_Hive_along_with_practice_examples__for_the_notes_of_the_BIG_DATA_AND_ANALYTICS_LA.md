# Installation of Hive along with practice examples

Hive is a data warehouse software that facilitates querying and managing large datasets residing in distributed storage. Hive provides a SQL-like interface to data stored in Hadoop. Hive can also be used to perform ETL (Extract, Transform, and Load) operations on big data.

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
export HIVE_CONF_DIR=/usr/local/hive/conf
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

- Initialize the Hive metastore using the schematool command:

```bash
schematool -initSchema -dbType derby
```

- Start the Hive shell using the hive command:

```bash
hive
```

- You can now use Hive to create tables, load data, and run queries. For example, to create a table called employees with four columns, use this command:

```sql
CREATE TABLE employees (id INT, name STRING, salary FLOAT, dept STRING);
```

- To load data from a local file into the table, use this command:

```sql
LOAD DATA LOCAL INPATH '/home/user/employees.txt' INTO TABLE employees;
```

- To query the table, use this command:

```sql
SELECT * FROM employees;
```

- To exit the Hive shell, use this command:

```sql
quit;
```