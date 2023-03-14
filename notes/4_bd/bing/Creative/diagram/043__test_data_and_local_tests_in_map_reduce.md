To test the map and reduce code locally, you can use the following steps:

1. Create a test data set in a local file, such as test.csv, with the input format expected by the mapper.
2. Write a map.py script that reads from stdin and writes to stdout the key-value pairs in the format "<key>\t<value>".
3. Write a reduce.py script that reads from stdin and writes to stdout the aggregated key-value pairs in the same format.
4. Use the cat, sort and pipe commands to simulate the map and shuffle phases, and pass the output to the reducer script. For example: cat test.csv | map.py | sort -k1,1 | reduce.py
5. Verify the output of the reducer script against the expected output.

Alternatively, you can use a testing framework such as MRUnit to write unit tests for the mapper and reducer classes. MRUnit provides mock objects and methods to simulate the input and output of the map and reduce methods, and to assert the expected results. For example, to test the WordCount mapper, you can write a test case like this:

```java
public class WordCountMapperTest extends TestCase {

  private Mapper mapper;
  private MapDriver driver;

  @Override
  public void setUp() {
    mapper = new WordCountMapper();
    driver = new MapDriver(mapper);
  }

  public void testMapper() {
    driver.withInput(new LongWritable(1), new Text("hello world"))
          .withOutput(new Text("hello"), new IntWritable(1))
          .withOutput(new Text("world"), new IntWritable(1))
          .runTest();
  }
}
```

#### Test data and local tests in map reduce

The following diagram illustrates the basic architecture of a map reduce job and how it can be tested locally using either the command line or MRUnit.

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Input File    |     |  Mapper Class  |     |  Reducer Class |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  cat command   |     |  map.py script |     |  reduce.py     |
|                |     |                |     |  script        |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  stdin         |     |  stdout        |     |  stdin         |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  MapDriver     |     |  MapReduceDriver |   |  ReduceDriver  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |