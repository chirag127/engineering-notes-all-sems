## Installation of Hive along with practice examples

Hive is a data warehouse software that facilitates querying and managing large datasets residing in distributed storage. Hive provides a SQL-like interface to data stored in Hadoop Distributed File System (HDFS) or other data storage systems such as Apache HBase. Hive also supports analysis of large datasets using MapReduce.

To install Hive on Ubuntu, you need to have Java and Hadoop installed on your system. You can follow these steps to install Hive:

- Download and extract the Hive tar file from the Apache Hive official download page . You can use the following command to download and untar Hive:

```bash
wget http://archive.apache.org/dist/hive/hive-2.1.0/apache-hive-2.1.0-bin.tar.gz
tar -xvzf apache-hive-2.1.0-bin.tar.gz
```

- Configure the Hive environment variables by editing the `~/.bashrc` file. You need to set the `$HIVE_HOME` variable to point to the Hive installation directory, and add the `$HIVE_HOME/bin` directory to the `$PATH` variable. You can use the following commands to edit the `~/.bashrc` file:

```bash
nano ~/.bashrc
```

Add the following lines at the end of the file:

```bash
export HIVE_HOME=/home/user/apache-hive-2.1.0-bin
export PATH=$PATH:$HIVE_HOME/bin
```

Save and exit the file, and then run the following command to apply the changes:

```bash
source ~/.bashrc
```

- Edit the `hive-config.sh` file in the `$HIVE_HOME/bin` directory. You need to add the `$HADOOP_HOME` variable to point to the Hadoop installation directory, and the `$HADOOP_HEAPSIZE` variable to specify the maximum heap size for the Hive client. You can use the following commands to edit the `hive-config.sh` file:

```bash
nano $HIVE_HOME/bin/hive-config.sh
```

Add the following lines at the end of the file:

```bash
export HADOOP_HOME=/home/user/hadoop-2.7.3
export HADOOP_HEAPSIZE=512
```

Save and exit the file.

- Create a Hive warehouse directory in HDFS. This is the default location where Hive stores the table data. You can use the following command to create the directory:

```bash
hdfs dfs -mkdir /user/hive/warehouse
```

- Start the Hive shell by running the following command:

```bash
hive
```

You should see a prompt like this:

```bash
Hive 2.1.0
hive>
```

You can now run Hive queries and commands from the shell. For example, you can create a table called `employees` with the following schema:

```sql
CREATE TABLE employees (
  id INT,
  name STRING,
  salary FLOAT,
  dept STRING
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```

You can load some data into the table from a local file called `employees.csv` with the following command:

```sql
LOAD DATA LOCAL INPATH '/home/user/employees.csv' INTO TABLE employees;
```

You can query the table with the following command:

```sql
SELECT * FROM employees;
```

You should see the output like this:

```bash
1 John 5000.0 IT
2 Mary 6000.0 HR
3 Bob 4000.0 Sales
4 Alice 7000.0 Marketing
```

You can exit the Hive shell by typing `quit;`.

This is a brief introduction to the installation and usage of Hive on Ubuntu. You can find more details and examples in the official Hive documentation  or other online resources  .