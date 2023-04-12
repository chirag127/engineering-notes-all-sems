

# BIG DATA AND ANALYTICS LAB

- Big data and analytics lab is a course that teaches students how to use various tools and techniques to analyze large and complex data sets.
- The course covers topics such as data preprocessing, data visualization, data mining, machine learning, and big data frameworks.
- The course also provides hands-on experience with various software and platforms such as R, Python, Weka, Tableau, Hadoop, Spark, and MongoDB.
- The course objectives are to:
  - Understand the concepts and challenges of big data and analytics.
  - Learn how to apply data preprocessing methods to clean, transform, and integrate data.
  - Learn how to use data visualization techniques to explore and communicate data insights.
  - Learn how to use data mining and machine learning algorithms to discover patterns and make predictions from data.
  - Learn how to use big data frameworks to process and analyze large-scale data in parallel and distributed environments.
  - Learn how to use NoSQL databases to store and query unstructured and semi-structured data.
- The course outcomes are to:
  - Demonstrate the ability to use various tools and techniques for big data and analytics.
  - Demonstrate the ability to perform data analysis tasks such as classification, clustering, association, and regression.
  - Demonstrate the ability to evaluate the quality and performance of data analysis results.
  - Demonstrate the ability to communicate data analysis findings and recommendations effectively.
  - Demonstrate the ability to work in teams and collaborate on data analysis projects.



## Downloading and installing Hadoop; Understanding different Hadoop modes. Startup scripts, Configuration files.

- Hadoop is an open-source framework for distributed storage and processing of large-scale data using clusters of commodity hardware.
- Hadoop consists of four main components: Hadoop Distributed File System (HDFS), MapReduce, YARN, and Hadoop Common.
- Hadoop can run in different modes: standalone, pseudo-distributed, and fully distributed.
- Standalone mode is the default mode of Hadoop, where it runs as a single Java process on a local file system. This mode is useful for testing and debugging purposes, but not for production use.
- Pseudo-distributed mode is where Hadoop runs on a single node, but simulates a distributed environment by using HDFS and running multiple Java processes. This mode is also useful for testing and development, but not for large-scale data processing.
- Fully distributed mode is where Hadoop runs on a cluster of multiple nodes, each running one or more Hadoop daemons. This mode is the most realistic and scalable mode of Hadoop, where it can handle petabytes of data and thousands of concurrent tasks.
- To download and install Hadoop on Ubuntu, follow these steps:
  - Visit the official Apache Hadoop project page, and select the version of Hadoop you want to implement. The steps outlined in this tutorial use the Binary download for Hadoop Version 3.2.1.
  - Use the provided mirror link and download the Hadoop package with the wget command: `wget https://downloads.apache.org/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz`
  - Once the download is complete, extract the files to initiate the Hadoop installation: `tar -xvzf hadoop-3.2.1.tar.gz`
  - Move the extracted files to the /usr/local directory: `sudo mv hadoop-3.2.1 /usr/local/hadoop`
  - Set the ownership of the Hadoop directory to the current user: `sudo chown -R $USER:$USER /usr/local/hadoop`
  - Set the JAVA_HOME environment variable in the /usr/local/hadoop/etc/hadoop/hadoop-env.sh file: `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64`
  - Edit the /usr/local/hadoop/etc/hadoop/core-site.xml file and add the following configuration: `<configuration> <property> <name>fs.defaultFS</name> <value>hdfs://localhost:9000</value> </property> </configuration>`
  - Edit the /usr/local/hadoop/etc/hadoop/hdfs-site.xml file and add the following configuration: `<configuration> <property> <name>dfs.replication</name> <value>1</value> </property> <property> <name>dfs.namenode.name.dir</name> <value>file:///home/$USER/hadoopdata/hdfs/namenode</value> </property> <property> <name>dfs.datanode.data.dir</name> <value>file:///home/$USER/hadoopdata/hdfs/datanode</value> </property> </configuration>`
  - Create the directories specified in the configuration files: `mkdir -p ~/hadoopdata/hdfs/namenode` and `mkdir -p ~/hadoopdata/hdfs/datanode`
  - Edit the /usr/local/hadoop/etc/hadoop/mapred-site.xml file and add the following configuration: `<configuration> <property> <name>mapreduce.framework.name</name> <value>yarn</value> </property> </configuration>`
  - Edit the /usr/local/hadoop/etc/hadoop/yarn-site.xml file and add the following configuration: `<configuration> <property> <name>yarn.nodemanager.aux-services</name> <value>mapreduce_shuffle</value> </property> <property> <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name> <value>org.apache.hadoop.mapred.ShuffleHandler</value> </property> </configuration>`
  - Format the HDFS namenode: `/usr/local/hadoop/bin/hdfs namenode -format`
  - Start the Hadoop daemons: `/usr/local/hadoop/sbin/start-dfs.sh` and `/usr/local/hadoop/sbin/start-yarn.sh`
  - Verify the Hadoop installation by browsing the web interfaces of the namenode and the resource manager: `http://localhost:9870` and `http://localhost:8088`
