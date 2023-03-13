#### Unit tests with MR unit

- MR unit is a Java library that helps developers unit test Hadoop MapReduce jobs   .
- MR unit allows you to do test-driven development (TDD) and write lightweight unit tests that accommodate Hadoop's specific architecture and constructs.
- MR unit supports testing mappers and reducers separately as well as testing MapReduce computations as a whole  .
- With MR unit, you can craft test input, push it through your mapper and/or reducer, and verify its output all in a JUnit test.
- As do other JUnit tests, this allows you to debug your code using the JUnit test as a driver.
- A map/reduce pair can be tested using MR unit's MapReduceDriver.
- MR unit also supports testing combiners, counters, partitioners, and custom writable classes .
- MR unit can be used with other testing frameworks such as Mockito, PowerMock, and EasyMock.
- MR unit can be integrated with Maven or Gradle for dependency management and build automation .

##### Example

- Suppose we are processing road surface data used to create maps.
- The input contains both linear surfaces and intersections.
- The mapper extracts the surface type and the length of each segment.
- The reducer sums up the lengths of each surface type and outputs the total length per type.
- The following code snippet shows how to write a unit test for this map/reduce pair using MR unit.

```java
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mrunit.mapreduce.MapReduceDriver;
import org.junit.Before;
import org.junit.Test;

public class RoadSurfaceTest {

  MapReduceDriver<Object, Text, Text, IntWritable, Text, IntWritable> mapReduceDriver;

  @Before
  public void setUp() {
    RoadSurfaceMapper mapper = new RoadSurfaceMapper();
    RoadSurfaceReducer reducer = new RoadSurfaceReducer();
    mapReduceDriver = MapReduceDriver.newMapReduceDriver(mapper, reducer);
  }

  @Test
  public void testMapReduce() {
    mapReduceDriver.withInput(new Text("road1"), new Text("asphalt,100"));
    mapReduceDriver.withInput(new Text("road2"), new Text("concrete,200"));
    mapReduceDriver.withInput(new Text("road3"), new Text("asphalt,150"));
    mapReduceDriver.withInput(new Text("road4"), new Text("gravel,50"));
    mapReduceDriver.withOutput(new Text("asphalt"), new IntWritable(250));
    mapReduceDriver.withOutput(new Text("concrete"), new IntWritable(200));
    mapReduceDriver.withOutput(new Text("gravel"), new IntWritable(50));
    mapReduceDriver.runTest();
  }
}
```

##### Advantages

- MR unit makes it easy to develop and maintain Hadoop MapReduce code bases.
- MR unit allows you to test your code without setting up a Hadoop cluster or writing files to HDFS  .
- MR unit provides a simple and intuitive API for writing test cases  .
- MR unit can help you catch bugs and errors early in the development cycle  .
- MR unit can improve the quality and reliability of your MapReduce programs  .

##### Disadvantages

- MR unit does not test the performance or scalability of your MapReduce programs  .
- MR unit does not test the integration of your MapReduce programs with other components such as input/output formats, compression codecs, or distributed cache  .
- MR unit does not test the behavior of your MapReduce programs under different cluster configurations or failure scenarios  .
- MR unit may not cover all the features or edge cases of your MapReduce programs  .

##### Mnemonics and learning tricks

- MR unit stands for MapReduce unit testing