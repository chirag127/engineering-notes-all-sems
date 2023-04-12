## Installation of Hive along with practice examples

Hive is a data warehouse software that facilitates querying and managing large datasets residing in distributed storage. Hive provides a SQL-like interface to data stored in Hadoop. To install Hive on Ubuntu, follow these steps:

- Step 1: Download and untar Hive. Visit the [Apache Hive official download page](https://hive.apache.org/downloads.html) and determine which Hive version is best suited for your Hadoop edition. Once you establish which version you need, select the Download a Release Now! option. The mirror link on the subsequent page leads to the directories containing available Hive tar packages. You can download the Hive tar file using the `wget` command in the terminal:

```bash
wget http://archive.apache.org/dist/hive/hive-2.1.0/apache-hive-2.1.0-bin.tar.gz
```

- Step 2: Configure Hive environment variables. The `$HIVE_HOME` environment variable needs to direct the client to the Hive installation directory. The `$PATH` variable should include the `$HIVE_HOME/bin` directory. To set these variables, edit the `.bashrc` file in your home directory using a text editor such as `nano`:

```bash
nano ~/.bashrc
```

- Add the following lines at the end of the file, replacing the Hive version with the one you downloaded:

```bash
export HIVE_HOME=/usr/local/hive/apache-hive-2.1.0-bin
export PATH=$PATH:$HIVE_HOME/bin
```

- Save and exit the file, and then source it to apply the changes:

```bash
source ~/.bashrc
```

- Step 3: Edit `hive-config.sh` file. This file is located in the `$HIVE_HOME/bin` directory and contains some configuration parameters for Hive. You need to edit this file to specify the location of the Hadoop installation directory and the Java home directory. To do this, open the file using a text editor such as `nano`:

```bash
nano $HIVE_HOME/bin/hive-config.sh
```

- Add the following lines at the end of the file, replacing the Hadoop and Java versions with the ones you have installed:

```bash
export HADOOP_HOME=/usr/local/hadoop/hadoop-2.7.3
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

- Save and exit the file.

- Step 4: Create a Hive warehouse directory. This is the directory where Hive will store the data for the tables. You need to create this directory in HDFS and give it appropriate permissions. To do this, use the following commands:

```bash
hdfs dfs -mkdir /user/hive/warehouse
hdfs dfs -chmod g+w /user/hive/warehouse
```

- Step 5: Start Hive shell. To verify that Hive is installed correctly, you can start the Hive shell and run some commands. To start the Hive shell, use the following command:

```bash
hive
```

- You should see a prompt like this:

```bash
hive>
```

- You can now run some Hive commands to create tables, load data, and query data. For example, you can create a table called `employees` with three columns: `id`, `name`, and `salary`:

```bash
hive> CREATE TABLE employees (id INT, name STRING, salary FLOAT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```

- You can load some data from a local file into the table using the `LOAD DATA` command. For example, if you have a file called `emp.txt` in your home directory with the following content:

```bash
1,John,5000
2,Mary,6000
3,Bob,7000
4,Alice,8000
```

- You can load this file into the `employees` table using the following command:

```bash
hive> LOAD DATA LOCAL INPATH '/home/ubuntu/emp.txt' INTO TABLE employees;
```

- You can query the data in the table using the `SELECT` command. For example, you can find the average salary of the employees using the following command:

```bash
hive> SELECT AVG(salary) FROM employees;
```

- You should see the output like this:

```bash
OK
6500.0
Time taken

```