- To download



## Implement the following file management tasks in Hadoop:

- Hadoop is a framework that allows distributed processing of large data sets across clusters of computers using simple programming models.
- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications. It provides high-performance access to data across highly scalable Hadoop clusters.
- HDFS is designed to handle large files that are typically in the range of terabytes or petabytes. It divides files into uniform sized blocks of 128 MB or 64 MB (preferably 128 MB) and distributes them across the cluster nodes.
- HDFS has a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as the DataNodes (slaves). The NameNode manages the file system namespace and the metadata of the files and blocks. The DataNodes store the actual data blocks and serve read and write requests from the clients.
- HDFS provides fault tolerance and reliability by replicating each block across multiple DataNodes. The default replication factor is 3, which means each block is stored on three different DataNodes. The replication factor can be configured according to the needs of the application.
- HDFS supports various file operations such as creating, deleting, renaming, copying, moving, appending, and truncating files and directories. It also supports setting and changing permissions, ownership, and quotas of files and directories.
- HDFS can be accessed through a command-line interface (CLI), a web-based user interface (UI), or a Java API. The CLI is the most common way of interacting with HDFS. The CLI commands are similar to the Unix/Linux commands for local file systems.
- Some of the common HDFS commands are:

  - `hadoop fs -ls`: List the contents of a directory.
  - `hadoop fs -mkdir`: Create a directory.
  - `hadoop fs -put`: Copy a file from the local file system to HDFS.
  - `hadoop fs -get`: Copy a file from HDFS to the local file system.
  - `hadoop fs -cat`: Display the contents of a file.
  - `hadoop fs -rm`: Delete a file or a directory.
  - `hadoop fs -mv`: Move or rename a file or a directory.
  - `hadoop fs -cp`: Copy a file or a directory within HDFS.
  - `hadoop fs -appendToFile`: Append data to an existing file.
  - `hadoop fs -setrep`: Change the replication factor of a file or a directory.
  - `hadoop fs -chmod`: Change the permissions of a file or a directory.
  - `hadoop fs -chown`: Change the owner and group of a file or a directory.
  - `hadoop fs -du`: Display the disk usage of a file or a directory.
  - `hadoop fs -df`: Display the available space in HDFS.
  - `hadoop fs -help`: Display the help for a command.

- For more details and examples of HDFS commands, refer to the official documentation or the tutorials .



## Adding files and directories for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

