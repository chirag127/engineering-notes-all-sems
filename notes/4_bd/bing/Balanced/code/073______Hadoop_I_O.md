#### Hadoop I/O

Hadoop I/O is the set of primitives for data input and output in Hadoop. It supports reading and writing data from different sources, such as local files, HDFS, or other distributed file systems. It also provides various features, such as data integrity, compression, serialization, and custom data types.

One of the key concepts in Hadoop I/O is the Writable interface, which defines how data is serialized and deserialized for network transmission or disk storage. Writable objects can be used as keys or values in MapReduce programs, or as fields in other Writable objects. Hadoop provides several built-in implementations of Writable, such as IntWritable, Text, ArrayWritable, etc. Users can also create their own custom Writable classes by implementing the readFields() and write() methods.

Another important concept in Hadoop I/O is the InputFormat and OutputFormat classes, which define how data is split into input splits and how output files are created. InputFormat and OutputFormat are responsible for creating RecordReader and RecordWriter objects, which read and write records from and to input and output sources. Hadoop provides several built-in implementations of InputFormat and OutputFormat, such as TextInputFormat, SequenceFileInputFormat, TextOutputFormat, SequenceFileOutputFormat, etc. Users can also create their own custom InputFormat and OutputFormat classes by extending the abstract classes FileInputFormat and FileOutputFormat.

Here is a simple example of Hadoop I/O code that reads a text file from HDFS and writes the number of words in each line to a sequence file in HDFS:

```java
// WordCount.java
import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.SequenceFile;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

  public static class WordCountMapper
       extends Mapper<LongWritable, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(LongWritable key, Text value, Context context
                    ) throws IOException, InterruptedException {
      String line = value.toString();
      int count = line.split("\\s+").length;
      word.set(line);
      context.write(word, new IntWritable(count));
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(WordCount.class);
    job.setMapperClass(WordCountMapper.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    job.setOutputFormatClass(SequenceFileOutputFormat.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
```