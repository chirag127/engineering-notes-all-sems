### Unit Tests with MRUnit

- MRUnit is a Java library that helps developers unit test Hadoop MapReduce jobs.
- MRUnit allows you to craft test input, push it through your mapper and/or reducer, and verify its output all in a JUnit test.
- MRUnit supports testing mappers and reducers separately as well as testing map/reduce pairs as a whole.
- MRUnit can also mock the context and counters objects used by mappers and reducers.
- MRUnit can be used with other testing frameworks such as Mockito or PowerMock to create more complex test cases.

#### Example of testing a mapper with MRUnit

- Suppose we have a mapper that processes road surface data used to create maps. The input contains both linear surfaces and intersections.
- The mapper emits the surface type and the length as the key-value pair.
- The mapper code is as follows:

```java
public class RoadMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
  @Override
  public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    String line = value.toString();
    String[] tokens = line.split(",");
    String surface = tokens[0];
    int length = Integer.parseInt(tokens[1]);
    context.write(new Text(surface), new IntWritable(length));
  }
}
```

- To test this mapper with MRUnit, we need to create a MapDriver object and set the mapper, input and expected output.
- The test code is as follows:

```java
public class RoadMapperTest {
  @Test
  public void testMapper() throws IOException {
    // Create a MapDriver object
    MapDriver<LongWritable, Text, Text, IntWritable> mapDriver = new MapDriver<>();
    // Set the mapper
    mapDriver.setMapper(new RoadMapper());
    // Set the input
    mapDriver.withInput(new LongWritable(0), new Text("asphalt,100"));
    // Set the expected output
    mapDriver.withOutput(new Text("asphalt"), new IntWritable(100));
    // Run the test
    mapDriver.runTest();
  }
}
```

- The test will pass if the mapper emits the expected output for the given input.
- The test will fail if the mapper emits a different output or throws an exception.