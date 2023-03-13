#### Installing Hive

Hive is a data warehouse system that runs on top of Hadoop. It provides a SQL-like interface to query and analyze large-scale structured and semi-structured data. To install Hive, you need to follow these steps:

- Download the latest version of Hive from the Apache website: https://hive.apache.org/downloads.html
- Extract the downloaded file to a desired location, such as /usr/local/hive
- Set the environment variables for Hive, such as HIVE_HOME, HIVE_CONF_DIR, and PATH. You can do this by editing the .bashrc file in your home directory and adding these lines:

```bash
export HIVE_HOME=/usr/local/hive
export HIVE_CONF_DIR=$HIVE_HOME/conf
export PATH=$PATH:$HIVE_HOME/bin
```

- Save and source the .bashrc file to apply the changes:

```bash
source ~/.bashrc
```

- Copy the MySQL JDBC driver to the Hive lib directory. You can download the driver from here: https://dev.mysql.com/downloads/connector/j/
- Create a MySQL database and user for Hive metastore. The metastore is a repository that stores the metadata of Hive tables, partitions, columns, etc. You can use these commands to create the database and user:

```sql
CREATE DATABASE hive;
CREATE USER 'hive'@'localhost' IDENTIFIED BY 'hive';
GRANT ALL PRIVILEGES ON hive.* TO 'hive'@'localhost';
FLUSH PRIVILEGES;
```

- Edit the hive-site.xml file in the Hive conf directory and set the following properties:

```xml
<property>
  <name>javax.jdo.option.ConnectionURL</name>
  <value>jdbc:mysql://localhost:3306/hive?createDatabaseIfNotExist=true</value>
  <description>JDBC connect string for a JDBC metastore</description>
</property>

<property>
  <name>javax.jdo.option.ConnectionDriverName</name>
  <value>com.mysql.jdbc.Driver</value>
  <description>Driver class name for a JDBC metastore</description>
</property>

<property>
  <name>javax.jdo.option.ConnectionUserName</name>
  <value>hive</value>
  <description>username to use against metastore database</description>
</property>

<property>
  <name>javax.jdo.option.ConnectionPassword</name>
  <value>hive</value>
  <description>password to use against metastore database</description>
</property>
```

- Initialize the Hive metastore schema by running this command:

```bash
schematool -dbType mysql -initSchema
```

- Start the Hive shell by running this command:

```bash
hive
```

- You can now use Hive to create and query tables. For example, you can create a table called employees with this command:

```sql
CREATE TABLE employees (
  id INT,
  name STRING,
  salary FLOAT,
  dept STRING
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```

- You can load data into the table from a local file with this command:

```sql
LOAD DATA LOCAL INPATH '/home/user/employees.csv' INTO TABLE employees;
```

- You can query the table with this command:

```sql
SELECT * FROM employees WHERE dept = 'Sales';
```

- You can exit the Hive shell with this command:

```sql
QUIT;
```

- A mnemonic to remember the steps of installing Hive is:

**D**ownload Hive
**E**xtract Hive
**S**et environment variables
**C**opy JDBC driver
**R**eate MySQL database and user
**I**nput hive-site.xml properties
**B**uild metastore schema
**E**nter Hive shell
**C**reate and query tables
**Q**uit Hive shell

**DESCRIBE CQ**