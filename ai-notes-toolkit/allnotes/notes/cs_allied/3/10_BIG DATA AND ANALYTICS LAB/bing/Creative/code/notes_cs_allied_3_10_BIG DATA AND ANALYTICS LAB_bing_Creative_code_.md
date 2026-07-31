

# BIG DATA AND ANALYTICS LAB

- Big data and analytics lab is a course that aims to provide students with practical skills and knowledge of big data technologies and applications.
- The course covers topics such as big data ecosystem, data mining, data warehousing, data visualization, data science, and data analytics using various tools and platforms such as Hadoop, Spark, R, Python, and Excel.
- The course also involves projects, internships, and paper presentations that allow students to apply their learning to real-world problems and scenarios.
- The course is divided into four semesters, each with different syllabus and objectives. The following is a brief overview of the syllabus for each semester:

  - Semester 1: Introduction to Computer Hardware, Statistics for Data Science, Technical Writing & Paper Presentation, Big Data and Internet of Things, System Software Concepts, Data Warehousing
  - Semester 2: Data Mining, Data Visualization, R Programming, Python Programming, Excel for Business Analytics, Machine Learning
  - Semester 3: Big Data Analytics, Data Science, Spark Core Fundamentals and Architecture, Structured and Unstructured Data, Main Big Data Technologies and Hadoop, Harvest Financial Information Using Big Data   
  - Semester 4: Project Work, Internship, Dissertation 

- The course is designed to equip students with the skills and knowledge to analyze, process, and manage large and complex data sets using various tools and techniques.
- The course also aims to develop students' critical thinking, problem-solving, communication, and presentation skills.



## Downloading and installing Hadoop; Understanding different Hadoop modes. Startup scripts, Configuration files.

- Hadoop is an open-source framework for distributed storage and processing of large-scale data using clusters of commodity hardware.
- Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and Hadoop MapReduce.
- Hadoop can run in different modes: standalone, pseudo-distributed, and fully distributed.
- Standalone mode is the default mode of Hadoop, where it runs on a single machine without using HDFS or MapReduce. It is useful for testing and debugging purposes.
- Pseudo-distributed mode is where Hadoop runs on a single machine, but simulates a cluster by using HDFS and MapReduce. It is useful for development and learning purposes.
- Fully distributed mode is where Hadoop runs on a cluster of multiple machines, each running a Hadoop daemon. It is the mode used for production and performance purposes.
- To download and install Hadoop on Ubuntu, follow these steps:
  - Visit the official Apache Hadoop project page, and select the version of Hadoop you want to implement. The steps outlined in this tutorial use the Binary download for Hadoop Version 3.2.1.
  - Use the provided mirror link and download the Hadoop package with the wget command: `wget https://downloads.apache.org/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz`
  - Once the download is complete, extract the files to initiate the Hadoop installation: `tar xvf hadoop-3.2.1.tar.gz`
  - Move the extracted files to the /usr/local directory: `sudo mv hadoop-3.2.1 /usr/local/hadoop`
  - Set the JAVA_HOME environment variable in the /etc/environment file: `sudo nano /etc/environment` and add the following line: `JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"`
  - Reload the environment variables: `source /etc/environment`
  - Set the HADOOP_HOME and HADOOP_CONF_DIR environment variables in the ~/.bashrc file: `nano ~/.bashrc` and add the following lines: `export HADOOP_HOME="/usr/local/hadoop"` and `export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop`
  - Reload the bashrc file: `source ~/.bashrc`
  - Edit the core-site.xml file in the Hadoop configuration directory: `nano $HADOOP_CONF_DIR/core-site.xml` and add the following lines between the `<configuration>` tags: `<property>` `<name>fs.defaultFS</name>` `<value>hdfs://localhost:9000</value>` `</property>`
  - Edit the hdfs-site.xml file in the Hadoop configuration directory: `nano $HADOOP_CONF_DIR/hdfs-site.xml` and add the following lines between the `<configuration>` tags: `<property>` `<name>dfs.replication</name>` `<value>1</value>` `</property>` `<property>` `<name>dfs.namenode.name.dir</name>` `<value>file:///home/hadoop/hadoopdata/hdfs/namenode</value>` `</property>` `<property>` `<name>dfs.datanode.data.dir</name>` `<value>file:///home/hadoop/hadoopdata/hdfs/datanode</value>` `</property>`
  - Edit the mapred-site.xml file in the Hadoop configuration directory: `nano $HADOOP_CONF_DIR/mapred-site.xml` and add the following lines between the `<configuration>` tags: `<property>` `<name>mapreduce.framework.name</name>` `<value>yarn</value>` `</property>`
  - Edit the yarn-site.xml file in the Hadoop configuration directory: `nano $HADOOP_CONF_DIR/yarn-site.xml` and add the following lines between the `<configuration>` tags: `<property>` `<name>yarn.nodemanager.aux-services</name>` `<value>mapreduce_shuffle</value>` `</property>` `<property>` `<name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>` `<value>org.apache.hadoop.mapred.ShuffleHandler</value>` `</property>`
  - Create the HDFS directories specified in the configuration files: `mkdir -p ~/hadoopdata/hdfs/namenode` and `mkdir -p ~/hadoopdata/hdfs/datanode`
  - Format the HDFS namenode: `hdfs namenode -format`
  - Start the H



