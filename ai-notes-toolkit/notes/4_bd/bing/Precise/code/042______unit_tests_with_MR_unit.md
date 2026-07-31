#### Unit tests with MRUnit

Here is an example of how to write unit tests for a MapReduce job using MRUnit:

```java
import org.apache.hadoop.io.*;
import org.apache.hadoop.mrunit.mapreduce.MapDriver;
import org.junit.Before;
import org.junit.Test;

public class WordCountTest {
  MapDriver<LongWritable, Text, Text, IntWritable> mapDriver;

  @Before
  public void setUp() {
    WordCountMapper mapper = new WordCountMapper();
    mapDriver = MapDriver.newMapDriver(mapper);
  }

  @Test
  public void testMapper() {
    mapDriver.withInput(new LongWritable(1), new Text("cat cat dog"));
    mapDriver.withOutput(new Text("cat"), new IntWritable(1));
    mapDriver.withOutput(new Text("cat"), new IntWritable(1));
    mapDriver.withOutput(new Text("dog"), new IntWritable(1));
    mapDriver.runTest();
  }
}
```

This code tests the `WordCountMapper` class, which is a mapper for a word count MapReduce job. The `setUp` method initializes the `mapDriver` object with an instance of the `WordCountMapper` class. The `testMapper` method then uses the `mapDriver` object to test the mapper with an input key-value pair and checks if the output key-value pairs match the expected output.
