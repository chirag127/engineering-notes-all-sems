### Unit Tests with MRUnit

- MRUnit is a Java library that allows you to write unit tests for Hadoop MapReduce jobs.
- MRUnit is based on JUnit and uses mock objects to simulate the Hadoop environment.
- MRUnit supports testing mappers, reducers, combiners, partitioners, and map-reduce chains.
- MRUnit provides various drivers to run the tests, such as MapDriver, ReduceDriver, MapReduceDriver, etc.
- MRUnit allows you to specify the input and output key-value pairs for each test case, and compare them with the expected results.
- MRUnit also allows you to set up counters, configuration, and custom comparators for the tests.
- MRUnit helps you to develop and debug your MapReduce code faster and easier, without the need of a real Hadoop cluster.

#### Example of a MRUnit test case

- Suppose you have a mapper class that takes a line of text as input and emits the word count for each word as output.
- The mapper class looks like this:

```java
public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

  private final static IntWritable one = new IntWritable(1);
  private Text word = new Text();

  @Override
  public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    String line = value.toString();
    StringTokenizer tokenizer = new StringTokenizer(line);
    while (tokenizer.hasMoreTokens()) {
      word.set(tokenizer.nextToken());
      context.write(word, one);
    }
  }
}
```

- To test this mapper class, you can use MRUnit's MapDriver and write a JUnit test case like this:

```java
public class WordCountMapperTest {

  private MapDriver<LongWritable, Text, Text, IntWritable> mapDriver;

  @Before
  public void setUp() {
    // create an instance of the mapper class
    WordCountMapper mapper = new WordCountMapper();
    // create a MapDriver with the mapper
    mapDriver = MapDriver.newMapDriver(mapper);
  }

  @Test
  public void testMapper() throws IOException {
    // set the input key-value pair for the mapper
    mapDriver.withInput(new LongWritable(1), new Text("hello world"));
    // set the expected output key-value pairs for the mapper
    mapDriver.withOutput(new Text("hello"), new IntWritable(1));
    mapDriver.withOutput(new Text("world"), new IntWritable(1));
    // run the test and verify the results
    mapDriver.runTest();
  }
}
```

- This test case will check if the mapper produces the correct output for the given input, and fail if there is any mismatch.