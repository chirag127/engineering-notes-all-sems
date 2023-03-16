## Installation of Hive along with practice examples

Hive is a data warehouse software that facilitates querying and managing large datasets residing in distributed storage. Hive provides a SQL-like interface to data stored in Hadoop Distributed File System (HDFS) or other storage systems such as Amazon S3. Hive can also be used to create tables, partitions, and buckets to organize data.

To install Hive on Ubuntu, you need to have Java and Hadoop installed on your system. You can follow these steps to install Hive:

- Download and untar Hive from the official website. You can use the following command to download the latest version of Hive:

```bash
wget http://archive.apache.org/dist/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz
```

- Extract the tar file using the following command:

```bash
tar -xvzf apache-hive-3.1.2-bin.tar.gz
```

- Move the extracted folder to a desired location, such as /usr/local/hive:

```bash
sudo mv apache-hive-3.1.2-bin /usr/local/hive
```

- Configure Hive environment variables by editing the ~/.bashrc file. You can use the following commands to open the file and append the variables:

```bash
nano ~/.bashrc
```

```bash
export HIVE_HOME=/usr/local/hive
export PATH=$PATH:$HIVE_HOME/bin
```

- Save and exit the file, and then source it to apply the changes:

```bash
source ~/.bashrc
```

- Edit the hive-config.sh file in the $HIVE_HOME/bin directory. You can use the following command to open the file and add the HADOOP_HOME variable:

```bash
nano $HIVE_HOME/bin/hive-config.sh
```

```bash
export HADOOP_HOME=/usr/local/hadoop
```

- Save and exit the file.

- Create a hive-site.xml file in the $HIVE_HOME/conf directory. You can use the following command to copy the template file and rename it:

```bash
cp $HIVE_HOME/conf/hive-default.xml.template $HIVE_HOME/conf/hive-site.xml
```

- Edit the hive-site.xml file and configure the Hive metastore. The metastore is a database that stores the metadata of the Hive tables and partitions. You can use any relational database such as MySQL, PostgreSQL, or Derby as the metastore. For this example, we will use Derby, which is bundled with Hive. You can use the following command to open the file and add the following properties:

```bash
nano $HIVE_HOME/conf/hive-site.xml
```

```xml
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
```

- Save and exit the file.

- Initialize the Hive metastore schema by running the following command:

```bash
schematool -dbType derby -initSchema
```

- You should see a message saying "Initialization script completed".

- You can now start the Hive shell by running the following command:

```bash
hive
```

- You should see a prompt like this:

```bash
hive>
```

- You can now run Hive queries and commands on the shell. For example, you can create a table called students with the following command:

```sql
CREATE TABLE students (id INT, name STRING, age INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```

- You can load some data into the table from a local file with the following command:

```sql
LOAD DATA LOCAL INPATH '/home/user/students.csv' INTO TABLE students;
```

- You can query the table with the following command:

```sql
SELECT * FROM students;
```

- You should see the output like this:

```bash
id      name    age
1       Alice   20
2       Bob     21
3       Charlie 19
```

- You can exit the Hive shell by typing `quit;` or pressing Ctrl+D.