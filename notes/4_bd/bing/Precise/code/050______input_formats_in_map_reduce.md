#### Input Formats in MapReduce

In MapReduce, the input data is divided into splits, which are then processed by the map tasks. The `InputFormat` class is responsible for defining how the input data is split and read. There are several built-in `InputFormat` classes in Hadoop, including:

- `TextInputFormat`: This is the default `InputFormat` for MapReduce jobs. It reads data line by line, where each line is a key-value pair. The key is the byte offset of the line, and the value is the content of the line.

- `KeyValueTextInputFormat`: This `InputFormat` reads data line by line, where each line is a key-value pair separated by a delimiter (by default, a tab character).

- `SequenceFileInputFormat`: This `InputFormat` reads data from a sequence file, which is a binary file format that stores key-value pairs.

- `NLineInputFormat`: This `InputFormat` reads data line by line, where `N` lines are grouped into a single split and processed by a single map task.

Here is an example of how to set the `InputFormat` for a MapReduce job in Java:

```java
Job job = Job.getInstance(conf, "MyJob");
job.setInputFormatClass(TextInputFormat.class);
```

You can also create your own custom `InputFormat` by extending the `InputFormat` class and overriding the `getSplits` and `createRecordReader` methods. This allows you to define your own logic for splitting and reading the input data.