- To add files and directories for the notes of the BIG DATA AND ANALYTICS LAB, one can use the following steps:
  - Create a directory named `BIG_DATA_AND_ANALYTICS_LAB` in the desired location on the computer. This directory will store all the notes and files related to the subject.
  - Inside the `BIG_DATA_AND_ANALYTICS_LAB` directory, create subdirectories for each topic or module of the subject. For example, one can create subdirectories named `Introduction`, `Hadoop`, `MapReduce`, `Spark`, `Hive`, `Pig`, etc.
  - Inside each subdirectory, create files for the notes of the corresponding topic or module. The files can be in any format, such as text, PDF, Word, etc. For example, one can create files named `Introduction.txt`, `Hadoop.pdf`, `MapReduce.docx`, etc.
  - To add content to the files, one can use any text editor or word processor of their choice. The content should be informative, concise, and relevant to the subject. One can also use diagrams, tables, charts, etc. to illustrate the concepts and examples.
  - To save the files, one can use the `Save` or `Save As` option in the text editor or word processor. One should choose a suitable name and location for the files. One can also use the `Copy` and `Paste` option to copy the files from other sources, such as websites, books, etc.
  - To organize the files and directories, one can use the `Rename`, `Move`, `Delete`, `Sort`, etc. options in the file manager or explorer of the computer. One should keep the files and directories in a logical and consistent order, such as alphabetical, numerical, chronological, etc.
  - To access the files and directories, one can use the `Open`, `Search`, `Browse`, etc. options in the file manager or explorer of the computer. One should also use the `Backup`, `Restore`, `Sync`, etc. options to keep the files and directories safe and updated.



## Retrieving files for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

- To retrieve files for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB, you need to follow these steps:
  - Access the online learning platform of your institution, such as Moodle, Blackboard, Canvas, etc.
  - Navigate to the course page of BIG DATA AND ANALYTICS LAB and look for the section that contains the notes or the lab manuals.
  - Download the files that are relevant to the topics or the experiments that you want to study or practice.
  - Alternatively, you can also use the search function of the online learning platform to find the files by entering keywords such as "BIG DATA AND ANALYTICS LAB", "notes", "lab manual", etc.
  - Save the files in a folder on your computer or a cloud storage service such as Google Drive, Dropbox, OneDrive, etc. for easy access and backup.
  - Open the files with a suitable application such as Microsoft Word, Adobe Acrobat Reader, etc. and read or print them as per your preference.



## Deleting files

- To delete files from HDFS, we can use the `hadoop fs -rm` command, which takes one or more paths as arguments and deletes them recursively.
- For example, to delete a file named `log.txt` from the `/user/sydney` directory, we can run:

```
hadoop fs -rm /user/sydney/log.txt
```

- To delete a directory and all its contents, we can use the `-r` option, which stands for recursive. For example, to delete the `/user/sydney/logs` directory, we can run:

```
hadoop fs -rm -r /user/sydney/logs
```

- To delete files or directories without confirmation, we can use the `-f` option, which stands for force. For example, to delete the `/user/sydney/temp` directory without asking for confirmation, we can run:

```
hadoop fs -rm -f -r /user/sydney/temp
```

- To delete files or directories and move them to the trash, we can use the `-skipTrash` option, which will skip the trash mechanism and delete the files or directories permanently. For example, to delete the `/user/sydney/data` directory and move it to the trash, we can run:

```
hadoop fs -rm -skipTrash /user/sydney/data
```

- To delete files or directories from the trash, we can use the `hadoop fs -expunge` command, which will empty the trash and free up space. For example, to delete all the files or directories from the trash, we can run:

```
hadoop fs -expunge
```

- To view the contents of the trash, we can use the `hadoop fs -ls` command with the `.Trash` directory as the argument. For example, to view the contents of the trash for the current user, we can run:

```
hadoop fs -ls .Trash
```

- To restore files or directories from the trash, we can use the `hadoop fs -mv` command with the `.Trash` directory as the source and the desired destination as the target. For example, to restore the `/user/sydney/data` directory from the trash, we can run:

```
hadoop fs -mv .Trash/Current/user/sydney/data /user/sydney/data
```

- Note: The trash mechanism is enabled by default and has a retention period of 6 hours. This means that the files or directories deleted from HDFS will be moved to the trash and will be deleted permanently after 6 hours. To disable the trash mechanism, we can set the `fs.trash.interval` property to 0 in the `core-site.xml` file. To change the retention period, we can set the `fs.trash.interval` property to a different value in minutes. For example, to set the retention period to 24 hours, we can set the `fs.trash.interval` property to 1440.



