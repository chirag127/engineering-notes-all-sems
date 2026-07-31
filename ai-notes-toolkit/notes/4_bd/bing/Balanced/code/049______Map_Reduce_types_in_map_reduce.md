MapReduce is a programming model for processing large-scale data sets in parallel and distributed manner. It consists of two main functions: map and reduce. The map function takes an input key-value pair and produces a list of intermediate key-value pairs. The reduce function takes an intermediate key and a list of values associated with that key, and merges them into a smaller set of values.

There are different types of map and reduce functions, depending on the input and output formats and types. The input and output formats define how the data is stored and read by the map and reduce tasks. The input and output types define the data types of the keys and values used by the map and reduce functions.

Some of the common input and output formats are:

- TextInputFormat: reads lines of text files and produces key-value pairs, where the key is the byte offset of the line and the value is the line itself.
- KeyValueTextInputFormat: reads lines of text files and splits each line into a key and a value, separated by a tab character.
- SequenceFileInputFormat: reads binary key-value pairs stored in a sequence file, which is a flat file consisting of binary key-value pairs.
- SequenceFileOutputFormat: writes binary key-value pairs to a sequence file.
- TextOutputFormat: writes key-value pairs to a text file, separated by a tab character.

Some of the common input and output types are:

- LongWritable: a 64-bit integer.
- IntWritable: a 32-bit integer.
- Text: a string of Unicode characters.
- BytesWritable: a byte array.

A simple example of a map and reduce function in Java is:

```java
// The map function takes a LongWritable key and a Text value, and produces a Text key and an IntWritable value
public static class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
  private final static IntWritable one = new IntWritable(1);
  private Text word = new Text();

  public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    // Split the input line into words
    StringTokenizer itr = new StringTokenizer(value.toString());
    while (itr.hasMoreTokens()) {
      // Set the word as the output key
      word.set(itr.nextToken());
      // Write the output key-value pair
      context.write(word, one);
    }
  }
}

// The reduce function takes a Text key and an Iterable of IntWritable values, and produces a Text key and an IntWritable value
public static class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
  private IntWritable result = new IntWritable();

  public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
    // Sum up the values for the same key
    int sum = 0;
    for (IntWritable val : values) {
      sum += val.get();
    }
    // Set the sum as the output value
    result.set(sum);
    // Write the output key-value pair
    context.write(key, result);
  }
}
```