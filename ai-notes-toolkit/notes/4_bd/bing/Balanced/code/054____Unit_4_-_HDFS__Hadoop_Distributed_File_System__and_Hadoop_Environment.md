## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

HDFS is a distributed file system that runs on a cluster of nodes and provides high availability, fault tolerance, scalability, and reliability for storing and processing large-scale data. HDFS follows a master-slave architecture, where one node acts as the NameNode (master) and manages the metadata of the file system, while the other nodes act as DataNodes (slaves) and store the actual data blocks.

Hadoop Environment is the set of software components and configurations that are required to run Hadoop applications on a cluster. Hadoop Environment includes the following components:

- Hadoop Common: The common utilities and libraries that support other Hadoop modules.
- Hadoop Distributed File System (HDFS): The distributed file system that provides high-throughput access to application data.
- Hadoop YARN: The framework for job scheduling and cluster resource management.
- Hadoop MapReduce: The programming model for large-scale data processing.
- Hadoop Ecosystem: The collection of tools and frameworks that extend the functionality of Hadoop, such as Hive, Pig, Spark, HBase, etc.

To write code for HDFS and Hadoop Environment, you need to use the Hadoop command-line interface (CLI) or the Hadoop Java API. The Hadoop CLI provides a set of commands to interact with HDFS and execute MapReduce jobs. The Hadoop Java API provides a set of classes and methods to programmatically access HDFS and write MapReduce applications.

Here are some examples of code for HDFS and Hadoop Environment:

- To create a directory in HDFS, you can use the `hadoop fs -mkdir` command or the `FileSystem.mkdirs()` method in the Java API.

```bash
# Using the Hadoop CLI
hadoop fs -mkdir /user/hadoop/dir

# Using the Hadoop Java API
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

Configuration conf = new Configuration();
FileSystem fs = FileSystem.get(conf);
Path dir = new Path("/user/hadoop/dir");
fs.mkdirs(dir);
```

- To copy a file from the local file system to HDFS, you can use the `hadoop fs -put` command or the `FileSystem.copyFromLocalFile()` method in the Java API.

```bash
# Using the Hadoop CLI
hadoop fs -put /home/hadoop/file.txt /user/hadoop/dir

# Using the Hadoop Java API
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

Configuration conf = new Configuration();
FileSystem fs = FileSystem.get(conf);
Path localFile = new Path("/home/hadoop/file.txt");
Path hdfsFile = new Path("/user/hadoop/dir/file.txt");
fs.copyFromLocalFile(localFile, hdfsFile);
```

- To write a MapReduce application in Java, you need to extend the `Mapper` and `Reducer` classes and implement the `map()` and `reduce()` methods. You also need to configure the input and output formats, the mapper and reducer classes, and the key and value types in the `Job` class.

```java
// Import the required packages
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// Define the Mapper class
public class WordCountMapper extends Mapper<Object, Text, Text, IntWritable> {

  // Define the output key and value objects
  private final static IntWritable one = new IntWritable(1);
  private Text word = new Text();

  // Implement the map() method
  public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
    // Split the input value into words
    String[] words = value.toString().split("\\s+");
    // Loop through the words and emit each word with a count of one
    for (String w : words) {
      word.set(w);
      context.write(word, one);
    }
  }
}

// Define the Reducer class
public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

  // Define the output value object
  private IntWritable result = new IntWritable();

  // Implement the reduce() method
  public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
    // Sum up the counts for each word
    int sum = 0;

```
