### MapReduce

MapReduce is a programming model and an associated implementation for processing and generating large datasets with a parallel, distributed algorithm on a cluster of computers. 

- MapReduce consists of two phases: map and reduce.
- The map phase takes an input dataset and transforms it into a set of key-value pairs, where the key and value can be any type of data.
- The reduce phase takes the output of the map phase and merges the values associated with the same key, producing a final output dataset.
- The MapReduce framework handles the distribution, parallelization, fault-tolerance, and monitoring of the map and reduce tasks on the cluster.
- The MapReduce framework can be used to implement various kinds of data analysis applications, such as word count, inverted index, PageRank, k-means clustering, etc.

#### Example: WordCount

- WordCount is a simple application that counts the frequency of each word in a given input text file.
- The map function takes a line of text as input and emits a key-value pair for each word in the line, where the key is the word and the value is 1.
- The reduce function takes a key and a list of values as input and sums up the values, producing a key-value pair where the key is the word and the value is the total count.
- The output of the WordCount application is a file that contains the frequency of each word in the input file.

#### Source Code

- The following is a Java implementation of the WordCount application using the Hadoop MapReduce API.

```java
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

public class WordCount {

  public static class TokenizerMapper
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

  public static class IntSumReducer
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

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(WordCount.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
```

#### Usage

- To run the WordCount application on a Hadoop cluster, the following steps are required:

  - Compile the Java source code into a jar file that contains the WordCount class and its dependencies.
  - Copy the input text file to the Hadoop Distributed File System (HDFS).
  - Submit the jar file and the input and output paths to the Hadoop MapReduce framework using the `hadoop jar` command.
  - Wait for the job to finish and check the output file on the HDFS.

- For example, assuming the input file is named `input.txt` and the jar file is named `wordcount.jar`, the following commands can be used to run the WordCount application:

  - `hadoop fs -put input.txt /user/hadoop/input` (copy the input file to the HDFS)
  - `hadoop jar wordcount.jar WordCount /user/hadoop/input /user/hadoop/output`