#### Test data and local tests in map reduce

- Test data is the input data that is used to test the functionality and performance of a map reduce program. Test data can be generated artificially or obtained from real sources, depending on the requirements and objectives of the testing.
- Local tests are the tests that are performed on a single machine, without using a distributed cluster. Local tests are useful for debugging and validating the logic of the map and reduce functions, as well as the data flow and format between them.
- Some of the ways to perform local tests in map reduce are:

  - Using hadoop streaming, which allows writing map and reduce scripts in any language that can read from standard input and write to standard output. For example, if the map and reduce scripts are written in Python, they can be tested locally like this:

    ```
    cat *.csv | map.py | sort -k1,1 | reducer.py
    ```

    This command simulates the map reduce process by piping the input data to the map script, sorting the output by key, and piping it to the reduce script.

  - Using MRUnit, which is a testing framework that lets you test and debug map reduce jobs in isolation without spinning up a hadoop cluster. MRUnit provides mock objects and drivers for testing the map and reduce functions, as well as the combiners, partitioners, and counters. For example, to test a mapper class using MRUnit, one can write a test case like this:

    ```
    public class WordCountMapperTest extends TestCase {

      public void testMapper() {
        Mapper mapper = new WordCountMapper();
        MapperDriver driver = new MapperDriver(mapper);

        driver.withInput(new LongWritable(1), new Text("cat cat dog"))
              .withOutput(new Text("cat"), new IntWritable(1))
              .withOutput(new Text("cat"), new IntWritable(1))
              .withOutput(new Text("dog"), new IntWritable(1))
              .runTest();
      }
    }
    ```

    This test case verifies that the mapper produces the expected key-value pairs for a given input.

  - Using JUnit, which is a general-purpose testing framework for Java programs. JUnit can be used to test the map and reduce classes, as well as the main driver class, by creating test cases and assertions. For example, to test a reducer class using JUnit, one can write a test case like this:

    ```
    public class WordCountReducerTest {

      @Test
      public void testReducer() throws IOException {
        Reducer reducer = new WordCountReducer();
        Reducer.Context context = mock(Reducer.Context.class);

        List<IntWritable> values = new ArrayList<IntWritable>();
        values.add(new IntWritable(1));
        values.add(new IntWritable(1));
        values.add(new IntWritable(1));

        reducer.reduce(new Text("cat"), values, context);

        verify(context).write(new Text("cat"), new IntWritable(3));
      }
    }
    ```

    This test case mocks the reducer context and verifies that the reducer produces the expected output for a given key and list of values.