## Implement of Matrix Multiplication with Hadoop Map Reduce

- Matrix multiplication is a common operation in many applications that deal with large-scale data, such as machine learning, graph analysis, and linear algebra.
- Hadoop is a framework that allows for distributed processing of large data sets across clusters of computers using simple programming models.
- MapReduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- Matrix multiplication with Hadoop MapReduce involves the following steps:
  - Define the input and output matrices, A and B, and their dimensions, m, n, and p.
  - Split the input matrices into blocks of rows and columns, and store them as key-value pairs in HDFS (Hadoop Distributed File System).
  - Write a mapper function that emits intermediate key-value pairs for each block of A and B, where the key is the index of the output matrix element, and the value is the block of A or B and its position.
  - Write a reducer function that receives all the intermediate values for a given output matrix element, and performs the dot product of the corresponding blocks of A and B, and emits the final key-value pair for the output matrix element.
  - Run the MapReduce job on the Hadoop cluster, and collect the output matrix from HDFS.

- An example of matrix multiplication with Hadoop MapReduce in Python is given below:

```python
# Matrix_Mapper.py
# This file contains the implementation of mapper.
# It maps keys according to the the matrix.
# For Example,
# A = |1 2|
#     |3 4|
# B = |5 6|
#     |7 8|
# C = A*B
# C = |19 22|
#     |43 50|
# The mapper will map the keys as follows
# A[0][0] -> C[0][0], C[0][1]
# A[0][1] -> C[0][0], C[0][1]
# A[1][0] -> C[1][0], C[1][1]
# A[1][1] -> C[1][0], C[1][1]
# B[0][0] -> C[0][0], C[1][0]
# B[0][1] -> C[0][1], C[1][1]
# B[1][0] -> C[0][0], C[1][0]
# B[1][1] -> C[0][1], C[1][1]

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # get the matrix name, row, column, and value
    matrix = words[0]
    row = int(words[1])
    col = int(words[2])
    val = int(words[3])
    # emit key-value pairs for each matrix element
    if matrix == "A":
        # for matrix A, the key is the row and column of the output matrix element
        # the value is the matrix name, the column of A, and the value of A
        for k in range(2):
            print '%d,%d\t%s,%d,%d' % (row, k, matrix, col, val)
    else:
        # for matrix B, the key is the row and column of the output matrix element
        # the value is the matrix name, the row of B, and the value of B
        for i in range(2):
            print '%d,%d\t%s,%d,%d' % (i, col, matrix, row, val)
```

```python
# Matrix_Reducer.py
# This file contains the implementation of reducer.
# It receives the intermediate values for a given output matrix element,
# and performs the dot product of the corresponding blocks of A and B,
# and emits the final key-value pair for the output matrix element.

import sys

# initialize the current key and the partial sum
current_key = None
current_sum = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)
    # convert value to

```




## Write a Map Reduce program that mines weather data. Hint: Weather sensors collecting data every hour at many locations across the globe gather a large volume of log data, which is a good candidate for analysis with Map Reduce, since it is semi structured and record-oriented for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

- Map Reduce is a programming model that allows processing large-scale data sets in parallel on a cluster of machines.
- Weather data is a type of semi-structured data that consists of records with different attributes, such as date, time, location, temperature, humidity, wind speed, etc.
- To mine weather data using Map Reduce, we need to define two functions: a mapper function and a reducer function.
- The mapper function takes a record of weather data as input and emits a key-value pair as output. The key is usually a composite of some attributes that define a group or a category of interest, such as year, month, location, etc. The value is usually a numeric attribute that we want to aggregate or analyze, such as temperature, humidity, etc.
- The reducer function takes a key and a list of values as input and emits a key-value pair as output. The key is the same as the input key, and the value is the result of some aggregation or analysis function applied to the list of values, such as sum, average, maximum, minimum, etc.
- For example, if we want to find the average temperature for each month and location, we can write the following mapper and reducer functions in Python:

