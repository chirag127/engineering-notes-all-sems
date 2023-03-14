#### Unit tests with MR unit

- MR unit is a Java library that helps developers unit test Apache Hadoop map reduce jobs.
- With MR unit, you can craft test input, push it through your mapper and/or reducer, and verify its output all in a JUnit test.
- You can also test a map/reduce pair, a combiner, or a workflow of map/reduce jobs using different drivers provided by MR unit.
- MR unit allows you to do test-driven development (TDD) and write light-weight unit tests which accommodate Hadoop’s specific architecture and constructs.
- You can use MR unit along with other mocking frameworks such as Mockito or PowerMock to mock static methods, business logic, counters, log statements, and exceptions.
- Here is an example of how to use MR unit to test a mapper and a reducer that process road surface data:

```java
//Specification of Mapper
MapDriver<LongWritable, Text, Text, IntWritable> mapDriver;
//Specification of Reduce
ReduceDriver<Text, IntWritable, Text, IntWritable> reduceDriver;
//Specification of MapReduce program
MapReduceDriver<LongWritable, Text, Text, IntWritable, Text, IntWritable> mapReduceDriver;

@Before
public void setUp() {
  MaxTemperatureMapper mapper = new MaxTemperatureMapper();
  MaxTemperatureReducer reducer = new MaxTemperatureReducer();
  //Setup Mapper
  mapDriver = MapDriver.newMapDriver(mapper);
  //Setup Reduce
  reduceDriver = ReduceDriver.newReduceDriver(reducer);
  //Setup MapReduce job
  mapReduceDriver = MapReduceDriver.newMapReduceDriver(mapper, reducer);
}

@Test
public void testMapper() {
  //Test Mapper with this input
  mapDriver.withInput(new LongWritable(), new Text(
      "0029029070999991901010106004+64333+023450FM-12+000599999V0202701N015919999999N0000001N9-00781+99999102001ADDGF108991999999999999999999"));
  //Expect this output
  mapDriver.withOutput(new Text("1901"), new IntWritable(-78));

  //Test Mapper with this input
  mapDriver.withInput(new LongWritable(), new Text(
      "0029029810999991901050720004+59500+020350FM-12+002699999V0201101N003119999999N0000001N9+00111+99999101281ADDGF107991999999999999999999"));
  //Expect this output
  mapDriver.withOutput(new Text("1901"), new IntWritable(11));
  try {
    //Run Map test with above input and ouput
    mapDriver.runTest();
  } catch (IOException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
  }
}

@Test
public void testReducer() {
  List<IntWritable> values = new ArrayList<IntWritable>();
  values.add(new IntWritable(-78));
  values.add(new IntWritable(11));
  //Test Reducer with this input
  reduceDriver.withInput(new Text("1901"), values);
  //Expect this output
  reduceDriver.withOutput(new Text("1901"), new IntWritable(11));
  try {
    //Run Reduce test with above input and output
    reduceDriver.runTest();
  } catch (IOException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
  }
}
```

- Some possible mnemonics and learning tricks for unit tests with MR unit are:

  - MR unit stands for MapReduce unit test.
  - MR unit drivers are named after the components they test: MapDriver, ReduceDriver, MapReduceDriver, etc.
  - MR unit tests use the same input and output types as the map and reduce methods: LongWritable, Text, IntWritable, etc.
  - MR unit tests use withInput and withOutput methods to specify the test data and the expected results.
  - MR unit tests use runTest method to execute the test and compare the actual and expected outputs.