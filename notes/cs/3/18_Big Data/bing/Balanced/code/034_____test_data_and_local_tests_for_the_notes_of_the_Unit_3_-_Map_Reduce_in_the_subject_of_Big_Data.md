### Test Data and Local Tests for Map Reduce

- Test data is a set of input values that can be used to verify the functionality and performance of a map reduce program.
- Local tests are tests that can be performed on a single machine without using a hadoop cluster.
- Local tests are useful for debugging and validating the logic of the map and reduce functions before deploying them on a large-scale distributed system.
- Local tests can be done by using the following methods:

  - **Using hadoop streaming**: Hadoop streaming is a utility that allows users to write map and reduce scripts in any language that can read from standard input and write to standard output. For example, if the map and reduce scripts are written in Python, they can be tested locally by using the following command:

    ```bash
    cat *.csv | map.py | sort -k1,1 | reducer.py
    ```

    This command will feed the input data from the csv files to the map script, sort the output by key, and pass it to the reduce script. The output of the reduce script will be displayed on the terminal .

  - **Using MRUnit**: MRUnit is a testing framework that allows users to write unit tests for map and reduce classes in Java. MRUnit provides drivers that can simulate the execution of map and reduce tasks and compare the expected and actual outputs. For example, to test a WordCount program, the following code can be used:

    ```java
    public class WordCountTest {
      private Mapper mapper;
      private Reducer reducer;
      private MapDriver mapDriver;
      private ReduceDriver reduceDriver;
      private MapReduceDriver mapReduceDriver;

      @Before
      public void setUp() {
        mapper = new WordCountMapper();
        reducer = new WordCountReducer();
        mapDriver = new MapDriver(mapper);
        reduceDriver = new ReduceDriver(reducer);
        mapReduceDriver = new MapReduceDriver(mapper, reducer);
      }

      @Test
      public void testMapper() {
        mapDriver.withInput(new LongWritable(1), new Text("hello world"));
        mapDriver.withOutput(new Text("hello"), new IntWritable(1));
        mapDriver.withOutput(new Text("world"), new IntWritable(1));
        mapDriver.runTest();
      }

      @Test
      public void testReducer() {
        List<IntWritable> values = new ArrayList<IntWritable>();
        values.add(new IntWritable(1));
        values.add(new IntWritable(1));
        reduceDriver.withInput(new Text("hello"), values);
        reduceDriver.withOutput(new Text("hello"), new IntWritable(2));
        reduceDriver.runTest();
      }

      @Test
      public void testMapReduce() {
        mapReduceDriver.withInput(new LongWritable(1), new Text("hello world"));
        mapReduceDriver.withOutput(new Text("hello"), new IntWritable(2));
        mapReduceDriver.withOutput(new Text("world"), new IntWritable(1));
        mapReduceDriver.runTest();
      }
    }
    ```

    This code will create a mapper, a reducer, and three drivers for testing the map, reduce, and map-reduce tasks. The drivers will provide the input and output values and check if they match the expected values  .

  - **Using mockito**: Mockito is a mocking framework that allows users to create and use mock objects in unit tests. Mock objects are objects that simulate the behavior of real objects without invoking their actual methods. Mockito can be used to mock the context and configuration objects that are passed to the map and reduce methods. For example, to test a WordCount program, the following code can be used:

    ```java
    public class WordCountTest {
      private Mapper mapper;
      private Reducer reducer;
      private Mapper.Context mapContext;
      private Reducer.Context reduceContext;

      @Before
      public void setUp() {
        mapper = new WordCountMapper();
        reducer = new WordCountReducer();
        mapContext = mock(Mapper.Context.class);
        reduceContext = mock(Reducer.Context.class);
      }

      @Test
      public void testMapper() throws IOException, InterruptedException {
        mapper.map(new LongWritable(1), new Text("hello world"), mapContext);
        verify(mapContext).write(new Text("hello"), new IntWritable(1));
        verify(mapContext).write(new Text("world"), new IntWritable(1));
      }

      @Test
      public void testReducer() throws IOException, InterruptedException {
        List<IntWritable> values = new