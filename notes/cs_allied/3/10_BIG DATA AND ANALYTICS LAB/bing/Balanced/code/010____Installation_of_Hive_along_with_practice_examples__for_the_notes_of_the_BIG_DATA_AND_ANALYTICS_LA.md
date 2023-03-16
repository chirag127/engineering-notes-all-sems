## Installation of Hive along with practice examples

Hive is a data warehouse software that facilitates querying and managing large datasets residing in distributed storage. Hive provides a SQL-like interface to data stored in Hadoop. To install Hive on Ubuntu, you can follow these steps:

- Download and untar Hive from the official Apache Hive website. You can use the following command in the terminal to download the Hive tar file:

```bash
wget http://archive.apache.org/dist/hive/hive-2.1.0/apache-hive-2.1.0-bin.tar.gz
```

- Extract the tar file using the following command:

```bash
tar -xvzf apache-hive-2.1.0-bin.tar.gz
```

- Move the extracted folder to a desired location, such as `/usr/local/hive`. You can use the following command:

```bash
sudo mv apache-hive-2.1.0-bin /usr/local/hive
```

- Configure the Hive environment variables by editing the `~/.bashrc` file. You can use the following command to open the file:

```bash
nano ~/.bashrc
```

- Add the following lines at the end of the file:

```bash
export HIVE_HOME=/usr/local/hive
export PATH=$PATH:$HIVE_HOME/bin
```

- Save and exit the file by pressing `Ctrl+O` and `Ctrl+X`.

- Source the `~/.bashrc` file to apply the changes:

```bash
source ~/.bashrc
```

- Edit the `hive-config.sh` file in the `$HIVE_HOME/bin` directory. You can use the following command to open the file:

```bash
nano $HIVE_HOME/bin/hive-config.sh
```

- Add the following line at the end of the file:

```bash
export HADOOP_HOME=/usr/local/hadoop
```

- Save and exit the file by pressing `Ctrl+O` and `Ctrl+X`.

- Create a `hive-site.xml` file in the `$HIVE_HOME/conf` directory. You can use the following command to create the file:

```bash
nano $HIVE_HOME/conf/hive-site.xml
```

- Add the following content to the file:

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

- Save and exit the file by pressing `Ctrl+O` and `Ctrl+X`.

- Initialize the Hive metastore by running the following command:

```bash
schematool -initSchema -dbType derby
```

- Start the Hive shell by running the following command:

```bash
hive
```

- You should see a prompt like this:

```bash
hive>
```

- You can now run Hive queries and commands in the shell. For example, you can create a table called `employees` with the following schema:

```sql
CREATE TABLE employees (
  id INT,
  name STRING,
  salary FLOAT,
  dept STRING
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```

- You can load some data into the table from a local file called `employees.csv` with the following command:

```sql
LOAD DATA LOCAL INPATH '/home/user/employees.csv' INTO TABLE employees;
```

- You can query the table with the following command:

```sql
SELECT * FROM employees;
```

- You can exit the Hive shell by typing `quit;` or `exit;`.