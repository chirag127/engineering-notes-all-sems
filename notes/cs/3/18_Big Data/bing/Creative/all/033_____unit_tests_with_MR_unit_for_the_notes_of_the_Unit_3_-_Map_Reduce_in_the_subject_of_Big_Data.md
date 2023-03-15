# Unit Tests with MRUnit

- MRUnit is a Java library that helps developers unit test Apache Hadoop map reduce jobs   .
- MRUnit allows you to craft test input, push it through your mapper and/or reducer, and verify its output all in a JUnit test.
- MRUnit supports testing mappers and reducers separately as well as testing map reduce computations as a whole.
- MRUnit enables test-driven development (TDD) and writing lightweight unit tests that accommodate Hadoop's specific architecture and constructs.
- MRUnit can be used with other testing frameworks such as Mockito, PowerMock, or EasyMock to mock out dependencies and interactions.

## Example of using MRUnit

- Suppose we are processing road surface data used to create maps. The input contains both linear surfaces and intersections.
- The mapper takes a line of input and emits a key-value pair where the key is the surface type and the value is the length of the surface.
- The reducer takes the surface type and a list of lengths and emits the total length of each surface type.
- The following code shows how to use MRUnit to test the mapper and the reducer separately.

```java
// Mapper test
public class SurfaceMapperTest extends TestCase {

  private Mapper mapper;
  private MapDriver driver;

  @Before
  public void setUp() {
    mapper = new SurfaceMapper();
    driver = new MapDriver(mapper);
  }

  @Test
  public void testMapper() throws IOException {
    driver.withInput(new LongWritable(1), new Text("LINEAR 10"));
    driver.withOutput(new Text("LINEAR"), new IntWritable(10));
    driver.runTest();
  }
}

// Reducer test
public class SurfaceReducerTest extends TestCase {

  private Reducer reducer;
  private ReduceDriver driver;

  @Before
  public void setUp() {
    reducer = new SurfaceReducer();
    driver = new ReduceDriver(reducer);
  }

  @Test
  public void testReducer() throws IOException {
    List values = new ArrayList();
    values.add(new IntWritable(10));
    values.add(new IntWritable(20));
    driver.withInput(new Text("LINEAR"), values);
    driver.withOutput(new Text("LINEAR"), new IntWritable(30));
    driver.runTest();
  }
}
```

## Example of using MRUnit with Mockito

- Suppose we have a map reduce job that reads data from a database using a custom input format and writes data to a file system using a custom output format.
- The mapper takes a record from the database and emits a key-value pair where the key is the record id and the value is the record content.
- The reducer takes the record id and a list of record contents and emits the record id and the concatenated record contents.
- The following code shows how to use MRUnit with Mockito to test the map reduce job as a whole by mocking out the input and output formats.

```java
// MapReduce test
public class RecordMapReduceTest extends TestCase {

  private MapReduceDriver driver;
  private DBInputFormat inputFormat;
  private FileSystemOutputFormat outputFormat;

  @Before
  public void setUp() {
    driver = new MapReduceDriver(new RecordMapper(), new RecordReducer());
    inputFormat = Mockito.mock(DBInputFormat.class);
    outputFormat = Mockito.mock(FileSystemOutputFormat.class);
    driver.withInputFormat(inputFormat);
    driver.withOutputFormat(outputFormat);
  }

  @Test
  public void testMapReduce() throws IOException {
    // Mock the input format to return a record with id 1 and content "foo"
    Mockito.when(inputFormat.nextKeyValue()).thenReturn(true).thenReturn(false);
    Mockito.when(inputFormat.getCurrentKey()).thenReturn(new LongWritable(1));
    Mockito.when(inputFormat.getCurrentValue()).thenReturn(new Text("foo"));

    // Mock the output format to verify the output
    Mockito.doAnswer(new Answer() {
      public Object answer(InvocationOnMock invocation) {
        Object[] args = invocation.getArguments();
        assertEquals(new LongWritable(1), args[0]);
        assertEquals(new Text("foo"), args[1]);
        return null;
      }
    }).when(outputFormat).write(Mockito.any(), Mockito.any());

    driver.runTest();
  }
}
```