## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Map Reduce consists of two phases: Map and Reduce.
- Map phase takes an input key-value pair and produces a set of intermediate key-value pairs.
- Reduce phase takes the intermediate key-value pairs with the same key and combines them to produce the final output.
- Word Count is a simple example of Map Reduce that counts the frequency of each word in a text file.
- The steps to run a Word Count Map Reduce program are:

  1. Write a Mapper class that implements the `map` method. The `map` method takes a line of text as input and splits it into words. For each word, it emits a key-value pair of the word and 1.
  2. Write a Reducer class that implements the `reduce` method. The `reduce` method takes a word and a list of values (counts) as input and sums up the values to get the total count of the word. It emits a key-value pair of the word and the total count.
  3. Write a Driver class that configures and runs the Map Reduce job. The Driver class specifies the input and output paths, the Mapper and Reducer classes, the input and output formats, and other job parameters.
  4. Compile and package the classes into a JAR file.
  5. Run the JAR file on a Hadoop cluster or a single-node setup using the `hadoop jar` command. The output will be stored in the specified output path.

- Here is a sample code for the Word Count Map Reduce program in Java:

  ```java
  // Mapper class
  import java.io.IOException;
  import java.util.StringTokenizer;
  import org.apache.hadoop.io.IntWritable;
  import org.apache.hadoop.io.LongWritable;
  import org.apache.hadoop.io.Text;
  import org.apache.hadoop.mapreduce.Mapper;

  public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
      // Split the line into words
      StringTokenizer itr = new StringTokenizer(value.toString());
      // For each word, emit a key-value pair of the word and 1
      while (itr.hasMoreTokens()) {
        word.set(itr.nextToken());
        context.write(word, one);
      }
    }
  }

  // Reducer class
  import java.io.IOException;
  import org.apache.hadoop.io.IntWritable;
  import org.apache.hadoop.io.Text;
  import org.apache.hadoop.mapreduce.Reducer;

  public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
      // Sum up the values (counts) for the same word
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      // Emit a key-value pair of the word and the total count
      result.set(sum);
      context.write(key, result);
    }
  }

  // Driver class
  import org.apache.hadoop.conf.Configuration;
  import org.apache.hadoop.fs.Path;
  import org.apache.hadoop.io.IntWritable;
  import org.apache.hadoop.io.Text;
  import org.apache.hadoop.mapreduce.Job;
  import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
  import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

  public class WordCount {

    public static void main(String[] args) throws Exception {
      // Create a new configuration object
      Configuration conf = new Configuration();
      // Create a new job object
      Job job = Job.getInstance(conf, "word count");
      // Set the jar file that contains the Mapper, Reducer, and Driver classes
      job.setJarByClass(WordCount.class);
      // Set the Mapper class
      job.setMapperClass(WordCountMapper.class);
      // Set the Reducer class
      job.setReducerClass(WordCountReducer.class);
      // Set the output key type
      job.setOutputKeyClass(Text.class);
      // Set the output value type
      job.setOutputValueClass(IntWritable.class);
      // Set the input path (a text file in HDFS)
      FileInputFormat.addInputPath(job, new Path(args[0]));