```python
# mapper function
def mapper(record):
  # split the record by comma
  fields = record.split(",")
  # extract the date, time, location and temperature fields
  date = fields[0]
  time = fields[1]
  location = fields[2]
  temperature = float(fields[3])
  # parse the date to get the year and month
  year, month, day = date.split("-")
  # emit a key-value pair with year, month and location as key and temperature as value
  key = (year, month, location)
  value = temperature
  print(key, value)

# reducer function
def reducer(key, values):
  # calculate the average temperature from the list of values
  sum = 0
  count = 0
  for value in values:
    sum += value
    count += 1
  average = sum / count
  # emit a key-value pair with the same key and the average temperature as value
  print(key, average)
```

- To run the Map Reduce program, we need to use a framework such as Hadoop or Spark that can distribute the data and the computation across a cluster of machines.
- The framework will take care of splitting the input data into chunks, assigning the chunks to different mapper tasks, shuffling and sorting the intermediate key-value pairs, assigning the pairs to different reducer tasks, and collecting the final output.



## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm.

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed environments.
- Map Reduce consists of two phases: map and reduce.
- The map phase takes an input key-value pair and produces a set of intermediate key-value pairs.
- The reduce phase takes all the intermediate values associated with the same key and combines them to produce a final output value.
- A Word Count Map Reduce program is a simple example of how to use Map Reduce to count the frequency of words in a text file.
- The steps to run a basic Word Count Map Reduce program are:

  1. Create a text file with some words and save it in a local directory.
  2. Copy the text file to the Hadoop Distributed File System (HDFS) using the command: `hadoop fs -put <local_file> <hdfs_file>`
  3. Write a Java class that implements the Mapper interface and overrides the map method. The map method should take a line of text as the input key and split it into words. For each word, it should emit a key-value pair with the word as the key and 1 as the value.
  4. Write a Java class that implements the Reducer interface and overrides the reduce method. The reduce method should take a word as the input key and a list of values as the input value. It should sum up all the values and emit a key-value pair with the word as the key and the sum as the value.
  5. Write a Java class that defines the main method and sets up the configuration and job parameters for the Map Reduce program. The main method should specify the input and output paths, the mapper and reducer classes, the output key and value types, and the number of reducers.
  6. Compile the Java classes and create a jar file using the command: `javac -classpath <hadoop_classpath> *.java` and `jar cf wc.jar *.class`
  7. Run the Map Reduce program using the command: `hadoop jar wc.jar <main_class> <input_path> <output_path>`
  8. Check the output file in the HDFS using the command: `hadoop fs -cat <output_path>/part-r-00000`
  9. The output file should contain the words and their frequencies in the text file.



## Implementation of K-means clustering using Map Reduce

- K-means clustering is a partitioning-based clustering algorithm that assigns data points to k clusters based on their distance to the cluster centers.
- Map Reduce is a parallel and distributed computing framework that processes large-scale data sets by dividing them into smaller chunks and applying a map function and a reduce function on each chunk.
- The Map Reduce solution of K-means clustering is an iteration scheme, in which each iteration implements a Map Reduce job.
- The steps of the Map Reduce solution of K-means clustering are as follows:

  - Step 1: Initialize k cluster centers randomly or using some heuristic method, such as k-means++.
  - Step 2: Assign each data point to the closest cluster center by computing the Euclidean distance. This is done by the map function, which emits the cluster center and the data point as a key-value pair.
  - Step 3: Compute the new cluster centers by averaging the data points assigned to each cluster. This is done by the reduce function, which receives the cluster center and the list of data points as a key-value pair, and emits the cluster center and the new cluster center as a key-value pair.
  - Step 4: Check the convergence condition, which is usually based on the change of cluster centers or the number of iterations. If the condition is met, stop the algorithm. Otherwise, repeat from step 2 with the new cluster centers.

