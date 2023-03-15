#### Output Formats in MapReduce

In Hadoop MapReduce, the output of the reduce task is written to the `OutputFormat` defined in the job configuration. The default `OutputFormat` is `TextOutputFormat`, which writes the output as text files in the output directory specified in the job configuration.

Here is an example of how to set the `OutputFormat` in the job configuration:

```java
Job job = Job.getInstance(conf, "MyJob");
job.setOutputFormatClass(TextOutputFormat.class);
```

Other available `OutputFormat`s include `SequenceFileOutputFormat`, which writes the output as Hadoop `SequenceFile`s, and `NullOutputFormat`, which discards the output.

To implement a custom `OutputFormat`, you can extend the `OutputFormat` class and override the `getRecordWriter` method to provide a custom `RecordWriter` implementation. The `RecordWriter` is responsible for writing the output data to the final output files.

Here is an example of a custom `OutputFormat` implementation:

```java
public class MyOutputFormat extends OutputFormat<Text, IntWritable> {
    @Override
    public RecordWriter<Text, IntWritable> getRecordWriter(TaskAttemptContext context) {
        // return a custom RecordWriter implementation
    }
}
```

To use the custom `OutputFormat`, set it in the job configuration as shown above:

```java
Job job = Job.getInstance(conf, "MyJob");
job.setOutputFormatClass(MyOutputFormat.class);
```