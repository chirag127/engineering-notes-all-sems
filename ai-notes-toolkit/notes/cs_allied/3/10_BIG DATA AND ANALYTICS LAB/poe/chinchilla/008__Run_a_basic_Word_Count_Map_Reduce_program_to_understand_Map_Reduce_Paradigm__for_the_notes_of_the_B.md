## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm

In this lab, we will learn about the Map Reduce paradigm, which is a popular programming model used to process large amounts of data in a distributed and parallel manner. We will run a basic Word Count Map Reduce program to understand how Map Reduce works.

### Prerequisites

Before we start, make sure you have the following installed:

- Hadoop
- Java Development Kit (JDK)

### Steps

1. Create a text file with some sample text. For example, create a file called `input.txt` and add the following text:

```
Hello world
Hello Map Reduce
Hello Big Data
```

2. Move the input file to the Hadoop file system using the following command:

```
hadoop fs -put input.txt /input/
```

This command will copy the `input.txt` file to the `/input/` directory in the Hadoop file system.

3. Create a Java class that implements the Map Reduce job. Here is an example of a Word Count Map Reduce job:

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

This Java class contains two inner classes: `TokenizerMapper` and `IntSumReducer`. The `TokenizerMapper` class maps each word in the input text file to a key-value pair, where the key is the word and the value is the number 1. The `IntSumReducer` class reduces the key-value pairs by summing up the values for each key.

4. Compile the Java class using the following command:

```
javac -classpath `hadoop classpath` WordCount.java
```

This command will compile the `WordCount.java` class and generate a `WordCount.class` file.

5. Create a JAR file containing the compiled class using the following command:

```
jar cf wc.jar WordCount*.class
```

This command will create a JAR file called `wc.jar` containing the `WordCount.class` files.

6. Run the Map Reduce job using the following command:

```
hadoop jar wc.jar WordCount /input /output
```

This command will run the `WordCount` Map Reduce job on the `input.txt` file in the `/input/` directory and store the output in the `/output/` directory.

7. View the output using the following command:

```
hadoop fs -cat /output/part-r-00000
```

This command will display the output of the Map Reduce job, which should look like this:

```
Big     1
Data    1
Hello   3
Map     1
Reduce  1
world   1
```

This output shows the count of each word in the input text file.

### Conclusion

In this lab, we learned about the Map Reduce paradigm and ran a basic Word Count Map Reduce program to understand how Map Reduce works. We also learned how to