- Some challenges and optimizations of the Map Reduce solution of K-means clustering are:

  - The random selection of initial cluster centers may lead to poor clustering results or slow convergence. To overcome this, some methods such as k-means++ or k-means** can be used to select the initial cluster centers more wisely.
  - The communication overhead among Map Reduce nodes may be expensive, especially when the data set is large and the number of clusters is high. To reduce this, some methods such as k-means+* can be used to compress the data points before sending them to the reducers.
  - The data skewing in data partitions may cause some reducers to be overloaded and some to be idle, which affects the load balancing and performance of the algorithm. To avoid this, some methods such as hashing or sampling can be used to partition the data more evenly.
  - The dependence of iteration may limit the scalability and efficiency of the algorithm, as each iteration has to wait for the previous one to finish. To eliminate this, some methods such as asynchronous updates or online learning can be used to update the cluster centers without waiting for the synchronization.



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

   HBase web UI

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



## Patrice importing and exporting data from various data bases

- Patrice is a tool that allows users to import and export data from various data bases, such as HBase, MySQL, MongoDB, and SQL Server.
- Patrice uses Thrift, a software framework for scalable cross-language services development, to communicate with different data bases and perform data operations.
- Patrice can be installed on Linux, Windows, or Mac OS, and requires Java and Thrift to run.
- Patrice provides a graphical user interface (GUI) and a command-line interface (CLI) for users to interact with data bases and perform data import and export tasks.
- Patrice supports various data formats, such as CSV, JSON, XML, and Parquet, for data import and export.
- Patrice can also perform data transformations, such as filtering, mapping, joining, and aggregating, during data import and export.
- Patrice can handle large-scale data sets and parallelize data operations for better performance and efficiency.
- Patrice can also integrate with other tools, such as Power BI, Excel, and Azure Synapse Link, for data analysis and visualization.



## Write Pig Latin scripts to sort, group, join, project, and filter your data.

Pig Latin is a high-level scripting language that allows you to manipulate data in Apache Pig. Pig Latin scripts consist of a series of statements that apply various operators to relations. Relations are named collections of tuples, which are ordered sets of fields. Fields can be of any type, such as int, chararray, float, etc.

Here are some examples of how to write Pig Latin scripts to sort, group, join, project, and filter your data.

### Sort

The SORT operator sorts a relation by one or more fields in ascending or descending order. The syntax is:

`sorted_relation = SORT relation BY field1 [ASC|DESC], field2 [ASC|DESC], ...;`

For example, to sort the student data by name in ascending order and then by age in descending order, you can write:

`Student_data = LOAD 'student_data.txt' USING PigStorage(',') AS (id:int, firstname:chararray, lastname:chararray, phone:chararray, city:chararray);`

`Sorted_data = SORT Student_data BY firstname ASC, age DESC;`

### Group

The GROUP operator groups a relation by one or more fields, creating a new relation with two fields: group and bag. The group field contains the values of the fields that were grouped by, and the bag field contains all the tuples that have the same group values. The syntax is:

`grouped_relation = GROUP relation BY field1, field2, ...;`

For example, to group the student data by city, you can write:

`Grouped_data = GROUP Student_data BY city;`

### Join

The JOIN operator joins two or more relations by a common field or a set of fields. The syntax is:

`joined_relation = JOIN relation1 BY field1, relation2 BY field2, ...;`

For example, to join the student data with another relation that contains the scores of each student, you can write:

`Score_data = LOAD 'score_data.txt' USING PigStorage(',') AS (id:int, score:int);`

`Joined_data = JOIN Student_data BY id, Score_data BY id;`

### Project

The PROJECT operator selects a subset of fields from a relation. The syntax is:

`projected_relation = FOREACH relation GENERATE field1, field2, ...;`

For example, to project only the name and score of each student, you can write:

`Projected_data = FOREACH Joined_data GENERATE firstname, lastname, score;`

### Filter

The FILTER operator filters a relation by applying a condition to each tuple. The syntax is:

`filtered_relation = FILTER relation BY condition;`

For example, to filter the student data by selecting only those who have a score above 80, you can write:

`Filtered_data = FILTER Joined_data BY score > 80;`



## Run the Pig Latin Scripts to find Word Count