## Implement the following file management tasks in Hadoop:

Hadoop is a framework that allows distributed processing of large data sets across clusters of computers using simple programming models. Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce. HDFS is a distributed file system that provides high-performance access to data across scalable Hadoop clusters. MapReduce is a programming model that enables parallel processing of large data sets on HDFS.

Some of the file management tasks that can be performed on HDFS are:

- Creating directories and files: HDFS provides commands to create directories and files on the file system. For example, `hadoop fs -mkdir /user/hadoop/dir1` creates a directory named dir1 under /user/hadoop. Similarly, `hadoop fs -touchz /user/hadoop/dir1/file1` creates an empty file named file1 under /user/hadoop/dir1.
- Listing directories and files: HDFS provides commands to list the contents of a directory or a file on the file system. For example, `hadoop fs -ls /user/hadoop/dir1` lists the files and subdirectories under /user/hadoop/dir1. Similarly, `hadoop fs -cat /user/hadoop/dir1/file1` displays the contents of file1 on the standard output.
- Copying files: HDFS provides commands to copy files from one location to another on the file system. For example, `hadoop fs -cp /user/hadoop/dir1/file1 /user/hadoop/dir2/file2` copies file1 from /user/hadoop/dir1 to /user/hadoop/dir2 as file2. The source and destination can also be local files or URIs.
- Moving files: HDFS provides commands to move files from one location to another on the file system. For example, `hadoop fs -mv /user/hadoop/dir1/file1 /user/hadoop/dir2/file2` moves file1 from /user/hadoop/dir1 to /user/hadoop/dir2 as file2. The source and destination can also be local files or URIs.
- Deleting files: HDFS provides commands to delete files or directories on the file system. For example, `hadoop fs -rm /user/hadoop/dir1/file1` deletes file1 from /user/hadoop/dir1. Similarly, `hadoop fs -rmdir /user/hadoop/dir1` deletes the directory dir1 and its contents from /user/hadoop.
- Changing permissions and ownership: HDFS provides commands to change the permissions and ownership of files or directories on the file system. For example, `hadoop fs -chmod 755 /user/hadoop/dir1` changes the permissions of dir1 to 755 (read, write, and execute for owner, read and execute for group and others). Similarly, `hadoop fs -chown hadoop:hadoop /user/hadoop/dir1` changes the owner and group of dir1 to hadoop.
- Checking the status and usage of the file system: HDFS provides commands to check the status and usage of the file system. For example, `hadoop fs -stat /user/hadoop/dir1` displays the status of dir1, such as modification time, access time, and block size. Similarly, `hadoop fs -du /user/hadoop/dir1` displays the disk usage of dir1 and its subdirectories.



Hello, I am Sydney, your AI assistant. I can help you with your notes for the Big Data and Analytics Lab subject. Here is some content on the topic of adding files and directories:

## Adding files and directories

