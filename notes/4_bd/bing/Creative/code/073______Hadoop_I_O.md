#### Hadoop I/O

Hadoop I/O is the data input and output system of the Hadoop framework. It supports reading and writing data from different sources, such as local files, HDFS, or other distributed file systems. It also provides various data types and serialization formats for efficient data processing.

One of the main components of Hadoop I/O is the `Writable` interface, which defines how data values are serialized and deserialized for network transmission or storage. Any data type that implements this interface can be used as a key or value in a Hadoop MapReduce job. Some common examples of `Writable` types are `IntWritable`, `Text`, `LongWritable`, `DoubleWritable`, etc.

Another component of Hadoop I/O is the `InputFormat` interface, which defines how data is split into logical units called `InputSplit`s, and how to create a `RecordReader` for each split. A `RecordReader` is responsible for reading key-value pairs from an `InputSplit`. Some common examples of `InputFormat` types are `TextInputFormat`, `SequenceFileInputFormat`, `KeyValueTextInputFormat`, etc.

Similarly, the `OutputFormat` interface defines how to create a `RecordWriter` for each output file. A `RecordWriter` is responsible for writing key-value pairs to an output file. Some common examples of `OutputFormat` types are `TextOutputFormat`, `SequenceFileOutputFormat`, `KeyValueTextOutputFormat`, etc.

Here is an example of a Java code snippet that uses Hadoop I/O to read and write text files:

```java
// Import the necessary classes
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// Define a mapper class that counts the words in each line of input
public class WordCountMapper extends Mapper<Object, Text, Text, IntWritable> {

  // Define a constant one as the value for each word
  private final static IntWritable one = new IntWritable(1);
  // Define a reusable text object as the key for each word
  private Text word = new Text();

  // Override the map method that takes an input key-value pair and emits output key-value pairs
  public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
    // Split the input value by whitespace and store it in an array of strings
    String[] words = value.toString().split("\\s+");
    // Loop through the array and emit each word as a key and one as a value
    for (String w : words) {
      word.set(w);
      context.write(word, one);
    }
  }
}

// Define a reducer class that sums the values for each word
public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

  // Define a reusable int writable object as the output value
  private IntWritable result = new IntWritable();

  // Override the reduce method that takes an input key and a list of values and emits an output key-value pair
  public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
    // Initialize a sum variable to zero
    int sum = 0;
    // Loop through the values and add them to the sum
    for (IntWritable val : values) {
      sum += val.get();
    }
    // Set the result to the sum
    result.set(sum);
    // Emit the key and the result as the output
    context.write(key, result);
  }
}

// Define a main class that creates and runs a MapReduce job
public class WordCount {

  // Define the main method that takes the input and output paths as arguments
  public static void main(String[] args) throws Exception {
    // Create a configuration object
    Configuration conf = new Configuration();
    // Create a job object with the configuration and a name
    Job job = Job.getInstance(conf, "word count");
    // Set the jar file that contains the mapper and reducer classes
    job.setJarByClass(WordCount.class);
    // Set the mapper class
    job.setMapperClass(WordCountMapper.class);
    // Set the combiner class (optional)
    job.setCombinerClass(WordCountReducer.class);
    // Set the reducer class
    job.setReducerClass(WordCountReducer.class);
    // Set the output key class
    job.setOutputKeyClass(Text.class);
    // Set the output value class