- Pig Latin is a high-level scripting language that is used to process and analyze large datasets using Apache Pig, a platform for big data analytics.
- Pig Latin scripts are composed of a series of statements that describe how to load, transform, and store data.
- To run a Pig Latin script, you need to have Apache Pig installed and configured on your system, and a text file that contains the script.
- One of the common tasks that can be performed using Pig Latin is to find the word count of a text file, which is the number of times each word appears in the file.
- To find the word count using Pig Latin, you can follow these steps:

  - Create a text file that contains some text, such as a paragraph from a book or an article. Save the file as input.txt in your working directory.
  - Create another text file that contains the following Pig Latin script and save it as wordcount.pig in your working directory:

    ```
    -- Load the input file using PigStorage loader
    input = LOAD 'input.txt' USING PigStorage() AS (line:chararray);

    -- Split each line into words using TOKENIZE function
    words = FOREACH input GENERATE FLATTEN(TOKENIZE(line)) AS word;

    -- Group the words by their value and count the occurrences using COUNT function
    grouped = GROUP words BY word;
    wordcount = FOREACH grouped GENERATE group, COUNT(words);

    -- Store the output in a file using PigStorage storer
    STORE wordcount INTO 'output.txt' USING PigStorage();
    ```

  - Open a terminal and navigate to your working directory. Run the following command to execute the Pig Latin script:

    ```
    pig wordcount.pig
    ```

  - The script will load the input file, split each line into words, group the words by their value, count the occurrences, and store the output in a file named output.txt in your working directory.
  - The output file will contain one line for each word, followed by a tab and the number of times the word appears in the input file. For example, if the input file contains the following text:

    ```
    The quick brown fox jumps over the lazy dog.
    ```

    The output file will contain the following lines:

    ```
    The	1
    brown	1
    dog.	1
    fox	1
    jumps	1
    lazy	1
    over	1
    quick	1
    the	1
    ```

- This is how you can run the Pig Latin scripts to find the word count of a text file using Apache Pig.



## Run the Pig Latin Scripts to find a max temp for each and every year.

- Pig Latin is a high-level scripting language that allows users to write complex data transformations using a simple syntax. Pig Latin scripts can run on Apache Hadoop, a framework for distributed processing of large data sets.
- To find the maximum temperature for each year from a data set of weather records, we can use the following steps:

  1. Load the data from a file into a relation using the `LOAD` operator. Specify the schema of the data using the `AS` clause. For example:

     ```pig
     weather = LOAD 'weather.txt' USING PigStorage(',') AS (year:int, month:int, day:int, temp:float);
     ```

  2. Filter out the records that have missing or invalid temperature values using the `FILTER` operator. For example:

     ```pig
     valid = FILTER weather BY temp > -99.0;
     ```

  3. Group the records by year using the `GROUP` operator. This will create a nested relation where each group contains all the records for a given year. For example:

     ```pig
     by_year = GROUP valid BY year;
     ```

  4. Find the maximum temperature for each group using the `MAX` function and the `FOREACH` operator. The `FOREACH` operator allows us to apply expressions or functions to each group or record. For example:

     ```pig
     max_temp = FOREACH by_year GENERATE group AS year, MAX(valid.temp) AS max_temp;
     ```

  5. Store the result into a file using the `STORE` operator. Specify the output format and the delimiter using the `USING` clause. For example:

     ```pig
     STORE max_temp INTO 'output' USING PigStorage(',');
     ```

- To run the Pig Latin script, we can use the `pig` command in the terminal. For example:

  ```bash
  pig -x local max_temp.pig
  ```

  The `-x` option specifies the execution mode. In this case, we use `local` mode, which means the script will run on a single machine without using Hadoop. Alternatively, we can use `mapreduce` mode, which means the script will run on a Hadoop cluster using MapReduce jobs.

- The output file will contain the maximum temperature for each year in the data set, separated by commas. For example:

  ```text
  1901,33.9
  1902,35.6
  1903,33.3
  ...
  ```