- To add files and directories to Hadoop Distributed File System (HDFS), you need to use the `hdfs dfs -put` command.
- The syntax of the command is `hdfs dfs -put <local_source> <hdfs_destination>`.
- The `<local_source>` can be a file or a directory on your local file system. The `<hdfs_destination>` can be a file or a directory on HDFS. If the destination does not exist, it will be created.
- You can also use the `-f` option to overwrite the existing destination file or directory.
- You can also use the `-p` option to preserve the permissions, ownership, and modification time of the source file or directory.
- You can also use the `-l` option to create a symbolic link to the source file or directory on HDFS.
- You can also use the `-r` option to recursively copy all the files and subdirectories from the source directory to the destination directory on HDFS.
- You can also use the `-v` option to display the verbose output of the command.
- For example, to copy a file named `data.txt` from your local file system to a directory named `/user/student` on HDFS, you can use the command `hdfs dfs -put data.txt /user/student`.
- To copy a directory named `input` from your local file system to a directory named `/user/student` on HDFS, you can use the command `hdfs dfs -put input /user/student`.
- To overwrite an existing file or directory named `output` on HDFS with a file or directory named `output` from your local file system, you can use the command `hdfs dfs -put -f output /user/student`.
- To create a symbolic link named `link` on HDFS that points to a file or directory named `source` on your local file system, you can use the command `hdfs dfs -put -l source /user/student/link`.
- To recursively copy all the files and subdirectories from a directory named `input` on your local file system to a directory named `/user/student` on HDFS, you can use the command `hdfs dfs -put -r input /user/student`.
- To display the verbose output of the command `hdfs dfs -put input /user/student`, you can use the command `hdfs dfs -put -v input /user/student`.



Hello, I am Sydney, your AI assistant. I can help you with retrieving files for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB. Here are the steps to follow:

- Locate the folder where you have stored the files for the subject of BIG DATA AND ANALYTICS LAB on your computer or cloud storage.
- Open the folder and look for the files that have the name or extension of .pdf, .docx, .pptx, or .txt. These are the common formats for notes files.
- Select the files that you want to retrieve and copy them to a new folder or a USB drive. You can also email them to yourself or upload them to a cloud service like Google Drive or Dropbox.
- If you want to print the files, you can open them with a compatible software like Adobe Reader, Microsoft Word, PowerPoint, or Notepad and use the print option.
- If you want to view the files on your phone or tablet, you can transfer them using a USB cable, Bluetooth, or Wi-Fi. You can also use a cloud service or an email to access them from your device.
- If you want to edit the files, you can use a software like Microsoft Word, PowerPoint, or Notepad and make the changes you want. You can also use an online tool like Google Docs or Slides to edit the files.
- If you want to share the files with others, you can use an email, a cloud service, or a social media platform like WhatsApp, Telegram, or Facebook Messenger. You can also use a file-sharing service like WeTransfer or Dropbox to send large files.



## Deleting files

- To delete files from HDFS, we can use the `hadoop fs -rm` command with the path of the file or directory to be deleted.
- For example, `hadoop fs -rm /user/hadoop/file.txt` will delete the file `file.txt` from the `/user/hadoop` directory in HDFS.
- To delete a directory and all its contents recursively, we can use the `-r` option with the `hadoop fs -rm` command.
- For example, `hadoop fs -rm -r /user/hadoop/dir` will delete the directory `dir` and all its subdirectories and files from the `/user/hadoop` directory in HDFS.
- To delete files or directories without moving them to the trash, we can use the `-skipTrash` option with the `hadoop fs -rm` command.
- For example, `hadoop fs -rm -skipTrash /user/hadoop/file.txt` will delete the file `file.txt` from the `/user/hadoop` directory in HDFS without moving it to the trash.
- To delete files or directories from the trash, we can use the `hadoop fs -expunge` command, which will permanently delete all the files and directories in the trash that have exceeded the retention period.
- For example, `hadoop fs -expunge` will delete all the files and directories in the trash that have been there for more than the configured retention period (default is 30 days).
- To view the contents of the trash, we can use the `hadoop fs -ls` command with the `.Trash` directory in the user's home directory in HDFS.
- For example, `hadoop fs -ls /user/hadoop/.Trash` will list all the files and directories in the trash for the user `hadoop`.



## Implement of Matrix Multiplication with Hadoop Map Reduce

Matrix multiplication is a common operation in many applications that deal with large-scale data, such as machine learning, graph analysis, and linear algebra. However, matrix multiplication is also computationally intensive and requires a lot of memory and communication. Therefore, it is challenging to perform matrix multiplication efficiently on distributed systems, such as Hadoop.

Hadoop is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. Hadoop consists of two main components: the Hadoop Distributed File System (HDFS) and the MapReduce programming model. HDFS is a distributed file system that provides high-throughput access to data stored on the cluster. MapReduce is a programming model that allows users to express their computation as a series of map and reduce functions that operate on key-value pairs.

MapReduce can be used to implement matrix multiplication in a parallel and scalable way. The basic idea is to divide the input matrices into smaller blocks and assign each block to a mapper. The mapper then emits key-value pairs that indicate the position and value of each element in the output matrix. The key consists of the row and column indices of the output element, and the value consists of the input element and its source matrix. The reducer then receives all the key-value pairs with the same key and performs the multiplication and summation of the corresponding values to produce the output element.

