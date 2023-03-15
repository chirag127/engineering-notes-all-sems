### Output Formats for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- OutputFormat is a class in Hadoop MapReduce that defines how the output files of a job are written and stored in a FileSystem .
- OutputFormat also provides the RecordWriter implementation to be used to write the output records of the map and reduce tasks .
- There are different types of OutputFormat in MapReduce, each with its own advantages and disadvantages. Some of the common types are :
  - TextOutputFormat: The default OutputFormat that writes plain text files as output. Each record is a line of text with the key and value separated by a tab character. This format is easy to read and process, but not very efficient in terms of space and speed.
  - SequenceFileOutputFormat: An OutputFormat that writes sequence files as output. Sequence files are binary files that store serialized key-value pairs. This format is more compact and faster than text files, and can handle arbitrary data types. Sequence files are also used as intermediate format between MapReduce jobs.
  - SequenceFileAsBinaryOutputFormat: A variant of SequenceFileOutputFormat that writes the keys and values as raw bytes instead of using serialization. This format is useful for binary data that does not need to be deserialized by the next job.
  - MapFileOutputFormat: An OutputFormat that writes map files as output. Map files are a special type of sequence files that support random access and indexing. This format is useful for applications that need to look up values by keys quickly and efficiently.
  - MultipleOutputs: An OutputFormat that allows writing to multiple output files with different formats and names. This format is useful for applications that need to partition or categorize the output data based on some criteria.
  - LazyOutputFormat: An OutputFormat that avoids creating empty output files for tasks that do not produce any output. This format is useful for reducing the number of output files and saving disk space.
  - DBOutputFormat: An OutputFormat that writes the output data to a relational database table. This format is useful for applications that need to store or query the output data using SQL. For example, HBase's TableOutputFormat enables the MapReduce program to work on the data stored in the HBase table and write the output to the same table.
- The output format of a MapReduce job can be specified by using the FileOutputFormat.setOutputPath() method to set the output directory, and the Job.setOutputFormatClass() method to set the output format class . For example, to use SequenceFileOutputFormat as the output format, the following code can be used:

```java
FileOutputFormat.setOutputPath(job, new Path("/output"));
job.setOutputFormatClass(SequenceFileOutputFormat.class);
```
- The output format of a MapReduce job can also be customized by extending the OutputFormat class and overriding its methods, such as getRecordWriter(), checkOutputSpecs(), and getOutputCommitter() . For example, to create a custom OutputFormat that writes the output data to a CSV file, the following code can be used:

```java
public class CSVOuputFormat extends FileOutputFormat<Text, Text> {

  @Override
  public RecordWriter<Text, Text> getRecordWriter(TaskAttemptContext context) throws IOException, InterruptedException {
    // get the output file path
    Path outputPath = FileOutputFormat.getOutputPath(context);
    // create a CSV writer
    CSVWriter writer = new CSVWriter(new FileWriter(outputPath.toString()));
    // return a custom record writer
    return new CSVRecordWriter(writer);
  }

  // a custom record writer that writes key-value pairs to a CSV file
  public static class CSVRecordWriter extends RecordWriter<Text, Text> {

    private CSVWriter writer;

    public CSVRecordWriter(CSVWriter writer) {
      this.writer = writer;
    }

    @Override
    public void write(Text key, Text value) throws IOException, InterruptedException {
      // write the key and value as a string array to the CSV file
      writer.writeNext(new String[] {key.toString(), value.toString()});
    }

    @Override
    public void close(TaskAttemptContext context) throws IOException, InterruptedException {
      // close the CSV writer
      writer.close();
    }
  }
}
```