### Test Data and Local Tests for Map Reduce

- Test data is a set of input values that can be used to verify the functionality and performance of a map reduce program.
- Local tests are tests that can be performed on a single machine without using a hadoop cluster or a distributed file system.
- Local tests are useful for debugging and validating the logic of the map and reduce functions before deploying them on a large-scale data set.
- Local tests can be done in different ways depending on the programming language and the framework used for map reduce.
- Some common methods for local testing are:

  - Using command-line tools such as `cat`, `sort`, and `awk` to simulate the map reduce process and pipe the output of the mapper to the input of the reducer .
  - Using a testing framework such as MRUnit   that provides mock objects and drivers for testing map, reduce, and combiner classes in isolation or in combination.
  - Using a local mode of execution that runs the map reduce job on a single JVM and uses the local file system as the input and output source. This mode can be enabled by setting the configuration property `mapreduce.framework.name` to `local`.