The following steps illustrate how to implement matrix multiplication with Hadoop MapReduce:

1. Assume that the input matrices are A and B, and the output matrix is C. Let m, n, and p be the dimensions of A, B, and C, respectively. That is, A is an m x n matrix, B is an n x p matrix, and C is an m x p matrix.
2. Divide A and B into smaller blocks of size b x b, where b is a parameter that determines the granularity of the parallelism. For example, if b = 2, then A and B are divided into four blocks each, as shown below:

Matrix blocks

3. Assign each block of A and B to a mapper. The mapper reads the block from HDFS and emits key-value pairs for each element in the block. The key consists of the row and column indices of the output element that the input element contributes to, and the value consists of the input element and its source matrix. For example, the mapper that processes the block A[0][0] emits the following key-value pairs:

| Key | Value |
| --- | ----- |
| (0, 0) | (A[0][0], A) |
| (0, 1) | (A[0][0], A) |
| (1, 0) | (A[0][1], A) |
| (1, 1) | (A[0][1], A) |

Similarly, the mapper that processes the block B[0][0] emits the following key-value pairs:

| Key | Value |
| --- | ----- |
| (0, 0) | (B[0][0], B) |
| (0, 1) | (B[0][1], B) |
| (1, 0) | (B[1][0], B) |
| (1, 1) | (B[1][1], B) |

4. The key-value pairs emitted by the mappers are shuffled and sorted by the Hadoop framework and sent to the reducers. The reducer receives all the key-value pairs with the same key and performs the multiplication and summation of the corresponding values to produce the output element. For example, the reducer that receives the key-value pairs with the key (0, 0) performs the following computation:

C[0][0] = (A[0][0] * B[0][0]) + (A[0][1] * B[1][0]) + ... + (A[0][n-1] * B[n-1][0])

The reducer then emits the key-value pair (0, 0) and C[0][0] as the output. Similarly, the reducer that receives the key-value pairs with the key (0, 1) performs the following computation:

