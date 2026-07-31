## Unit 2 - Hadoop and Map Reduce

Hadoop MapReduce is a programming paradigm that allows processing large amounts of data in parallel on a cluster of commodity hardware. It consists of two phases: map and reduce. In the map phase, the input data is split into key-value pairs and processed by user-defined functions called mappers. In the reduce phase, the output of the mappers is shuffled and sorted by key, and then processed by user-defined functions called reducers. The reducers produce the final output of the MapReduce job.

To write a MapReduce program, you need to implement the Mapper and Reducer interfaces and optionally the Partitioner, Combiner, and InputFormat interfaces. You also need to specify the input and output types, paths, and formats for the job. You can use the Hadoop API or other frameworks such as Apache Pig or Apache Hive to write MapReduce programs.

Here is an example of a MapReduce program that counts the number of occurrences of each word in a text file. The program is written in Java using the Hadoop API.

```java
// Import the necessary libraries
import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// Define the WordCount class
public class WordCount {

  // Define the Mapper class
  public static class TokenizerMapper
       extends Mapper<Object, Text, Text, IntWritable>{

    // Define the IntWritable constant one
    private final static IntWritable one = new IntWritable(1);
    // Define the Text object word
    private Text word = new Text();

    // Override the map method
    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      // Tokenize the input value
      StringTokenizer itr = new StringTokenizer(value.toString());
      // Iterate over the tokens
      while (itr.hasMoreTokens()) {
        // Set the word object with the token
        word.set(itr.nextToken());
        // Write the word and one to the context
        context.write(word, one);
      }
    }
  }

  // Define the Reducer class
  public static class IntSumReducer
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    // Define the IntWritable object result
    private IntWritable result = new IntWritable();

    // Override the reduce method
    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      // Initialize the sum to zero
      int sum = 0;
      // Iterate over the values
      for (IntWritable val : values) {
        // Add the value to the sum
        sum += val.get();
      }
      // Set the result with the sum
      result.set(sum);
      // Write the key and result to the context
      context.write(key, result);
    }
  }

  // Define the main method
  public static void main(String[] args) throws Exception {
    // Create a Configuration object
    Configuration conf = new Configuration();
    // Create a Job object with the configuration and a name
    Job job = Job.getInstance(conf, "word count");
    // Set the jar by finding the class
    job.setJarByClass(WordCount.class);
    // Set the mapper class
    job.setMapperClass(TokenizerMapper.class);
    // Set the combiner class
    job.setCombinerClass(IntSumReducer.class);
    // Set the reducer class
    job.setReducerClass(IntSumReducer.class);
    // Set the output key class
    job.setOutputKeyClass(Text.class);
    // Set the output value class
    job.setOutputValueClass(IntWritable.class);
    // Set the input path from the arguments
    FileInputFormat.addInputPath(job, new Path(args[0]));
    // Set the output path from the arguments
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    // Wait for the job to complete and exit
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
```