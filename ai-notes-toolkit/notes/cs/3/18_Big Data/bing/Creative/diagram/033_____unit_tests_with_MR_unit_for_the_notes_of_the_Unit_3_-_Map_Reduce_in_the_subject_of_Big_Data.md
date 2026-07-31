### Unit Tests with MRUnit

- MRUnit is a JUnit-based Java library that allows us to unit test Hadoop MapReduce programs  .
- MRUnit supports testing Mappers and Reducers separately as well as testing MapReduce computations as a whole.
- MRUnit allows us to do Test Driven Development (TDD) and write lightweight unit tests which accommodate Hadoop’s specific architecture and constructs.
- With MRUnit, we can craft test input, push it through our mapper and/or reducer, and verify its output all in a JUnit test.
- MRUnit also provides mock objects for testing the context and the counters of the MapReduce jobs.
- MRUnit makes it easy to develop and maintain Hadoop MapReduce code bases.

#### Example of testing a Mapper with MRUnit 

```java
public class RoadMapperTest extends TestCase {

  private Mapper mapper;
  private MapDriver driver;

  @Before
  public void setUp() {
    mapper = new RoadMapper();
    driver = new MapDriver(mapper);
  }

  @Test
  public void testMapper() throws IOException {
    driver.withInput(new LongWritable(1), new Text("road1,linear,asphalt,10"));
    driver.withOutput(new Text("linear"), new IntWritable(10));
    driver.runTest();
  }
}
```

#### Example of testing a Reducer with MRUnit 

```java
public class RoadReducerTest extends TestCase {

  private Reducer reducer;
  private ReduceDriver driver;

  @Before
  public void setUp() {
    reducer = new RoadReducer();
    driver = new ReduceDriver(reducer);
  }

  @Test
  public void testReducer() throws IOException {
    List<IntWritable> values = new ArrayList<IntWritable>();
    values.add(new IntWritable(10));
    values.add(new IntWritable(20));
    driver.withInput(new Text("linear"), values);
    driver.withOutput(new Text("linear"), new IntWritable(30));
    driver.runTest();
  }
}
```

#### Example of testing a MapReduce job with MRUnit 

```java
public class RoadMapReduceTest extends TestCase {

  private MapReduceDriver driver;

  @Before
  public void setUp() {
    Mapper mapper = new RoadMapper();
    Reducer reducer = new RoadReducer();
    driver = new MapReduceDriver(mapper, reducer);
  }

  @Test
  public void testMapReduce() throws IOException {
    driver.withInput(new LongWritable(1), new Text("road1,linear,asphalt,10"));
    driver.withInput(new LongWritable(2), new Text("road2,linear,concrete,20"));
    driver.withInput(new LongWritable(3), new Text("road3,intersection,asphalt,5"));
    driver.withOutput(new Text("intersection"), new IntWritable(5));
    driver.withOutput(new Text("linear"), new IntWritable(30));
    driver.runTest();
  }
}
```