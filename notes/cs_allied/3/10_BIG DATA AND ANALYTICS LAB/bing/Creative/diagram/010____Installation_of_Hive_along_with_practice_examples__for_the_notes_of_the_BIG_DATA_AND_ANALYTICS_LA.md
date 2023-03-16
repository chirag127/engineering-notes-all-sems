## Installation of Hive along with practice examples

Hive is a data warehouse software that facilitates querying and managing large datasets residing in distributed storage. Hive provides a SQL-like interface to data stored in Hadoop Distributed File System (HDFS) or other data storage systems such as Apache HBase. Hive also supports analysis of large datasets using MapReduce.

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

- Configure the environment variables for Hive by editing the ~/.bashrc file. You can use the following commands to open the file and append the variables:

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

- Edit the hive-config.sh file in the $HIVE_HOME/bin directory to add the Hadoop home directory. You can use the following command to open the file and add the line:

```bash
nano $HIVE_HOME/bin/hive-config.sh
```

```bash
export HADOOP_HOME=/usr/local/hadoop
```

- Save and exit the file.

- Create a Hive warehouse directory in HDFS to store the Hive data. You can use the following command to create the directory:

```bash
hdfs dfs -mkdir -p /user/hive/warehouse
```

- Change the permission of the warehouse directory to allow read and write access. You can use the following command to change the permission:

```bash
hdfs dfs -chmod g+w /user/hive/warehouse
```

- Verify the installation by running the hive command. You should see the Hive shell prompt:

```bash
hive
```

```bash
Hive 3.1.2
hive>
```

To practice some examples of Hive queries, you can use the sample data provided by Hive. You can follow these steps to load and query the sample data:

- In the Hive shell, create a database called sampledb:

```sql
CREATE DATABASE sampledb;
```

- Use the sampledb database:

```sql
USE sampledb;
```

- Create a table called employees with four columns: name, salary, dept, and subdept:

```sql
CREATE TABLE employees (name STRING, salary INT, dept STRING, subdept STRING);
```

- Load the sample data from the $HIVE_HOME/examples/files/emp.txt file into the employees table:

```sql
LOAD DATA LOCAL INPATH '$HIVE_HOME/examples/files/emp.txt' INTO TABLE employees;
```

- Verify the data by selecting all the rows from the employees table:

```sql
SELECT * FROM employees;
```

- You should see the following output:

```sql
Alice	10000	IT	Software
Bob	12000	IT	Hardware
Charlie	8000	Marketing	Digital
David	9000	Marketing	Offline
Eve	11000	Finance	Accounting
Frank	13000	Finance	Auditing
```

- You can perform various queries on the employees table, such as:

  - Find the average salary of each department:

  ```sql
  SELECT dept, AVG(salary) FROM employees GROUP BY dept;
  ```

  - Find the name and salary of the highest paid employee in each subdepartment:

  ```sql
  SELECT e.name, e.salary FROM employees e JOIN (SELECT subdept, MAX(salary) AS max_salary FROM employees GROUP BY subdept) m ON e.subdept = m.subdept AND e.salary = m.max_salary;
  ```

  - Find the name and salary of the employees who earn more than the average salary of their department:

  ```sql
  SELECT e.name, e.salary FROM employees e JOIN (SELECT dept, AVG(salary) AS avg_salary FROM employees