Unit tests with MR unit are a way of testing Hadoop MapReduce jobs using a JUnit-based Java library called MRUnit. MRUnit allows you to create test input, run it through your mapper and/or reducer, and verify the output all in a JUnit test. This helps you to debug your code and ensure its correctness.

The following diagram illustrates the basic architecture of a unit test with MR unit:

```
+-----------------+     +-----------------+     +-----------------+
| Test Input Data | --> | Mapper/Reducer  | --> | Expected Output |
+-----------------+     +-----------------+     +-----------------+
          |                     |                         |
          |                     |                         |
          v                     v                         v
+-----------------+     +-----------------+     +-----------------+
| InputSplit      | --> | MapDriver       | --> | OutputCollector |
|                 |     | or              |     |                 |
| RecordReader    | --> | ReduceDriver    | --> | OutputVerifier  |
|                 |     | or              |     |                 |
| InputFormat     | --> | MapReduceDriver | --> | JUnit Assert    |
+-----------------+     +-----------------+     +-----------------+
```

The test input data is a set of key-value pairs that represent the input to the mapper or reducer. The expected output is another set of key-value pairs that represent the expected output from the mapper or reducer. The input split, record reader, and input format are classes that handle the reading and parsing of the input data. The map driver, reduce driver, or map reduce driver are classes that simulate the execution of the mapper, reducer, or both. The output collector, output verifier, and JUnit assert are classes that collect, verify, and assert the output of the mapper or reducer. The MRUnit library provides these classes and methods to make it easy to write unit tests for Hadoop MapReduce jobs.