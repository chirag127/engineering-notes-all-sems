#### Analyzing data with Hadoop

Hadoop is a framework that allows distributed processing of large datasets across clusters of computers using simple programming models. Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce. HDFS is a distributed file system that stores data across multiple nodes in a cluster. MapReduce is a programming model that allows parallel processing of data using two types of functions: map and reduce. Map functions take input data and transform it into intermediate key-value pairs. Reduce functions take intermediate key-value pairs and aggregate them to produce output data.

To analyze data with Hadoop, you need to write a Java program that implements the map and reduce functions for your specific problem. You also need to specify the input and output paths for your data in HDFS. You can then run your program using the Hadoop command-line interface or a graphical user interface such as Hue.

Here is an example of a Hadoop program that counts the number of occurrences of each word in a text file. The program consists of three classes: WordCount, WordCountMapper, and WordCountReducer. WordCount is the main class that sets up the configuration and launches the job. WordCountMapper is the map class that reads each line of the input file and emits a key-value pair for each word with the value of 1. WordCountReducer is the reduce class that sums up the values for each word and writes the result to the output file.

```java
// WordCount.java
import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(WordCount.class);
    job.setMapperClass(WordCountMapper.class);
    job.setReducerClass(WordCountReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
```

```java
// WordCountMapper.java
import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class WordCountMapper
       extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString());
      while (itr.hasMoreTokens()) {
        word.set(itr.nextToken());
        context.write(word, one);
      }
    }
  }
```

```java
// WordCountReducer.java
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class WordCountReducer
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }
```

To run this program, you need to compile it and create a jar file. You also need to have a text file as the input data and a directory in HDFS as the output path. For example, if you have a file called input.txt in your local file system and a directory called output in HDFS, you can run the following commands:

```bash
# Compile the program and create a jar file
javac -cp $(hadoop classpath) WordCount.java WordCountMapper.java WordCountReducer.java
jar cf wc.jar WordCount*.class

# Copy the input file to HDFS
hadoop fs -put input.txt /user/hadoop/input.txt

# Run the program using the jar file and the input and output paths
hadoop jar wc.jar WordCount /user/hadoop