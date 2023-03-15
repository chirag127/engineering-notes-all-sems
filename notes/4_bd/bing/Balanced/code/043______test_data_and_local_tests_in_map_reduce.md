#### Test data and local tests in map reduce

One way to test your map and reduce code locally is to use hadoop streaming, which allows you to write your scripts in any language that can read from standard input and write to standard output. For example, if you have a map.py and a reduce.py script, you can test them locally like this:

```bash
cat *.csv | map.py | sort -k1,1 | reduce.py
```

This will simulate the map and reduce phases of hadoop, but without the distributed file system and the parallelism. To pass data from the mapper to the reducer, you need to write the key and value pairs separated by a tab character to the standard output.

Another way to test your map and reduce code locally is to use MRUnit, which is a testing framework that lets you test and debug map reduce jobs in isolation without spinning up a hadoop cluster. MRUnit provides mock objects and assertions for the map and reduce contexts, as well as drivers for running the map and reduce tasks. For example, if you have a WordCountMapper and a WordCountReducer class, you can test them with MRUnit like this:

```java
public class WordCountTest {

  @Test
  public void testMapper() {
    // create a mock map context
    MapDriver<LongWritable, Text, Text, IntWritable> mapDriver = new MapDriver<>();
    mapDriver.setMapper(new WordCountMapper());

    // input a line of text
    mapDriver.withInput(new LongWritable(1), new Text("hello world"));

    // output the word counts
    mapDriver.withOutput(new Text("hello"), new IntWritable(1));
    mapDriver.withOutput(new Text("world"), new IntWritable(1));

    // run the test
    mapDriver.runTest();
  }

  @Test
  public void testReducer() {
    // create a mock reduce context
    ReduceDriver<Text, IntWritable, Text, IntWritable> reduceDriver = new ReduceDriver<>();
    reduceDriver.setReducer(new WordCountReducer());

    // input a list of values for a key
    reduceDriver.withInput(new Text("hello"), Arrays.asList(new IntWritable(1), new IntWritable(2)));

    // output the sum of the values
    reduceDriver.withOutput(new Text("hello"), new IntWritable(3));

    // run the test
    reduceDriver.runTest();
  }
}
```

This will test the logic of the mapper and reducer classes, but without the input and output formats, the partitioner, the combiner, and the job configuration. MRUnit also provides drivers for testing the map and reduce tasks together, as well as the entire map reduce job.
