### Unit Tests with MRUnit

- MRUnit is a Java library that helps developers unit test Hadoop MapReduce jobs   .
- MRUnit allows you to craft test input, push it through your mapper and/or reducer, and verify its output all in a JUnit test.
- MRUnit supports testing mappers and reducers separately as well as testing map-reduce computations as a whole.
- MRUnit also supports testing combiners, counters, partitioners, and custom writable types.
- MRUnit is based on JUnit, so it integrates well with IDEs and build tools that support JUnit.
- MRUnit helps you to do test-driven development (TDD) and write lightweight unit tests that accommodate Hadoop's specific architecture and constructs.

#### Example of using MRUnit to test a mapper

- Suppose we have a mapper that processes road surface data used to create maps.
- The input contains both linear surfaces and intersections, and the mapper emits the surface type and the length as key-value pairs.
- The mapper code is as follows:

```java
public class RoadMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
  @Override
  public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {
    String line = value.toString();
    String[] tokens = line.split(",");
    String surfaceType = tokens[0];
    int length = Integer.parseInt(tokens[1]);
    context.write(new Text(surfaceType), new IntWritable(length));
  }
}
```

- To test this mapper using MRUnit, we need to create a MapDriver object and set the mapper, input, and expected output .
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
    mapDriver.withInput(new LongWritable(1), new Text("asphalt,100"));
    // Set the expected output
    mapDriver.withOutput(new Text("asphalt"), new IntWritable(100));
    // Run the test
    mapDriver.runTest();
  }
}
```

- The test will pass if the mapper emits the expected output for the given input, otherwise it will fail and show the differences .
- MRUnit provides similar drivers for testing reducers, combiners, partitioners, and map-reduce jobs .