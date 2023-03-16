## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm

- MapReduce is a framework for processing large-scale data sets in parallel and distributed manner using clusters of commodity hardware.
- Word Count is a simple application that counts the number of occurrences of each word in a given input set. It is often used as a "Hello World" program in MapReduce.
- To run a basic Word Count Map Reduce program, we need to follow these steps:

  - Define a mapper class that implements the `Mapper` interface and overrides the `map` method. The `map` method takes a key-value pair as input and emits intermediate key-value pairs. For example, the mapper can take a line of text as input and emit each word and its count (1) as output.
  - Define a reducer class that implements the `Reducer` interface and overrides the `reduce` method. The `reduce` method takes a key and a list of values as input and emits a final key-value pair as output. For example, the reducer can take a word and a list of counts as input and emit the word and its total count as output.
  - Define a driver class that configures and runs the MapReduce job. The driver class sets the input and output paths, the mapper and reducer classes, the output key and value types, and other job parameters. The driver class then submits the job to the cluster and waits for its completion.
  - Compile and package the Java classes into a JAR file and copy it to the Hadoop cluster.
  - Run the JAR file using the `hadoop jar` command and specify the input and output directories.
  - Check the output files in the output directory and verify the word counts.

- Here is an example of a Word Count Map Reduce program in Java:

```java
// WCMapper.java
import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class WCMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

  private final static IntWritable one = new IntWritable(1);
  private Text word = new Text();

  public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    // get the input line as a string
    String line = value.toString();
    // split the line into words using StringTokenizer
    StringTokenizer tokenizer = new StringTokenizer(line);
    // iterate over the tokens and emit each word and 1 as a key-value pair
    while (tokenizer.hasMoreTokens()) {
      word.set(tokenizer.nextToken());
      context.write(word, one);
    }
  }
}
```

```java
// WCReducer.java
import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class WCReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

  public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
    // initialize the sum to zero
    int sum = 0;
    // iterate over the values and add them to the sum
    for (IntWritable value : values) {
      sum += value.get();
    }
    // emit the word and its total count as a key-value pair
    context.write(key, new IntWritable(sum));
  }
}
```

```java
// WCDriver.java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WCDriver {

  public static void main(String[] args) throws Exception {
    // create a configuration object
    Configuration conf = new Configuration();
    // create a job object and name it
    Job job = Job.getInstance(conf, "word count");
    // set the jar file that contains the driver, mapper and reducer classes
    job.setJarByClass(WCDriver.class);
    // set the mapper class
    job.setMapperClass(WCMapper.class);
    // set the reducer class
    job.setReducerClass(WCReducer.class);
    // set the output key type
    job.setOutputKeyClass(Text.class);
    //