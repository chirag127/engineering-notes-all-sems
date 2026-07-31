# Test Data and Local Tests for Map Reduce

- Test data is a set of input values that can be used to verify the functionality and performance of a map reduce program.
- Local tests are tests that can be performed on a single machine without using a hadoop cluster or a distributed file system.
- Local tests are useful for debugging and validating the logic of the map and reduce functions before deploying them on a large-scale data set.
- Local tests can be done in different ways depending on the programming language and the framework used for map reduce.

## Local Tests for Hadoop Streaming

- Hadoop streaming is a utility that allows users to write map and reduce scripts in any language that can read from standard input and write to standard output, such as Python, Ruby, Perl, etc.
- To test a map reduce script locally using hadoop streaming, one can use the following command:

```
cat input_file | map_script | sort -k1,1 | reduce_script
```

- This command simulates the map reduce process by piping the input file to the map script, sorting the output by key, and piping it to the reduce script.
- The input file should contain one record per line, and the map and reduce scripts should write key-value pairs in the format `<key>\t<value>` to standard output.

## Local Tests for Hadoop Java API

- Hadoop Java API is the native Java interface for writing map and reduce classes that implement the Mapper and Reducer interfaces.
- To test a map reduce class locally using the hadoop Java API, one can use the MRUnit framework  .
- MRUnit is a library that provides mock objects and drivers for testing map, reduce, and combiner classes in isolation or in combination.
- To use MRUnit, one needs to add the MRUnit dependency to the project's pom.xml file, and write test cases using JUnit or TestNG.
- An example of a test case for a map reduce class using MRUnit is:

```
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mrunit.mapreduce.MapReduceDriver;
import org.junit.Before;
import org.junit.Test;

public class WordCountTest {

  private MapReduceDriver<Object, Text, Text, IntWritable, Text, IntWritable> mapReduceDriver;

  @Before
  public void setUp() {
    WordCountMapper mapper = new WordCountMapper();
    WordCountReducer reducer = new WordCountReducer();
    mapReduceDriver = MapReduceDriver.newMapReduceDriver(mapper, reducer);
  }

  @Test
  public void testMapReduce() throws IOException {
    mapReduceDriver.withInput(new Text("hello world"));
    mapReduceDriver.withOutput(new Text("hello"), new IntWritable(1));
    mapReduceDriver.withOutput(new Text("world"), new IntWritable(1));
    mapReduceDriver.runTest();
  }
}
```

- This test case creates a map reduce driver with the WordCountMapper and WordCountReducer classes, and verifies that the output matches the expected key-value pairs for a given input.