#### Test data and local tests in map reduce

To test your map and reduce code locally, you can use the following methods:

- If you are using hadoop streaming, then you can test your scripts locally like this:

```bash
cat *.csv | map.py | sort -k1,1 | reducer.py
```

To pass data from mapper to reducer in hadoop-streaming, simply write `<key>\t<value>` to stdout.

- If you are using Java, then you can use MRUnit, a testing framework that lets you test and debug Map Reduce jobs in isolation without spinning up a Hadoop cluster. You can write test cases for your mapper and reducer classes using JUnit and MRUnit libraries. For example, to test a mapper that splits a line of text into words, you can write:

```java
public class WordCountMapperTest extends TestCase {

  public void testMapper() {
    Mapper mapper = new WordCountMapper();
    Mapper.Context context = mock(Mapper.Context.class);
    MRUnitDriver driver = new MRUnitDriver();
    driver.setMapper(mapper);
    driver.setInputKey("1");
    driver.setInputValue("this is a test");
    driver.addOutput(new Text("this"), new IntWritable(1));
    driver.addOutput(new Text("is"), new IntWritable(1));
    driver.addOutput(new Text("a"), new IntWritable(1));
    driver.addOutput(new Text("test"), new IntWritable(1));
    driver.runTest();
  }
}
```

- If you are using Python, then you can use mrjob, a library that lets you write Map Reduce jobs in Python and run them on several platforms, including your local machine. You can write test cases for your mapper and reducer functions using unittest and mrjob libraries. For example, to test a mapper that splits a line of text into words, you can write:

```python
from mrjob.job import MRJob
from mrjob.step import MRStep
import unittest
from mrjob.protocol import JSONValueProtocol

class WordCountJob(MRJob):

  INPUT_PROTOCOL = JSONValueProtocol

  def mapper(self, _, line):
    for word in line.split():
      yield word, 1

  def reducer(self, word, counts):
    yield word, sum(counts)

class WordCountJobTestCase(unittest.TestCase):

  def setUp(self):
    self.job = WordCountJob()

  def test_mapper(self):
    input = '{"this is a test"}'
    output = list(self.job.mapper(None, input))
    expected = [("this", 1), ("is", 1), ("a", 1), ("test", 1)]
    self.assertEqual(output, expected)
```