C[0][1] = (A[0][0] * B[0][1]) + (A[0][1] * B[1][1]) + ... + (A[0][n-1



Hello, I am Sydney, your AI assistant. I can help you with writing a Map Reduce program that mines weather data. Here is an outline of the steps involved:

- Define the input and output format of the data. For example, the input could be a CSV file with columns such as date, time, location, temperature, humidity, wind speed, etc. The output could be another CSV file with columns such as location, average temperature, maximum temperature, minimum temperature, etc.
- Define the mapper function that takes a line of input and emits key-value pairs. For example, the mapper could emit the location as the key and the temperature as the value for each line of input.
- Define the reducer function that takes a key and a list of values and emits a summary of the values. For example, the reducer could compute the average, maximum, and minimum temperature for each location and emit them as the output.
- Write the driver code that sets up the Map Reduce job and runs it on the input data. For example, the driver code could use the Hadoop Map Reduce API to specify the input and output paths, the mapper and reducer classes, the number of reducers, etc.

Here is a possible code snippet for the Map Reduce program in Java:

```java
// Import the necessary libraries
import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// Define the mapper class that extends the Mapper interface
public class WeatherMapper extends Mapper<Object, Text, Text, DoubleWritable> {

  // Define the map method that takes a line of input and emits key-value pairs
  public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
    // Split the line by comma and store the fields in an array
    String[] fields = value.toString().split(",");
    // Extract the location and temperature from the array
    String location = fields[2];
    double temperature = Double.parseDouble(fields[3]);
    // Emit the location as the key and the temperature as the value
    context.write(new Text(location), new DoubleWritable(temperature));
  }
}

// Define the reducer class that extends the Reducer interface
public class WeatherReducer extends Reducer<Text, DoubleWritable, Text, Text> {

  // Define the reduce method that takes a key and a list of values and emits a summary of the values
  public void reduce(Text key, Iterable<DoubleWritable> values, Context context) throws IOException, InterruptedException {
    // Initialize the variables to store the average, maximum, and minimum temperature
    double sum = 0.0;
    double count = 0.0;
    double max = Double.MIN_VALUE;
    double min = Double.MAX_VALUE;
    // Loop through the values and update the variables
    for (DoubleWritable value : values) {
      double temp = value.get();
      sum += temp;
      count += 1.0;
      if (temp > max) {
        max = temp;
      }
      if (temp < min) {
        min = temp;
      }
    }
    // Compute the average temperature
    double avg = sum / count;
    // Format the output as a comma-separated string
    String output = String.format("%.2f,%.2f,%.2f", avg, max, min);
    // Emit the key and the output as the final result
    context.write(key, new Text(output));
  }
}

// Define the driver class that sets up and runs the Map Reduce job
public class WeatherDriver {

  // Define the main method that takes the input and output paths as arguments
  public static void main(String[] args) throws Exception {
    // Create a configuration object
    Configuration conf = new Configuration();
    // Create a job object and set the name
    Job job = Job.getInstance(conf, "weather analysis");
    // Set the jar file that contains the driver, mapper, and reducer classes
    job.setJarByClass(WeatherDriver.class);
    // Set the mapper class
    job.setMapperClass(WeatherMapper.class);
    // Set the reducer class
    job.setReducerClass(WeatherReducer.class);
    // Set the output key class
    job.setOutputKeyClass(Text.class);
    // Set the output value class
    job.setOutputValueClass(Text.class);
    // Set the number of reducers
    job.setNumReduceTasks(1);
    // Set the input and output paths from the arguments
    FileInput

```




## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm.

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed environments.
- Map Reduce consists of two phases: map and reduce.
- The map phase takes an input key-value pair and produces a set of intermediate key-value pairs.
- The reduce phase takes the intermediate key-value pairs with the same key and combines them to produce an output key-value pair.
- A Word Count Map Reduce program is a simple example of how to use Map Reduce to count the frequency of words in a text file.
- The steps to run a basic Word Count Map Reduce program are:

  1. Create a text file with some text and save it in a local directory.
  2. Copy the text file to the Hadoop Distributed File System (HDFS) using the command: `hadoop fs -put <local_file> <hdfs_file>`
  3. Write a Java class that implements the Mapper interface and overrides the map method. The map method should take a line of text as the input key-value pair and split it into words. For each word, it should emit a key-value pair with the word as the key and 1 as the value.
  4. Write a Java class that implements the Reducer interface and overrides the reduce method. The reduce method should take a word and a list of values as the input key-value pair and sum up the values. It should emit a key-value pair with the word as the key and the sum as the value.
  5. Write a Java class that defines the main method and sets up the configuration and job parameters for the Map Reduce program. The main method should specify the input and output paths, the mapper and reducer classes, the output key and value types, and the number of reducers.
  6. Compile the Java classes and create a jar file using the command: `javac -classpath <hadoop_classpath> *.java` and `jar cf wc.jar *.class`
  7. Run the Map Reduce program using the command: `hadoop jar wc.jar <main_class> <input_path> <output_path>`
  8. Check the output file in the HDFS using the command: `hadoop fs -cat <output_path>/part-r-00000`
  9. The output file should contain the words and their frequencies in the text file.



## Implementation of K-means clustering using Map Reduce

K-means clustering is a partitioning-based clustering algorithm that aims to group data points into k clusters based on their similarity. The algorithm works by randomly selecting k initial cluster centers, assigning each data point to the nearest cluster center, and updating the cluster centers by taking the mean of the data points in each cluster. The algorithm repeats these steps until the cluster centers converge or a maximum number of iterations is reached.

Map Reduce is a programming model for distributed computing that allows parallel processing of large-scale data sets. The model consists of two phases: map and reduce. In the map phase, the input data is split into smaller chunks and processed by multiple map tasks that produce intermediate key-value pairs. In the reduce phase, the intermediate key-value pairs are shuffled and sorted by key and processed by multiple reduce tasks that produce the final output.

The implementation of K-means clustering using Map Reduce is an iterative scheme, in which each iteration performs a Map Reduce job. The steps of the implementation are as follows:

1. Randomly select k initial cluster centers and store them in a file or a distributed cache.
2. In the map phase, each map task reads a chunk of the input data and assigns each data point to the nearest cluster center based on the Euclidean distance. The map task emits the cluster center and the data point as a key-value pair.
3. In the reduce phase, each reduce task receives the key-value pairs for a cluster center and computes the new cluster center by taking the mean of the data points. The reduce task emits the new cluster center and the number of data points in the cluster as a key-value pair.
4. Check the convergence condition by comparing the new cluster centers with the old ones. If the cluster centers have not changed significantly or a maximum number of iterations is reached, stop the algorithm. Otherwise, update the cluster centers and repeat steps 2 to 4.

The advantages of using Map Reduce for K-means clustering are:

- It can handle large-scale data sets that do not fit in memory.
- It can exploit the parallelism and scalability of distributed systems.
- It can tolerate failures and stragglers by using replication and backup tasks.

The challenges of using Map Reduce for K-means clustering are:

- It requires multiple iterations and data shuffling, which can incur high network and disk I/O costs.
- It depends on the random selection of initial cluster centers, which can affect the quality and speed of the clustering.
- It may suffer from data skewing and load imbalance, which can reduce the performance and efficiency of the algorithm.

Some possible solutions to overcome these challenges are:

- Using advanced initialization methods, such as k-means++ or k-means**, which can improve the quality and speed of the clustering by choosing better initial cluster centers.
- Using optimized algorithms, such as k-means+* or optimized big data K-means clustering, which can reduce the number of iterations and the computation cost of the algorithm by eliminating the dependence of iteration or using a dynamic threshold.
- Using data partitioning and load balancing techniques, such as canopy clustering or sampling, which can reduce the data skewing and load imbalance by grouping similar data points or selecting representative data points.



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




## Installation of HBase, Installing thrift along with Practice examples for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

HBase is a distributed, scalable, and column-oriented database that runs on top of the Hadoop Distributed File System (HDFS). It provides random, real-time read/write access to large datasets. HBase is modeled after Google's Bigtable, a distributed storage system for structured data.

To install HBase, you need to have Java and Hadoop installed on your Linux machine. HBase can be installed in three modes: standalone, pseudo-distributed, and fully distributed. In this note, we will focus on the standalone mode, which is the simplest and easiest way to get started with HBase.

### Installing HBase in Standalone Mode

- Download the latest stable version of HBase from http://www.interior-dsgn.com/apache/hbase/stable/ and unzip it with the following commands:

```bash
$ wget http://www.interior-dsgn.com/apache/hbase/stable/hbase-2.4.8-bin.tar.gz
$ tar xzf hbase-2.4.8-bin.tar.gz
$ cd hbase-2.4.8
```

- Edit the `conf/hbase-env.sh` file and set the `JAVA_HOME` environment variable to point to your Java installation directory :

```bash
$ vi conf/hbase-env.sh
# Uncomment the following line and set the correct path
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

- Edit the `conf/hbase-site.xml` file and add the following properties to configure HBase to use the local file system instead of HDFS :

```xml
<configuration>
  <property>
    <name>hbase.rootdir</name>
    <value>file:///home/hadoop/hbase</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.dataDir</name>
    <value>/home/hadoop/zookeeper</value>
  </property>
</configuration>
```

- Start HBase by running the `bin/start-hbase.sh` script :

```bash
$ bin/start-hbase.sh
```

- Verify that HBase is running by using the `jps` command, which should show the `HMaster` and `HRegionServer` processes :

```bash
$ jps
1234 HMaster
5678 HRegionServer
9012 Jps
```

- Connect to your running instance of HBase using the `hbase shell` command, located in the `bin/` directory of your HBase install:

```bash
$ bin/hbase shell
HBase Shell
Use "help" to get list of supported commands.
Use "exit" to quit this interactive shell.
For Reference, please visit: http://hbase.apache.org/2.0/book.html#shell
Version 2.4.8, rUnknown, Mon Oct 18 18:22:01 UTC 2021
Took 0.0051 seconds
hbase(main):001:0>
```

### Installing Thrift

Thrift is a software framework that allows cross-language service development. It supports several languages, including Java, Python, Ruby, C++, and PHP. Thrift can be used to access HBase from languages other than Java, using a Thrift server that acts as a proxy between the client and the HBase cluster.

To install Thrift, you need to have some prerequisites installed, such as automake, libtool, bison, flex, and libboost:

```bash
$ sudo apt-get install automake libtool flex bison pkg-config g++ libssl-dev libboost-all-dev
```

Then, you can download the latest stable version of Thrift from https://thrift.apache.org/download and compile it from source:

```bash
$ wget https://downloads.apache.org/thrift/0.15.0/thrift-0.15.0.tar.gz
$ tar xzf thrift-0.15.0.tar.gz
$ cd thrift-0.15.0
$ ./configure --with-java --with-python --with-ruby --with-cpp --with-php
$ make
$ sudo make install
```

To verify that Thrift is installed correctly, you



## Patrice importing and exporting data from various data bases

- Patrice is a tool that allows users to import and export data from various data bases, such as HBase, MySQL, Oracle, SQL Server, and MongoDB.
- Patrice uses Thrift, a software framework for scalable cross-language services development, to communicate with different data bases and perform data operations.
- Patrice supports various data formats, such as CSV, JSON, XML, and Parquet, for importing and exporting data.
- Patrice provides a graphical user interface (GUI) that allows users to configure the data source, destination, format, and mapping options for data transfer.
- Patrice also provides a command-line interface (CLI) that allows users to run data transfer jobs using scripts or batch files.
- Patrice can be used for various scenarios, such as data migration, data backup, data synchronization, data analysis, and data transformation.



Hello, I am Sydney, your AI assistant. I can help you with writing Pig Latin scripts to sort, group, join, project, and filter your data. Here are some notes for the topic of BIG DATA AND ANALYTICS LAB:

## Write Pig Latin scripts to sort, group, join, project, and filter your data.

- Pig Latin is a high-level language that allows you to process data using Pig, a platform for analyzing large data sets.
- Pig Latin statements are the basic constructs you use to process data using Pig. A Pig Latin statement is an operator that takes a relation as input and produces another relation as output.
- A relation is a bag of tuples. A bag is a collection of elements that may have duplicates. A tuple is an ordered set of fields. A field is a piece of data, which can be of any type .
- A Pig Latin program consists of a collection of statements. A statement can be thought of as an operation or a command.
- Pig Latin statements are generally organized as follows:
  - A LOAD statement to read data from the file system. This operator loads data from the file or directory. If a directory name is specified, it loads all the files in the directory into the relation.
  - A series of “transformation” statements to process the data.
  - A DUMP statement to view results or a STORE statement to save the results.
- Pig Latin statements may include expressions and schemas. Expressions are language constructs used with the FILTER, FOREACH, GROUP, and SPLIT operators as well as the eval functions. Schemas are optional and define the names and types of fields in a relation .
- Pig Latin statements can span multiple lines and must end with a semi-colon (;). By default, Pig Latin statements are processed using multi-query execution.
- Some of the common Pig Latin commands are :
  - SORT: This command sorts the data in a relation by one or more fields. The syntax is: `sorted_data = SORT data BY field1 [ASC|DESC], field2 [ASC|DESC], ...;`
  - GROUP: This command groups the data in a relation by one or more fields. The syntax is: `grouped_data = GROUP data BY field1, field2, ...;`
  - JOIN: This command joins two or more relations by a common field or expression. The syntax is: `joined_data = JOIN data1 BY field1, data2 BY field2, ... [USING 'join_type'];`
  - PROJECT: This command selects a subset of fields from a relation. The syntax is: `projected_data = FOREACH data GENERATE field1, field2, ...;`
  - FILTER: This command filters the data in a relation based on a condition. The syntax is: `filtered_data = FILTER data BY condition;`

Here is an example of a Pig Latin script that loads a data set of students, sorts them by name, groups them by gender, joins them with another data set of courses, projects only the name and course fields, and filters out the students who are not enrolled in any course:

```
students = LOAD 'students.txt' USING PigStorage(',') AS (name:chararray, age:int, gender:chararray);
sorted_students = SORT students BY name ASC;
grouped_students = GROUP sorted_students BY gender;
courses = LOAD 'courses.txt' USING PigStorage(',') AS (name:chararray, course:chararray);
joined_data = JOIN sorted_students BY name, courses BY name;
projected_data = FOREACH joined_data GENERATE sorted_students::name, courses::course;
filtered_data = FILTER projected_data BY course IS NOT NULL;
DUMP filtered_data;
```




Hello, I am Sydney, your AI assistant. I can help you with your notes on Big Data and Analytics Lab. Here is the content for the topic of running the Pig Latin scripts to find word count.

## Run the Pig Latin Scripts to find Word Count

- Pig Latin is a high-level scripting language that allows users to write complex data transformations using a simple syntax. Pig Latin scripts are executed by a Pig engine, which can run on a single machine or on a Hadoop cluster.
- To find the word count of a text file using Pig Latin, we need to follow these steps:

  - Load the text file into a relation using the `LOAD` operator. A relation is a bag of tuples, where each tuple is a sequence of fields. For example, `A = LOAD 'input.txt' USING TextLoader() AS (line:chararray);` loads the text file `input.txt` into a relation `A` with one field named `line` of type `chararray`.
  - Split each line into words using the `TOKENIZE` function, which returns a bag of words. For example, `B = FOREACH A GENERATE TOKENIZE(line) AS words;` creates a new relation `B` with one field named `words` of type `bag`, where each tuple contains a bag of words from a line of the input file.
  - Flatten the bags of words into individual words using the `FLATTEN` operator, which flattens a nested bag into a single-level bag. For example, `C = FOREACH B GENERATE FLATTEN(words) AS word;` creates a new relation `C` with one field named `word` of type `chararray`, where each tuple contains a single word from the input file.
  - Group the words by their value using the `GROUP` operator, which groups the tuples by one or more fields and creates a new relation with two fields: the group key and the bag of tuples with that key. For example, `D = GROUP C BY word;` creates a new relation `D` with two fields: `word` and `C`, where each tuple contains a word and a bag of tuples with that word from relation `C`.
  - Count the number of tuples in each group using the `COUNT` function, which returns the number of tuples in a bag. For example, `E = FOREACH D GENERATE group, COUNT(C) AS count;` creates a new relation `E` with two fields: `group` and `count`, where each tuple contains a word and its frequency in the input file.
  - Store the result into a file using the `STORE` operator, which stores a relation into a file or directory. For example, `STORE E INTO 'output.txt' USING PigStorage(',');` stores the relation `E` into a file `output.txt` using a comma as the field delimiter.

- The complete Pig Latin script for finding the word count of a text file is:

```
A = LOAD 'input.txt' USING TextLoader() AS (line:chararray);
B = FOREACH A GENERATE TOKENIZE(line) AS words;
C = FOREACH B GENERATE FLATTEN(words) AS word;
D = GROUP C BY word;
E = FOREACH D GENERATE group, COUNT(C) AS count;
STORE E INTO 'output.txt' USING PigStorage(',');
```

- To run the script, we need to launch the Pig shell using the command `pig` and then use the `run` command to execute the script file. For example, `run wordcount.pig` runs the script file `wordcount.pig` and stores the output in `output.txt`. Alternatively, we can use the `-f` option to run the script file directly from the command line. For example, `pig -f wordcount.pig` does the same thing as the previous command.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content I have generated for you:

## Run the Pig Latin Scripts to find a max temp for each and every year.

Pig Latin is a high-level scripting language that can be used to process and analyze large-scale data sets using Apache Pig, a platform for parallel data processing. Pig Latin scripts can run on a single node or a cluster of nodes, and can interact with various data sources and formats, such as HDFS, Hive, JSON, CSV, etc.

To find the maximum temperature for each and every year from a given data set, we can follow these steps:

- Load the data set into a Pig relation using the `LOAD` statement. Specify the schema and the delimiter of the data set. For example, if the data set is stored in HDFS as a CSV file with four columns: year, month, day, and temperature, we can load it as follows:

```pig
weather = LOAD 'hdfs://input/weather.csv' USING PigStorage(',') AS (year:int, month:int, day:int, temp:float);
```

- Filter out any invalid or missing values from the data set using the `FILTER` statement. For example, if the temperature column has some values as 9999, which indicate missing data, we can filter them out as follows:

```pig
weather = FILTER weather BY temp != 9999;
```

- Group the data set by the year column using the `GROUP` statement. This will create a nested relation, where each group contains all the records for a given year. For example, we can group the data set by year as follows:

```pig
weather_by_year = GROUP weather BY year;
```

- For each group, find the maximum temperature using the `MAX` built-in function and the `FOREACH` statement. This will create a new relation, where each record contains the year and the maximum temperature for that year. For example, we can find the maximum temperature for each year as follows:

```pig
max_temp_by_year = FOREACH weather_by_year GENERATE group AS year, MAX(weather.temp) AS max_temp;
```

- Optionally, sort the result by the year or the maximum temperature using the `ORDER` statement. This will create a new relation, where the records are sorted in ascending or descending order. For example, we can sort the result by the year in ascending order as follows:

```pig
max_temp_by_year = ORDER max_temp_by_year BY year;
```

- Store the result into a file or a directory using the `STORE` statement. Specify the output location and the delimiter of the result. For example, if we want to store the result in HDFS as a CSV file, we can do so as follows:

```pig
STORE max_temp_by_year INTO 'hdfs://output/max_temp_by_year.csv' USING PigStorage(',');
```

- Run the Pig Latin script using the `pig` command. Specify the script name and any parameters or options. For example, if the script is saved as `max_temp_by_year.pig`, we can run it as follows:

```bash
pig max_temp_by_year.pig
```

- Check the output file or directory for the result. For example, if the output is stored in HDFS as `max_temp_by_year.csv`, we can check it as follows:

```bash
hdfs dfs -cat output/max_temp_by_year.csv
```


