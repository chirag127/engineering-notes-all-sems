# Unit Tests with MRUnit

- MRUnit is a Java library that helps developers unit test Hadoop MapReduce jobs   .
- MRUnit allows you to craft test input, push it through your mapper and/or reducer, and verify its output all in a JUnit test.
- MRUnit supports testing mappers and reducers separately as well as testing map-reduce computations as a whole.
- MRUnit also supports testing combiners, counters, partitions, and custom writable types.
- MRUnit is useful for test-driven development (TDD) and writing lightweight unit tests that accommodate Hadoop's specific architecture and constructs.
- MRUnit can be used with other testing frameworks such as Mockito, PowerMock, or EasyMock.

## Example of using MRUnit

- Suppose we are processing road surface data used to create maps. The input contains both linear surfaces and intersections.
- The mapper takes a line of input and emits the surface type and the length as a key-value pair. The reducer sums up the lengths for each surface type and emits the total length as the value.
- The mapper code looks like this:

```java
public class SurfaceMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
  private static final IntWritable ONE = new IntWritable(1);
  private Text surface = new Text();

  public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    String line = value.toString();
    String[] tokens = line.split(",");
    surface.set(tokens[0]);
    context.write(surface, new IntWritable(Integer.parseInt(tokens[1])));
  }
}
```

- The reducer code looks like this:

```java
public class SurfaceReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
  public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
    int sum = 0;
    for (IntWritable value : values) {
      sum += value.get();
    }
    context.write(key, new IntWritable(sum));
  }
}
```

- To test the mapper using MRUnit, we can write a JUnit test like this:

```java
public class SurfaceMapperTest extends TestCase {
  private Mapper<LongWritable, Text, Text, IntWritable> mapper;
  private MapDriver<LongWritable, Text, Text, IntWritable> driver;

  @Before
  public void setUp() {
    mapper = new SurfaceMapper();
    driver = new MapDriver<LongWritable, Text, Text, IntWritable>(mapper);
  }

  @Test
  public void testMapper() throws IOException {
    driver.withInput(new LongWritable(1), new Text("asphalt,100"))
          .withOutput(new Text("asphalt"), new IntWritable(100))
          .runTest();
  }
}
```

- To test the reducer using MRUnit, we can write a JUnit test like this:

```java
public class SurfaceReducerTest extends TestCase {
  private Reducer<Text, IntWritable, Text, IntWritable> reducer;
  private ReduceDriver<Text, IntWritable, Text, IntWritable> driver;

  @Before
  public void setUp() {
    reducer = new SurfaceReducer();
    driver = new ReduceDriver<Text, IntWritable, Text, IntWritable>(reducer);
  }

  @Test
  public void testReducer() throws IOException {
    List<IntWritable> values = new ArrayList<IntWritable>();
    values.add(new IntWritable(100));
    values.add(new IntWritable(200));
    driver.withInput(new Text("asphalt"), values)
          .withOutput(new Text("asphalt"), new IntWritable(300))
          .runTest();
  }
}
```

- To test the map-reduce computation using MRUnit, we can write a JUnit test like this:

```java
public class SurfaceMapReduceTest extends TestCase {
  private MapReduceDriver<LongWritable, Text, Text, IntWritable, Text, IntWritable> driver;

  @Before
  public void setUp() {
    Mapper<LongWritable, Text, Text, IntWritable> mapper = new SurfaceMapper();
    Reducer<Text, IntWritable, Text, IntWritable> reducer = new SurfaceReducer();
    driver = new MapReduceDriver<LongWritable, Text, Text, IntWritable, Text, IntWritable>(mapper, reducer);
  }

  @Test
  public void testMapReduce() throws IOException {
    driver.withInput(new LongWritable(1), new Text("

```
