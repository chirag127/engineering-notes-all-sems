## Unit 2 - Hadoop and Map Reduce

Hadoop MapReduce is a programming paradigm that runs in the background of Hadoop to provide scalability and easy data-processing solutions. It is based on the idea of splitting a large data set into smaller chunks and processing them in parallel on multiple nodes of a cluster. The MapReduce model consists of two phases: map and reduce. In the map phase, each input record is transformed into a key-value pair by a user-defined function called mapper. In the reduce phase, the key-value pairs are grouped by key and aggregated by a user-defined function called reducer. The output of the reduce phase is the final result of the MapReduce job.

The following code snippet shows a simple example of a MapReduce program in Java that counts the number of occurrences of each word in a text file. The mapper function takes a line of text as input and emits a key-value pair for each word with the word as the key and 1 as the value. The reducer function takes a key and a list of values as input and sums up the values to get the total count of the word.

```java
// Import the required packages
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

// Define the mapper class
public class WordCountMapper extends Mapper<Object, Text, Text, IntWritable> {

  // Define a constant for the value 1
  private final static IntWritable one = new IntWritable(1);
  // Define a variable for the key
  private Text word = new Text();

  // Override the map method
  public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
    // Tokenize the input line by whitespace
    StringTokenizer itr = new StringTokenizer(value.toString());
    // Loop through the tokens
    while (itr.hasMoreTokens()) {
      // Set the word as the key
      word.set(itr.nextToken());
      // Emit the key-value pair
      context.write(word, one);
    }
  }
}

// Define the reducer class
public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

  // Define a variable for the result
  private IntWritable result = new IntWritable();

  // Override the reduce method
  public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
    // Initialize a variable for the sum
    int sum = 0;
    // Loop through the values
    for (IntWritable val : values) {
      // Add the value to the sum
      sum += val.get();
    }
    // Set the result as the sum
    result.set(sum);
    // Emit the key-value pair
    context.write(key, result);
  }
}

// Define the main class
public class WordCount {

  // Define the main method
  public static void main(String[] args) throws Exception {
    // Create a configuration object
    Configuration conf = new Configuration();
    // Create a job object
    Job job = Job.getInstance(conf, "word count");
    // Set the jar by class
    job.setJarByClass(WordCount.class);
    // Set the mapper class
    job.setMapperClass(WordCountMapper.class);
    // Set the combiner class
    job.setCombinerClass(WordCountReducer.class);
    // Set the reducer class
    job.setReducerClass(WordCountReducer.class);
    // Set the output key class
    job.setOutputKeyClass(Text.class);
    // Set the output value class
    job.setOutputValueClass(IntWritable.class);
    // Set the input path
    FileInputFormat.addInputPath(job, new Path(args[0]));
    // Set the output path
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    // Wait for the job to complete
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
```